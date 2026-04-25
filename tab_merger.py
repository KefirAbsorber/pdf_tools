from PySide6.QtWidgets import QFileDialog, QAbstractItemView, QMessageBox, QWidget
from PySide6.QtCore import Qt
from pypdf import PdfWriter

class MergerTab(QWidget):
    def __init__(self, ui, parent=None):
        #class
        super().__init__(parent)
        self.ui = ui

        #list
        self.ui.list_files.setDragDropMode(QAbstractItemView.InternalMove)
        self.ui.list_files.setDefaultDropAction(Qt.MoveAction)

        #text
        self.ui.text_outputFile.setPlaceholderText('Insert the output file location')

        #buttons
        self.ui.button_addFile.clicked.connect(self.file_dialog_input)

        self.ui.button_removeFile.clicked.connect(self.remove_file)

        self.ui.button_clearList.clicked.connect(self.clear_files)

        self.ui.button_choseLocation.clicked.connect(self.file_dialog_output)

        self.ui.button_merge.clicked.connect(self.merge_files)

    def file_dialog_input(self):
        file_paths, _ = QFileDialog.getOpenFileNames(self, 'Pick the pdf file', '', 'PDF files (*.pdf)')

        for path in file_paths:
            if not self.ui.list_files.findItems(path, Qt.MatchExactly):
                self.ui.list_files.addItem(path)

    def remove_file(self):
        for item in self.ui.list_files.selectedItems():
            self.ui.list_files.takeItem(self.ui.list_files.row(item))

    def clear_files(self):
        self.ui.list_files.clear()

    def file_dialog_output(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Output PDF', '', 'PDF Files (*.pdf);;All Files (*)')
        if file_path:
            self.ui.text_outputFile.setPlainText(file_path)

    def merge_files(self):
        # check if all needed field are filled
        if self.ui.list_files.count() == 0 or self.ui.text_outputFile.toPlainText() == '':
            QMessageBox.information(None, 'Error', 'Please fill all required fields.')
            return

        # merge
        merger = PdfWriter()
        for i in range(self.ui.list_files.count()):
            merger.append(self.ui.list_files.item(i).text())
        merger.write(self.ui.text_outputFile.toPlainText())

        # clear app
        QMessageBox.information(None, 'Succes', 'Merge successful.')
        self.ui.text_outputFile.setPlainText('')
        self.ui.list_files.clear()