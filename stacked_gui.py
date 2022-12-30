import sys
from PySide2.QtWidgets import QApplication 
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Qt

from ui_game import UiGame

from map import Map

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UiGame()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.level_screen_q)

        
        self.ui.quit.clicked.connect(self.back_to_level)

    def back_to_level(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.level_screen_q)
        self.ui.state = "level"
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_B:
                print(self.ui.unlocked_levels)
        if self.ui.state == "game":
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
            if self.ui.map.check_if_win():
                self.ui.show_won_game()
 
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())