"""Define classes used in game."""


class Room():
    """This class represents rooms in the game."""

    def __init__(self, room_name):
        """Hold all the fields for a room."""
        self.name = room_name  # room name key
        self.description = None  # room description to be printed
        self.linked_rooms = {}
        self.character = None
        self.content = []


class Character():
    """This class represents the characters in the game."""

    def __init__(self, char_name, char_description):
        """Hold all the character attributes."""
        self.name = char_name  # character name
        self.description = char_description
        self.conversation = None
        self.madness = None  # charter madness (maybe use 1-10)
        # TODO: Add more character traits


class Item():
    """This class represents items in the game."""

    def __init__(self):
        """Hold all fields for Item."""
        self.name = ""  # name of the object
        self.description = ""  # description of item to be printed
