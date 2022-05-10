from turtle import Turtle

class SideBars(Turtle):
    
    def __init__(self, bar_pos):
        super().__init__()
        
        self.bar_pos = bar_pos
        
        self.shape("square")
        self.color("white")
        self.penup()
        self.barPositions()
        
    def barPositions(self):
        if self.bar_pos == "top":
            self.goto(0, 265)
            self.shapesize(0.2, 500)
            
        elif self.bar_pos == "bottom":
            self.goto(0, -290)
            self.shapesize(0.2, 500)
        
        elif self.bar_pos == "left":
            self.goto(-396, 0)
            self.shapesize(500, 0.2)
            
        elif self.bar_pos == "right":
            self.goto(389, 0)
            self.shapesize(500, 0.2)
    
        