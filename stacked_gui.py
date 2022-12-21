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
        self.state = "level"
        self.ui.stackedWidget.setCurrentWidget(self.ui.level_screen_q)

        self.ui.buttons[0].clicked.connect(self.choose_level_1)
        self.ui.buttons[1].clicked.connect(self.choose_level_2)
        self.ui.buttons[2].clicked.connect(self.choose_level_3)
        self.ui.buttons[3].clicked.connect(self.choose_level_4)
        self.ui.buttons[4].clicked.connect(self.choose_level_5)
        self.ui.buttons[5].clicked.connect(self.choose_level_6)
        self.ui.buttons[6].clicked.connect(self.choose_level_7)
        self.ui.buttons[7].clicked.connect(self.choose_level_8)
        self.ui.quit.clicked.connect(self.back_to_level)

    def back_to_level(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.level_screen_q)
        self.state = "level"

    def choose_level_1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.game_screen_q)
        self.ui.map = Map("maps/map_1.txt")
        self.ui.source = "maps/map_1.txt"
        self.ui.change_score()
        self.ui.load_png()
        self.state = "game"
    
    def choose_level_2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.game_screen_q)
        self.ui.map = Map("maps/map_2.txt")
        self.ui.source = "maps/map_2.txt"
        self.ui.change_score()
        self.ui.load_png()
        self.state = "game"
    
    def choose_level_3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.game_screen_q)
        self.ui.map = Map("maps/map_3.txt")
        self.ui.source = "maps/map_3.txt"
        self.ui.change_score()
        self.ui.load_png()
        self.state = "game"
    
    def choose_level_4(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.game_screen_q)
        self.ui.map = Map("maps/map_4.txt")
        self.ui.source = "maps/map_4.txt"
        self.ui.change_score()
        self.ui.load_png()
        self.state = "game"
    
    def choose_level_5(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.game_screen_q)
        self.ui.map = Map("maps/map_5.txt")
        self.ui.source = "maps/map_5.txt"
        self.ui.change_score()
        self.ui.load_png()
        self.state = "game"
     
    def choose_level_6(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.game_screen_q)
        self.ui.map = Map("maps/map_6.txt")
        self.ui.source = "maps/map_6.txt"
        self.ui.change_score()
        self.ui.load_png()
        self.state = "game"
    
    def choose_level_7(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.game_screen_q)
        self.ui.map = Map("maps/map_7.txt")
        self.ui.source = "maps/map_7.txt"
        self.ui.change_score()
        self.ui.load_png()
        self.state = "game"

    def choose_level_8(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.game_screen_q)
        self.ui.map = Map("maps/map_8.txt")
        self.ui.source = "maps/map_8.txt"
        self.ui.change_score()
        self.ui.load_png()
        self.state = "game"
    
    def keyPressEvent(self, event):
        if self.state == "game":
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