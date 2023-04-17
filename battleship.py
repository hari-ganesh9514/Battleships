"""
Battleship Project
Name: V Hari Ganesh
Roll No: 20211A0846
"""

import battleship_tests as test
# import pdb; pdb.set_trace()


project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["number of rows"] = 10
    data["number of cols"] = 10
    data["board size"] = 500
    data["number of ships"] = 5
    data["cell size"] = data["board size"]/data["number of rows"]
    data["computer"] = emptyGrid(data["number of rows"], data["number of cols"])
    data["user"] = emptyGrid(data["number of rows"], data["number of cols"])
    # data["user"] = test.testShip()
    # data["user"] = test.testGrid()
    data["comp"] = addShips(data["computer"], data["number of ships"])
    data['tempShip'] = []
    data["user ships"] = 0
    data["winner"] = None
    data["max turns"] = 50
    data["current turns"] = 0
    return 

'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
# P1B-2 --> Step-3
# def makeView(data, userCanvas, compCanvas):
#     drawGrid(data, compCanvas, data["computer"], True)
#     drawGrid(data, userCanvas, data["user"], True)
#    return

def makeView(data, userCanvas, compCanvas):
    drawGrid(data, compCanvas, data["computer"], True)
    drawGrid(data, userCanvas, data["user"], True)
    drawShip(data, userCanvas, data["tempShip"])
    return

'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
# P1B-2 --> Step-5:
# def mousePressed(data, event, board):
#     pass
def mousePressed(data, event, board):
    if data["winner"] == None:
        cell = getClickedCell(data, event)

        if board == 'comp':
            if data["number of ships"] == 5:
                runGameTurn(data, cell[0], cell[1])

        if board == 'user':
            clickUserBoard(data, cell[0], cell[1])

    

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid = []
    for row in range(rows):
        grid.append([])
        d = grid[row]
        for col in range(cols):
            d.append(EMPTY_UNCLICKED)
    return grid


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    row = random.randint(1,8)
    col = random.randint(1,8)
    align = random.randint(0,1)

    if align == 0:
        ship = [[row-1,col],[row,col],[row-1,col]]
    else:
        ship = [[row,col-1],[row,col],[row,col-1]]
    return ship


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    for i in ship:
        x = i[0]
        y = i[1]
        if grid[x][y] != EMPTY_UNCLICKED:
            return False
    return True


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    j = 0
    while j < numShips:
        ship = createShip()
        if checkShip(grid,ship):
            for i in ship:
                x = i[0]
                y = i[1]
                grid[x][y] = SHIP_UNCLICKED
            j += 1
    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    i = data["cell size"]
    for row in range(data["number of rows"]):
        for col in range(data["number of cols"]):
            if grid[row][col] == SHIP_UNCLICKED:
                canvas.create_rectangle(col*i, row*i, data["cell size"] +col*i, data["cell size"] +row*i, fill="yellow")
            # elif grid[row][col]==EMPTY_CLICKED:
            #     canvas.create_rectangle(col*i,row*i, data["cell size"] +col*i, data["cell size"] +row*i, fill="white")
            else:
                canvas.create_rectangle(col*i, row*i, data["cell size"] +col*i, data["cell size"] +row*i, fill="blue")

    


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
# P1B-2 --> Step-1
# def isVertical(ship):
#     return


# '''
# isHorizontal(ship)
# Parameters: 2D list of ints
# Returns: bool
# '''
# def isHorizontal(ship):
#     return

# def isVertical(ship):
#     ship = sorted(ship)
#     col = ship[0][1]  
#     for i in range(1, len(ship)):
#         if ship[i][1] != col:  
#             return False
#         if ship[i][0] != ship[i-1][0] + 1:  
#             return False
#     return True

def isVertical(ship):
    if ship[0][1] == ship[1][1] == ship[2][1]:
        ship.sort()
        for i in ship:
            if ship[0][0] + 1 == ship[1][0] == ship[2][0] - 1:
                return True
    return False


def isHorizontal(ship):
    if ship[0][0] == ship[1][0] == ship[2][0]:
        ship.sort()
        for i in ship:
            if ship[0][1] + 1 == ship[1][1] == ship[2][1] - 1:
                return True
    return False


# def isHorizontal(ship):
#     row = ship[0][0]  
#     for i in range(1, len(ship)):
#         if ship[i][0] != row:  
#             return False
#         if ship[i][1] != ship[i-1][1] + 1:  
#             return False
#     return True
# def isHorizontal(ship):
#     ship = sorted(ship)
#     if ship[0][0] != ship[1][0] or ship[0][0] != ship[2][0] or ship[1][0] != ship[2][0]:
#         return False
#     elif abs(ship[0][1] - ship[1][1]) != 1 or abs(ship[2][1] - ship[1][1]) != 1:
#         return False
#     return True


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''

# P1B-2 --> Step-2
# def getClickedCell(data, event):
#     return
def getClickedCell(data, event):
    x = int(event.x/data["cell size"])
    y = int(event.y/data["cell size"])
    return [y, x]



'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
# P1B-2 Step--> 3
# def drawShip(data, canvas, ship):
#     return

def drawShip(data, canvas, ship):
    s = data["cell size"]
    for i in range(len(ship)):
        canvas.create_rectangle(s*ship[i][1], s*ship[i][0], s*(ship[i][1]+1), s*(ship[i][0]+1), fill="white")


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
# P1B-2 --> Step-4
# def shipIsValid(grid, ship):
#     return

"""def shipIsValid(grid, ship):
    # Check if ship is length 3
    if len(ship) != 3:
        return False
    
    # Check if ship overlaps with any other ship
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == SHIP_UNCLICKED:
                if (i,j) in ship:
                    return False
    
    # Check if ship is in a straight line
    if not checkShip(ship):
        return False
    
    # Check if ship is vertical
    if isVertical(ship):
        for cell in ship:
            if cell[1] != ship[0][1]:
                return False
    # Check if ship is horizontal
    elif isHorizontal(ship):
        for cell in ship:
            if cell[0] != ship[0][0]:
                return False
    else:
        return False
    
    return True"""


def shipIsValid(grid, ship):
    if len(ship) == 3:
        if (isVertical(ship) or isHorizontal(ship)) and checkShip(grid, ship):
            return True
    return False



'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
# P1B-2 --> Step-4
# def placeShip(data):
#     return
def placeShip(data):
    if shipIsValid(data["user"], data["tempShip"]):
        for ship in data["tempShip"]:
            data["user"][ship[0]][ship[1]] = SHIP_UNCLICKED
        data["user ships"] += 1
    else:
        print("ship is not valid")
    data["tempShip"] = []
    return 


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
# P1B-2 --> Step-4:
# def clickUserBoard(data, row, col):
#     return
def clickUserBoard(data, row, col):
    if data["user ships"] == 5:
        print("5 ships are placed. Start the game!")
        return
    
    if [row, col] in data["tempShip"]:
        print("Select Another Cell")
        return
    
    data["tempShip"].append([row, col])
    if len(data["tempShip"]) == 3:
        placeShip(data)
    return 

### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    return


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    return


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":

    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
