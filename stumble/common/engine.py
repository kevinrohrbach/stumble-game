"""Define core functionality of game."""

import time
import json
import jsons
from os import path
import common


SAVEGAME_FILENAME = "game/savegame.json"


# Load, save, initialise game state #
def load_game():
    """Load game state."""
    command = input("Do you want to load your existing game? (y/n)\n> ")
    if command == "y":
        with open(SAVEGAME_FILENAME, 'r') as savegame:
            state = json.load(savegame)
        return state
    else:
        state = initialize_game()
        return state


def save_game(locations, chars, items):
    """Save the current game state."""
    global game_state
    print('You seriously want to chicken out and save?')
    command = input('\n>')
    if command == 'y':
        for location in locations:
            game_state['locations'].update(
                {location: jsons.dump(locations[location])})
        for perp in chars:
            game_state['characters'].update({perp: jsons.dump(chars[perp])})
        for i in items:
            game_state['items'].update({i: jsons.dump(items[i])})
        with open(SAVEGAME_FILENAME, 'w') as savegame:
            savegame.write(json.dumps(game_state, indent=4))
    pass


def initialize_game():
    """Initialise game state if no game exists."""
    with open("./game/elements.json") as universe:
        state = json.load(universe)
    return state
# END game state manipulation ----------- #


def start():
    """Define game start function."""
    global game_state
    if not path.isfile(SAVEGAME_FILENAME):
        game_state = initialize_game()
    else:
        game_state = load_game()
    return game_state


# World building ------------------------ #
def build_world(data):
    """Build game world."""
    location_load = "Building locations"
    character_load = "Placing characters"
    item_load = "Hiding items"
    for i in range(4):
        print(f"{location_load}", end='\r')
        location_load += "."
        time.sleep(0.1)
    locations = build_locations(data)
    print("\r")
    for i in range(4):
        print(f"{character_load}", end='\r')
        character_load += "."
        time.sleep(0.1)
    characters = create_characters(data)
    print("\r")
    for i in range(4):
        print(f"{item_load}", end='\r')
        item_load += "."
        time.sleep(0.1)
    items = create_items(data)
    print("\r\r\r")
    return locations, characters, items


def build_locations(data):
    """Build locations out of game_state."""
    locations = {}
    for location in data['locations']:
        locations.update({location: common.Location(data, location)})
    return locations


def create_characters(data):
    """Build characters out of game_state."""
    characters = {}
    for character in data['characters']:
        characters.update({character: common.Character(data, character)})
    return characters

def spawn_player(data, name):
    """Spawn character from game_state."""
    player = common.Player(data, name)
    player.inventory.append(game_state['player']['inventory'])
    return player


def create_items(data):
    """Build items out of game_state."""
    items = {}
    for item in data['items']:
        items.update({item: common.Item(data, item)})
    return items


# Help File ----------------------------- #
def show_help():
    """Show in-game help."""
    with open('./common/commands.txt', 'r') as help:
        print(help.read())
