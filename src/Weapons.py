class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

def MakeSword():
    sword = Weapon("Flimsy Sword", 2)
    return sword