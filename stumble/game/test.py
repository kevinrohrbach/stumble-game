"""Test universe import and class instance creation."""

import jsonpickle
# import os
# import sys
# sys.path.append(os.path.abspath('../common'))
import classes

game_state = dict()


def initialize_game():
    """Initialise game state if no game exists."""
    with open("elements.json") as universe:
        state = jsonpickle.decode(universe.read())
    return state


game_state = initialize_game()
print(game_state)  # This is a dict now

player = classes.Player("Kevin", "bedroom")

# print(game_state)

rooms = []


def build_rooms(data):
    """Build rooms out of JSON."""
    for location in data['rooms']:
        room = classes.Room(data, location)
        rooms.append(room.name)


build_rooms(game_state)


print(rooms)
