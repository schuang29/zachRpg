import Units
import Weapons
import Rooms
import Map

stop = False
while stop == False:
    print("You are at:", str(Map.pos[0]) + ",", str(Map.pos[1]))
    
    moveOptions = Map.MoveOptions()
    
    print("You may move:" + moveOptions)
    inp = input("Which way would you like to go? ")

    Map.Move(inp)

def Encounter():
    room = Rooms.FirstRoom()
    print("--- " + room.name + " ---")
    print(room.text)
    
    for option in room.options:
        print(option)

    inp = input("What would you like to do? ")