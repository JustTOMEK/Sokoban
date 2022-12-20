import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow

from ui_game import UiGame

from map import Map

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = UiGame()
        self.ui.setupUi(self.main_win)

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

    def choose_level_1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.game_screen_q)
        self.ui.map = Map("maps/map_1.txt")
        self.ui.load_png()
    
    def choose_level_2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.game_screen_q)
        self.ui.map = Map("maps/map_2.txt")
        self.ui.load_png()
    
    def choose_level_3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.game_screen_q)
        self.ui.map = Map("maps/map_3.txt")
        self.ui.load_png()
    
    def choose_level_4(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.game_screen_q)
        self.ui.map = Map("maps/map_4.txt")
        self.ui.load_png()
    
    def choose_level_5(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.game_screen_q)
        self.ui.map = Map("maps/map_5.txt")
        self.ui.load_png()
    
    def choose_level_6(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.game_screen_q)
        self.ui.map = Map("maps/map_6.txt")
        self.ui.load_png()
    
    def choose_level_7(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.game_screen_q)
        self.ui.map = Map("maps/map_7.txt")
        self.ui.load_png()

    def choose_level_8(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.game_screen_q)
        self.ui.map = Map("maps/map_8.txt")
        self.ui.load_png()

    def show(self):
        self.main_win.show()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())