from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.setpos(STARTING_POSITION)

    def Up(self):
        if self.ycor() <= FINISH_LINE_Y:
            self.goto(0, self.ycor()+MOVE_DISTANCE)

    def Down(self):
        if self.ycor() > -280:
            self.goto(0, self.ycor()-MOVE_DISTANCE)

    def resetPosition(self):
        self.goto(STARTING_POSITION)

    def finishLine(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False
