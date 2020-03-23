"""Run the game."""

from sys import exit
from os import path
import json
import jsonpickle

# Import classes --------------- #
import common

# load universe ---------------- #
with open("game/elements.json") as elements:
    universe = json.load(elements)


# Starting values -------------- #
playerName = "Kevin"  # input('> ')
room = "bedroom"

"""Create and place player."""
player = common.Player(playerName, room)
player.name = playerName
player.room = common.Room(universe, room)
player.madness = 0
player.inventory = []

# Create save file


# Main game --------------------- #
def game_loop():
    """Define main game loop."""
    dead = False

    while dead is False:
        command = input('\n> ')
        if command in {'N', 'E', 'S', 'W'}:
            player_move = player.move(command)
            if player_move is not None:
                player.room = common.Room(universe, player_move)
            pass
        elif command == 'look':
            print(player.room.descr_light)
        else:
            print('Invalid command.')
    dead = True
    exit(0)


# Main function -------------- #
def main():
    """Define main function. Currently only calling game loop."""
    # global game_state
    # if not os.path.isfile(SAVEGAME_FILENAME):
    #     game_state = initialize_game()
    # else:
    #     game_state = load_game()
    game_loop()
# TODO: Add load, initialise


if __name__ == '__main__':
    main()
