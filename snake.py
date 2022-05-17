import random
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = [ ]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            tuna = Turtle(shape="square")
            tuna.penup()
            tuna.color("white")
            tuna.goto(STARTING_POSITIONS[i])
            self.segments.append(tuna)
            self.head = self.segments[0] #self.segments[0] yerine self.head de yazılabilir!

    def add_segments(self):
        tuna = Turtle(shape="square")
        tuna.penup()
        tuna.color("white")
        last_segment = self.segments[len(self.segments)-1]
        tuna.goto(last_segment.xcor(),last_segment.ycor())
        self.segments.append(tuna)


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def position(self):
        return self.head.position()

    def reset(self):
        for  i in self.segments: #segmentler görünemeyecek bir yere gönderilirki ki sahnede kalmasın ölünce!
            i.goto(random.randint(-2000,-1000),random.randint(-2000,-1000))
        self.segments.clear() #listedeki tüm elemanlar silinecek!
        self.create_snake()
        self.head = self.segments[0]
