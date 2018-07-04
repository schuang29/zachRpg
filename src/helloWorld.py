import sys

commandList = ['? - Help', 'go - Move direction', 'exit - Exit game']

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
    print ('\tYour command is ', command)

    command = input('What\'s your next command?: ')

    if command == '?': listCommands(commandList)

print('See you later')