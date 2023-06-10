import logging

from PySide6 import QtCore
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QListWidget, QAbstractItemView, QTreeView, QListView, QFileDialog, QLineEdit, \
    QTreeWidgetItem, QTreeWidget


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
                if len(lw.findItems(d, QtCore.Qt.MatchFlag.MatchExactly)) == 0:
                    lw.addItem(d)
                    logging.debug(f"Directory chosen: {d}")
        dialog.deleteLater()

    @staticmethod
    @Slot()
    def delete_item(lw: QListWidget):
        for name in lw.selectedItems():
            lw.model().removeRow(lw.row(name))
            logging.debug(f"Item deleted: {name.text()}")

    @staticmethod
    @Slot()
    def add_to_list_from_line_edit(lw: QListWidget, le: QLineEdit):
        text = le.text()
        if not text:
            return
        if len(lw.findItems(text, QtCore.Qt.MatchFlag.MatchExactly)) == 0:
            lw.addItem(text)
            le.clear()
            logging.debug(f"Item added to list: {text}")

    @staticmethod
    @Slot()
    def on_item_change(item: QTreeWidgetItem, on_click=False):

        def get_children_states(parent: QTreeWidgetItem):
            children_states = [parent.child(i).checkState(0) for i in range(parent.childCount())]
            at_least_one_checked = any(state == QtCore.Qt.CheckState.Checked for state in children_states)
            all_checked = all(state == QtCore.Qt.CheckState.Checked for state in children_states)
            if all_checked:
                return QtCore.Qt.CheckState.Checked
            elif at_least_one_checked:
                return QtCore.Qt.CheckState.PartiallyChecked
            return QtCore.Qt.CheckState.Unchecked

        try:
            item.treeWidget().blockSignals(True)

            if on_click:
                if item.checkState(0) == QtCore.Qt.CheckState.Checked:
                    item.setCheckState(0, QtCore.Qt.CheckState.Unchecked)
                else:
                    item.setCheckState(0, QtCore.Qt.CheckState.Checked)

            parent = item.parent()
            if parent:
                children_states = get_children_states(parent)
                if children_states == QtCore.Qt.CheckState.Checked:
                    parent.setCheckState(0, QtCore.Qt.CheckState.Checked)
                elif children_states == QtCore.Qt.CheckState.PartiallyChecked:
                    parent.setCheckState(0, QtCore.Qt.CheckState.PartiallyChecked)
                else:
                    parent.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            target_check = item.checkState(0)

            for i in range(item.childCount()):
                child = item.child(i)
                child.setCheckState(0, target_check)
        finally:
            item.treeWidget().blockSignals(False)

        logging.debug(f"Item changed: {item.text(0)}, Checked: {item.checkState(0)}")

    @staticmethod
    @Slot()
    def invert_selection(tree: QTreeWidget, *args):
        target_check = QtCore.Qt.CheckState.Unchecked
        for i in range(tree.topLevelItemCount()):
            top = tree.topLevelItem(i)
            if top.checkState(0) == QtCore.Qt.CheckState.Checked:
                continue
            target_check = QtCore.Qt.CheckState.Checked
            break
        for i in range(tree.topLevelItemCount()):
            top = tree.topLevelItem(i)
            top.setCheckState(0, target_check)
            logging.debug(f"Invert selection: Item: {top.text(0)}, Checked: {target_check}")
