import sys
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    lives = 2
    def __init__(self, location):
        self.location = location
    def __str__(self):
        return f"Location {self.location}".format(self=self)
    def updatelocation(self, location):
        self.location = location 
    def decreaselives(self):
        self.lives = self.lives - 1 
        return self.lives 
