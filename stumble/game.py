"""Run the game."""

# Import modules ----------------#
# from sys import exit
# import json

# Import classes --------------- #
import common

# load universe ---------------- #
# with open("game/elements.json") as elements:
#     universe = json.load(elements)

game_state = dict()
rooms = dict()

# Starting values -------------- #
playerName = "Kevin"  # input('> ')
room = 'bedroom'

player = common.Player(game_state, playerName, room)


# # Main game --------------------- #
def game_loop():
    """Define main game loop."""
    dead = False
    global game_state, rooms

    while dead is False:
        if player.room.visits is False:
            common.Room.get_details(player.room)
            common.Room.set_visit(player.room, True)
        elif player.room.visits is True:
            common.Room.get_name(player.room)
        command = input('\n> ')
        if command in {'N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'U', 'D'}:
            player_move = player.move(command)
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
            common.functionality.save_game()
        else:
            print('Invalid command.')
    dead = True
    exit(0)


# Main function ------------------ #
def main():
    """Define main function. Load State. Start game."""
    global game_state, rooms

    game_state = dict(common.functionality.start())
    rooms = common.functionality.build_rooms(game_state)  # Builds room objects
    player.name = playerName
    player.room = rooms[room]  # from line 19
    game_loop()


if __name__ == '__main__':
    main()
