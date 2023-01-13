from PySide2.QtGui import Qt, QPixmap
from PySide2.QtWidgets import (QLabel, QMessageBox)
from tile import Floor, Box, Player, Wall
from map import Map
from ui_game import UiGame


class UiGameWithFunctions(UiGame):
    def back_to_level(self):
        """
        This Function takes player back to level screen, when
        quit is clicked in game screen.
        """
        self.stackedWidget.setCurrentWidget(self.level_screen_q)
        self.state = "level"

    def undo(self):
        """
        Undoes a move, when undo button is clicked.
        """
        self.map.undo_move()
        self.load_png()
        self.change_score()

    def map_set_board_size(self):
        """
        Deletes all labels from level screen and adds
        row*column new labels according to map size.
        """
        # deleting all widgets from game layout
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.removeItem(self.gridLayout.itemAt(i))
        # adding tiles to game layout
        self.tiles = []
        for row in range(self.map.rows()):
            for column in range(self.map.columns()):
                self.tiles.append(QLabel(self.frame))
                tile = self.tiles[row * self.map.columns() + column]
                self.gridLayout.addWidget(tile, row, column, 1, 1)

    def reset_game(self):
        """
        Resets, when reset button clicked.
        """
        file = open(self.source, "r")
        self.map = Map(file.read())
        self.load_png()
        self.change_score()

    def change_score(self):
        """
        Changes score on score caption to move_count.
        """
        self.score.setText(f'Score : {self.map.move_count()}')

    def show_help(self):
        """
        Opens Message box when help button clicked.
        """
        dialog = QMessageBox(self.stackedWidget)
        dialog.setStyleSheet(u"background-color: yellow;")
        dialog.setWindowTitle("Help")
        dialog.setText('To finish Sokoban map move all boxes to targets. \n'
                       'At the beggining only level 1 is unlocked.\n'
                       'When level is finished the next one is unlocked.\n'
                       'Game can be reseted at all times.\n'
                       'Move can be undone at all times.\n'
                       'Move in game using WASD keys.\n')
        dialog.addButton('Back to level selection', QMessageBox.YesRole)
        dialog.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint |
                              Qt.CustomizeWindowHint)
        dialog.exec_()

    def show_won_game(self):
        """
        Opens Message box when game finished.
        It ables player to go to next level or go to level choose screen.
        """
        dialog = QMessageBox(self.stackedWidget)
        dialog.setStyleSheet(u"background-color: yellow;")
        dialog.setWindowTitle(f'You finished level {self.level}')
        if self.level != 8:
            self.unlocked_levels[self.level] = 1
            dialog.addButton('Next Level', QMessageBox.YesRole)
        else:
            dialog.setText('There is no next level. You finished the game'
                           'congratulations.')
        dialog.addButton('Main Menu', QMessageBox.YesRole)
        dialog.buttonClicked.connect(self.won_game_on_clicked)
        dialog.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint |
                              Qt.CustomizeWindowHint)
        dialog.exec_()

    def show_not_unlocked(self):
        """
        Opens Message box when locked level button clicked.
        """
        dialog = QMessageBox(self.stackedWidget)
        dialog.setStyleSheet(u"background-color: yellow;")
        dialog.setWindowTitle("You have not unlocked this level")
        dialog.setText('In order to play this level finish all previous ones.')
        dialog.addButton('Choose another level', QMessageBox.YesRole)
        dialog.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint |
                              Qt.CustomizeWindowHint)
        dialog.exec_()

    def won_game_on_clicked(self, btn):
        """
        Assigns functions to won game MessageBox.
        """
        if btn.text() == "Next Level":
            self.next_level(self.level + 1)
        if btn.text() == "Main Menu":
            self.stackedWidget.setCurrentWidget(self.level_screen_q)

    def load_png(self):
        """
        Reads map.tiles() and assigns a QPixmap to tile at according postion.
        Sets QPixmap according to tile.type().
        """
        no_targets = {Wall: "tiles_for_pyqt/wall.png",
                      Box: "tiles_for_pyqt/box_not.png",
                      Player: "tiles_for_pyqt/player_on_floor.png",
                      Floor: "tiles_for_pyqt/floor.png"}
        targets = {Box: "tiles_for_pyqt/box_yes.png",
                   Floor: "tiles_for_pyqt/target_on_floor.png",
                   Player: "tiles_for_pyqt/player_on_target.png"}
        for row in range(self.map.rows()):
            for column in range(self.map.columns()):
                tile_type = type(self.map.tiles()[row][column])
                if self.map.tiles()[row][column].is_target():
                    pixmap = QPixmap(targets[tile_type])
                else:
                    pixmap = QPixmap(no_targets[tile_type])
                tile = self.tiles[row * self.map.columns() + column]
                tile.setPixmap(pixmap)
                tile.setScaledContents(True)

    def choose_level(self, level):
        """
        When level button clicks changes screen to according level.
        If level locked shows message box.
        """
        if self.unlocked_levels[level - 1]:
            self.level = level
            file = open(f'maps/map_{level}.txt', "r")
            self.map = Map(file.read())
            self.map_set_board_size()
            self.stackedWidget.setCurrentWidget(self.game_screen_q)
            self.source = f'maps/map_{level}.txt'
            self.change_score()
            self.load_png()
            self.state = "game"
        else:
            self.show_not_unlocked()

    def next_level(self, level):
        """
        When level finished and nex_level clicked switchess
        tiles to next level tiles.
        """
        self.level = level
        file = open(f'maps/map_{level}.txt', "r")
        self.map = Map(file.read())
        self.map_set_board_size()
        self.source = f'maps/map_{level}.txt'
        self.change_score()
        self.state = "game"
        self.load_png()
