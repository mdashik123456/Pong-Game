from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, x_pos, y_pos, color):
        super().__init__()
        
        self.penup()
        self.shape("square")
        self.color(color)
        self.goto(x_pos, y_pos)
        self.shapesize(2.5, 1)


    def Up(self):
        if self.ycor() < 215: # Paddle up with border limitation
            self.goto(self.xcor(), self.ycor() + 40)
        
    def down(self):
        if self.ycor() > -240: # Paddle down with border limitation
            self.goto(self.xcor(), self.ycor() - 40)