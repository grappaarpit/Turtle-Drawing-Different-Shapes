import turtle as t
from random import randint

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########
tim.shape("turtle")
t.colormode(255)

#screen.colormode(255)

def change_color():
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  tim.color(r,g,b)

########### Challenge 3 - Draw Shapes ########
for i in range (3,11):
  num = 0
  change_color()
  while(num<i):
    tim.forward(100)
    tim.right(360/i)
    num+=1
    