from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.snake[0].color('blue')
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.shapesize(1)
        new_segment.setpos(position)
        self.snake.append(new_segment)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for n in range(len(self.snake) - 1, 0, -1):
            new_position = self.snake[n-1].pos()
            self.snake[n].goto(new_position)
        self.head.forward(17)

    def up(self):
        if self.head.heading() == 270:
            pass
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            pass
        else:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            pass
        else:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            pass
        else:
            self.head.setheading(0)

    def reset_snake(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.__init__()





