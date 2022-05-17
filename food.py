from turtle import Turtle,colormode
import random

colormode(256)
COLORS = ["gold", "blue", "hot pink" , "forest green", "orange red",  "olive", "red"]
for i in COLORS:
    i.strip()
#turtle = self, Turtle dan inherit alacak! => bir Turtle objesine yeni attributes lar ekleyerek extend edicez!
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color(random.choice(COLORS))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(COLORS))
        self.goto(random.randrange(-275, 275), random.randrange(-275, 275))
