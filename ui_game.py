from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from map import Map


class UiGame(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(880, 724)
        self.main_screen = QWidget(MainWindow)
        self.main_screen.setObjectName(u"centralwidget")

        self.stackedWidget = QStackedWidget(self.main_screen)
        self.stackedWidget.setObjectName(u"stackedWidget")
        
        self.stackedWidget.setGeometry(QRect(0, 0, 880, 724))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        

        self.game_screen_q = QWidget()

        self.game_screen = QVBoxLayout(self.game_screen_q)
        self.game_screen.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.game_screen_q)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(0)
        
    


        self.game_screen.addWidget(self.frame)

        self.frame_2 = QFrame(self.game_screen_q)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        
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

        self.score = QLabel(self.frame_2)
        self.score.setAlignment(Qt.AlignCenter)
        self.score.setStyleSheet(u"font-size: 20px;\n"
                                      "background-color: rgb(236, 221, 11);\n"
                                      "border-radius:10px;")

        self.horizontalLayout.addWidget(self.score)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.game_screen.addWidget(self.frame_2)



        self.level_screen_q = QWidget()
        self.level_screen_q.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.level_screen = QVBoxLayout(self.level_screen_q)
        self.level_screen.setObjectName(u"verticalLayout")
        self.horizontalLayout_level = QHBoxLayout()
        self.horizontalLayout_level.setSpacing(70)
        self.horizontalLayout_level.setObjectName(u"horizontalLayout")
        self.horizontalLayout_level.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_level.setContentsMargins(20, -1, 20, -1)

        self.buttons=[]
        for button in range(4):
                self.buttons.append(QPushButton(self.level_screen_q))
                self.buttons[button].setStyleSheet(u"font-size: 80px;\n"
                                                "background-color: rgb(236, 221, 11);\n"
                                                "border-radius:10px;")
                self.horizontalLayout_level.addWidget(self.buttons[button])


        self.level_screen.addLayout(self.horizontalLayout_level)

        self.horizontalLayout_2_level = QHBoxLayout()
        self.horizontalLayout_2_level.setSpacing(70)
        self.horizontalLayout_2_level.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2_level.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_2_level.setContentsMargins(20, -1, 20, -1)
        
        for button in range(4, 8):
                self.buttons.append(QPushButton(self.level_screen_q))
                self.buttons[button].setStyleSheet(u"font-size: 80px;\n"
                                                "background-color: rgb(236, 221, 11);\n"
                                                "border-radius:10px;")
                self.horizontalLayout_2_level.addWidget(self.buttons[button])

        self.level_screen.addLayout(self.horizontalLayout_2_level)





        self.stackedWidget.addWidget(self.level_screen_q)
        self.stackedWidget.addWidget(self.game_screen_q)

        MainWindow.setCentralWidget(self.main_screen)

        self.retranslateGame(MainWindow)
        self.retranslateLevel(MainWindow)



        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def undo(self):
        self.map.undo_move()
        self.map.change_box_coordinates()
        self.load_png()
        self.change_score()
    
    def map_set_board_size(self):
        for i in reversed(range(self.gridLayout_3.count())):
            self.gridLayout_3.removeItem(self.gridLayout_3.itemAt(i))
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.removeItem(self.gridLayout.itemAt(i))
        self.tiles = []
        for row in range(self.map._rows):
            for column in range(self.map._columns):
                self.tiles.append(QLabel(self.frame))
                self.gridLayout.addWidget(self.tiles[row * self.map._columns + column], row, column, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
    
    def reset_game(self):
        self.map = Map(self.source)
        self.load_png()
        self.change_score()

    def change_score(self):
        self.score.setText(f'Score : {self.map._move_count}')
    
    def show_won_game(self):
        dialog = QMessageBox(self.main_screen)
        dialog.setText('You won the game')
        dialog.setWindowTitle('This is the title')
        dialog.addButton('Next Level', QMessageBox.YesRole)
        dialog.addButton('Main Menu', QMessageBox.YesRole)
        dialog.buttonClicked.connect(self.onClicked)
        dialog.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.CustomizeWindowHint)
        dialog.exec_()
    
    def onClicked(self, btn):
        if btn.text() == "Next Level":
            self.stackedWidget.setCurrentWidget(self.game_screen_q)
        if btn.text() == "Main Menu":
            self.stackedWidget.setCurrentWidget(self.level_screen_q)

    def load_png(self):
        letter_to_image = {"w": "tiles_for_pyqt/wall.png",
                        "B": "tiles_for_pyqt/box_yes.png",
                        "b": "tiles_for_pyqt/box_not.png",
                        "p": "tiles_for_pyqt/player_on_floor.png",
                        "F": "tiles_for_pyqt/target_on_floor.png",
                        "P": "tiles_for_pyqt/player_on_target.png",
                        "f": "tiles_for_pyqt/floor.png"}
        for row in range(self.map._rows):
            for column in range(self.map._columns):
                pixmap = QPixmap(letter_to_image[self.map.current_map[row][column]])
                width = self.tiles[0].width()
                height = self.tiles[0].height()
                self.tiles[row * self.map._columns + column].setPixmap(pixmap.scaled(width, height))


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
    
    # retranslateUi

