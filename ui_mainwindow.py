# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(679, 455)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button_addFile = QPushButton(self.centralwidget)
        self.button_addFile.setObjectName(u"button_addFile")
        self.button_addFile.setGeometry(QRect(40, 20, 101, 29))
        self.list_files = QListWidget(self.centralwidget)
        self.list_files.setObjectName(u"list_files")
        self.list_files.setGeometry(QRect(40, 60, 391, 192))
        self.button_removeFile = QPushButton(self.centralwidget)
        self.button_removeFile.setObjectName(u"button_removeFile")
        self.button_removeFile.setGeometry(QRect(180, 20, 101, 29))
        self.button_clearList = QPushButton(self.centralwidget)
        self.button_clearList.setObjectName(u"button_clearList")
        self.button_clearList.setGeometry(QRect(330, 20, 90, 29))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 679, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_addFile.setText(QCoreApplication.translate("MainWindow", u"Add file", None))
        self.button_removeFile.setText(QCoreApplication.translate("MainWindow", u"Remove selected", None))
        self.button_clearList.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi

