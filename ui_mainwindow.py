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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(665, 608)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button_addFile = QPushButton(self.centralwidget)
        self.button_addFile.setObjectName(u"button_addFile")
        self.button_addFile.setGeometry(QRect(40, 20, 151, 51))
        self.list_files = QListWidget(self.centralwidget)
        self.list_files.setObjectName(u"list_files")
        self.list_files.setGeometry(QRect(70, 100, 511, 281))
        self.button_removeFile = QPushButton(self.centralwidget)
        self.button_removeFile.setObjectName(u"button_removeFile")
        self.button_removeFile.setGeometry(QRect(250, 20, 151, 51))
        self.button_clearList = QPushButton(self.centralwidget)
        self.button_clearList.setObjectName(u"button_clearList")
        self.button_clearList.setGeometry(QRect(450, 20, 151, 51))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 460, 91, 20))
        self.button_merge = QPushButton(self.centralwidget)
        self.button_merge.setObjectName(u"button_merge")
        self.button_merge.setGeometry(QRect(280, 390, 90, 51))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 80, 91, 20))
        self.button_choseLocation = QPushButton(self.centralwidget)
        self.button_choseLocation.setObjectName(u"button_choseLocation")
        self.button_choseLocation.setGeometry(QRect(40, 430, 121, 29))
        self.text_outputFile = QTextEdit(self.centralwidget)
        self.text_outputFile.setObjectName(u"text_outputFile")
        self.text_outputFile.setGeometry(QRect(70, 480, 511, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 665, 25))
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Output file", None))
        self.button_merge.setText(QCoreApplication.translate("MainWindow", u"Merge ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Input files", None))
        self.button_choseLocation.setText(QCoreApplication.translate("MainWindow", u"Chose location", None))
    # retranslateUi

