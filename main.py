# making the board
board = [
          ["_","_","_" ],
          ["_","_","_" ],
          ["_","_","_" ]
          ]


# This function will show the current condition of the board
def show_board():
  print(*board[0])
  print(*board[1])
  print(*board[2])


# this function will decide who wins
def is_win(b, c): # b = board, c = chosen charecter
  if ((b[0][0] == b[0][1] == b[0][2] == c) or
  (b[0][0] == b[1][0] == b[2][0] == c)) :
    return True
  elif ((b[2][2] == b[1][2] == b[0][2] == c) or
        (b[2][2] == b[2][1] == b[2][0] == c)) :
    return True
  elif ((b[0][0] == b[1][1] == b[2][2] == c) or
        (b[0][1] == b[1][1] == b[2][1] == c) or
        (b[0][2] == b[1][1] == b[2][0] == c) or
        (b[1][2] == b[1][1] == b[1][0] == c)):
    return True
  else:
    return False


#this function is responsible for actual playing
def play():
  for chance in range(1,6): # five time this game will play
    p1 = input ("Player1 enter your position: ")
    board[int(p1[0])][int(p1[1])]= "X"
    show_board()
    if chance >2 and is_win(board, "X")==True:
      print("Player2 Loose! ")
      break
    if chance==5:
      print("Match Draw")
      break
    p2 = input ("Player2 enter your position: ")
    board[int(p2[0])][int(p2[1])] = "0"
    show_board()
    if chance >2 and is_win(board, "0")==True:
      print("Player1 Loose! ")
      break
# Work flow of the game
def start_game():
  show_board()
  play()

#starting the game
start_game()