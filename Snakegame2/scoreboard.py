from turtle import Turtle
FONT=('Courier', 24, 'bold')

class score(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
    def update(self):
        self.write(f"Score: {self.score}", align="center", font=FONT)
    def increasescore(self):
        self.score+=1
        self.clear()
        self.update()
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=('Courier', 42, 'bold'))
