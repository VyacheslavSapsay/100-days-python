from turtle import Turtle
import random

class Ball(Turtle):
    DEFAULT_STEP = 3
    HEADINGS = {
        'to_right': (0, 45),
        'to_left': (160, 200)
    }
    
    def __init__(self, heading = None, speed = None):
        super().__init__()
        if heading is None:
            heading = random.choice(list(self.HEADINGS.keys()))
        self.setheading(random.choice(self.HEADINGS[heading]))
        self.color('white')
        self.shape('circle')
        self.speed(0.5)
        self.penup()
        self.step = self.DEFAULT_STEP

    def move(self):
        self.forward(self.step)
        
    def bounce(self):
        self.setheading(-self.heading())
    
    def bounce_by_paddle(self):
        self.step += 0.05
        self.setheading(self.heading() - 180 - random.randint(-30, 30))
        # self.setheading(self.heading() - random.randint(-30, 30))

    