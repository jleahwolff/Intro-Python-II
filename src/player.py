# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, roomIn, items=None):
        self.name = name
        self.roomIn = roomIn
        self.items = items

    def move(self, direction, roomIn):
        attribute = direction

# Trick learned from Emma - hasattr source(https://www.programiz.com/python-programming/methods/built-in/hasattr)
        if hasattr(roomIn, attribute):
            return getattr(roomIn, attribute)
        else:
            print("xx---- Cannot travel that way ----xx")

        return roomIn