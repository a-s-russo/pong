from turtle import Turtle

import parameters


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.side = side
        self.shape('square')
        self.shapesize(stretch_wid=parameters.PADDLE_SIZE, stretch_len=1)
        self.color('white')
        self.penup()
        if self.side == 'left':
            self.goto(parameters.LEFT_BOUNDARY +
                      parameters.BALL_SHAPE_SIZE * 2, 0)
        if self.side == 'right':
            self.goto(parameters.RIGHT_BOUNDARY -
                      parameters.BALL_SHAPE_SIZE * 2, 0)

    def up(self):
        new_y = self.ycor() + 20
        if new_y <= parameters.TOP_BOUNDARY - parameters.BALL_SHAPE_SIZE * (round(parameters.PADDLE_SIZE / 2) + 1):
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        if new_y >= parameters.BOTTOM_BOUNDARY + parameters.BALL_SHAPE_SIZE * (round(parameters.PADDLE_SIZE / 2) + 1):
            self.goto(self.xcor(), new_y)
