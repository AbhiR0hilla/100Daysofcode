import turtle as tmodule
from turtle import Screen
import random

colors=["red","black","orange","yellow","green"]
screen = Screen()
screen.bgcolor("Antiquewhite2")
tmodule.colormode(255)
screen.setup(width=500,height=400)
y=[-50,-80,-20,10,40,70]
allturtle=[]
userbet=screen.textinput(title="make your bet",prompt="Which turtle will win the race?").lower()

for i in range(0,4):                    #For putting the turtles to a race
    tim = tmodule.Turtle(shape='turtle')
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-200,y= y[i])
    allturtle.append(tim)

if userbet in colors:
    israceon=True
else:
    print("enter a valid bet!")
while israceon==True:
    for tim in allturtle:
        randistance = random.randint(0,10)
        tim.forward(randistance)
        if tim.xcor()>100:                  #For finding who has won the race out of all the turtles
            israceon=False
            winningcol=tim.pencolor()
            if winningcol==userbet:
                print("You have WON and winner is ",winningcol,"!!")
                break
            else:
                print("you have lost,winner is",winningcol)
                break

screen.exitonclick()

