import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Qt
from ui_game_with_functions import UiGameWithFunctions


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UiGameWithFunctions()
        self.ui.create_widgets(self)

    def keyPressEvent(self, event):
        if self.ui.state == "game":
            if event.key() == Qt.Key_W:
                self.ui.map.move("Up")
            if event.key() == Qt.Key_S:
                self.ui.map.move("Down")
            if event.key() == Qt.Key_D:
                self.ui.map.move("Right")
            if event.key() == Qt.Key_A:
                self.ui.map.move("Left")
            self.ui.load_png()
            self.ui.change_score()
            if self.ui.map.check_if_win():
                self.ui.show_won_game()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.resize(720, 500)
    main_win.show()
    sys.exit(app.exec_())
