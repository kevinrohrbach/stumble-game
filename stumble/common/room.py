"""Define Room class."""


class Room():
    """This class represents rooms in the game."""

    def __init__(self, data, current_room):
        """Hold all the fields for a room."""
        self.name = data['rooms'][current_room]['name']
        self.descr_light = data['rooms'][current_room]['description_light']
        self.descr_dark = data['rooms'][current_room]['description_dark']
        self.exits = data['rooms'][current_room]['exits']
        self.character = None
        self.content = data['rooms'][current_room]['content']
        self.light = None
        self.visits = False

    def get_name(self):
        """Get current room name."""
        print(self.name)

    def get_details(self):
        """Get full details of room."""
        print(self.name)
        print("----------------")
        print(self.descr_light)
