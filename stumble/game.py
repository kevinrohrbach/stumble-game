"""Run the game."""

# Import modules ---------------- #
from sys import exit

# Import classes --------------- #
import common

# load universe ---------------- #

game_state = dict()
locations = dict()
characters = dict()
items = dict()

playerName = None
player = common.Player(game_state, playerName)


# # Main game --------------------- #
def game_loop():
    """Define main game loop."""
    global game_state, locations, characters, player, items

    while player.dead is False:
        if player.location.visits is False:
            common.Location.get_details(player.location)
            common.Location.set_visit(player.location, True)
        elif player.location.visits is True:
            common.Location.get_name(player.location)
        command = input('\n> ').lower()
        if command in {'n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw', 'u', 'd'}:
            player_move = player.move(command.upper())
            if player_move is not None:
                player.location = locations[player_move]
            pass
        elif command == 'look':
            print(common.Location.get_details(player.location))
        elif command == 'help':
            common.engine.show_help()
        elif command == 'print':
            print(game_state)  # This needs to do soemthing more meaningful
        elif command == 'save':
            common.engine.save_game(locations, characters, items)
            exit(0)  # TODO: remove in production so save without quit poss.
        elif command == 'inventory':
            player.list_inventory()
        else:
            print('Invalid command.')
    player.dead = True
    exit(0)
# TODO: Move most of command tree into engine


# Main function ------------------ #
def main():
    """Define main function. Load State. Start game."""
    global game_state, locations, characters, player, items

    game_state = dict(common.engine.start())

# Build world
    locations, characters, items = common.engine.build_world(game_state)
# Create and place player
    name = 'Kevin'  # input('> ')
    player = common.engine.spawn_player(game_state,name)
    player.location = locations[game_state['player']['location']]
    print(player.__dict__)
    game_loop()


if __name__ == '__main__':
    main()
