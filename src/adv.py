from room import Room
from player import Player
import random 
import sys
from items import Items

# Declare all the room_dicts

room_dict = {
    'outside':  Room("outside",
                     "North of you, the cave mount beckons", [Items("Lamp", "lights your way in the dark"), Items("Sleeping mat", "rest your head wanderer")]),

    'foyer':    Room("foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Items("Picture frame", "See who has been watching")]),

    'overlook': Room("overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Items("Rope", "climb to safety"), Items("Note", "A message from your love"), Items("bird", "fly away")]),

    'narrow':   Room("narrow", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Items("canoe", "to navigate safely"), Items("a knife", "in case of wild beasts")]),

    'treasure': Room("treasure", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[Items("a code", "leads you to the real treasure")])
}

quotes= ["money is the worst discovery of human life. But it is the most trusted material to test human nature.", "There is no fear for one whose mind is not filled with desires. Buddha", "Money is the root of all evil", "It is better to say goodbye", "so long"]


# Link room_dicts together
# Map

room_dict['outside'].n_to = room_dict['foyer']
room_dict['foyer'].s_to = room_dict['outside']
room_dict['foyer'].n_to = room_dict['overlook']
room_dict['foyer'].e_to = room_dict['narrow']
room_dict['overlook'].s_to = room_dict['foyer']
room_dict['narrow'].w_to = room_dict['foyer']
room_dict['narrow'].n_to = room_dict['treasure']
room_dict['treasure'].s_to = room_dict['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room_dict.
name = input("Enter your name: ").split(',')
player1 = Player(name[0], room_dict['outside'])  

beginning = True

while True:  
    if(beginning == True):
        print(f"*************************FORTUNE'S QUEST******************************************************************************************************************************************\nWelcome to a very simple game with very simple rules:\n 1) You can go 4 directions, n - s - e - w . Your mission is to reach the treasure. If you go a wrong direction more than 2 times you will fall into a pit of lava 🔥 and must start over. You win the game when you find the treasure. Along the way you will meet lots of friendly and not so friendly creatures. Some will help you and and some will try to steer you away from the treasure. You can also collect items as you go to feed the bad creatures and make them fall into the pit. Good luck. May Fortune 💰 be with you {player1.name}.")
    
    print(player1.location)
    room_dict[player1.location.name].print_roomitems()
    # print(sys.argv)
    print(player1.name)
    beginning = False 
    
    command = input("> (q to quit)").split(',')
    if (command[0] == 'q'):
        print(random.choice(quotes))
        break
    elif(command[0] == 'n'):
        if(player1.location.n_to == 'undefined'):
            player1.decreaselives()
            print(f"Lives remaining {player1.lives}")
            print(f"Wrong location try again. Remember to look at the hint {player1.name}")
        else:
            player1.updatelocation(room_dict[player1.location.name].n_to)
            room_dict[player1.location.name].print_roomitems()
               
        #if player hits any other key besides n then return 'not the right direction. try again' (add feature that if direction is wrong 2 times you die)
    elif(command[0] == 's'):
        if(player1.location.s_to == 'undefined'):
            player1.decreaselives()
            print(f"Lives remaining {player1.lives}")
            print(f"Wrong location try again. Remember to look at the hint {player1.name}")
        else:
            player1.updatelocation(room_dict[player1.location.name].s_to)
            room_dict[player1.location.name].print_roomitems()
    elif(command[0] == 'e'):
        if(player1.location.e_to == 'undefined'):
            player1.decreaselives()
            print(f"Lives remaining {player1.lives}")
            print(f"Wrong location try again. Remember to look at the hint {player1.name}")
        else:
            player1.updatelocation(room_dict[player1.location.name].e_to)
            room_dict[player1.location.name].print_roomitems()
    elif(command[0] == 'w'):
        if(player1.location.w_to == 'undefined'):
            player1.decreaselives()
            print(f"Lives remaining {player1.lives}")
            print(f"Wrong location try again. Remember to look at the hint {player1.name}")
        else:
            player1.updatelocation(room_dict[player1.location.name].w_to)
            room_dict[player1.location.name].print_roomitems()
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
