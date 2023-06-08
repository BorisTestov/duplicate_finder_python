# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QButtonGroup, QComboBox,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(872, 701)
        MainWindow.setStyleSheet(u"/*Copyright (c) DevSec Studio. All rights reserved.\n"
"\n"
"MIT License\n"
"\n"
"Permission is hereby granted, free of charge, to any person obtaining a copy\n"
"of this software and associated documentation files (the \"Software\"), to deal\n"
"in the Software without restriction, including without limitation the rights\n"
"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
"copies of the Software, and to permit persons to whom the Software is\n"
"furnished to do so, subject to the following conditions:\n"
"\n"
"The above copyright notice and this permission notice shall be included in all\n"
"copies or substantial portions of the Software.\n"
"\n"
"THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACT"
                        "ION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n"
"SOFTWARE.\n"
"*/\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(102, 115, 140, 255),stop:1 rgba(56, 63, 77, 255));\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel::disabled\n"
"{\n"
"	background-color: transparent;\n"
"	color: #898988;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenuBar-----*/\n"
"QMenuBar\n"
"{\n"
"	background-color: #484c58;\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #898988;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background-color: transpare"
                        "nt;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background-color: #c4c5c3;\n"
"	color: #000000;\n"
"    border: 1px solid #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background-color: #979796;\n"
"    border: 1px solid #000;\n"
"    margin-bottom: -1px;\n"
"    padding-bottom: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: #c4c5c3;\n"
"    border: 1px solid;\n"
"    color: #000000;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #363942;\n"
"    color: #ffffff;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    min-width : 150px;\n"
"    padding: 3px 20px 3px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: #363942;\n"
"    color: #ffffff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #898988;\n"
"}\n"
"\n"
"\n"
"/*-"
                        "----QToolTip-----*/\n"
"QToolTip\n"
"{\n"
"	background-color: #bbbcba;\n"
"	color: #000000;\n"
"	border-color: #051a39;\n"
"	border : 1px solid #000000;\n"
"	border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(170, 0, 0, 255),stop:1 rgba(122, 0, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #9c0000;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #880000;\n"
"	color:"
                        " #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 3px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(177, 181, 193, 255),stop:1 rgba(159, 163, 174, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::hover\n"
"{\n"
"	background-color: #9fa3ae;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"	background-color: #7b7e86;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width:"
                        " 2px;\n"
"	border-radius: 3px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(118, 118, 118, 255),stop:1 rgba(70, 70, 70, 255));\n"
"    border: 1px solid #333333;\n"
"    border-radius: 3px;\n"
"    padding-left: 6px;\n"
"    color: lightgray;\n"
"	font-weight: bold;\n"
"    height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:hover\n"
"{\n"
"    background-color: #646464;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #979796;\n"
"	color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #c4c5c3;\n"
"    color: #000000;\n"
"    border: 1px solid black;\n"
"    selection-background-color: #363942;\n"
"    selection-color: #ffffff;\n"
"    outline: 0;\n"
"\n"
""
                        "}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"	background-color: #000000;\n"
"	color: #00ff00;\n"
"	font-weight: bold;\n"
"    border: 1px solid #333333;\n"
"	padding: 4px;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"    border: 1px solid #00ff00;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTextEdit-----*/\n"
"QTextEdit\n"
"{\n"
"	background-color: #808080;\n"
"	color: #fff;\n"
"	border: 1px groove #333333;\n"
"\n"
"}\n"
"\n"
"\n"
"QTextEdit::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QGroupBox-----*/\n"
"QGroupBox \n"
"{\n"
"    border: 1px groove #333333;\n"
"	border-radius: 2px;\n"
"    margin-top: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox \n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0,"
                        " x2:0.505, y2:1, stop:0.00480769 rgba(170, 169, 169, 255),stop:1 rgba(122, 122, 122, 255));\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title  \n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(71, 75, 87, 255),stop:1 rgba(35, 37, 43, 255));\n"
"    color: #ffffff;\n"
"    border: 2px groove #333333;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 5px;\n"
"	border-top-left-radius: 3px;\n"
"	border-top-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox{\n"
"	background-color: transparent;\n"
"	font-weight: bold;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 2px solid #222222"
                        ";\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(://checkbox.png);\n"
"    border: 2px solid #00ff00;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 2px solid #00ff00;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QRadioButton-----*/\n"
"QRadioButton{\n"
"	background-color: transparent;\n"
"	font-weight: bold;\n"
"	color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked\n"
"{ \n"
"	border: 2px inset #222222; \n"
"	border-radius: 6px; \n"
"	background-color:  #323232;\n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked:hover\n"
"{ \n"
"	border: 2px solid #00ff00; \n"
"	border-radius: 5px; \n"
"	background-color:  #323232;\n"
"	width: 9px;"
                        " \n"
"	height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::checked\n"
"{ \n"
"	border: 2px inset #222222; \n"
"	border-radius: 5px; \n"
"	background-color: #00ff00; \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 2px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTableView & QTableWidget-----*/\n"
"QTableView\n"
"{\n"
"    background-color: #808080;\n"
"    border: 1px groove #333333;\n"
"    color: #f0f0f0;\n"
"	font-weight: bold;\n"
"    gridline-color: #333333;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::disabled\n"
"{\n"
"    background-color: #242526;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:hover \n"
"{\n"
"    background-color: #484c58;\n"
"    color: #f0f0f0;\n"
"\n"
"}"
                        "\n"
"\n"
"\n"
"QTableView::item:selected \n"
"{\n"
"    background-color: #484c58;\n"
"    border: 2px groove #00ff00;\n"
"    color: #F0F0F0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected:disabled\n"
"{\n"
"    background-color: #1a1b1c;\n"
"    border: 2px solid #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: #282830;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #282830;\n"
"    color: #fff;\n"
"	font-weight: bold;\n"
"    text-align: left;\n"
"	padding: 4px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    background-color: #00ff00;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked:disabled\n"
"{\n"
"    color: #656565;\n"
"    background-color: #525251;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-on"
                        "e\n"
"{\n"
"    border-top: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTabWidget-----*/\n"
"QTabBar::tab\n"
"{\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	width: 80px;\n"
"	height: 9px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane \n"
"{\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"	border: 1px groove #333333;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    background-color: #484c58;\n"
"	color: #ffffff;\n"
"	border: 1px groove #333333;\n"
"	border-bottom: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected:disabled\n"
"{\n"
"	"
                        "background-color: #404040;\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected \n"
"{\n"
"    background-color: #a3a7b2;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected:hover \n"
"{\n"
"    background-color: #484c58;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top:!selected \n"
"{\n"
"    margin-top: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:bottom:!selected \n"
"{\n"
"    margin-bottom: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom \n"
"{\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top:selected \n"
"{\n"
"    border-bottom-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:bottom:selected \n"
"{\n"
"    border-top-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one \n"
"{\n"
"    margin-right: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left:!selected \n"
"{\n"
"    margin-right: 2px;\n"
"\n"
"}\n"
"\n"
""
                        "\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    margin-left: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right \n"
"{\n"
"    min-height: 15ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left:selected \n"
"{\n"
"    border-left-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:right:selected \n"
"{\n"
"    border-right-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one \n"
"{\n"
"    margin-bottom: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSlider-----*/\n"
"QSlider{\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::groove:horizontal \n"
"{\n"
"	background-color: transparent;\n"
"	height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal \n"
"{\n"
"	background-color: qlineargradient(spread:reflect, x1:1, y1:0, x2:1, y2:1, stop:0.00480769 rgba(201, 201, 201, 255),stop:1 rgba(72, 72, 72, 255));\n"
"	border: 1px solid #"
                        "000;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal \n"
"{\n"
"	background-color: #404040;\n"
"	border: 1px solid #000; \n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal \n"
"{\n"
"	background-color: qlineargradient(spread:reflect, x1:1, y1:0, x2:1, y2:1, stop:0.00480769 rgba(201, 201, 201, 255),stop:1 rgba(72, 72, 72, 255));\n"
"	border: 1px solid #000; \n"
"	width: 12px;\n"
"	margin-top: -6px;\n"
"	margin-bottom: -6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover \n"
"{\n"
"	background-color: #808080;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal:disabled \n"
"{\n"
"	background-color: #bbb;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border: 1px solid #aaa;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::groove:vertical \n"
"{\n"
"	background-color: transparent;\n"
"	width: 6px;\n"
"\n"
""
                        "}\n"
"\n"
"\n"
"QSlider::sub-page:vertical \n"
"{\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0.483, x2:1, y2:0.517, stop:0.00480769 rgba(201, 201, 201, 255),stop:1 rgba(72, 72, 72, 255));\n"
"	border: 1px solid #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:vertical \n"
"{\n"
"	background-color: #404040;\n"
"	border: 1px solid #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:vertical \n"
"{\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0.483, x2:1, y2:0.517, stop:0.00480769 rgba(201, 201, 201, 255),stop:1 rgba(72, 72, 72, 255));\n"
"	border: 1px solid #000;\n"
"	height: 12px;\n"
"	margin-left: -6px;\n"
"	margin-right: -6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:vertical:hover \n"
"{\n"
"	background-color: #808080;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:vertical:disabled \n"
"{\n"
"	background-color: #bbb;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:vertical:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border-color: #999;\n"
"\n"
"}\n"
""
                        "\n"
"\n"
"QSlider::handle:vertical:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border: 1px solid #aaa;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QDial-----*/\n"
"QDial\n"
"{\n"
"	background-color: #600000;\n"
"\n"
"}\n"
"\n"
"\n"
"QDial::disabled\n"
"{\n"
"	background-color: #404040;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #63676d;\n"
"    height: 18px;\n"
"    margin: 0px 18px 0 18px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #a6acb3;\n"
"	border: 1px solid #656565;\n"
"	border-radius: 2px;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #a6acb3;\n"
"    width: 18px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    ba"
                        "ckground-color: #a6acb3;\n"
"    width: 18px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-right.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-left.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #63676d;\n"
"    width: 18px;\n"
"    margin: 18px 0 18px 0;\n"
"    border: 1px solid #222222;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #a6acb3;\n"
"	border: 1px solid #656565;\n"
"	border-radius: 2px;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #a6acb3;\n"
"    height"
                        ": 18px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #a6acb3;\n"
"    height: 18px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QProgressBar-----*/\n"
"QProgressBar\n"
"{\n"
"	background-color: #000;\n"
"	color: #000;\n"
"	font-weight: bold;\n"
"	border: 0px groove #000;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar:disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color:"
                        " #656565;\n"
"	border-color: #051a39;\n"
"	border: 1px solid #000;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: #ffaf02;\n"
"	border: 0px;\n"
"	border-radius: 10px;\n"
"	color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk:disabled {\n"
"	background-color: #333;\n"
"	border: 0px;\n"
"	border-radius: 10px;\n"
"	color: #656565;\n"
"}\n"
"\n"
"\n"
"/*-----QStatusBar-----*/\n"
"QStatusBar\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(102, 115, 140, 255),stop:1 rgba(56, 63, 77, 255));\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.Russian = QAction(MainWindow)
        self.Russian.setObjectName(u"Russian")
        self.English = QAction(MainWindow)
        self.English.setObjectName(u"English")
        self.dark = QAction(MainWindow)
        self.dark.setObjectName(u"dark")
        self.light = QAction(MainWindow)
        self.light.setObjectName(u"light")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.search_runner_layout = QGridLayout()
        self.search_runner_layout.setObjectName(u"search_runner_layout")
        self.search_button = QPushButton(self.centralwidget)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setMinimumSize(QSize(200, 56))
        self.search_button.setMaximumSize(QSize(16777215, 56))
        self.search_button.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:0.486, y1:0, x2:0.505, y2:1, stop:0.00480769 rgba(0, 170, 0, 255),stop:1 rgba(0, 122, 0, 255));\n"
"	color: #ffffff;\n"
"	font-weight: bold;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #009c00;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #008800;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-radius: 3px;\n"
"	border-color: #000000;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"")

        self.search_runner_layout.addWidget(self.search_button, 1, 1, 1, 1)

        self.right_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.search_runner_layout.addItem(self.right_spacer, 1, 2, 1, 1)

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

        self.left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.search_runner_layout.addItem(self.left_spacer, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.search_runner_layout, 1, 0, 1, 1)

        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        font1 = QFont()
        font1.setPointSize(8)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.include_directories_group_box.sizePolicy().hasHeightForWidth())
        self.include_directories_group_box.setSizePolicy(sizePolicy1)
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

        self.search_parameters_layput = QVBoxLayout()
        self.search_parameters_layput.setObjectName(u"search_parameters_layput")
        self.search_type_group_box = QGroupBox(self.directories)
        self.search_type_group_box.setObjectName(u"search_type_group_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.search_type_group_box.sizePolicy().hasHeightForWidth())
        self.search_type_group_box.setSizePolicy(sizePolicy2)
        self.search_type_group_box.setMinimumSize(QSize(130, 100))
        self.search_type_group_box.setMaximumSize(QSize(130, 200))
        self.verticalLayout_3 = QVBoxLayout(self.search_type_group_box)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.hash = QRadioButton(self.search_type_group_box)
        self.search_type_button_group = QButtonGroup(MainWindow)
        self.search_type_button_group.setObjectName(u"search_type_button_group")
        self.search_type_button_group.addButton(self.hash)
        self.hash.setObjectName(u"hash")
        self.hash.setChecked(True)

        self.verticalLayout_3.addWidget(self.hash)

        self.name = QRadioButton(self.search_type_group_box)
        self.search_type_button_group.addButton(self.name)
        self.name.setObjectName(u"name")

        self.verticalLayout_3.addWidget(self.name)


        self.search_parameters_layput.addWidget(self.search_type_group_box)

        self.parameters_group_box = QGroupBox(self.directories)
        self.parameters_group_box.setObjectName(u"parameters_group_box")
        sizePolicy2.setHeightForWidth(self.parameters_group_box.sizePolicy().hasHeightForWidth())
        self.parameters_group_box.setSizePolicy(sizePolicy2)
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

        self.horizontalLayout.addWidget(self.size_suffix_box)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.depth_label = QLabel(self.parameters_group_box)
        self.depth_label.setObjectName(u"depth_label")
        self.depth_label.setMaximumSize(QSize(16777215, 33))

        self.verticalLayout_4.addWidget(self.depth_label)

        self.depth_spin_box = QSpinBox(self.parameters_group_box)
        self.depth_spin_box.setObjectName(u"depth_spin_box")
        self.depth_spin_box.setStyleSheet(u"")
        self.depth_spin_box.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.depth_spin_box.setAccelerated(True)
        self.depth_spin_box.setMinimum(0)
        self.depth_spin_box.setMaximum(10000000)
        self.depth_spin_box.setSingleStep(1)
        self.depth_spin_box.setValue(0)

        self.verticalLayout_4.addWidget(self.depth_spin_box)


        self.search_parameters_layput.addWidget(self.parameters_group_box)


        self.gridLayout_3.addLayout(self.search_parameters_layput, 0, 4, 1, 2)

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
        sizePolicy2.setHeightForWidth(self.include_masks_group_box.sizePolicy().hasHeightForWidth())
        self.include_masks_group_box.setSizePolicy(sizePolicy2)
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
        self.duplicates_tree_widget.setColumnCount(0)

        self.gridLayout_7.addWidget(self.duplicates_tree_widget, 0, 0, 1, 3)

        self.tabs.addTab(self.results, "")

        self.gridLayout.addWidget(self.tabs, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 872, 22))
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuLanguage = QMenu(self.menuSettings)
        self.menuLanguage.setObjectName(u"menuLanguage")
        self.menuTheme = QMenu(self.menuSettings)
        self.menuTheme.setObjectName(u"menuTheme")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuSettings.addAction(self.menuTheme.menuAction())
        self.menuSettings.addAction(self.menuLanguage.menuAction())
        self.menuLanguage.addAction(self.Russian)
        self.menuLanguage.addAction(self.English)
        self.menuTheme.addAction(self.dark)
        self.menuTheme.addAction(self.light)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Russian.setText(QCoreApplication.translate("MainWindow", u"TBA", None))
        self.English.setText(QCoreApplication.translate("MainWindow", u"TBA", None))
        self.dark.setText(QCoreApplication.translate("MainWindow", u"TBA", None))
        self.light.setText(QCoreApplication.translate("MainWindow", u"TBA", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        self.progress_bar.setFormat(QCoreApplication.translate("MainWindow", u"Adding Files: %p%", None))
        self.include_directories_group_box.setTitle(QCoreApplication.translate("MainWindow", u"Include Directories", None))
        self.choose_include_directories.setText(QCoreApplication.translate("MainWindow", u"Choose...", None))
        self.exclude_directories_group_box.setTitle(QCoreApplication.translate("MainWindow", u"Exclude Directories", None))
        self.choose_exclude_directories.setText(QCoreApplication.translate("MainWindow", u"Choose...", None))
        self.search_type_group_box.setTitle(QCoreApplication.translate("MainWindow", u"Search Type", None))
        self.hash.setText(QCoreApplication.translate("MainWindow", u"Hash", None))
        self.name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.parameters_group_box.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.min_file_size_label.setText(QCoreApplication.translate("MainWindow", u"Min File Size", None))
        self.min_file_size_spin_box.setSuffix("")
        self.size_suffix_box.setItemText(0, QCoreApplication.translate("MainWindow", u"b", None))
        self.size_suffix_box.setItemText(1, QCoreApplication.translate("MainWindow", u"KB", None))
        self.size_suffix_box.setItemText(2, QCoreApplication.translate("MainWindow", u"MB", None))
        self.size_suffix_box.setItemText(3, QCoreApplication.translate("MainWindow", u"GB", None))

        self.depth_label.setText(QCoreApplication.translate("MainWindow", u"Search Depth", None))
        self.depth_spin_box.setSuffix("")
        self.tabs.setTabText(self.tabs.indexOf(self.directories), QCoreApplication.translate("MainWindow", u"Directories", None))
        self.exclude_masks_group_box.setTitle(QCoreApplication.translate("MainWindow", u"Exclude Masks", None))
        self.exclude_mask_line_edit.setText("")
        self.exclude_mask_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter python-style mask here...", None))
        self.add_exclude_mask_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.include_masks_group_box.setTitle(QCoreApplication.translate("MainWindow", u"Include Masks", None))
        self.include_mask_line_edit.setText("")
        self.include_mask_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter python-style mask here...", None))
        self.add_include_mask_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.tabs.setTabText(self.tabs.indexOf(self.masks), QCoreApplication.translate("MainWindow", u"Masks", None))
        self.remove_selected_duplicates_button.setText(QCoreApplication.translate("MainWindow", u"Remove Selected", None))
        self.tabs.setTabText(self.tabs.indexOf(self.results), QCoreApplication.translate("MainWindow", u"Results", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuLanguage.setTitle(QCoreApplication.translate("MainWindow", u"Language", None))
        self.menuTheme.setTitle(QCoreApplication.translate("MainWindow", u"Theme", None))
    # retranslateUi

