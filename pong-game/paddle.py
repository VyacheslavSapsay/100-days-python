from turtle import Turtle

class Paddle(Turtle):
    
    PADDLE_POSITIONS = {
        'right': (350, 0),
        'left': (-350, 0)
    }
    
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(5, 1)
        self.color('white')
        self.speed('fastest')
        self.setposition(self.PADDLE_POSITIONS[position])

    def up(self):
        if self.ycor() < 245:
            self.sety(self.ycor() + 30)
    
    def down(self):
        if self.ycor() > -245:
            self.sety(self.ycor() - 30)
