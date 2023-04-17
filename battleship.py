"""
Battleship Project
Name: V Hari Ganesh
Roll No: 20211A0846
"""

import battleship_tests as test


project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


def makeModel(data):
    data["number of rows"] = 10
    data["number of cols"] = 10
    data["board size"] = 500
    data["number of ships"] = 5
    data["cell size"] = data["board size"]/data["number of rows"]
    data["computer"] = emptyGrid(data["number of rows"], data["number of cols"])
    data["user"] = emptyGrid(data["number of rows"], data["number of cols"])
    data["comp"] = addShips(data["computer"], data["number of ships"])
    data['tempShip'] = []
    data["user ships"] = 0
    data["winner"] = None
    data["max turns"] = 50
    data["current turns"] = 0
    return 

def makeView(data, userCanvas, compCanvas):
    drawGrid(data, compCanvas, data["computer"], False)
    drawGrid(data, userCanvas, data["user"], True)
    drawShip(data, userCanvas, data["tempShip"])
    drawGameOver(data, userCanvas)
    return


def keyPressed(data, event):
    if event.char == '\r':
        makeModel(data)


def mousePressed(data, event, board):
    if data["winner"] == None:
        cell = getClickedCell(data, event)

        if board == 'comp':
            if data["number of ships"] == 5:
                runGameTurn(data, cell[0], cell[1])

        if board == 'user':
            clickUserBoard(data, cell[0], cell[1])

    

#### WEEK 1 ####

def emptyGrid(rows, cols):
    grid = []
    for row in range(rows):
        grid.append([])
        d = grid[row]
        for col in range(cols):
            d.append(EMPTY_UNCLICKED)
    return grid


def createShip():
    row = random.randint(1,8)
    col = random.randint(1,8)
    align = random.randint(0,1)

    if align == 0:
        ship = [[row-1,col],[row,col],[row+1,col]]
    else:
        ship = [[row,col-1],[row,col],[row,col+1]]
    return ship

def checkShip(grid, ship):
    for i in ship:
        x = i[0]
        y = i[1]
        if grid[x][y] != EMPTY_UNCLICKED:
            return False
    return True

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

def drawGrid(data, canvas, grid, showShips):
    i = data["cell size"]
    for row in range(data["number of rows"]):
        for col in range(data["number of cols"]):
            if grid[row][col] == SHIP_UNCLICKED:
                canvas.create_rectangle(col*i, row*i, data["cell size"] +col*i, data["cell size"] +row*i, fill="yellow")
            if grid[row][col] == SHIP_CLICKED:
                canvas.create_rectangle(col*i, row*i, data["cell size"] +col*i, data["cell size"] +row*i, fill="red")
            if grid[row][col] == EMPTY_UNCLICKED:
                canvas.create_rectangle(col*i, row*i, data["cell size"] +col*i, data["cell size"] +row*i, fill="blue")
            if grid[row][col] == EMPTY_CLICKED:
                canvas.create_rectangle(col*i, row*i, data["cell size"] +col*i, data["cell size"] +row*i, fill="white")
            if showShips == False:
                if grid[row][col] == SHIP_UNCLICKED:
                    canvas.create_rectangle(col*i, row*i, data["cell size"] +col*i, data["cell size"] +row*i, fill="blue")
            
    
### WEEK 2 ###

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

def getClickedCell(data, event):
    x = int(event.x/data["cell size"])
    y = int(event.y/data["cell size"])
    return [y, x]


def drawShip(data, canvas, ship):
    s = data["cell size"]
    for i in range(len(ship)):
        canvas.create_rectangle(s*ship[i][1], s*ship[i][0], s*(ship[i][1]+1), s*(ship[i][0]+1), fill="white")


def shipIsValid(grid, ship):
    if len(ship) == 3:
        if (isVertical(ship) or isHorizontal(ship)) and checkShip(grid, ship):
            return True
    return False


def placeShip(data):
    if shipIsValid(data["user"], data["tempShip"]):
        for ship in data["tempShip"]:
            data["user"][ship[0]][ship[1]] = SHIP_UNCLICKED
        data["user ships"] += 1
    else:
        print("ship is not valid")
    data["tempShip"] = []
    return 


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

def updateBoard(data, board, row, col, player):
    if board[row][col] == SHIP_UNCLICKED:
        board[row][col] = SHIP_CLICKED
    elif board[row][col] == EMPTY_UNCLICKED:
        board[row][col] = EMPTY_CLICKED    
    if isGameOver(board):
        data["winner"] = player
    return 

def runGameTurn(data, row, col):
    if data["computer"][row][col] == SHIP_CLICKED or data["computer"][row][col] == EMPTY_CLICKED:
        return
    if data["computer"][row][col] == SHIP_UNCLICKED or data["computer"][row][col] == EMPTY_UNCLICKED:
        updateBoard(data, data["computer"], row, col, "user")
        guess = getComputerGuess(data["user"])
        updateBoard(data, data["user"], guess[0], guess[1], "comp")
        
        data["current turns"] += 1
        
        if data["current turns"] == data["max turns"]:
            data["winner"] = "draw"
    return 


def getComputerGuess(board):
    row = random.randint(0,9)
    col = random.randint(0,9)
    while board[row][col] == SHIP_CLICKED or board[row][col] == EMPTY_CLICKED:
        row = random.randint(0,9)
        col = random.randint(0,9)
    return [row, col]


def isGameOver(board):
    for i in range(len(board)):
        row = board[i]        
        for j in range(len(row)):
            if row[j] == SHIP_UNCLICKED:
                return False
    return True


def drawGameOver(data, canvas):
    if data["winner"] == "user":
        canvas.create_text(200, 200, text = "you won", font = "Arial 40", fill = "pink")
        canvas.create_text(200, 300, text = "Press Enter to restart", font = "Arial 30", fill = "pink")
    elif data["winner"] == "comp":
        canvas.create_text(200, 200, text = "you lost", font = "Arial 40", fill = "pink")
        canvas.create_text(200, 300, text = "Press Enter to restart", font = "Arial 30", fill = "pink")
    if data["winner"] == "draw":
        canvas.create_text(200, 200, text = "draw", font = "Arial 40", fill = "pink")
        canvas.create_text(200, 300, text = "Press Enter to restart", font = "Arial 30", fill = "pink")
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

    runSimulation(500, 500)
