import math
import turtle
import pathlib

game = turtle.Screen()
game.bgcolor("white")
game.title("Collision Detection by SoftL.Y")
game.tracer(0)

pen= turtle.Turtle()
pen.speed(0)
pen.hideturtle()

shapes = ["wizard.gif", "goblin.gif", "pacman.gif", "cherry.gif", "bar.gif", "ball.gif", "x.gif"]

for shape in shapes:
    game.register_shape(shape)


class Sprite():
    def __init__(self,x,y,width,height,image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
    
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.stamp()

    def is_overlapping_collision(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    
    def is_distance_collision(self, other):
        distance = (((self.x-other.x)**2)+((self.y-other.y)**2))**0.5
        if distance < (self.width + other.width)/2.0:
            return True
        else:
            return False
    
    def is_aabb_collision(self, other):
        x_collision = (math.fabs(self.x-other.x)*2) < (self.width + other.width)
        y_collision = (math.fabs(self.y-other.y)*2) < (self.height + other.height)
        return (x_collision and y_collision)
    
wizard = Sprite(-128, 200, 128, 128, "wizard.gif")
goblin = Sprite(128, 200, 108, 128, "goblin.gif")

pacman = Sprite(-128, 0, 128, 128, "pacman.gif")
cherry = Sprite(128, 0, 128, 128, "cherry.gif")

bar = Sprite(0, -400, 128, 24, "bar.gif")
ball = Sprite(0, -200, 32, 32, "ball.gif")

sprites = [wizard, goblin, cherry, pacman, bar, ball]

