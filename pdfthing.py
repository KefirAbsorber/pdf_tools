import sys

from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.file_list = []

        self.ui.button_addFile.clicked.connect(self.open_file_dialog)

        self.ui.button_removeFile.clicked.connect(self.remove_file)

    def open_file_dialog(self):
        file_paths, _ = QFileDialog.getOpenFileNames(self, 'Pick the pdf file', '', 'PDF files (*.pdf)' )

        for path in file_paths:
            if path not in self.file_list:
                self.file_list.append(path)
                self.ui.list_files.addItem(path)
    def remove_file(self):
        pass

    def clear_files(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())