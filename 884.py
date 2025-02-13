# CONSTANTS
MARK_A = "X"
MARK_B = "O"
CELL_EMPTY = "-"
TYPE_A = "Player A"
TYPE_B = "Player B"
WIDTH = 8
HEIGHT = 8
VALUE_A = 65

# CLASSES
class Player:
  def __init__(self, name, mark, isAI):
    self.name = name
    self.mark = mark
    self.isAI = isAI

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
    header += "="
  header += "+"
  print(header)

def printFooter():
  footer = "+"
  for i in range(0, WIDTH):
    footer += chr(VALUE_A+i)
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

def clearScreen():
  for i in range(0, 40):
    print("")

def printBoard(board):
  clearScreen()
  printHeader()
  printCells(board)
  printFooter()

def putMark(board, col, mark):
  for row in range(0, HEIGHT):
    if board[row][col] == CELL_EMPTY:
      board[row][col] = mark
      break

def getMoveAI(board, player):
  print("playAI")

def getMovePlayer(board, player):
  moveCol = input(f"{player.name}: ").upper()
  col = ord(moveCol) - VALUE_A
  return col

def getWinner(board):
  return None

def play(board, player):
  clearScreen()
  printBoard(board)
  moveCol = 0
  if player.isAI:
    moveCol = getMoveAI(board, player)
  else:
    moveCol = getMovePlayer(board, player)
  putMark(board, moveCol, player.mark)

# LOGIC
playerA = Player(TYPE_A, MARK_A, getIsPlayerAI(TYPE_A))
playerB = Player(TYPE_B, MARK_B, getIsPlayerAI(TYPE_B))
board = getBoard()
isGoing = True
winner = None

while winner is None:
  play(board, playerA)
  play(board, playerB)
  winner = getWinner(board)
