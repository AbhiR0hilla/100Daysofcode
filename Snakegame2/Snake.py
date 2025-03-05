from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Use uppercase for constants
DOWN=270
UP=90
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):                 #THIS PART CREATES THE SNAKE ITSELF
        for position in STARTING_POSITIONS:
            self.addsegment(position)
    def addsegment(self,position):
            segment = Turtle("square")
            segment.color("white")
            segment.speed('fast')
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
    def extend(self):
        self.addsegment(self.segments[-1].position())
        # Optional: Set a minimum speed to prevent it from becoming too fast

    def move(self):
        # Move each segment to the position of the one ahead of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(15)
    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
