# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirmation_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_delete_files_dialog(object):
    def setupUi(self, delete_files_dialog):
        if not delete_files_dialog.objectName():
            delete_files_dialog.setObjectName(u"delete_files_dialog")
        delete_files_dialog.resize(352, 131)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(delete_files_dialog.sizePolicy().hasHeightForWidth())
        delete_files_dialog.setSizePolicy(sizePolicy)
        delete_files_dialog.setMinimumSize(QSize(352, 131))
        delete_files_dialog.setMaximumSize(QSize(352, 131))
        delete_files_dialog.setStyleSheet(u"")
        delete_files_dialog.setSizeGripEnabled(True)
        self.gridLayout = QGridLayout(delete_files_dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.delete_files_dialog_label = QLabel(delete_files_dialog)
        self.delete_files_dialog_label.setObjectName(u"delete_files_dialog_label")
        self.delete_files_dialog_label.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.delete_files_dialog_label, 0, 0, 1, 2, Qt.AlignHCenter|Qt.AlignVCenter)

        self.delete_files_ok_button = QPushButton(delete_files_dialog)
        self.delete_files_ok_button.setObjectName(u"delete_files_ok_button")
        self.delete_files_ok_button.setStyleSheet(u"")

        self.gridLayout.addWidget(self.delete_files_ok_button, 1, 0, 1, 1)

        self.delete_files_cancel_button = QPushButton(delete_files_dialog)
        self.delete_files_cancel_button.setObjectName(u"delete_files_cancel_button")

        self.gridLayout.addWidget(self.delete_files_cancel_button, 1, 1, 1, 1)


        self.retranslateUi(delete_files_dialog)

        QMetaObject.connectSlotsByName(delete_files_dialog)
    # setupUi

    def retranslateUi(self, delete_files_dialog):
        delete_files_dialog.setWindowTitle(QCoreApplication.translate("delete_files_dialog", u"Confirmation", None))
        self.delete_files_dialog_label.setText(QCoreApplication.translate("delete_files_dialog", u"Move selected files to thrash?", None))
        self.delete_files_ok_button.setText(QCoreApplication.translate("delete_files_dialog", u"OK", None))
        self.delete_files_cancel_button.setText(QCoreApplication.translate("delete_files_dialog", u"Cancel", None))
    # retranslateUi

