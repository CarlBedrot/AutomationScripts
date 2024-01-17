import turtle
class Paddle(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed(0)
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(x, y)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    def move_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.dx = 0.25
        self.dy = -0.25

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

# Set up the screen
wn = turtle.Screen()
wn.title('Pong by Beddan!')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Create paddles and ball
paddle_a = Paddle(-350, 0)
paddle_b = Paddle(350, 0)
ball = Ball()

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a.move_up, 'w')
wn.onkeypress(paddle_a.move_down, 's')
wn.onkeypress(paddle_b.move_up, 'i')
wn.onkeypress(paddle_b.move_down, 'k')

# Main game loop
while True:
    wn.update()
    ball.move()

    # Border collision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.bounce_y()

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.bounce_y()

    # Paddle collision
    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.color("blue")
        ball.bounce_x()

    elif (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.color("red")
        ball.bounce_x()