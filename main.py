def makeboard():
  board = []
  for i in range(3):
    row = [' ',' ',' ']
    board.append(row)
  return board
def displayboard(board):
  print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
  print("-"*11)
  print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
  print("-"*11)
  print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")
def isValidMove(board, row, column):
  return board[int(row)-1][int(column)-1] == ' '
def CheckWin(board, player):
  if board[0][0] == board[0][1] == board[0][2] == player:
    return player
  if board[1][0] == board[1][1] == board[1][2] == player:
    return player
  if board[2][0] == board[2][1] == board[2][2] == player:
    return player
  
  if board[0][0] == board[1][0] == board[2][0] == player:
    return player
  if board[0][1] == board[1][1] == board[2][1] == player:
    return player
  if board[0][2] == board[1][2] == board[2][2] == player:
    return player
  
  if board[0][0] == board[1][1] == board[2][2] == player:
    return player
  if board[0][2] == board[1][1] == board[2][0] == player:
    return player
  for r in range(3):
    for c in range(3):
      if board[r][c] == " ":
        return "continue"
      if r+c == 4:
        return "tie"
board = makeboard()  
player = 'x'
Status = "continue"
while True:
  displayboard(board)
  userinput = input("Choose a Row (1-3): ")
  row = userinput
  userinput = input("Choose a Column (1-3): ")
  column = userinput
  if row.isdecimal() and column.isdecimal():
    if 1 <= int(row) <= 3 and 1 <= int(column) <= 3:
      if isValidMove(board, row, column):
          board[int(row)-1][int(column)-1] = player 
          Status = CheckWin(board,player)
          if Status != "continue":
            break
          if player == 'o':
            player = 'x'
          else:
            player = 'o'
      else:
        print("That spot is already taken")
    else:
      print("Your number must be in between 1 and 3")
  else:
    print("You must type a number")
displayboard(board)
if Status == "tie":
  print("It is a tie")
else:
  print(f"Player {Status} won")
