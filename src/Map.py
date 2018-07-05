pos = (0, 0)
mapArr = [
    (0, 0), (1, 0), (2, 0)
]

def MakeMap():
    highX = 0
    for coord in mapArr:
        if coord[0] > highest:
             return

def MoveOptions():
    moveOptions = ""

    if (pos[0] + 1, pos[1]) in mapArr:
        moveOptions += " E"
    if (pos[0] - 1, pos[1]) in mapArr:
        moveOptions += " W"
    if (pos[0], pos[1] - 1) in mapArr:
        moveOptions += " S"
    if (pos[0], pos[1] + 1) in mapArr:
        moveOptions += " N"

    return moveOptions

def Move(inp):
    global pos
    if inp == "N" and (pos[0], pos[1] + 1) in mapArr:
        pos = (pos[0], pos[1] + 1)
    elif inp == "E" and (pos[0] + 1, pos[1]) in mapArr:
        pos = (pos[0] + 1, pos[1])
    elif inp == "S" and (pos[0], pos[1] - 1) in mapArr:
        pos = (pos[0], pos[1] - 1)
    elif inp == "W" and (pos[0] - 1, pos[1]) in mapArr:
        pos = (pos[0] - 1, pos[1])
    else:
        print("Cannot move that way!")