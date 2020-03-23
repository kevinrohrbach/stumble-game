"""Define character class."""


class Character():
    """This class represents the characters in the game."""

    def __init__(self, name, room):
        """Hold all the character attributes."""
        self.name = None  # character name
        self.description = None
        self.room = None
        self.conversation = None
        self.madness = None  # charter madness (maybe use 1-10)
        self.inventory = []
        # TODO: Add more character traits


class Player(Character):
    """This class represents the player in the game."""

    def __init__(self, name, room):
        """Hold extra player attributes."""
        Character.__init__(self, name, room)

    def move(self, direction):
        """Define player's movement."""
        if self.room.exits[direction] is None:
            print("Cannot move in that direction!")
            return
        return self.room.exits[direction]
