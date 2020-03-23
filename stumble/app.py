"""Run the game."""


import json

import common

with open("game/elements.json") as elements:
    universe = json.load(elements)

# --------------------------------------------------------
# Starting values
playerName = "Kevin"  # input('> ')
room = "bedroom"

"""Create and place player."""
player = common.Player(playerName, room)
player.name = playerName
player.room = common.Room(universe, room)
player.madness = 0
player.inventory = []


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
    # dead = True
