from turtle import *
import time

my_t = Turtle()
my_s = Screen()
my_t.hideturtle()
hideturtle()

def vd(col1,col2):
  penup()
  goto(-200,200)
  pendown()

  pencolor(col1)
  fillcolor(col1)
  begin_fill()
  for i in range(4):
    forward(150)
    right(90)
  forward(150)
  end_fill()

  pencolor(col2)
  fillcolor(col2)
  begin_fill()
  for i in range(4):
    forward(150)
    right(90)
  forward(150)
  end_fill()


def vt(col1,col2,col3):
  penup()
  goto(-200,200)
  pendown()

  pencolor(col1)
  fillcolor(col1)
  begin_fill()
  forward(100)
  right(90)
  forward(150)
  right(90)
  forward(100)
  right(90)
  forward(150)
  right(90)
  forward(100)
  end_fill()

  pencolor(col2)
  fillcolor(col2)
  begin_fill()
  forward(100)
  right(90)
  forward(150)
  right(90)
  forward(100)
  right(90)
  forward(150)
  right(90)
  forward(100)
  end_fill()

  pencolor(col3)
  fillcolor(col3)
  begin_fill()
  forward(100)
  right(90)
  forward(150)
  right(90)
  forward(100)
  right(90)
  forward(150)
  right(90)
  forward(100)
  end_fill()

def hd(col1,col2):
  penup()
  goto(-200,200)
  pendown()

  pencolor(col1)
  fillcolor(col1)
  begin_fill()
  forward(300)
  right(90)
  forward(75)
  right(90)
  forward(300)
  right(90)
  forward(75)
  right(180)
  forward(75)
  left(90)
  end_fill()

  pencolor(col2)
  fillcolor(col2)
  begin_fill()
  forward(300)
  right(90)
  forward(75)
  right(90)
  forward(300)
  right(90)
  forward(75)
  right(180)
  forward(75)
  left(90)
  end_fill()


def ht(col1,col2,col3):

  penup()
  goto(-200,200)
  pendown()

  pencolor(col1)
  fillcolor(col1)
  begin_fill()
  forward(300)
  right(90)
  forward(75)
  right(90)
  forward(300)
  right(90)
  forward(75)
  right(180)
  forward(75)
  left(90)
  end_fill()

  pencolor(col2)
  fillcolor(col2)
  begin_fill()
  forward(300)
  right(90)
  forward(75)
  right(90)
  forward(300)
  right(90)
  forward(75)
  right(180)
  forward(75)
  left(90)
  end_fill()

  pencolor(col3)
  fillcolor(col3)
  begin_fill()
  forward(300)
  right(90)
  forward(75)
  right(90)
  forward(300)
  right(90)
  forward(75)
  right(180)
  forward(75)
  left(90)
  end_fill()

ht("orange","white","green")  

my_s.addshape("ashoka-chakra-png-transparent-image-0 (1).gif")
my_t.shape("ashoka-chakra-png-transparent-image-0 (1).gif")
my_t.penup()
my_t.goto(-50,87.5)
my_t.pendown()
my_t.showturtle()


"""
print("Here are some common flag layouts:")
print("1. Vertical Dualcolor")
print("2. Vertical Tricolour")
print("3. Horizontal Dualcolour")
print("4. Horizontal Tricolour")

type = int(input("Flag Layout Option:"))

if type == 1:
  vd(input("Colour1"),input("Colour2"))
elif type == 2: 
  vt(input("Colour1"),input("Colour2"),input("Colour3"))
elif type == 3:
  hd(input("Colour1"),input("Colour2"))
elif type == 4:
  ht(input("Colour1"),input("Colour2"),input("Colour3"))
"""

time.sleep(3)