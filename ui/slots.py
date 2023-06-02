from PySide6.QtCore import Slot
from PySide6.QtWidgets import QListWidget, QAbstractItemView, QTreeView, QListView, QFileDialog, QLineEdit


class Slots:
    @staticmethod
    @Slot()
    def choose_directories(lw: QListWidget):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setOption(QFileDialog.Option.ShowDirsOnly, True)
        dialog.setViewMode(QFileDialog.ViewMode.List)
        dialog.setOption(QFileDialog.Option.DontUseNativeDialog, True)

        file_view = dialog.findChild(QListView, 'listView')
        if file_view:
            file_view.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        file_view = dialog.findChild(QTreeView)
        if file_view:
            file_view.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        if dialog.exec():
            directories = dialog.selectedFiles()
            for d in directories:
                lw.addItem(d)
        dialog.deleteLater()

    @staticmethod
    @Slot()
    def delete_item(lw: QListWidget):
        for name in lw.selectedItems():
            lw.model().removeRow(lw.row(name))

    @staticmethod
    @Slot()
    def add_to_list_from_line_edit(lw: QListWidget, le: QLineEdit):
        text = le.text()
        if not text:
            return
        lw.addItem(text)
        le.clear()
