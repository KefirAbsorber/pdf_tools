from PySide6.QtWidgets import QFileDialog, QAbstractItemView, QMessageBox, QWidget
from PySide6.QtCore import Qt
from pypdf import PdfWriter, PdfReader


class SplitterTab(QWidget):
    def __init__(self, ui, parent=None):
        #class
        super().__init__(parent)
        self.ui = ui

        #buttons
        self.ui.button_choseFile.clicked.connect(self.set_inputFile)

        self.ui.button_outputPicker.clicked.connect(self.set_outputFile)

    def set_inputFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Pick the pdf file', '', 'PDF files (*.pdf)')
        self.ui.text_inputFile.setText(file_path)

        #get the number of pages
        reader = PdfReader(file_path)
        pages_number = len(reader.pages)

        #set number of pages in input ui
        self.ui.text_pagesNumber.setText(str(pages_number))

        #set number of pages in output combo
        self.ui.combo_startingPage.clear()
        self.ui.combo_endingPage.clear()
        self.ui.combo_startingPage.addItems([str(i) for i in range(1, pages_number + 1)])
        self.ui.combo_endingPage.addItems([str(i) for i in range(1, pages_number + 1)])

    def set_outputFile(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Output PDF', '', 'PDF Files (*.pdf);;All Files (*)')
        self.ui.button_outputPicker.setText(file_path)

