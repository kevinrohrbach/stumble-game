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
    global game_state

    while dead is False:
        if player.room.visits is False:
            common.Room.get_details(player.room)
            common.Room.set_visit(player.room, True)
            print(rooms)
            # game_state.update({'player': {'room': {'visits': True}}})
            # print(game_state)
        command = input('\n> ')
        if command in {'N', 'E', 'S', 'W'}:
            player_move = player.move(command)
            print(player_move)
            print(rooms)
            if player_move is not None:
                player.room = rooms[player_move]
            pass
        elif command == 'look':
            print(player.room.descr_light)
        elif command == 'print':
            print(game_state)
        else:
            print('Invalid command.')
    dead = True
    exit(0)


# Main function ------------------ #
def main():
    """Define main function. Load State. Start game."""
    global game_state

    game_state = dict(common.functionality.start())
    rooms = common.functionality.build_rooms(game_state)
    print(rooms)
    player.room = rooms[room]
    game_loop()


if __name__ == '__main__':
    main()
