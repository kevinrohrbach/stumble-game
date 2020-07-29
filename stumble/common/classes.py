"""Define classes."""

import textwrap


# Location Classes ------------------------------------------------ #
class Location():
    """This class represents locations in the game."""

    global game_state

    def __init__(self, game_state, location):
        """Hold all the fields for a location."""
        self.name = game_state['locations'][location]['name']
        self.descr_light = game_state['locations'][location]['descr_light']
        self.descr_dark = game_state['locations'][location]['descr_dark']
        self.exits = game_state['locations'][location]['exits']
        self.character = None
        self.items = game_state['locations'][location]['items']
        self.light = None
        self.visits = False  # TODO: numbers instead of boolean?

    def get_name(self):
        """Get current location name."""
        print(f"\n{self.name}\n----------------")

    def get_details(self):
        """Get full details of location."""
        print(self.name)
        print("----------------")
        print(textwrap.fill(self.descr_light, 80))

    def set_visit(self, value):
        """Set to visited."""
        self.visits = value


# Character classes ------------------------------------------- #
class Character():
    """This class represents the characters in the game."""

    global game_state

    def __init__(self, game_state):
        """Hold all the character attributes."""
        self.name = None  # character name
        self.description = None
        self.location = None
        self.conversation = None
        self.madness = 0  # charter madness (maybe use 1-10)
        self.dead = False
        self.inventory = ()
        # TODO: Add more character attributes


# Player class ------------------------------------------------ #
class Player(Character):
    """This class represents the player in the game."""

    global game_state

    def __init__(self, game_state):
        """Hold extra player attributes."""
        super().__init__(game_state)

    def set_name(self, name):
        """Set player's name."""
        self.name = name

    def move(self, direction):
        """Define player's movement."""
        if self.location.exits[direction] is None:
            print(f"There's nowhere to go that way {self.name}.")
            return
        return self.location.exits[direction]

    def list_inventory(self):
        """List player's inventory."""
        if not self.inventory:
            print("You don't have anything. Poor you.")
        else:
            for i in self.inventory:
                print(i)

    def take_item(self, item):
        """Define picking up item."""
        if item not in self.location.items:
            print("I don't see that here. You must be halucinating...")
        elif 'take' in item.actions:  # TODO: implement weight check
            pass  # print("You're not strong enough for that, mate.")
        else:
            print("Taken.")
            self.location.items.remove(item)
            self.inventory.append(item)


# Item classes --------------------------------------------- #
class Item():
    """This class represents items in the game."""

    global game_state

    def __init__(self, game_state, name):
        """Hold all fields for Item."""
        self.name = ""  # name of the object
        self.description = ""  # description of item to be printed
        self.weight = ""
        self.actions = ""
