import time
import turtle
import random

screen = turtle.Screen()
turtle.pendown()
turn = 'x'

def setup_game():
  turtle.penup()
  turtle.speed(0)
  turtle.goto(-200 ,200) 
  turtle.forward(100)
  turtle.pendown()
  turtle.right(90)
  turtle.forward(300)
  turtle.penup()
  turtle.right(-90)
  turtle.forward(100)
  turtle.right(-90)
  turtle.pendown()
  turtle.forward(300)
  turtle.penup()
  turtle.goto(-200, 200)
  turtle.right(180)
  turtle.forward(100)
  turtle.right(-90)
  turtle.pendown()
  turtle.forward(300)
  turtle.penup()
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.pendown()
  turtle.forward(300)

def draw_x (location):
  if location == 0:
    turtle.speed(2.5)
    turtle.penup()
    turtle.goto(-175,175)
    turtle.pendown()
    turtle.goto(-125,125)

    turtle.penup()
    turtle.goto(-125, 175)
    turtle.pendown()
    turtle.goto(-175, 125)

  elif location == 1:
    turtle.speed(2.5)
    turtle.penup()
    turtle.goto(-75,175)
    turtle.pendown()
    turtle.goto(-25,125)

    turtle.penup()
    turtle.goto(-25, 175)
    turtle.pendown()
    turtle.goto(-75, 125)

  elif location == 2:
    turtle.speed(2.5)
    turtle.penup()
    turtle.goto( 25,175)
    turtle.pendown()
    turtle.goto( 75,125)

    turtle.penup()
    turtle.goto(75, 175)
    turtle.pendown()
    turtle.goto(25, 125)

  elif location == 3:
    turtle.speed(2.5)
    turtle.penup()
    turtle.goto(-175, 75 )
    turtle.pendown()
    turtle.goto(-125,25)

    turtle.penup()
    turtle.goto(-125, 75)
    turtle.pendown()
    turtle.goto(-175, 25)

  elif location == 4:
    turtle.speed(2.5)
    turtle.penup()
    turtle.goto(-75,75)
    turtle.pendown()
    turtle.goto(-25,25)

    turtle.penup()
    turtle.goto(-25, 75)
    turtle.pendown()
    turtle.goto(-75, 25)

  elif location == 5:
    turtle.speed(2.5)
    turtle.penup()
    turtle.goto(25,75)
    turtle.pendown()
    turtle.goto(75,25)

    turtle.penup()
    turtle.goto(75, 75)
    turtle.pendown()
    turtle.goto(25, 25)

  elif location == 6:
    turtle.speed(2.5)
    turtle.penup()
    turtle.goto(-175,-25)
    turtle.pendown()
    turtle.goto(-125, -75)

    turtle.penup()
    turtle.goto(-125,-25)
    turtle.pendown()
    turtle.goto(-175, -75)

  elif location == 7:
    turtle.speed(2.5)
    turtle.penup()
    turtle.goto(-75,-25)
    turtle.pendown()
    turtle.goto(-25,-75)

    turtle.penup()
    turtle.goto(-25, -25)
    turtle.pendown()
    turtle.goto(-75, -75)

  elif location == 8:
    turtle.speed(2.5)
    turtle.penup()
    turtle.goto(25,-25)
    turtle.pendown()
    turtle.goto(75,-75)

    turtle.penup()
    turtle.goto(75, -25)
    turtle.pendown()
    turtle.goto(25, -75)

# def draw_o(location): 
def draw_o (location):
  if location == 0:
    turtle.speed(2.5)
    turtle.penup()
    turtle.goto(-150, 175)
    turtle.pendown()
    turtle.circle(25)

  if location == 1:
    turtle.speed(2.5)
    turtle.penup()
    turtle.goto(-50, 175)
    turtle.pendown()
    turtle.circle(25)

  if location == 2:
    turtle.speed(2.5)
    turtle.penup()
    turtle.goto( 50, 175)
    turtle.pendown()
    turtle.circle(25)

  if location == 3:
    turtle.speed(2.5)
    turtle.penup()
    turtle.goto(-150, 75)
    turtle.pendown()
    turtle.circle(25)

  if location == 4:
    turtle.speed(2.5)
    turtle.penup()
    turtle.goto(-50, 75)
    turtle.pendown()
    turtle.circle(25)

  if location == 5:
    turtle.speed(2.5)
    turtle.penup()
    turtle.goto(50, 75)
    turtle.pendown()
    turtle.circle(25)

  if location == 6:
    turtle.speed(2.5)
    turtle.penup()
    turtle.goto(-150 ,-25)
    turtle.pendown()
    turtle.circle(25)

  if location == 7:
    turtle.speed(2.5)
    turtle.penup()
    turtle.goto(-50, -25)
    turtle.pendown()
    turtle.circle(25)

  if location == 8:
    turtle.speed(2.5)
    turtle.penup()
    turtle.goto(50, -25)
    turtle.pendown()
    turtle.circle(25)

def win_check():
    # horizontal check
    for i in range(0, 9, 3):
        if (board[i] == board[i + 1] == board[i + 2]):
            return True

    # vertical check
    for i in range(3):
        if (board[i] == board[i + 3] == board[i + 6]):
            return True

    # diagonal check
    if ((board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6])):
        return True

# user vs computer      
def computer_move (move):

  global board, turn, game, random

  if board[move] >= 0 and board[move] <= 8:
    board[move] = turn
    print ("heres board", board)

    if turn == 'o':
      move = random.choice(board)
      draw_o(move)
      if (win_check()):
        game = 'over'
      turn = 'x'

    elif turn == 'x':
      draw_x(move)
      if (win_check()):
        game = 'over'
      turn = 'o'  

def which_square (x,y):

  """This function will convert the xy coordinate into squares of the tic tac toe board 
  [ 0 | 1 | 2 ]
  [ 3 | 4 | 5 ]
  [ 6 | 7 | 8 ]
  """

  global game

  if game == 'over':
    return None

  # check which square does the xy coordinate belongs to
  # if not((x < -200) or (x > 100)) or ((y > 200) or (y <-100)):
  if y <= 200 and y >= 100:
    if x >= 0:
      move = 2 
    elif x >= -100:
      move = 1 
    elif x >= -200:
      move = 0 

  elif y < 100 and y >=0:
    if x >= 0:
      move = 5 
    elif x >= -100:
      move = 4
    elif x >= -200:
      move = 3

  elif y <0 and y >= -100:
    if x >= 0:
      move = 8
    elif x >= -100:
      move = 7
    elif x >= -200:
      move = 6 

  # draws 
  computer_move(move)

setup_game()

game = 'not over'
move = None
board = [0,1,2,3,4,5,6,7,8]


#Everytime this function is called, it passes xy coordinate into a function inside the parathensis.
screen.onscreenclick(which_square)

print('User 1, please click where you want to go. (You may have to click twice.)')

turtle.done()