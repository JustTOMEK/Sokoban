from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
import sys
from PySide2.QtCore import Qt
from map import Map
from ui_game import UiGame
from ui_level import UiChooseLevel


class ChooseLevel(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UiChooseLevel()
        self.ui.setupUi(self)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            print("W")
        if event.key() == Qt.Key_S:            
            print("S")
        if event.key() == Qt.Key_D:
            print("D")
        if event.key() == Qt.Key_A:
            print("A")
    
    

def guiMain(args):
    app = QApplication(args)
    window = ChooseLevel()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)