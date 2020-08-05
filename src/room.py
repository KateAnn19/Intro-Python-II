# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    n_to = ''
    #if you are in outside n points to foyer
    #if you are in foyer n points to foyer 
    s_to = ''
    e_to = ''
    w_to = ''
    def __init__(self, name, description):
        self.name = name 
        self.description = description
    def __str__(self):
        return f"\n\nYou are in the {self.name}\n{self.description}".format(self=self)