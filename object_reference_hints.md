Remember that multiple variables can refer to the same object.

In the diagram below, there are only 2 `Room` objects, total. (There are more in the game, obviously, but in this diagram, there are 2.)

There are 5 variables. 3 of them point to the one Room object that is the foyer:

* `room_dict['foyer']`
* `room_dict['outside'].n_to`
* `player.location`

The remaining 2 point to the one Room object that is the outside:

* `room_dict['outside']`
* `room_dict['foyer'].s_to`

```
room_dict['outside'] -> Room("Outside Cave Entrance")
                               ^
                               |
                     room_dict['foyer'].s_to


room_dict['foyer'] -> Room("Foyer") <- player.location
                     ^
                     |
              room_dict['outside'].n_to
```

If you want to move the player (who is in the foyer in the diagram) to another room_dict, you just need to reassign that to any variable that points to that other room_dict.

So if the player is in the foyer and types `s` to go south, we could set:

```
player.location = room_dict['foyer'].s_to  # we were in the foyer, then went south
```

and after that, the variable references would look like this, with player location pointing to the outside object:

```
                        player.location
                               |
                               v
room_dict['outside'] -> Room("Outside Cave Entrance")
                               ^
                               |
                     room_dict['foyer'].s_to


room_dict['foyer'] -> Room("Foyer")
                     ^
                     |
              room_dict['outside'].n_to
```

_Assigning doesn't copy the object. It just makes another reference to the same object._
