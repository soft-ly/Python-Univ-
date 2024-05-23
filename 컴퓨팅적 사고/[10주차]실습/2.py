import turtle
p1= turtle.Turtle()
p1.shape('turtle')
p1.color('orange')

p1.circle(50)

p2=turtle.Turtle()
p2.shape('circle')
p2.color('blue')

for idx in range(1,5):
    p2.forward(50)
    p2.left(90)