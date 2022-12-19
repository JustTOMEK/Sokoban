from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
import sys
from PySide2.QtCore import Qt
from map import Map
from ui_game import Ui_Game


class Game(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Game()
        self.ui.setupUi(self)
        self.map = Map("maps/map_1.txt")
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.map.move("U")
        if event.key() == Qt.Key_Down:
            self.map.move("D")
        if event.key() == Qt.Key_Right:
            self.map.move("R")
        if event.key() == Qt.Key_Left:
            self.map.move("L")
        self.ui.load_png(self.map.current_map)

def guiMain(args):
    app = QApplication(args)
    window =Game()
    window.ui.load_png(window.map.current_map)
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)