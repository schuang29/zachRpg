pos = (0, 0)
mapDict = {
    (0, 0): [1], 
    (1, 0): [1, 3]
}

def MoveOptions():
    moveOptions = ""
    options = mapDict[pos]
    for option in options:
        if option == 0:
            moveOptions = " N"
        elif option == 1:
            moveOptions = " E"
        elif option == 2:
            moveOptions = " S"
        else:
            moveOptions = " W"
    return moveOptions

def Move(inp):
    global pos
    if inp == "N" and (pos[0], pos[1] + 1) in mapDict.keys():
        pos = (pos[0], pos[1] + 1)
    elif inp == "E" and (pos[0] + 1, pos[1]) in mapDict.keys():
        pos = (pos[0] + 1, pos[1])
    elif inp == "S" and (pos[0], pos[1] - 1) in mapDict.keys():
        pos = (pos[0], pos[1] - 1)
    elif inp == "W" and (pos[0] - 1, pos[1]) in mapDict.keys():
        pos = (pos[0] - 1, pos[1])
    else:
        print("Cannot move that way!")