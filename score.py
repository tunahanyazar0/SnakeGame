from turtle import Turtle
FONT = ("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.text = 0
        self.highscore = 0
        self.gethighscore()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(arg=f"Score: {self.text} High Score: {self.highscore}", align="center", font=FONT)

    def updatescoreboard(self):
        self.clear()
        self.gethighscore()
        self.write(arg=f"Score: {self.text} High Score: {self.highscore}", align="center", font=FONT)

    def increase_score(self):
        self.text += 10
        self.updatescoreboard()

    def reset(self):
        if self.highscore < self.text :
            self.highscore = self.text
        self.text = 0
        self.updatescoreboard()

        // keeping ath score with the use of files 
    def gethighscore(self):
        with open("The Location of all the scores are being kept",mode="r") as scores:
            self.highscore = int(max(scores.readlines()))

    def appendscore(self):
        with open("The Location of all the scores are being kept",mode="a") as scores:
            scores.write(f"\n{self.text}")
