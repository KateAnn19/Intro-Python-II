from room import Room
from player import Player
import random 
import sys
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

quotes= ["money is the worst discovery of human life. But it is the most trusted material to test human nature.", "There is no fear for one whose mind is not filled with desires. Buddha", "Money is the root of all evil", "It is better to say goodbye", "so long"]


# Link rooms together
# Map

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player(room['outside'])  

while True:   
    print("*************************FORTUNE'S QUEST******************************************************************************************************************************************\nWelcome to a very simple game with very simple rules:\n 1) You can go 4 directions, n - s - e - w . Your mission is to reach the treasure. If you go a wrong direction more than 2 times you will fall into a pit of lava 🔥 and must start over. You win the game when you find the treasure. Along the way you will meet lots of friendly and not so friendly creatures. Some will help you and and some will try to steer you away from the treasure. You can also collect items as you go to feed the bad creatures and make them fall into the pit. Good luck. May Fortune \💰 be with you.")
    print(player1.location)
    # print(sys.argv)
    command = input("> (q to quit)").split(',')
    if (command[0] == 'q'):
        print(random.choice(quotes))
        break
    elif(command[0] == 'n'):
        if(player1.location == room['outside']):
            player1.updatelocation(room['outside'].n_to)
        elif(player1.location == room['foyer']):
            player1.updatelocation(room['foyer'].n_to)
        elif(player1.location == room['narrow']):
            player1.updatelocation(room['narrow'].n_to)
               
        #if player hits any other key besides n then return 'not the right direction. try again' (add feature that if direction is wrong 2 times you die)
    elif(command[0] == 's'):
        if(player1.location == room['foyer']):
            player1.updatelocation(room['foyer'].s_to)
        elif(player1.location == room['overlook']):
            player1.updatelocation(room['overlook'].s_to)
        elif(player1.location == room['treasure']):
            player1.updatelocation(room['treasure'].s_to)
    elif(command[0] == 'e'):
        if(player1.location == room['foyer']):
            player1.updatelocation(room['foyer'].e_to)
    elif(command[0] == 'w'):
        if(player1.location == room['narrow']):
            player1.updatelocation(room['narrow'].w_to)
    else:
        player1.decreaselives()
        if(player1.lives == 0):
            print("WWWWWWWMMMMMMMMMMMWWWWWWMMMMMWWWWVVVVVVVNNNN\nFire Fire Fire AWWWWWWW\nGame Over")
            sys.exit(1)
        print("You have selected a inappropriate key. Even your cat's random keyboard press counts. Careful.") 
        print(f"Lives remaining {player1.lives}")



# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
