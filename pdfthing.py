import sys

from PySide6.QtWidgets import QFileDialog, QAbstractItemView
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, Qt
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.list_files.setDragDropMode(QAbstractItemView.InternalMove)
        self.ui.list_files.setDefaultDropAction(Qt.MoveAction)

        self.ui.button_addFile.clicked.connect(self.open_file_dialog)

        self.ui.button_removeFile.clicked.connect(self.remove_file)

        self.ui.button_clearList.clicked.connect(self.clear_files)

    def open_file_dialog(self):
        file_paths, _ = QFileDialog.getOpenFileNames(self, 'Pick the pdf file', '', 'PDF files (*.pdf)' )

        for path in file_paths:
            if not self.ui.list_files.findItems(path, Qt.MatchExactly):
                self.ui.list_files.addItem(path)

    def remove_file(self):
        for item in self.ui.list_files.selectedItems():
            self.ui.list_files.takeItem(self.ui.list_files.row(item))

    def clear_files(self):
        self.ui.list_files.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())