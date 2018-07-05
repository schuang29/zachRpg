class Unit:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

def MakeGoblin():
    goblin = Unit("Baby Goblin", 5, 1)
    
    return goblin