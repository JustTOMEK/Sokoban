from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout
from PySide2.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from map import Map
import sys

from ui_level import Ui_ChooseLevel
from ui_game import Ui_Game


class Game(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Game()
        self.ui.setupUi(self)
        self.ui.load_png()

def guiMain(args):
    app = QApplication(args)
    window =Game()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)