import sys
import Weapons

disk = Weapons.Weapon("Scratched Fortnite Disk", 2, "Blah")
backpack = ['scratched fortnite disk']

def showInv():
    print ('You have ')
    for stuff in backpack:
        print(stuff)

commandList = ['? - Help', 'go - Move direction', 'exit - Exit game', 'inventory - Open inventory']

def listCommands(commandList):
    print ('\tYou can do the folowing: ')
    for x in commandList:
        print ('\t', x)


print ("Hello, welcome to our house!")


name = input("What\'s you name? ")

print("Hi", name)

command = ''
command = input("What would you like to do? ")

while command != 'exit':
    if command == '?': listCommands(commandList)

    if command == 'inventory': showInv()

    command = input('What\'s your next command?: ')

print('See you later')