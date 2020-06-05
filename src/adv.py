from room import Room
from player import Player

# Declare all the rooms

room = {
'outside':  Room("Outside Cave Entrance",
    "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n = room['foyer']
room['foyer'].s = room['outside']
room['foyer'].n = room['overlook']
room['foyer'].e = room['narrow']
room['overlook'].s = room['foyer']
room['narrow'].w = room['foyer']
room['narrow'].n = room['treasure']
room['treasure'].s = room['narrow']

#
# Main
#
# Welcome Message
print()
print()
print("Welcome hero, to >>-- WOLVES ADVENTURE -->")
print()
print()
yourName = input("Choose your players name: ")
print()
print()
print(f"Welcome to the Adventure, {yourName}")
print()
print()

# Make a new player object that is currently in the 'outside' room.

# ================= name dynamic!!!!! 

player = Player({yourName}, room['outside'])
user = str(input("Press any key to start"))
# Set done to false


# Write a loop that:
while not user == "quit":
# What will it prompt when not done?
    print()
    print()
    print('>>-- WOLVES ADVENTURE -->')
    print()
    print(f"{yourName}, {player.roomIn}")
    print(f"{player.roomIn.desc}")
    print()
    print( "Choose: n / e / s / w / quit")
    print()
    print('>>---------------------->')
    print()
    command = input('Where do you want to go? ')
    print()
    print()

    if command == 'quit':
        break


    else:
        player.roomIn = player.move(command, player.roomIn)

# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
