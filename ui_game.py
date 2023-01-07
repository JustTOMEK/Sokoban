from PySide2.QtCore import QRect, QCoreApplication
from PySide2.QtGui import Qt, QPixmap
from PySide2.QtWidgets import (QWidget, QSizePolicy, QStackedWidget,
                               QVBoxLayout, QFrame, QGridLayout,
                               QHBoxLayout, QPushButton, QLabel,
                               QLayout, QMessageBox)


from map import Map
from functools import partial


class UiGame(object):

    def setupUi(self, MainWindow):
        self.state = "level"
        self.unlocked_levels = [1, 0, 0, 0, 0, 0, 0, 0]
        MainWindow.setFixedSize(880, 724)
        self.main_screen = QWidget(MainWindow)
        self.stackedWidget = QStackedWidget(self.main_screen)
        self.stackedWidget.setGeometry(QRect(0, 0, 880, 724))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        # Here start game_screen widgets
        self.game_screen_q = QWidget()
        self.game_screen = QVBoxLayout(self.game_screen_q)
        self.frame = QFrame(self.game_screen_q)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout = QGridLayout()
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(0)
        self.game_screen.addWidget(self.frame)
        self.frame_2 = QFrame(self.game_screen_q)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.horizontalLayout = QHBoxLayout()
        self.undo_move = QPushButton(self.frame_2)
        self.undo_move.setStyleSheet(u"font-size: 20px;\n"
                                     "background-color: rgb(236, 221, 11);\n"
                                     "border-radius:10px;")
        self.undo_move.clicked.connect(self.undo)
        self.horizontalLayout.addWidget(self.undo_move)

        self.reset = QPushButton(self.frame_2)
        self.reset.setStyleSheet(u"font-size: 20px;\n"
                                 "background-color: rgb(236, 221, 11);\n"
                                 "border-radius:10px;")
        self.reset.clicked.connect(self.reset_game)
        self.horizontalLayout.addWidget(self.reset)
        self.quit = QPushButton(self.frame_2)
        self.quit.setStyleSheet(u"font-size: 20px;\n"
                                "background-color: rgb(236, 221, 11);\n"
                                "border-radius:10px;")
        self.horizontalLayout.addWidget(self.quit)
        self.quit.clicked.connect(self.back_to_level)
        self.score = QLabel(self.frame_2)
        self.score.setAlignment(Qt.AlignCenter)
        self.score.setStyleSheet(u"font-size: 20px;\n"
                                 "background-color: rgb(236, 221, 11);\n"
                                 "border-radius:10px;")
        self.horizontalLayout.addWidget(self.score)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.game_screen.addWidget(self.frame_2)
        # Here starts level screen
        self.level_screen_q = QWidget()
        self.level_screen_q.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.level_screen = QVBoxLayout(self.level_screen_q)
        self.horizontalLayout_caption = QHBoxLayout()
        self.horizontalLayout_caption.setSpacing(70)
        self.horizontalLayout_caption.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_caption.setContentsMargins(20, -1, 20, -1)
        self.choose_caption = QPushButton()
        self.choose_caption.setStyleSheet(u"font-size: 80px;\n"
                                          "background-color: rgb(250, 0, 0);\n"
                                          "border-radius:10px;" "padding :15px;")
        self.choose_caption.setText("Choose Level")
        self.choose_caption.resize(100, 100)
        self.help = QPushButton()
        self.help.setStyleSheet(u"font-size: 40px;"
                                "background-color: rgb(250, 0, 0);"
                                "border-radius:10px;"
                                "padding :15px;")
        self.help.setText("Help")
        self.help.clicked.connect(self.show_help)
        self.horizontalLayout_caption.addWidget(self.choose_caption)
        self.horizontalLayout_caption.addWidget(self.help)
        self.level_screen.addLayout(self.horizontalLayout_caption)
        self.horizontalLayout_level = QHBoxLayout()
        self.horizontalLayout_level.setSpacing(70)
        self.horizontalLayout_level.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_level.setContentsMargins(20, -1, 20, -1)
        self.buttons = []
        for button in range(4):
            self.buttons.append(QPushButton(self.level_screen_q))
            self.buttons[button].setStyleSheet(u"font-size: 80px;\n"
                                               "background-color: rgb(236, 221, 11);\n"
                                               "border-radius:10px;")
            self.buttons[button].clicked.connect(partial(self.choose_level, button + 1))
            self.horizontalLayout_level.addWidget(self.buttons[button])
        self.level_screen.addLayout(self.horizontalLayout_level)
        self.horizontalLayout_2_level = QHBoxLayout()
        self.horizontalLayout_2_level.setSpacing(70)
        self.horizontalLayout_2_level.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_2_level.setContentsMargins(20, -1, 20, -1)
        for button in range(4, 8):
            self.buttons.append(QPushButton(self.level_screen_q))
            self.buttons[button].setStyleSheet(u"font-size: 80px;\n"
                                               "background-color: rgb(236, 221, 11);\n"
                                               "border-radius:10px;")
            self.buttons[button].clicked.connect(partial(self.choose_level, button + 1))
            self.horizontalLayout_2_level.addWidget(self.buttons[button])
        self.level_screen.addLayout(self.horizontalLayout_2_level)
        self.stackedWidget.addWidget(self.level_screen_q)
        self.stackedWidget.addWidget(self.game_screen_q)
        MainWindow.setCentralWidget(self.main_screen)
        self.retranslateGame(MainWindow)
        self.retranslateLevel(MainWindow)

    def back_to_level(self):
        self.stackedWidget.setCurrentWidget(self.level_screen_q)
        self.state = "level"

    def undo(self):
        self.map.undo_move()
        self.load_png()
        self.change_score()

    def map_set_board_size(self):
        for i in reversed(range(self.gridLayout_3.count())):
            self.gridLayout_3.removeItem(self.gridLayout_3.itemAt(i))
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.removeItem(self.gridLayout.itemAt(i))
        self.tiles = []
        for row in range(self.map.rows()):
            for column in range(self.map.columns()):
                self.tiles.append(QLabel(self.frame))
                self.gridLayout.addWidget(self.tiles[row * self.map.columns() + column], row, column, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

    def reset_game(self):
        file = open(self.source, "r")
        self.map = Map(file.read())
        self.load_png()
        self.change_score()

    def change_score(self):
        self.score.setText(f'Score : {self.map.move_count()}')

    def show_help(self):
        dialog = QMessageBox(self.main_screen)
        dialog.setWindowTitle("Help")
        dialog.setText('To finish Sokoban map move all boxes to targets. \n'
                       'At the beggining only level 1 is unlocked.\n'
                       'When level is finished the next one is unlocked.\n'
                       'Game can be reseted at all times.\n'
                       'Move can be undone at all times.\n'
                       'Move in game using WASD keys.\n')
        dialog.addButton('Back to level selection', QMessageBox.YesRole)
        dialog.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.CustomizeWindowHint)
        dialog.exec_()

    def show_won_game(self):
        dialog = QMessageBox(self.main_screen)
        dialog.setWindowTitle(f'You finished level {self.level}')
        if self.level != 8:
            self.unlocked_levels[self.level] = 1
            dialog.addButton('Next Level', QMessageBox.YesRole)
        else:
            dialog.setText('There is no next level. You finished the game congratulations.')
        dialog.addButton('Main Menu', QMessageBox.YesRole)
        dialog.buttonClicked.connect(self.onClicked)
        dialog.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.CustomizeWindowHint)
        dialog.exec_()

    def show_not_unlocked(self):
        dialog = QMessageBox(self.main_screen)
        dialog.setWindowTitle("You have not unlocked this level")
        dialog.setText('In order to play this level finish all previous ones.')
        dialog.addButton('Choose another level', QMessageBox.YesRole)
        dialog.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.CustomizeWindowHint)
        dialog.exec_()

    def onClicked(self, btn):
        if btn.text() == "Next Level":
            self.next_level(self.level + 1)
        if btn.text() == "Main Menu":
            self.stackedWidget.setCurrentWidget(self.level_screen_q)

    def load_png(self):
        no_targets = {"wall": "tiles_for_pyqt/wall.png",
                      "box": "tiles_for_pyqt/box_not.png",
                      "player": "tiles_for_pyqt/player_on_floor.png",
                      "floor": "tiles_for_pyqt/floor.png"}
        targets = {"box": "tiles_for_pyqt/box_yes.png",
                   "floor": "tiles_for_pyqt/target_on_floor.png",
                   "player": "tiles_for_pyqt/player_on_target.png"}
        for row in range(self.map.rows()):
            for column in range(self.map.columns()):
                if self.map.tiles()[row][column].is_target():
                    pixmap = QPixmap(targets[self.map.tiles()[row][column].type()])
                else:
                    pixmap = QPixmap(no_targets[self.map.tiles()[row][column].type()])
                width = self.tiles[0].width()
                height = self.tiles[0].height()
                self.tiles[row * self.map._columns + column].setPixmap(pixmap.scaled(width, height))

    def choose_level(self, level):
        if self.unlocked_levels[level - 1]:
            self.level = level
            file = open(f'maps/map_{level}.txt', "r")
            self.map = Map(file.read())
            self.map_set_board_size()
            self.stackedWidget.setCurrentWidget(self.game_screen_q)
            self.source = f'maps/map_{level}.txt'
            self.change_score()
            self.tiles[0].resize(self.frame.width() / self.map.columns(), self.frame.height() / self.map.rows())
            self.load_png()
            self.state = "game"
        else:
            self.show_not_unlocked()

    def next_level(self, level):
        self.level = level
        file = open(f'maps/map_{level}.txt', "r")
        self.map = Map(file.read())
        self.map_set_board_size()
        self.source = f'maps/map_{level}.txt'
        self.change_score()
        self.state = "game"
        self.tiles[0].resize(self.frame.width() / self.map.columns(), self.frame.height() / self.map.rows())
        self.load_png()

    def retranslateGame(self, MainWindow):
        MainWindow.setWindowTitle("Sokoban")
        self.undo_move.setText("Undo Move")
        self.reset.setText("Reset")
        self.quit.setText("Quit")
        self.score.setText("Score : 0")

    def retranslateLevel(self, ChooseLevel):
        ChooseLevel.setWindowTitle(QCoreApplication.translate("ChooseLevel", u"Sokoban", None))
        for level, button in enumerate(self.buttons):
            button.setText(str(level + 1))
