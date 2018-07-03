import Weapons
import Units

class Room:
    def __init__(self, name, text, options, units, rewards):
        self.name = name
        self.text = text
        self.options = options
        self.units = units
        self.rewards = rewards

def FirstRoom():
    goblin = Units.MakeGoblin()
    units = [goblin]
    
    sword = Weapons.MakeSword()
    rewards = [sword]

    return Room("Basic", "You have entered the first room", ["[1] option 1", "[2] option 2"], units, rewards)