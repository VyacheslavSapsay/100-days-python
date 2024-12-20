from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 25, 'bold')

class ScoreBoard(Turtle):
    SCORE_POSITIONS = {
        'right': (300, 270),
        'left': (-300, 270)
    }
    def __init__(self):
        super().__init__(visible=False)
        self.color('white')
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.refresh()
    
    def refresh(self):
        self.clear()
        self.setposition(300, 270)
        self.write(self.l_score, False, align=ALIGN, font=FONT)
        self.setposition(-300, 270)
        self.write(self.r_score, False, align=ALIGN, font=FONT)
        
    def l_point(self):
        self.l_score += 1
        self.refresh()
    
    def r_point(self):
        self.r_score +=1
        self.refresh()