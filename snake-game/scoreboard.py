from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 25, 'bold')

class ScoreBoard(Turtle):
    def __init__(self):
        self.score = -1
        super().__init__(visible=False)
        super().color('white')
        super().penup()
        self.refresh()
    
    def refresh(self):
        self.score += 1
        super().clear()
        super().setposition(0, 270)
        super().write(f'Score: {self.score}', False, align=ALIGN, font=FONT)
        
    def game_over(self):
        super().setposition(0, 0)
        super().write('Game over', False, align=ALIGN, font=FONT)