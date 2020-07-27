"""Run the game."""

# Import modules ---------------- #
from sys import exit

# Import classes --------------- #
import common

# load universe ---------------- #

game_state = dict()
rooms = dict()
characters = dict()
items = dict()

playerName = None
player = common.Player(game_state, playerName)


# # Main game --------------------- #
def game_loop():
    """Define main game loop."""
    dead = False
    global game_state, rooms, characters, items

    # print(game_state['player']['room'])

    while dead is False:
        if player.room.visits is False:
            common.Room.get_details(player.room)
            common.Room.set_visit(player.room, True)
        elif player.room.visits is True:
            common.Room.get_name(player.room)
        command = input('\n> ').lower()
        if command in {'n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw', 'u', 'd'}:
            player_move = player.move(command.upper())
            if player_move is not None:
                player.room = rooms[player_move]
            pass
        elif command == 'look':
            print(player.room.descr_light)
        elif command == 'help':
            common.functionality.show_help()
        elif command == 'print':
            print(game_state)  # This needs to do soemthing more meaningful
        elif command == 'save':
            common.functionality.save_game(rooms, characters, items)
            exit(0)  # TODO: remove in production so save without quit poss.
        else:
            print('Invalid command.')
    dead = True
    exit(0)


# Main function ------------------ #
def main():
    """Define main function. Load State. Start game."""
    global game_state, rooms, characters, items

    game_state = dict(common.functionality.start())

# Build world
    rooms, characters, items = common.functionality.build_world(game_state)
# Create and place player
    player.name = "Kevin"  # input('> ')
    player.room = rooms[game_state['player']['room']]
    game_loop()


if __name__ == '__main__':
    main()
