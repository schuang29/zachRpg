import sys
<<<<<<< HEAD
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

=======
import Main

commandList = ['? - Help', 'go - Move direction', 'bye - Exit game']

def listCommands(commandList):
    print ('\tYou can do the folowing: ')
    for x in commandList:
        print ('\t', x)


print ("Hello World!")

command = ''

while command != 'bye':
    command = input('What\'s your command: ')

    print ('\tYou entered', command)

    if command == '?':
        listCommands(commandList)
    elif command == 'go':
        Main.Start()
    
>>>>>>> a49f22ff4580b765bccdf9213a631f69c19a8b90
print('See you later')