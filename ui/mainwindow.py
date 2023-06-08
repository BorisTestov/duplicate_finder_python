import os
from collections import deque
from functools import partial

from PySide6 import QtCore
from PySide6.QtCore import QThreadPool, Slot, Signal
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QMainWindow, QAbstractItemView, QTreeWidgetItem, QProgressBar

from interruptible_task import InterruptibleTask
from search_types import SearchTypes
from searcher import Searcher
from ui.confirmation_dialog import ConfirmationDialog
from ui.mappings import Mappings
from ui.slots import Slots
from ui.ui_mainwindow import Ui_MainWindow
from version import APP_VERSION, BUILD_NUMBER


class ProgressBarHelper:
    def __init__(self, pb: QProgressBar):
        self.pb = pb
        self.__value = 0
        self.step_size = 0
        self.total_elements = 0
        self.pb.setValue(0)
        self.pb.setMaximum(100)

    def clear(self):
        self.pb.setValue(0)
        self.__value = 0
        self.step_size = 0
        self.total_elements = 0
        self.pb.setMaximum(100)

    def set_total_elements(self, total_elements: int) -> None:
        self.total_elements = total_elements
        if self.total_elements > 0:
            self.step_size = 100 / self.total_elements

    @Slot()
    def step(self) -> None:
        self.__value += self.step_size
        self.pb.setValue(self.__value)


class MainWindow(QMainWindow):
    files_removed = Signal()

    searcher = Searcher()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__dialog = ConfirmationDialog()
        self.total_directories = 0
        self.thread_pool = QThreadPool()

        self.pbh = ProgressBarHelper(self.ui.progress_bar)
        self.__setup()
        self.__connect_slots()

    def __setup(self):
        self.ui.progress_bar.setVisible(False)
        self.ui.progress_bar.setEnabled(True)

        self.ui.include_directories_list_widget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        shortcut_include_directories = QShortcut(QKeySequence(QtCore.Qt.Key.Key_Delete),
                                                 self.ui.include_directories_list_widget)
        shortcut_include_directories.setContext(QtCore.Qt.ShortcutContext.WidgetWithChildrenShortcut)
        shortcut_include_directories.activated.connect(
            lambda: Slots.delete_item(self.ui.include_directories_list_widget))

        self.ui.exclude_directories_list_widget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        shortcut_exclude_directories = QShortcut(QKeySequence(QtCore.Qt.Key.Key_Delete),
                                                 self.ui.exclude_directories_list_widget)
        shortcut_exclude_directories.setContext(QtCore.Qt.ShortcutContext.WidgetWithChildrenShortcut)
        shortcut_exclude_directories.activated.connect(
            lambda: Slots.delete_item(self.ui.exclude_directories_list_widget))

        self.ui.include_masks_list_widget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        shortcut_include_masks = QShortcut(QKeySequence(QtCore.Qt.Key.Key_Delete),
                                           self.ui.include_masks_list_widget)
        shortcut_include_masks.setContext(QtCore.Qt.ShortcutContext.WidgetWithChildrenShortcut)
        shortcut_include_masks.activated.connect(
            lambda: Slots.delete_item(self.ui.include_masks_list_widget))

        self.ui.exclude_masks_list_widget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        shortcut_exclude_masks = QShortcut(QKeySequence(QtCore.Qt.Key.Key_Delete),
                                           self.ui.exclude_masks_list_widget)
        shortcut_exclude_masks.setContext(QtCore.Qt.ShortcutContext.WidgetWithChildrenShortcut)
        shortcut_exclude_masks.activated.connect(
            lambda: Slots.delete_item(self.ui.exclude_masks_list_widget))

        headers = ['Path']
        self.ui.duplicates_tree_widget.setColumnCount(len(headers))
        self.ui.duplicates_tree_widget.setHeaderLabels(headers)

        self.ui.statusBar.showMessage(f"version: {APP_VERSION} build: {BUILD_NUMBER}")

    def __start_in_thread(self, fn, *args, **kwargs):
        worker = InterruptibleTask(fn, *args, **kwargs)
        self.thread_pool.start(worker)

    def __connect_slots(self):
        self.ui.choose_include_directories.clicked.connect(
            partial(Slots.choose_directories, self.ui.include_directories_list_widget)
        )

        self.ui.choose_exclude_directories.clicked.connect(
            partial(Slots.choose_directories, self.ui.exclude_directories_list_widget)
        )

        self.ui.add_include_mask_button.clicked.connect(
            partial(Slots.add_to_list_from_line_edit, self.ui.include_masks_list_widget,
                    self.ui.include_mask_line_edit)
        )
        self.ui.include_mask_line_edit.returnPressed.connect(
            partial(Slots.add_to_list_from_line_edit, self.ui.include_masks_list_widget,
                    self.ui.include_mask_line_edit)
        )

        self.ui.add_exclude_mask_button.clicked.connect(
            partial(Slots.add_to_list_from_line_edit, self.ui.exclude_masks_list_widget,
                    self.ui.exclude_mask_line_edit)
        )
        self.ui.exclude_mask_line_edit.returnPressed.connect(
            partial(Slots.add_to_list_from_line_edit, self.ui.exclude_masks_list_widget,
                    self.ui.exclude_mask_line_edit)
        )

        self.ui.search_button.clicked.connect(self.search)

        self.ui.duplicates_tree_widget.itemChanged.connect(Slots.on_item_change)
        self.ui.duplicates_tree_widget.itemPressed.connect(lambda item: Slots.on_item_change(item, on_click=True))
        header = self.ui.duplicates_tree_widget.header()
        header.setSectionsClickable(True)
        header.sectionDoubleClicked.connect(partial(Slots.invert_selection, self.ui.duplicates_tree_widget))

        self.ui.remove_selected_duplicates_button.clicked.connect(self.__show_dialog)
        self.__dialog.accepted.connect(self.__remove_files)

        self.searcher.search_done.connect(self.__add_to_tree)
        self.searcher.all_files_added.connect(
            lambda value: self.__handle_progress_bar(len(value),
                                                     "Searching duplicates: %p%"))

        self.searcher.file_scanned.connect(self.pbh.step)
        self.searcher.search_done.connect(lambda: self.ui.progress_bar.setFormat("Search complete"))
        self.searcher.search_done.connect(lambda: self.ui.progress_bar.setValue(100))
        self.searcher.file_removed.connect(lambda x: self.pbh.step())
        self.searcher.file_removed.connect(self.__handle_file_removing)
        self.searcher.all_files_removed.connect(lambda: self.ui.progress_bar.setFormat("Removing complete"))
        self.searcher.all_files_removed.connect(lambda: self.ui.progress_bar.setValue(100))
        self.searcher.all_files_added.connect(lambda value: self.__start_in_thread(self.searcher.find, value))

    def __show_dialog(self):
        files_chosen = 0
        for i in range(self.ui.duplicates_tree_widget.topLevelItemCount()):
            original = self.ui.duplicates_tree_widget.topLevelItem(i)
            for j in range(original.childCount()):
                if original.child(i).checkState(0) == QtCore.Qt.CheckState.Checked:
                    files_chosen += 1
        if files_chosen == 0:
            return
        self.__dialog.exec()

    def __remove_files(self):
        self.__handle_progress_bar(self.ui.duplicates_tree_widget.topLevelItemCount(),
                                   "Removing files: %p%")
        files_matrix = deque()
        for parent_i in range(self.ui.duplicates_tree_widget.topLevelItemCount()):
            files_to_remove = set()
            original_file = self.ui.duplicates_tree_widget.topLevelItem(parent_i)
            if original_file.checkState(0) == QtCore.Qt.CheckState.Unchecked:
                continue
            for child_i in range(original_file.childCount()):
                duplicate_file = original_file.child(child_i)
                if duplicate_file.checkState(0) == QtCore.Qt.CheckState.Unchecked:
                    continue
                files_to_remove.add(duplicate_file.text(0))
            files_matrix.append(files_to_remove)
        self.searcher.remove(files_matrix)

    def __handle_file_removing(self, path):
        for parent_i in range(self.ui.duplicates_tree_widget.topLevelItemCount()):
            original_file = self.ui.duplicates_tree_widget.topLevelItem(parent_i)
            for child_i in range(original_file.childCount()):
                duplicate_file = original_file.child(child_i)
                if not duplicate_file or duplicate_file.text(0) != path:
                    continue
                original_file.removeChild(duplicate_file)
                if original_file.childCount() == 0:
                    index = self.ui.duplicates_tree_widget.indexOfTopLevelItem(original_file)
                    self.ui.duplicates_tree_widget.takeTopLevelItem(index)

    def __add_to_tree(self, files):
        self.ui.duplicates_tree_widget.clear()
        for top, childs in files.items():
            top_item = QTreeWidgetItem()
            top_item.setText(0, top)
            top_item.setCheckState(0, QtCore.Qt.CheckState.Checked)
            for child in childs:
                child_item = QTreeWidgetItem()
                child_item.setText(0, child)
                child_item.setCheckState(0, QtCore.Qt.CheckState.Checked)
                top_item.addChild(child_item)
            self.ui.duplicates_tree_widget.addTopLevelItem(top_item)
        self.ui.duplicates_tree_widget.expandAll()

    def __handle_progress_bar(self, total_files, format):
        self.ui.progress_bar.setVisible(True)
        self.ui.progress_bar.setFormat(format)
        self.pbh.clear()
        self.pbh.set_total_elements(total_files)

    def __handle_progress_bar_no_max(self):
        self.ui.progress_bar.setVisible(True)
        self.pbh.clear()
        self.ui.progress_bar.setMaximum(0)

    def search(self):
        inc_dir_lw = self.ui.include_directories_list_widget
        include_directories = {os.path.normpath(inc_dir_lw.item(row).text()) for row in range(inc_dir_lw.count())}
        if not include_directories:
            return
        exc_dir_lw = self.ui.exclude_directories_list_widget
        exclude_directories = {os.path.normpath(exc_dir_lw.item(row).text()) for row in range(exc_dir_lw.count())}
        if not exclude_directories:
            exclude_directories = None
        inc_mask_lw = self.ui.include_masks_list_widget
        include_masks = {inc_mask_lw.item(row).text() for row in range(inc_mask_lw.count())}
        if not include_masks:
            include_masks = None
        exc_mask_lw = self.ui.exclude_masks_list_widget
        exclude_masks = {exc_mask_lw.item(row).text() for row in range(exc_mask_lw.count())}
        if not exclude_masks:
            exclude_masks = None
        min_file_size = self.ui.min_file_size_spin_box.value()
        size_modifier = Mappings.size_mappings.get(self.ui.size_suffix_box.currentText(), 0)
        min_file_size *= size_modifier
        depth = self.ui.depth_spin_box.value()
        search_type = Mappings.type_mappings.get(self.ui.search_type_button_group.checkedButton().objectName(),
                                                 SearchTypes.BY_HASH)

        self.__handle_progress_bar_no_max()
        self.__start_in_thread(self.searcher.scan, include_directories, exclude_directories, include_masks,
                               exclude_masks, depth, min_file_size, search_type)
