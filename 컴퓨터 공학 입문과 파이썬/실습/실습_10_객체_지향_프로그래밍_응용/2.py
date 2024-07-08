import turtle
wn = turtle.Screen()

colors = ['black', 'magenta']

p0 = turtle.Turtle()
p0.shape('arrow')
for i in range(4):
    p0.forward(50)
    p0.left(90)


p1 = turtle.Turtle()
p1.shape('turtle')
p1.penup()
p1.goto(-50, 0)
p1.pendown()
for i in range(3):
    p1.forward(50)
    p1.right(120)
    


wn.mainloop()