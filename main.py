from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

score = 0

position = [(0,0) , (-20, 0) ,(-40, 0)]
screen = Screen()   
segments = []
#Setting up the Screen

screen.setup(height=600, width=600)
screen.bgcolor("black")

screen.tracer(0) # Turns of the animation happening on the screen so as to not display each of the segments being created 
game_on = True

snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()
# CODE TO MOVE THE SNAKE ON KEY PRESSES

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
# We turn on the anaimation once all the segments are created
while game_on:
    screen.update() 
    time.sleep(0.1) # The screen gets updated only when all the three segments have moved forward 
    snake.move()
    
    
    # Detecting Collision with food
    if snake.segments[0].distance(food) < 15 :    # Checks if the distance between the head of snake and food is < 15
        food.move_food()
        snake.extend()
        score_board.update_score()
    # detect collision with wall
    if snake.segments[0].xcor() < -280 or snake.segments[0].xcor() > 280 or snake.segments[0].ycor() < -280 or snake.segments[0].ycor() > 280:
        score_board.game_over()
        game_on = False

    # detect collision with tail
    for segment in snake.segments[1:]:  # eliminates the first iteration bcoz at first the head would be at the position of current segment (0,0)
        if snake.segments[0].distance(segment) < 10:
            score_board.game_over()
            game_on = False
    
screen.exitonclick()
