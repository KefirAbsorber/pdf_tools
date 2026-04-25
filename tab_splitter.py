from PySide6.QtWidgets import QFileDialog, QAbstractItemView, QMessageBox, QWidget, QTableWidgetItem
from PySide6.QtCore import Qt

from pypdf import PdfWriter, PdfReader


class SplitterTab(QWidget):
    def __init__(self, ui, parent=None):
        # class
        super().__init__(parent)
        self.ui = ui

        self.ui.table_outputFiles.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.ui.text_inputFile.textChanged.connect(self.update_pages)
        self.ui.text_inputFile.textChanged.connect(self.clear_files)

        # buttons
        self.ui.button_choseFile.clicked.connect(self.set_inputFile)

        self.ui.button_outputPicker.clicked.connect(self.set_outputFile)

        self.ui.button_clearList_2.clicked.connect(self.clear_files)

        self.ui.button_addFile_2.clicked.connect(self.append_table)

        self.ui.button_removeFile_2.clicked.connect(self.remove_file)

        self.ui.button_split.clicked.connect(self.split_files)

    def set_inputFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Pick the pdf file', '', 'PDF files (*.pdf)')
        self.ui.text_inputFile.setText(file_path)

    def update_pages(self):
        # get the number of pages
        file_path = self.ui.text_inputFile.toPlainText()
        try:
            reader = PdfReader(file_path)
            pages_number = len(reader.pages)

            # set number of pages in input ui
            self.ui.text_pagesNumber.setText(str(pages_number))

            # set number of pages in output combo
            self.ui.combo_startingPage.clear()
            self.ui.combo_endingPage.clear()
            self.ui.combo_startingPage.addItems([str(i) for i in range(1, pages_number + 1)])
            self.ui.combo_endingPage.addItems([str(i) for i in range(1, pages_number + 1)])
        except FileNotFoundError:
            self.ui.text_pagesNumber.clear()
            self.ui.combo_startingPage.clear()
            self.ui.combo_endingPage.clear()

    def set_outputFile(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Output PDF', '', 'PDF Files (*.pdf);;All Files (*)')
        self.ui.button_outputPicker.setText(file_path)

    def clear_files(self):
        self.ui.table_outputFiles.setRowCount(0)

    def append_table(self):
        start_page = self.ui.combo_startingPage.currentText()
        end_page = self.ui.combo_endingPage.currentText()
        file_path = self.ui.button_outputPicker.text()

        # check if all filled
        if start_page == "" or end_page == "" or file_path == "" or file_path == "Chose an output file":
            QMessageBox.information(None, 'Error', 'Please fill all required fields.')
            return

        # check if names are unique
        if not self.ui.table_outputFiles.findItems(file_path, Qt.MatchExactly):
            row = self.ui.table_outputFiles.rowCount()
            self.ui.table_outputFiles.insertRow(row)

            self.ui.table_outputFiles.setItem(row, 0, QTableWidgetItem(start_page))
            self.ui.table_outputFiles.setItem(row, 1, QTableWidgetItem(end_page))
            self.ui.table_outputFiles.setItem(row, 2, QTableWidgetItem(file_path))
        else:
            QMessageBox.information(None, 'Error', 'File name already chosen.')
            return

        # reset UI
        self.ui.button_outputPicker.setText("Chose an output file")
        self.ui.combo_startingPage.setCurrentIndex(0)
        self.ui.combo_endingPage.setCurrentIndex(0)

    def remove_file(self):
        for item in self.ui.table_outputFiles.selectedItems():
            self.ui.table_outputFiles.removeRow(self.ui.table_outputFiles.row(item))

    def split_files(self):
        reader = PdfReader(self.ui.text_inputFile.toPlainText())

        for row in range(self.ui.table_outputFiles.rowCount()):
            writer = PdfWriter()
            start_page = int(self.ui.table_outputFiles.item(row, 0).text()) - 1
            end_page = int(self.ui.table_outputFiles.item(row, 1).text())
            output_path = self.ui.table_outputFiles.item(row, 2).text()

            for i in range(start_page, end_page):
                writer.add_page(reader.pages[i])

            writer.write(output_path)

        self.clear_files()
        QMessageBox.information(None, 'Succes', 'Splitting successful.')