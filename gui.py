from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
import sys
from PySide2.QtCore import Qt
from map import Map
from ui_game import UiGame
from ui_level import UiChooseLevel

class Game(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UiGame("maps/map_1.txt")
        self.ui.setupUi(self)
        self.ui.load_png()
    
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            self.ui.map.move("U")
        if event.key() == Qt.Key_S:            
            self.ui.map.move("D")
        if event.key() == Qt.Key_D:
            self.ui.map.move("R")
        if event.key() == Qt.Key_A:
            self.ui.map.move("L")
        self.ui.map.change_box_coordinates()
        self.ui.load_png()  
        self.ui.change_score()


class ChooseLevel(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UiChooseLevel()
        self.ui.setupUi(self)
    
    

def guiMain(args):
    app = QApplication(args)
    window = ChooseLevel()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)