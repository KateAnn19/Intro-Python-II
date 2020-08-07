# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    n_to = 'undefined'
    #if you are in outside n points to foyer
    #if you are in foyer n points to foyer 
    s_to = 'undefined'
    e_to = 'undefined'
    w_to = 'undefined'
    def __init__(self, name, description, items=[]):
        self.name = name 
        self.description = description
        self.items= items
    def __str__(self):
        return f"\n\nRoom: {self.name}\n{self.description}".format(self=self)
    def print_roomitems(self):
        for rid, r in enumerate(self.items):
            print()
            print(f"{rid}: {r}")
        print()
    def remove_items(self, item):
        self.items.remove(item)
        if(len(self.items) == 0):
            print('ALL GONE, Move on soldier!!!')
        else:
            print(f'Got item[{item.name}] to remove in Room:{self.name}. After removal here is whats left in this room')
            self.print_roomitems();
        