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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QHeaderView,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(567, 603)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 571, 581))
        self.tabWidget.setAcceptDrops(False)
        self.tab_merger = QWidget()
        self.tab_merger.setObjectName(u"tab_merger")
        self.widget_merger = QWidget(self.tab_merger)
        self.widget_merger.setObjectName(u"widget_merger")
        self.widget_merger.setGeometry(QRect(0, 0, 571, 521))
        self.button_merge = QPushButton(self.widget_merger)
        self.button_merge.setObjectName(u"button_merge")
        self.button_merge.setGeometry(QRect(230, 460, 90, 51))
        self.label = QLabel(self.widget_merger)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 400, 91, 20))
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
        self.button_choseLocation.setGeometry(QRect(0, 370, 121, 29))
        self.label_2 = QLabel(self.widget_merger)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 91, 20))
        self.text_outputFile = QTextEdit(self.widget_merger)
        self.text_outputFile.setObjectName(u"text_outputFile")
        self.text_outputFile.setGeometry(QRect(30, 420, 511, 31))
        self.tabWidget.addTab(self.tab_merger, "")
        self.tab_splitter = QWidget()
        self.tab_splitter.setObjectName(u"tab_splitter")
        self.widget_splitter = QWidget(self.tab_splitter)
        self.widget_splitter.setObjectName(u"widget_splitter")
        self.widget_splitter.setGeometry(QRect(0, 0, 631, 531))
        self.text_inputFile = QTextEdit(self.widget_splitter)
        self.text_inputFile.setObjectName(u"text_inputFile")
        self.text_inputFile.setGeometry(QRect(80, 50, 461, 31))
        self.label_3 = QLabel(self.widget_splitter)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 30, 91, 20))
        self.button_choseFile = QPushButton(self.widget_splitter)
        self.button_choseFile.setObjectName(u"button_choseFile")
        self.button_choseFile.setGeometry(QRect(0, 0, 121, 29))
        self.label_4 = QLabel(self.widget_splitter)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 30, 91, 20))
        self.text_pagesNumber = QTextEdit(self.widget_splitter)
        self.text_pagesNumber.setObjectName(u"text_pagesNumber")
        self.text_pagesNumber.setGeometry(QRect(10, 50, 51, 31))
        self.text_pagesNumber.setReadOnly(True)
        self.table_outputFiles = QTableWidget(self.widget_splitter)
        if (self.table_outputFiles.columnCount() < 3):
            self.table_outputFiles.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_outputFiles.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_outputFiles.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_outputFiles.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_outputFiles.setObjectName(u"table_outputFiles")
        self.table_outputFiles.setGeometry(QRect(10, 230, 531, 201))
        self.table_outputFiles.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.button_removeFile_2 = QPushButton(self.widget_splitter)
        self.button_removeFile_2.setObjectName(u"button_removeFile_2")
        self.button_removeFile_2.setGeometry(QRect(190, 170, 151, 51))
        self.button_clearList_2 = QPushButton(self.widget_splitter)
        self.button_clearList_2.setObjectName(u"button_clearList_2")
        self.button_clearList_2.setGeometry(QRect(400, 170, 151, 51))
        self.button_addFile_2 = QPushButton(self.widget_splitter)
        self.button_addFile_2.setObjectName(u"button_addFile_2")
        self.button_addFile_2.setGeometry(QRect(0, 170, 151, 51))
        self.combo_startingPage = QComboBox(self.widget_splitter)
        self.combo_startingPage.setObjectName(u"combo_startingPage")
        self.combo_startingPage.setGeometry(QRect(0, 130, 82, 31))
        self.combo_endingPage = QComboBox(self.widget_splitter)
        self.combo_endingPage.setObjectName(u"combo_endingPage")
        self.combo_endingPage.setGeometry(QRect(80, 130, 82, 31))
        self.button_split = QPushButton(self.widget_splitter)
        self.button_split.setObjectName(u"button_split")
        self.button_split.setGeometry(QRect(150, 450, 261, 51))
        self.label_5 = QLabel(self.widget_splitter)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 100, 201, 20))
        self.button_outputPicker = QPushButton(self.widget_splitter)
        self.button_outputPicker.setObjectName(u"button_outputPicker")
        self.button_outputPicker.setGeometry(QRect(160, 130, 381, 31))
        self.tabWidget.addTab(self.tab_splitter, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 567, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Input file", None))
        self.button_choseFile.setText(QCoreApplication.translate("MainWindow", u"Chose a file", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Pages", None))
        ___qtablewidgetitem = self.table_outputFiles.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Starting page", None));
        ___qtablewidgetitem1 = self.table_outputFiles.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Ending Page", None));
        ___qtablewidgetitem2 = self.table_outputFiles.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Output file", None));
        self.button_removeFile_2.setText(QCoreApplication.translate("MainWindow", u"Remove selected", None))
        self.button_clearList_2.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.button_addFile_2.setText(QCoreApplication.translate("MainWindow", u"Add file", None))
        self.button_split.setText(QCoreApplication.translate("MainWindow", u"Split", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Output files", None))
        self.button_outputPicker.setText(QCoreApplication.translate("MainWindow", u"Chose an output file", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_splitter), QCoreApplication.translate("MainWindow", u"Splitter", None))
    # retranslateUi

