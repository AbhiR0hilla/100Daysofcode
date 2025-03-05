from turtle import Turtle,Screen
from Snake import Snake
from food import Food
from scoreboard import score

screen = Screen()
screen.bgcolor("black")
screen.title("The Snake Game")
screen.setup(width=600,height=600)
scorebord=score()
segments=[]
gameon=True
food=Food()
snake=Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.down,"Down")

while gameon:
    screen.update()
    snake.move()
    scorebord.update()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scorebord.increasescore()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        gameon=False
        scorebord.gameover()

    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<12:
            gameon=False
            scorebord.gameover()
screen.exitonclick()

