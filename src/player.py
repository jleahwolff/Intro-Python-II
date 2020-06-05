# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, roomIn):
        self.name = name
        self.roomIn = roomIn

    def move(self, direction, roomIn):
        attribute = direction

        if hasattr(roomIn, attribute):
            return getattr(roomIn, attribute)
        
        print("Cannot move in that direction")

        return roomIn
