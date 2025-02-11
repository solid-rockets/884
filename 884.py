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
  # Single row, with columns that can be accessed.
  board = []
  for colCount in range(0, WIDTH):
    col = []
    for colDepth in range(0, HEIGHT):
      col.append(CELL_EMPTY)
    board.append(col)
  return board

def printHeader():
  headerString = ""
  valueForA = 65
  for i in range(0, WIDTH):
    headerString += chr(valueForA+i)
  print(headerString)

def printBoard(board):
  printHeader()
  for r in range(0, HEIGHT):
    row = ""
    for c in range(0, WIDTH):
      # 1st, select column; 2nd, select cell.
      # This way, a row is built.
      row += board[c][r]
    print(row)

def playAI():
  print("playAI")

def playPlayer():
  print("playPlayer")

# LOGIC
AisAI = getIsPlayerAI(PLAYER_A)
BisAI = getIsPlayerAI(PLAYER_B)
board = getBoard()
isGoing = True

while isGoing:
  if AisAI is True:
    print("ok")
  else:
    print("ok")
  if BisAI is True:
    print("ok")
  else:
    print("ok")
  printBoard(board)
  isGoing = False
