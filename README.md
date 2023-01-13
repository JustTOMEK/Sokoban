The only library, apart from default libraries is gui library PySide2. <br />
Tests are run on pytest. <br />
In order to launch the app user has to have PySide2 and python installed. <br />
In order to use test files user has to have pytest installed. <br />
In order to launch the app user has to run stacked_gui.py. <br />
Changes in file arrangment may cause ERRORS. <br />

- Projects consists of files and folders:
- folder map contains 9 txt files, that represent maps, and README.MD
- folder tiles_for_pyqt contains 7 png files that are visual representation of tiles
- file map.py has Map class in it
- file test_map.py contains tests for Map class
- file tile.py has Tile class in it
- file test_tile.py contains tests for Tile class
- file move.py has NormalMove class in it
- file test_move.py contains test for Move class
- file stacked_gui.py opens app in a window
- file ui_game_with_functions.py inherits from ui_game.py and adds methods that control widgets
- file ui_game.py contains two methods and creates two stacked widgets and other widgets inside
- file README.MD that you are reading

Now what does the project do and how the files communicate with each_other. <br />


The game logic is handled by 3 files map.py tile.py move.py <br />

Starting with map.py. It consists of map class that takes care of most game. <br />
It gets a string representation of a map in init and enables actions such as move and undo_move <br />
It creates a "map", that consists of Tile objects from tile.py <br />
When user wants to make a move it checks if it is legal by creating available_moves list <br />
Available_moves list consists of NormalMove or BoxMove objects from move.py <br />

tile.py consists of abstract Tile class and Wall, Player, Floor, Box subclasses, that inherit from Tile. <br />
Every subclass has a set can_move_into <br />

move.py consists of NormalMove class and BoxMove, that inherits from NormalMove <br />


About GUI it is handled by 3 files stacked_gui.py ui_game.py ui_game_with_functions <br />

ui_game.py creates a UiGame class.  <br />
It has one method create_widgets <br />
It checks how many maps are in maps folder and according to that creates this many levels <br />
Aside from that it creates 2 Stacked Widgets: game_screen and level_screen <br />

ui_game_with_functions creates a UiGameWithFunctions that inherits from UiGame from ui_game.py  <br />
UiGameWithFunctions adds new method that enable all buttons and game in general to work  <br />
In level_screen it loads pngs from tiles_for_pyqt in order to make game visual  <br />

stacked_gui_py creates an object of MainWindow and then sets self.ui to UiGameWithFunctions from ui_game_with_functions.py <br />
It calls .create_widgets() on it sets MainWindow base size to  (720, 500) and shows whe window <br />
It also enables keyboard WASD control of the game when in game_screen <br />

What functionalities does the project have:
- an easy working map.py class that would be able to add new game features in future such as new tiles.
- as many levels as user wants. In order to create a new level only thing user has to do is create a new .txt file and put it in maps folder for more info go to maps/README.md
- Levels locked as long as you don't finish all previous ones
- Keyboard control in game, reset, undo move buttons
- Resizable and nice looking GUI :-)


In order to get more insight on how code works clone it and read in file comments. <br />
