import Units
import Weapons
import Rooms

stop = False
while stop == False:
    room = Rooms.FirstRoom()
    print("--- " + room.name + " ---")
    print(room.text)
    
    for option in room.options:
        print(option)

    inp = input("What would you like to do? ")