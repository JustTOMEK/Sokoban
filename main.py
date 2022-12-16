from map import Map
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    new_map = Map("maps/map_1.txt")
    while not new_map.check_if_win():
        new_map.display_map()
        decision = input('Whats your move: ')
        if decision == "Redo":
            new_map.redo_move()
        elif decision == "Undo":
            new_map.undo_move()
        else:
            new_map.move(decision)
        cls()
    print('You won')
