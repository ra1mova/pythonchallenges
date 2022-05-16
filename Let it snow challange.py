import turtle
from random import randint

myPen = turtle.Turtle()
myPen.shape("turtle")
myPen.speed(500)
myPen.pensize(2)

def snowflake(color,x,y,size,branches):
  myPen.penup()
  myPen.goto(x,y)
  myPen.pendown()
  
  myPen.color(color)
  myPen.left(90)
  
  for i in range(0,branches):
    myPen.forward(100*size/100)
    myPen.forward(-40* size/100)
    myPen.left(40)
    myPen.forward(30* size/100)
    myPen.forward(-30*size/100)
    myPen.right(80)
    myPen.forward(30*size/100)
    myPen.forward(-30*size/100)
    myPen.left(40)
    myPen.forward(-60*size/100)
    myPen.right(360/branches)

for i in range(0,20):
  randomX = randint(-180,180)
  randomY = randint(-180,180)
  randoms = randint(5,40)
  red = randint(0,255)
  green = randint(0,255)
  blue = randint(0,255)
  branches = randint(5,10)
  
  snowflake((red,green,blue),randomX,randomY,randoms,branches)
  
