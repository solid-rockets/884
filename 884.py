# CONSTANTS
CELL_A = "X"
CELL_B = "O"
CELL_EMPTY = "-"
PLAYER_A = "Player A"
PLAYER_B = "Player B"

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
  print("getBoard")

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
  isGoing = False
