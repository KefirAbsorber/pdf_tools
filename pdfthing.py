import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_mainwindow import Ui_MainWindow
from tab_merger import MergerTab
from tab_splitter import SplitterTab

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.merger_tab = MergerTab(self.ui)
        self.splitter_tab = SplitterTab(self.ui)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
