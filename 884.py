# CONSTANTS
CELL_A = "X"
CELL_B = "O"
CELL_EMPTY = "-"
PLAYER_A = "Player A"
PLAYER_B = "Player B"
WIDTH = 8
HEIGHT = 8

# FUNCTIONS
def getIsPlayerAI(player):
  res = input(f"Is {player} computer: (Y/N) ").lower()
  if res == "y":
    return True
  elif res == "n":
    return False
  else:
    print("Please input Y or N")
    exit()

def getBoard():
  # First row (array), then column (cell).
  board = []
  for r in range(0, HEIGHT):
    row = []
    for c in range(0, WIDTH):
      row.append(CELL_EMPTY)
    board.append(row)
  return board

def printHeader():
  header = "+"
  for i in range(0, WIDTH):
    header += "-"
  header += "+"
  print(header)

def printFooter():
  footer = "+"
  valueForA = 65
  for i in range(0, WIDTH):
    footer += chr(valueForA+i)
  footer += "+"
  print(footer)

def printRow(row):
  cells = "|"
  for i in range(0, WIDTH):
    cells += row[i]
  cells += "|"
  print(cells)

def printCells(board):
  # The rows are printed from last to first to emulate column height:
  # row of highest index will be on top.
  for r in range(HEIGHT-1, -1, -1):
    printRow(board[r])

def printBoard(board):
  printHeader()
  printCells(board)
  printFooter()

def playAI():
  print("playAI")

def playPlayer():
  print("playPlayer")

def clearScreen():
  for i in range(0, 40):
    print("")

def getWinner(board):
  return None

# LOGIC
AisAI = getIsPlayerAI(PLAYER_A)
BisAI = getIsPlayerAI(PLAYER_B)
board = getBoard()
isGoing = True
winner = None

while winner is None:
  if AisAI is True:
    print("ok")
  else:
    print("ok")
  if BisAI is True:
    print("ok")
  else:
    print("ok")
  clearScreen()
  printBoard(board)
  test = input()
  winner = getWinner(board)
