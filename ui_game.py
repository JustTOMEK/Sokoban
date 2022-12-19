from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from map import Map


class Ui_Game(object):

    def __init__(self, map_source):
        self.source = map_source
        self.map = Map(map_source)


    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(880, 724)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
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
        
        self.tiles = []

        for row in range(10):
            for column in range(10):
                self.tiles.append(QLabel(self.frame))
                name = "label_" + str(row + column * 10)
                self.tiles[row * 10 + column].setObjectName(name)
                self.gridLayout.addWidget(self.tiles[row * 10 + column], row, column, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
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
        self.undo_move.clicked.connect(self.undo)

        self.horizontalLayout.addWidget(self.undo_move)

        self.reset = QPushButton(self.frame_2)
        self.reset.clicked.connect(self.reset_game)

        self.horizontalLayout.addWidget(self.reset)

        self.quit = QPushButton(self.frame_2)

        self.horizontalLayout.addWidget(self.quit)

        self.score = QLineEdit(self.frame_2)

        self.horizontalLayout.addWidget(self.score)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def undo(self):
        self.map.undo_move()
        self.map.change_box_coordinates()
        self.load_png()
    
    def reset_game(self):
        self.map = Map(self.source)
        self.load_png()


    def load_png(self):
        letter_to_image = {"w": "tiles_for_pyqt/wall.png",
                        "B": "tiles_for_pyqt/box_yes.png",
                        "b": "tiles_for_pyqt/box_not.png",
                        "p": "tiles_for_pyqt/player_on_floor.png",
                        "F": "tiles_for_pyqt/target_on_floor.png",
                        "P": "tiles_for_pyqt/player_on_target.png",
                        "f": "tiles_for_pyqt/floor.png"}
        for row in range(10):
            for column in range(10):
                pixmap = QPixmap(letter_to_image[self.map.current_map[row][column]])
                width = self.tiles[row * 10 + column].width()
                height = self.tiles[row * 10 + column].height()
                self.tiles[row * 10 + column].setPixmap(pixmap.scaled(width, height))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sokoban", None))
        self.undo_move.setText(QCoreApplication.translate("MainWindow", u"Undo Move", None))
        self.reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.score.setText(QCoreApplication.translate("MainWindow", u"Score :", None))
    
    # retranslateUi

