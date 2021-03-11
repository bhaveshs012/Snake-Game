from turtle import Turtle

STARTING_POSITIONS = [(0,0) , (-20, 0) ,(-40, 0)]  # Constants are declared in all caps
MOVE_DIST = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    # Creating The Snake Body using 3 squares aligned next to each other
    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)
            
    def add_segment(self,i):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(i)
        self.segments.append(new_seg)

    def extend(self):
        self.add_segment(self.segments[-1].position())   # add a new segment at the end  .position() returns a tuple with the position of the segment

    
    def move(self):
        for seg_number in range(len(self.segments)-1,0,-1):   # Here we are iterating through each segment in reverse order
            prev_x = self.segments[seg_number - 1].xcor()  # gets the coordeinates of the prev segment
            prev_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(prev_x,prev_y)   # now the new segment moves to where the previous segment was
            # for e.g. in segment [3,2,1]
            # segment 3 occupies the place of segment 2
        self.segments[0].forward(MOVE_DIST)


    def up(self):
        if self.segments[0].heading() != DOWN:  # when its moving up it shouldnt be able to move down
            self.segments[0].setheading(UP)
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)