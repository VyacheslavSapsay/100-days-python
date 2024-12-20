from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__(visible=False)
        super().color('black')
        super().penup()
        self.refresh()
    
    def refresh(self):
        super().clear()
        super().setposition(0, 270)
        super().write(f'Level: {self.level}', False, align='center', font=FONT)
    
    def level_up(self):
        self.level += 1
        self.refresh()
    
    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
