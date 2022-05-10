from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.color("white")
        self.hideturtle()
        self.penup()
        
        self.b_score = 0
        self.r_score = 0
        
    
    def UpdateScoreBoard(self):
        
        self.clear()
    
        self.goto(-50, 265)
        self.color("sky blue")
        self.write(self.b_score, align="center", font=("Courier", 22, "normal"))
        
        self.goto(0, 265)
        self.color("yellow")
        self.write("|", align="center", font=("Courier", 22, "normal"))
        
        self.goto(50, 265)
        self.color("red")
        self.write(self.r_score, align="center", font=("Courier", 22, "normal"))
    
    def l_point(self):
        self.b_score += 1
        
    def r_point(self):
        self.r_score += 1