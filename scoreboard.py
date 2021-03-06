from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18 , "normal")




class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.show_score()
    
    def show_score(self):
        self.write(f"Score = {self.score} ", align=ALIGNMENT, font=(FONT))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=(FONT))


    def update_score(self):
        self.score += 1
        self.clear()  # To avoid overlapping of prev scores
        self.show_score()