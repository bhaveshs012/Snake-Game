from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("green")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) # Makes the food size half 
        self.move_food()

    def move_food(self):
        x_coord = random.randint(-280,280)
        y_coord = random.randint(-280,280)  # TO make sure that the food doesnt go out of the 300*300 screen
        self.goto(x_coord,y_coord)
