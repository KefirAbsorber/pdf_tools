import sys

from PySide6.QtWidgets import QFileDialog, QAbstractItemView, QApplication, QMainWindow
from PySide6.QtCore import Qt
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.list_files.setDragDropMode(QAbstractItemView.InternalMove)
        self.ui.list_files.setDefaultDropAction(Qt.MoveAction)

        self.ui.button_addFile.clicked.connect(self.file_dialog_input)

        self.ui.button_removeFile.clicked.connect(self.remove_file)

        self.ui.button_clearList.clicked.connect(self.clear_files)

        self.ui.button_choseLocation.clicked.connect(self.file_dialog_output)

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
        file_path, _ = QFileDialog.getSaveFileName(self,'Save Output PDF','','PDF Files (*.pdf);;All Files (*)')
        if file_path:
            self.ui.text_outputFile.setPlainText(file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
