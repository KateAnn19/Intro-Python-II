import sys
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    lives = 2
    def __init__(self, name, location):
        self.location = location
        self.name = name
        self.inventory = []
    def __str__(self):
        return f"{self.name} {self.location}\nitems:{self.inventory}".format(self=self)
    def updatelocation(self, location):
        self.location = location
    def add_to_inventory(self, item):
        self.inventory.append(item)
        self.print_inventory() 
    def decreaselives(self):
        if(self.lives == 1):
            print("Game Over")
            return sys.exit(1);
        self.lives = self.lives - 1 
        return self.lives

    def drop_from_inventory(self, item):
        self.inventory.remove(item)
        self.print_inventory()

    def print_inventory(self):
        print(f"Your bag contents: ", [f"{i.name}" for i in self.inventory], '\n') 
