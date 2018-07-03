import sys

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

    if command == '?': listCommands(commandList)

print('See you later')