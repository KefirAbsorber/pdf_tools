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
    QStatusBar, QTabWidget, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(574, 590)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 651, 561))
        self.tabWidget.setAcceptDrops(False)
        self.tab_merger = QWidget()
        self.tab_merger.setObjectName(u"tab_merger")
        self.widget_merger = QWidget(self.tab_merger)
        self.widget_merger.setObjectName(u"widget_merger")
        self.widget_merger.setGeometry(QRect(0, 0, 631, 511))
        self.button_merge = QPushButton(self.widget_merger)
        self.button_merge.setObjectName(u"button_merge")
        self.button_merge.setGeometry(QRect(240, 370, 90, 51))
        self.label = QLabel(self.widget_merger)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 440, 91, 20))
        self.button_clearList = QPushButton(self.widget_merger)
        self.button_clearList.setObjectName(u"button_clearList")
        self.button_clearList.setGeometry(QRect(410, 0, 151, 51))
        self.button_addFile = QPushButton(self.widget_merger)
        self.button_addFile.setObjectName(u"button_addFile")
        self.button_addFile.setGeometry(QRect(0, 0, 151, 51))
        self.list_files = QListWidget(self.widget_merger)
        self.list_files.setObjectName(u"list_files")
        self.list_files.setGeometry(QRect(30, 80, 511, 281))
        self.button_removeFile = QPushButton(self.widget_merger)
        self.button_removeFile.setObjectName(u"button_removeFile")
        self.button_removeFile.setGeometry(QRect(210, 0, 151, 51))
        self.button_choseLocation = QPushButton(self.widget_merger)
        self.button_choseLocation.setObjectName(u"button_choseLocation")
        self.button_choseLocation.setGeometry(QRect(0, 410, 121, 29))
        self.label_2 = QLabel(self.widget_merger)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 91, 20))
        self.text_outputFile = QTextEdit(self.widget_merger)
        self.text_outputFile.setObjectName(u"text_outputFile")
        self.text_outputFile.setGeometry(QRect(30, 460, 511, 31))
        self.tabWidget.addTab(self.tab_merger, "")
        self.tab_splitter = QWidget()
        self.tab_splitter.setObjectName(u"tab_splitter")
        self.widget_splitter = QWidget(self.tab_splitter)
        self.widget_splitter.setObjectName(u"widget_splitter")
        self.widget_splitter.setGeometry(QRect(0, 0, 631, 531))
        self.tabWidget.addTab(self.tab_splitter, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 574, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_merge.setText(QCoreApplication.translate("MainWindow", u"Merge ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Output file", None))
        self.button_clearList.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.button_addFile.setText(QCoreApplication.translate("MainWindow", u"Add file", None))
        self.button_removeFile.setText(QCoreApplication.translate("MainWindow", u"Remove selected", None))
        self.button_choseLocation.setText(QCoreApplication.translate("MainWindow", u"Chose location", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Input files", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_merger), QCoreApplication.translate("MainWindow", u"Merger", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_splitter), QCoreApplication.translate("MainWindow", u"Splitter", None))
    # retranslateUi

