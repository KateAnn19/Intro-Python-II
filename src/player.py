import sys
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    lives = 2
    def __init__(self, name, location):
        self.location = location
        self.name = name
    def __str__(self):
        return f"Location {self.location}".format(self=self)
    def updatelocation(self, location):
        self.location = location 
    def decreaselives(self):
        if(self.lives == 1):
            print("Game Over")
            return sys.exit(1);
        
        self.lives = self.lives - 1 
        return self.lives 
