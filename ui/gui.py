import os

from PySide6 import QtCore
from PySide6.QtCore import QCryptographicHash
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QMainWindow, QDialog, QAbstractItemView

from duplicate_finder import DuplicateFinder
from search_types import SearchTypes
from ui.slots import Slots
from ui.ui_confirmation_dialog import Ui_delete_files_dialog
from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__setup()
        self.__connect_slots()

    def __setup(self):
        self.ui.progress_bar.setVisible(False)

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
        print(finder.find())


class ConfirmationDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_delete_files_dialog()
        self.ui.setupUi(self)
