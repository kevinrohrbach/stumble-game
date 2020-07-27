"""Define classes."""

import textwrap


# Room Classes ------------------------------------------------ #
class Room():
    """This class represents rooms in the game."""

    global game_state

    def __init__(self, game_state, room):
        """Hold all the fields for a room."""
        self.name = game_state['rooms'][room]['name']
        self.descr_light = game_state['rooms'][room]['descr_light']
        self.descr_dark = game_state['rooms'][room]['descr_dark']
        self.exits = game_state['rooms'][room]['exits']
        self.character = None
        self.content = game_state['rooms'][room]['content']
        self.light = None
        self.visits = False  # TODO: numbers instead of boolean?

    def get_name(self):
        """Get current room name."""
        print('\n')
        print(self.name)
        print("----------------")

    def get_details(self):
        """Get full details of room."""
        print('\n')
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

    def __init__(self, game_state, name):
        """Hold all the character attributes."""
        self.name = None  # character name
        self.description = None
        self.room = None
        self.conversation = None
        self.madness = 0  # charter madness (maybe use 1-10)
        self.inventory = []
        # TODO: Add more character traits


class Player(Character):
    """This class represents the player in the game."""

    global game_state

    def __init__(self, game_state, name):
        """Hold extra player attributes."""
        Character.__init__(self, game_state, name)

    def move(self, direction):
        """Define player's movement."""
        if self.room.exits[direction] is None:
            print(f"You can't go there {self.name}.")
            return
        return self.room.exits[direction]


# Item classes --------------------------------------------- #
class Item():
    """This class represents items in the game."""

    global game_state

    def __init__(self, game_state, name):
        """Hold all fields for Item."""
        self.name = ""  # name of the object
        self.description = ""  # description of item to be printed
