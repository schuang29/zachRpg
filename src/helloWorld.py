import sys
import Weapons
import Main
import Map

disk = Weapons.Weapon("Scratched Fortnite Disk", 2, "Blah")
backpack = [disk]

def showInv():
    print ('You have ')
    for stuff in backpack:
        print(stuff.getName())

commandList = ['? - Help', 'go - Move direction', 'exit - Exit game', 'inventory - Open inventory']

def listCommands(commandList):
    print ('\tYou can do the folowing: ')
    for x in commandList:
        print ('\t', x)


print ("Hello, welcome to our house!")


name = input("What\'s your name? ")

print("\tHi", name)

command = ''
command = input("What would you like to do? ")

while command != 'exit':
    print()
    
    if command == '?': 
        listCommands(commandList)
        print()
        print("\tYour move options are: ", Map.MoveOptions())
        print()

    if command == 'inventory': 
        showInv()
    elif command == 'go':
        Main.Start()
    
    command = input('What\'s your next command?: ')

print('See you later')