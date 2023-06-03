import os

from PySide6 import QtCore
from PySide6.QtCore import QCryptographicHash
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QMainWindow, QAbstractItemView, QTreeWidgetItem
from send2trash import send2trash

from duplicate_finder import DuplicateFinder
from search_types import SearchTypes
from ui.confirmation_dialog import ConfirmationDialog
from ui.slots import Slots
from ui.ui_mainwindow import Ui_MainWindow


class ProgressBarHelper:
    def __init__(self):
        self.__value = 0
        self.__step = 0
        self.__total_elements = 0

    def set_total_elements(self, total_elements: int) -> None:
        self.__total_elements = total_elements
        self.__step = 100 / self.__total_elements

    def step(self) -> int:
        self.__value += self.__step
        return self.__value // 1


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__dialog = ConfirmationDialog()
        self.__setup()
        self.__connect_slots()
        self.total_directories = 0

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

    def __connect_slots(self):
        self.ui.choose_include_directories.clicked.connect(
            lambda: Slots.choose_directories(self.ui.include_directories_list_widget)
        )

        self.ui.choose_exclude_directories.clicked.connect(
            lambda: Slots.choose_directories(self.ui.exclude_directories_list_widget)
        )

        self.ui.add_include_mask_button.clicked.connect(
            lambda: Slots.add_to_list_from_line_edit(self.ui.include_masks_list_widget,
                                                     self.ui.include_mask_line_edit)
        )
        self.ui.include_mask_line_edit.returnPressed.connect(
            lambda: Slots.add_to_list_from_line_edit(self.ui.include_masks_list_widget,
                                                     self.ui.include_mask_line_edit)
        )

        self.ui.add_exclude_mask_button.clicked.connect(
            lambda: Slots.add_to_list_from_line_edit(self.ui.exclude_masks_list_widget,
                                                     self.ui.exclude_mask_line_edit)
        )
        self.ui.exclude_mask_line_edit.returnPressed.connect(
            lambda: Slots.add_to_list_from_line_edit(self.ui.exclude_masks_list_widget,
                                                     self.ui.exclude_mask_line_edit)
        )

        self.ui.search_button.clicked.connect(lambda: self.search())

        self.ui.duplicates_tree_widget.itemChanged.connect(Slots.on_item_change)
        self.ui.duplicates_tree_widget.itemPressed.connect(lambda item: Slots.on_item_change(item, on_click=True))
        header = self.ui.duplicates_tree_widget.header()
        header.setSectionsClickable(True)
        header.sectionDoubleClicked.connect(lambda: Slots.invert_selection(self.ui.duplicates_tree_widget))

        self.ui.remove_selected_duplicates_button.clicked.connect(self.__show_dialog)
        self.__dialog.accepted.connect(self.__remove_files)

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

    def __update_results(self, results):
        self.ui.duplicates_tree_widget.clear()

        for key, value in results.items():
            original_file = QTreeWidgetItem()
            original_file.setText(0, key)
            original_file.setCheckState(0, QtCore.Qt.CheckState.Checked)
            for path in value:
                duplicate_file = QTreeWidgetItem()
                duplicate_file.setText(0, path)
                duplicate_file.setCheckState(0, QtCore.Qt.CheckState.Checked)
                original_file.addChild(duplicate_file)
            self.ui.duplicates_tree_widget.addTopLevelItem(original_file)
        self.ui.duplicates_tree_widget.expandAll()

    def __remove_files(self):
        files_to_remove = set()
        for parent_i in range(self.ui.duplicates_tree_widget.topLevelItemCount()):
            original_file = self.ui.duplicates_tree_widget.topLevelItem(parent_i)
            if original_file.checkState(0) == QtCore.Qt.CheckState.Unchecked:
                continue
            for child_i in range(original_file.childCount()):
                duplicate_file = original_file.child(child_i)
                if duplicate_file.checkState(0) == QtCore.Qt.CheckState.Unchecked:
                    continue
                files_to_remove.add(duplicate_file)
        self.ui.progress_bar.setFormat("Removing files: %p%")
        self.ui.progress_bar.setVisible(True)
        pbh = ProgressBarHelper()
        pbh.set_total_elements(len(files_to_remove))
        for file in files_to_remove:
            try:
                send2trash(file.text(0))
            except FileNotFoundError:
                pass
            parent = file.parent()
            parent.removeChild(file)
            if parent.childCount() == 0:
                index = self.ui.duplicates_tree_widget.indexOfTopLevelItem(parent)
                self.ui.duplicates_tree_widget.takeTopLevelItem(index)
            self.ui.progress_bar.setValue(pbh.step())
        self.ui.progress_bar.setFormat("Duplicates moved to thrash")

    def __set_bar_step(self, i):
        self.__bar_step = 100 / i

    def __update_bar_on_directory(self):
        self.ui.progress_bar.value()

    def search(self):
        hash_mappings = {
            'md5_radio_button': QCryptographicHash.Algorithm.Md5,
            'sha1_radio_button': QCryptographicHash.Algorithm.Sha1,
            'sha512_radio_button': QCryptographicHash.Algorithm.Sha512
        }
        type_mappings = {
            'hash_type': SearchTypes.BY_HASH,
            'name_type': SearchTypes.BY_NAME
        }

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
        block_size = self.ui.block_size_spin_box.value()
        min_file_size = self.ui.min_file_size_spin_box.value()
        depth = self.ui.depth_spin_box.value()
        hash_method = hash_mappings[self.ui.hashing_button_group.checkedButton().objectName()]
        search_type = type_mappings[self.ui.search_type_button_group.checkedButton().objectName()]
        finder = DuplicateFinder(search_type, hash_method, depth, min_file_size, block_size, include_directories,
                                 exclude_directories, include_masks, exclude_masks)
        self.ui.progress_bar.setVisible(True)
        self.ui.progress_bar.setFormat("Searching duplicates: %p%")
        pbh = ProgressBarHelper()
        finder.all_directories_added.connect(lambda i: pbh.set_total_elements(i))
        finder.directory_scanned.connect(lambda: self.ui.progress_bar.setValue(pbh.step()))
        self.ui.progress_bar.setFormat("Search complete")
        self.__update_results(finder.find())
