# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        #  need to add ITEMS to room

    def __str__(self):
        return f'you are located in the {self.name}'

    def print_desc(self):
        return f'{self.desc}'
