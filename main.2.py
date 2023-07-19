import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
race = False
input = screen.textinput("What's your bet", "Which one you think might win?")
color = ["red", "black", "green", "blue", "orange", "yellow"]


ram = Turtle(shape="turtle")
ram.color(color[0])
ram.penup()
ram.goto(-200,99)

aam = Turtle(shape="turtle")
aam.color(color[2])
aam.penup()
aam.goto(-200,66)

lam = Turtle(shape="turtle")
lam.color(color[3])
lam.penup()
lam.goto(-200,33)

cam = Turtle(shape="turtle")
cam.color(color[4])
cam.penup()
cam.goto(-200,0)

zam = Turtle(shape="turtle")
zam.color(color[5])
zam.penup()
zam.goto(-200,-33)

sam = Turtle(shape="turtle")
sam.color(color[1])
sam.penup()
sam.goto(-200,-66)

if input :
    race = True

while race:
    dis = random.randint(0, 10)
    ram.forward(dis)
    zis = random.randint(0, 5)
    aam.forward(zis)
    sam.forward(dis)
    fax = random.randint(0, 15)
    zam.forward(fax)
    cam.forward(fax)
    lam.forward(dis)





screen.exitonclick()



