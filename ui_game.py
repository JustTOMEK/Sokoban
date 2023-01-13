from PySide2.QtCore import QRect
from PySide2.QtGui import Qt
from PySide2.QtWidgets import (QWidget, QSizePolicy, QStackedWidget,
                               QVBoxLayout, QFrame, QGridLayout,
                               QHBoxLayout, QPushButton, QLabel,
                               QLayout)

from functools import partial


class UiGame(object):
    def create_widgets(self, MainWindow):
        self.state = "level"
        self.unlocked_levels = [1, 0, 0, 0, 0, 0, 0, 0]
        MainWindow.setWindowTitle("Sokoban")
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
        self.undo_move.setText("Undo Move")
        self.horizontalLayout.addWidget(self.undo_move)

        self.reset = QPushButton(self.frame_2)
        self.reset.setStyleSheet(u"font-size: 20px;\n"
                                 "background-color: rgb(236, 221, 11);\n"
                                 "border-radius:10px;")
        self.reset.clicked.connect(self.reset_game)
        self.reset.setText("Reset")
        self.horizontalLayout.addWidget(self.reset)
        self.quit = QPushButton(self.frame_2)
        self.quit.setStyleSheet(u"font-size: 20px;\n"
                                "background-color: rgb(236, 221, 11);\n"
                                "border-radius:10px;")
        self.horizontalLayout.addWidget(self.quit)
        self.quit.setText("Quit")
        self.quit.clicked.connect(self.back_to_level)
        self.score = QLabel(self.frame_2)
        self.score.setAlignment(Qt.AlignCenter)
        self.score.setStyleSheet(u"font-size: 20px;\n"
                                 "background-color: rgb(236, 221, 11);\n"
                                 "border-radius:10px;")
        self.score.setText("Score : 0")
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
            self.buttons[button].setText(str(button + 1))
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
            self.buttons[button].setText(str(button + 1))
        self.level_screen.addLayout(self.horizontalLayout_2_level)
        self.stackedWidget.addWidget(self.level_screen_q)
        self.stackedWidget.addWidget(self.game_screen_q)
        MainWindow.setCentralWidget(self.main_screen)
        self.stackedWidget.setCurrentWidget(self.level_screen_q)