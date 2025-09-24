from turtle import Turtle

# turtles are 20x20 pixels
TURTLE_HEIGHT = 20
TURTLE_WIDTH = 20

MOVE_DISTANCE = 20

UP = 90
DOWN= 270
LEFT = 180
RIGHT = 0

NUM_STARTING_TURTLES = 15

class Snake:
    def __init__(self):
        self.segments = []
        self.grow = False

        self.create_snake()

    def create_snake(self):

        # add in the first segment
        self.add_segment(0, 0)

        # add the remaining segments
        for i in range(1, NUM_STARTING_TURTLES):
            if len(self.segments) > 0:
                last_turtle = self.segments[len(self.segments) - 1]
                last_turtle_position_x = last_turtle.xcor() - TURTLE_WIDTH
                last_turtle_position_y = last_turtle.ycor()
                self.add_segment(last_turtle_position_x, last_turtle_position_y)

    def add_segment(self, x_pos, y_pos):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.setpos(x_pos, y_pos)
        self.segments.append(t)

    def extend(self):
        self.grow = True

    def collide_with_tail(self):
        first_segment = self.segments[0]
        remaining_segments = self.segments[1:]
        for segment in remaining_segments:
            if first_segment.distance(segment) < 10:
                return True

        return False

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()

        self.segments.clear()
        self.create_snake()

    def move(self, direction):
        '''move the snake forward'''

        # if we were asked to grow the snake, add in a new segment at the end of the array (but not necessarily at the
        # end of the tail)
        if self.grow:
            self.add_segment(0, 0)
            self.grow = False

        # we move the snake forward by removing the last segment of the snake and repositioning it to the front

        # get the last segment and the first segment
        first_segment = self.segments[0]
        last_segment = self.segments[len(self.segments) - 1]
        self.segments.remove(last_segment)

        # move the last segment to the specified position
        if direction == "up":
            last_segment.setpos(first_segment.xcor(), first_segment.ycor() + MOVE_DISTANCE)
            last_segment.setheading(UP)
        elif direction == "down":
            last_segment.setpos(first_segment.xcor(), first_segment.ycor() - MOVE_DISTANCE)
            last_segment.setheading(DOWN)
        elif direction == "left":
            last_segment.setpos(first_segment.xcor() - MOVE_DISTANCE, first_segment.ycor())
            last_segment.setheading(LEFT)
        elif direction == "right":
            last_segment.setpos(first_segment.xcor() + MOVE_DISTANCE, first_segment.ycor())
            last_segment.setheading(RIGHT)

        self.segments.insert(0, last_segment)

    def move_up(self):
        first_segment = self.segments[0]
        if int(first_segment.heading()) != DOWN:
            self.move("up")

    def move_down(self):
        first_segment = self.segments[0]
        if int(first_segment.heading()) != UP:
            self.move("down")

    def move_left(self):
        first_segment = self.segments[0]
        if int(first_segment.heading()) != RIGHT:
            self.move("left")

    def move_right(self):
        first_segment = self.segments[0]
        if int(first_segment.heading()) != LEFT:
            self.move("right")

    def continue_moving(self):
        # move in the same direction the head is pointing
        first_segment = self.segments[0]
        if int(first_segment.heading()) == DOWN:
            self.move_down()
        if int(first_segment.heading()) == UP:
            self.move_up()
        if int(first_segment.heading()) == RIGHT:
            self.move_right()
        if int(first_segment.heading()) == LEFT:
            self.move_left()
