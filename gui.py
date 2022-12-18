from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout
from PySide2.QtWidgets import QMainWindow
import sys

from ui_level import Ui_ChooseLevel


class ChooseLevel(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ChooseLevel()
        self.ui.setupUi(self)

def guiMain(args):
    app = QApplication(args)
    window =ChooseLevel()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)