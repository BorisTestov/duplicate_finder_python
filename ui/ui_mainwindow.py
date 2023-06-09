# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QAction, QFont)
from PySide6.QtWidgets import (QAbstractSpinBox, QButtonGroup, QComboBox,
                               QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QListWidget, QMenu, QMenuBar, QProgressBar,
                               QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
                               QSpinBox, QStatusBar, QTabWidget, QTreeWidget,
                               QVBoxLayout, QWidget)


class Ui_DuplicateFinder(object):
    def setupUi(self, DuplicateFinder):
        if not DuplicateFinder.objectName():
            DuplicateFinder.setObjectName(u"DuplicateFinder")
        DuplicateFinder.setEnabled(True)
        DuplicateFinder.resize(738, 701)

        DuplicateFinder.setTabShape(QTabWidget.Rounded)
        self.Russian = QAction(DuplicateFinder)
        self.Russian.setObjectName(u"Russian")
        self.English = QAction(DuplicateFinder)
        self.English.setObjectName(u"English")
        self.dark = QAction(DuplicateFinder)
        self.dark.setObjectName(u"dark")
        self.light = QAction(DuplicateFinder)
        self.light.setObjectName(u"light")
        self.actionGerman = QAction(DuplicateFinder)
        self.actionGerman.setObjectName(u"actionGerman")
        self.actionFrench = QAction(DuplicateFinder)
        self.actionFrench.setObjectName(u"actionFrench")
        self.actionSpanish = QAction(DuplicateFinder)
        self.actionSpanish.setObjectName(u"actionSpanish")
        self.actionFrench_2 = QAction(DuplicateFinder)
        self.actionFrench_2.setObjectName(u"actionFrench_2")
        self.actionChinese = QAction(DuplicateFinder)
        self.actionChinese.setObjectName(u"actionChinese")
        self.actionJapanese = QAction(DuplicateFinder)
        self.actionJapanese.setObjectName(u"actionJapanese")
        self.chinese = QAction(DuplicateFinder)
        self.chinese.setObjectName(u"chinese")
        self.english = QAction(DuplicateFinder)
        self.english.setObjectName(u"english")
        self.french = QAction(DuplicateFinder)
        self.french.setObjectName(u"french")
        self.german = QAction(DuplicateFinder)
        self.german.setObjectName(u"german")
        self.italian = QAction(DuplicateFinder)
        self.italian.setObjectName(u"italian")
        self.japanese = QAction(DuplicateFinder)
        self.japanese.setObjectName(u"japanese")
        self.russian = QAction(DuplicateFinder)
        self.russian.setObjectName(u"russian")
        self.spanish = QAction(DuplicateFinder)
        self.spanish.setObjectName(u"spanish")
        self.centralwidget = QWidget(DuplicateFinder)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.search_runner_layout = QGridLayout()
        self.search_runner_layout.setObjectName(u"search_runner_layout")
        self.progress_bar = QProgressBar(self.centralwidget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress_bar.sizePolicy().hasHeightForWidth())
        self.progress_bar.setSizePolicy(sizePolicy)
        self.progress_bar.setMaximumSize(QSize(16777215, 26))
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        self.progress_bar.setFont(font)
        self.progress_bar.setValue(100)
        self.progress_bar.setTextVisible(True)

        self.search_runner_layout.addWidget(self.progress_bar, 0, 0, 1, 3)

        self.abort_button = QPushButton(self.centralwidget)
        self.abort_button.setObjectName(u"abort_button")
        self.abort_button.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.abort_button.sizePolicy().hasHeightForWidth())
        self.abort_button.setSizePolicy(sizePolicy1)

        self.search_runner_layout.addWidget(self.abort_button, 1, 0, 1, 1)

        self.search_button = QPushButton(self.centralwidget)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setMinimumSize(QSize(200, 56))
        self.search_button.setMaximumSize(QSize(16777215, 56))
        self.search_button.setStyleSheet(u"")

        self.search_runner_layout.addWidget(self.search_button, 1, 2, 1, 1)

        self.gridLayout.addLayout(self.search_runner_layout, 1, 0, 1, 1)

        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.tabs.setFont(font1)
        self.tabs.setFocusPolicy(Qt.NoFocus)
        self.tabs.setTabShape(QTabWidget.Triangular)
        self.tabs.setUsesScrollButtons(False)
        self.tabs.setTabBarAutoHide(False)
        self.directories = QWidget()
        self.directories.setObjectName(u"directories")
        self.gridLayout_3 = QGridLayout(self.directories)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.include_directories_group_box = QGroupBox(self.directories)
        self.include_directories_group_box.setObjectName(u"include_directories_group_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.include_directories_group_box.sizePolicy().hasHeightForWidth())
        self.include_directories_group_box.setSizePolicy(sizePolicy2)
        self.include_directories_group_box.setMinimumSize(QSize(276, 500))
        self.include_directories_group_box.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.include_directories_group_box)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.include_directories_list_widget = QListWidget(self.include_directories_group_box)
        self.include_directories_list_widget.setObjectName(u"include_directories_list_widget")

        self.verticalLayout_2.addWidget(self.include_directories_list_widget)

        self.choose_include_directories = QPushButton(self.include_directories_group_box)
        self.choose_include_directories.setObjectName(u"choose_include_directories")

        self.verticalLayout_2.addWidget(self.choose_include_directories)

        self.gridLayout_3.addWidget(self.include_directories_group_box, 0, 0, 1, 1)

        self.exclude_directories_group_box = QGroupBox(self.directories)
        self.exclude_directories_group_box.setObjectName(u"exclude_directories_group_box")
        self.exclude_directories_group_box.setMinimumSize(QSize(276, 500))
        self.exclude_directories_group_box.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.exclude_directories_group_box)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.exclude_directories_list_widget = QListWidget(self.exclude_directories_group_box)
        self.exclude_directories_list_widget.setObjectName(u"exclude_directories_list_widget")

        self.verticalLayout.addWidget(self.exclude_directories_list_widget)

        self.choose_exclude_directories = QPushButton(self.exclude_directories_group_box)
        self.choose_exclude_directories.setObjectName(u"choose_exclude_directories")

        self.verticalLayout.addWidget(self.choose_exclude_directories)

        self.gridLayout_3.addWidget(self.exclude_directories_group_box, 0, 1, 1, 1)

        self.search_parameters_layout = QVBoxLayout()
        self.search_parameters_layout.setObjectName(u"search_parameters_layout")
        self.search_type_group_box = QGroupBox(self.directories)
        self.search_type_group_box.setObjectName(u"search_type_group_box")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.search_type_group_box.sizePolicy().hasHeightForWidth())
        self.search_type_group_box.setSizePolicy(sizePolicy3)
        self.search_type_group_box.setMinimumSize(QSize(130, 100))
        self.search_type_group_box.setMaximumSize(QSize(130, 200))
        self.verticalLayout_3 = QVBoxLayout(self.search_type_group_box)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.hash = QRadioButton(self.search_type_group_box)
        self.search_type_button_group = QButtonGroup(DuplicateFinder)
        self.search_type_button_group.setObjectName(u"search_type_button_group")
        self.search_type_button_group.addButton(self.hash)
        self.hash.setObjectName(u"hash")
        self.hash.setChecked(True)

        self.verticalLayout_3.addWidget(self.hash)

        self.name = QRadioButton(self.search_type_group_box)
        self.search_type_button_group.addButton(self.name)
        self.name.setObjectName(u"name")

        self.verticalLayout_3.addWidget(self.name)

        self.search_parameters_layout.addWidget(self.search_type_group_box)

        self.parameters_group_box = QGroupBox(self.directories)
        self.parameters_group_box.setObjectName(u"parameters_group_box")
        sizePolicy3.setHeightForWidth(self.parameters_group_box.sizePolicy().hasHeightForWidth())
        self.parameters_group_box.setSizePolicy(sizePolicy3)
        self.parameters_group_box.setMinimumSize(QSize(130, 100))
        self.parameters_group_box.setMaximumSize(QSize(130, 200))
        self.verticalLayout_4 = QVBoxLayout(self.parameters_group_box)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.min_file_size_label = QLabel(self.parameters_group_box)
        self.min_file_size_label.setObjectName(u"min_file_size_label")
        self.min_file_size_label.setMaximumSize(QSize(16777215, 33))

        self.verticalLayout_4.addWidget(self.min_file_size_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.min_file_size_spin_box = QSpinBox(self.parameters_group_box)
        self.min_file_size_spin_box.setObjectName(u"min_file_size_spin_box")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.min_file_size_spin_box.sizePolicy().hasHeightForWidth())
        self.min_file_size_spin_box.setSizePolicy(sizePolicy4)
        self.min_file_size_spin_box.setStyleSheet(u"")
        self.min_file_size_spin_box.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.min_file_size_spin_box.setAccelerated(True)
        self.min_file_size_spin_box.setMinimum(0)
        self.min_file_size_spin_box.setMaximum(99999)
        self.min_file_size_spin_box.setSingleStep(1)
        self.min_file_size_spin_box.setValue(0)

        self.horizontalLayout.addWidget(self.min_file_size_spin_box)

        self.size_suffix_box = QComboBox(self.parameters_group_box)
        self.size_suffix_box.addItem("")
        self.size_suffix_box.addItem("")
        self.size_suffix_box.addItem("")
        self.size_suffix_box.addItem("")
        self.size_suffix_box.setObjectName(u"size_suffix_box")
        sizePolicy4.setHeightForWidth(self.size_suffix_box.sizePolicy().hasHeightForWidth())
        self.size_suffix_box.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.size_suffix_box)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.depth_label = QLabel(self.parameters_group_box)
        self.depth_label.setObjectName(u"depth_label")
        self.depth_label.setMaximumSize(QSize(16777215, 33))

        self.verticalLayout_4.addWidget(self.depth_label)

        self.depth_spin_box = QSpinBox(self.parameters_group_box)
        self.depth_spin_box.setObjectName(u"depth_spin_box")
        sizePolicy4.setHeightForWidth(self.depth_spin_box.sizePolicy().hasHeightForWidth())
        self.depth_spin_box.setSizePolicy(sizePolicy4)
        self.depth_spin_box.setStyleSheet(u"")
        self.depth_spin_box.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.depth_spin_box.setAccelerated(True)
        self.depth_spin_box.setMinimum(0)
        self.depth_spin_box.setMaximum(10000000)
        self.depth_spin_box.setSingleStep(1)
        self.depth_spin_box.setValue(0)

        self.verticalLayout_4.addWidget(self.depth_spin_box)

        self.search_parameters_layout.addWidget(self.parameters_group_box)

        self.gridLayout_3.addLayout(self.search_parameters_layout, 0, 4, 1, 2)

        self.tabs.addTab(self.directories, "")
        self.masks = QWidget()
        self.masks.setObjectName(u"masks")
        self.gridLayout_6 = QGridLayout(self.masks)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.exclude_masks_group_box = QGroupBox(self.masks)
        self.exclude_masks_group_box.setObjectName(u"exclude_masks_group_box")
        self.gridLayout_8 = QGridLayout(self.exclude_masks_group_box)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.exclude_mask_line_edit = QLineEdit(self.exclude_masks_group_box)
        self.exclude_mask_line_edit.setObjectName(u"exclude_mask_line_edit")
        self.exclude_mask_line_edit.setAutoFillBackground(False)
        self.exclude_mask_line_edit.setClearButtonEnabled(True)

        self.gridLayout_8.addWidget(self.exclude_mask_line_edit, 1, 1, 1, 1)

        self.add_exclude_mask_button = QPushButton(self.exclude_masks_group_box)
        self.add_exclude_mask_button.setObjectName(u"add_exclude_mask_button")

        self.gridLayout_8.addWidget(self.add_exclude_mask_button, 2, 1, 1, 1)

        self.exclude_masks_list_widget = QListWidget(self.exclude_masks_group_box)
        self.exclude_masks_list_widget.setObjectName(u"exclude_masks_list_widget")

        self.gridLayout_8.addWidget(self.exclude_masks_list_widget, 0, 1, 1, 1)

        self.gridLayout_6.addWidget(self.exclude_masks_group_box, 0, 1, 2, 1)

        self.include_masks_group_box = QGroupBox(self.masks)
        self.include_masks_group_box.setObjectName(u"include_masks_group_box")
        sizePolicy3.setHeightForWidth(self.include_masks_group_box.sizePolicy().hasHeightForWidth())
        self.include_masks_group_box.setSizePolicy(sizePolicy3)
        self.gridLayout_9 = QGridLayout(self.include_masks_group_box)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.include_mask_line_edit = QLineEdit(self.include_masks_group_box)
        self.include_mask_line_edit.setObjectName(u"include_mask_line_edit")
        self.include_mask_line_edit.setAutoFillBackground(False)
        self.include_mask_line_edit.setClearButtonEnabled(True)

        self.gridLayout_9.addWidget(self.include_mask_line_edit, 1, 1, 1, 1)

        self.add_include_mask_button = QPushButton(self.include_masks_group_box)
        self.add_include_mask_button.setObjectName(u"add_include_mask_button")

        self.gridLayout_9.addWidget(self.add_include_mask_button, 2, 1, 1, 1)

        self.include_masks_list_widget = QListWidget(self.include_masks_group_box)
        self.include_masks_list_widget.setObjectName(u"include_masks_list_widget")

        self.gridLayout_9.addWidget(self.include_masks_list_widget, 0, 1, 1, 1)

        self.gridLayout_6.addWidget(self.include_masks_group_box, 0, 0, 2, 1)

        self.tabs.addTab(self.masks, "")
        self.results = QWidget()
        self.results.setObjectName(u"results")
        self.gridLayout_7 = QGridLayout(self.results)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.left_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.left_spacer_2, 1, 0, 1, 1)

        self.remove_selected_duplicates_button = QPushButton(self.results)
        self.remove_selected_duplicates_button.setObjectName(u"remove_selected_duplicates_button")
        self.remove_selected_duplicates_button.setMinimumSize(QSize(300, 0))

        self.gridLayout_7.addWidget(self.remove_selected_duplicates_button, 1, 1, 1, 1)

        self.right_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.right_spacer_2, 1, 2, 1, 1)

        self.duplicates_tree_widget = QTreeWidget(self.results)
        self.duplicates_tree_widget.setObjectName(u"duplicates_tree_widget")
        self.duplicates_tree_widget.setColumnCount(1)

        self.gridLayout_7.addWidget(self.duplicates_tree_widget, 0, 0, 1, 3)

        self.tabs.addTab(self.results, "")

        self.gridLayout.addWidget(self.tabs, 0, 0, 1, 1)

        DuplicateFinder.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(DuplicateFinder)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 738, 22))
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuTheme = QMenu(self.menuSettings)
        self.menuTheme.setObjectName(u"menuTheme")
        self.languages = QMenu(self.menuSettings)
        self.languages.setObjectName(u"languages")
        DuplicateFinder.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(DuplicateFinder)
        self.statusBar.setObjectName(u"statusBar")
        DuplicateFinder.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuSettings.addAction(self.menuTheme.menuAction())
        self.menuSettings.addAction(self.languages.menuAction())
        self.menuTheme.addAction(self.dark)
        self.menuTheme.addAction(self.light)
        self.languages.addAction(self.chinese)
        self.languages.addAction(self.english)
        self.languages.addAction(self.french)
        self.languages.addAction(self.german)
        self.languages.addAction(self.italian)
        self.languages.addAction(self.japanese)
        self.languages.addAction(self.russian)
        self.languages.addAction(self.spanish)

        self.retranslateUi(DuplicateFinder)

        self.tabs.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(DuplicateFinder)

    # setupUi

    def retranslateUi(self, DuplicateFinder):
        DuplicateFinder.setWindowTitle(QCoreApplication.translate("DuplicateFinder", u"Duplicate Finder", None))
        self.Russian.setText(QCoreApplication.translate("DuplicateFinder", u"Russian", None))
        self.English.setText(QCoreApplication.translate("DuplicateFinder", u"English", None))
        self.dark.setText(QCoreApplication.translate("DuplicateFinder", u"Dark", None))
        self.light.setText(QCoreApplication.translate("DuplicateFinder", u"Light", None))
        self.actionGerman.setText(QCoreApplication.translate("DuplicateFinder", u"German", None))
        self.actionFrench.setText(QCoreApplication.translate("DuplicateFinder", u"French", None))
        self.actionSpanish.setText(QCoreApplication.translate("DuplicateFinder", u"Spanish", None))
        self.actionFrench_2.setText(QCoreApplication.translate("DuplicateFinder", u"French", None))
        self.actionChinese.setText(QCoreApplication.translate("DuplicateFinder", u"Chinese", None))
        self.actionJapanese.setText(QCoreApplication.translate("DuplicateFinder", u"Japanese", None))
        self.chinese.setText(QCoreApplication.translate("DuplicateFinder", u"Chinese", None))
        self.english.setText(QCoreApplication.translate("DuplicateFinder", u"English", None))
        self.french.setText(QCoreApplication.translate("DuplicateFinder", u"French", None))
        self.german.setText(QCoreApplication.translate("DuplicateFinder", u"German", None))
        self.italian.setText(QCoreApplication.translate("DuplicateFinder", u"Italian", None))
        self.japanese.setText(QCoreApplication.translate("DuplicateFinder", u"Japanese", None))
        self.russian.setText(QCoreApplication.translate("DuplicateFinder", u"Russian", None))
        self.spanish.setText(QCoreApplication.translate("DuplicateFinder", u"Spanish", None))
        self.progress_bar.setFormat(QCoreApplication.translate("DuplicateFinder", u"Adding Files: %p%", None))
        self.abort_button.setText(QCoreApplication.translate("DuplicateFinder", u"CANCEL", None))
        self.search_button.setText(QCoreApplication.translate("DuplicateFinder", u"SEARCH", None))
        self.include_directories_group_box.setTitle(
            QCoreApplication.translate("DuplicateFinder", u"Included Directories", None))
        self.choose_include_directories.setText(QCoreApplication.translate("DuplicateFinder", u"Choose...", None))
        self.exclude_directories_group_box.setTitle(
            QCoreApplication.translate("DuplicateFinder", u"Excluded Directories", None))
        self.choose_exclude_directories.setText(QCoreApplication.translate("DuplicateFinder", u"Choose...", None))
        self.search_type_group_box.setTitle(QCoreApplication.translate("DuplicateFinder", u"Search Type", None))
        self.hash.setText(QCoreApplication.translate("DuplicateFinder", u"Hash", None))
        self.name.setText(QCoreApplication.translate("DuplicateFinder", u"Name", None))
        self.parameters_group_box.setTitle(QCoreApplication.translate("DuplicateFinder", u"Parameters", None))
        self.min_file_size_label.setText(QCoreApplication.translate("DuplicateFinder", u"Min File Size", None))
        self.min_file_size_spin_box.setSuffix("")
        self.size_suffix_box.setItemText(0, QCoreApplication.translate("DuplicateFinder", u"b", None))
        self.size_suffix_box.setItemText(1, QCoreApplication.translate("DuplicateFinder", u"KB", None))
        self.size_suffix_box.setItemText(2, QCoreApplication.translate("DuplicateFinder", u"MB", None))
        self.size_suffix_box.setItemText(3, QCoreApplication.translate("DuplicateFinder", u"GB", None))

        self.depth_label.setText(QCoreApplication.translate("DuplicateFinder", u"Search Depth", None))
        self.depth_spin_box.setSuffix("")
        self.tabs.setTabText(self.tabs.indexOf(self.directories),
                             QCoreApplication.translate("DuplicateFinder", u"Directories", None))
        self.exclude_masks_group_box.setTitle(QCoreApplication.translate("DuplicateFinder", u"Excluded Masks", None))
        self.exclude_mask_line_edit.setText("")
        self.exclude_mask_line_edit.setPlaceholderText(
            QCoreApplication.translate("DuplicateFinder", u"Enter python-style mask here...", None))
        self.add_exclude_mask_button.setText(QCoreApplication.translate("DuplicateFinder", u"Add", None))
        self.include_masks_group_box.setTitle(QCoreApplication.translate("DuplicateFinder", u"Included Masks", None))
        self.include_mask_line_edit.setText("")
        self.include_mask_line_edit.setPlaceholderText(
            QCoreApplication.translate("DuplicateFinder", u"Enter python-style mask here...", None))
        self.add_include_mask_button.setText(QCoreApplication.translate("DuplicateFinder", u"Add", None))
        self.tabs.setTabText(self.tabs.indexOf(self.masks),
                             QCoreApplication.translate("DuplicateFinder", u"Masks", None))
        self.remove_selected_duplicates_button.setText(
            QCoreApplication.translate("DuplicateFinder", u"Remove Selected", None))
        ___qtreewidgetitem = self.duplicates_tree_widget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("DuplicateFinder", u"Path", None));
        self.tabs.setTabText(self.tabs.indexOf(self.results),
                             QCoreApplication.translate("DuplicateFinder", u"Results", None))
        self.menuSettings.setTitle(QCoreApplication.translate("DuplicateFinder", u"Settings", None))
        self.menuTheme.setTitle(QCoreApplication.translate("DuplicateFinder", u"Theme", None))
        self.languages.setTitle(QCoreApplication.translate("DuplicateFinder", u"Language", None))
    # retranslateUi
