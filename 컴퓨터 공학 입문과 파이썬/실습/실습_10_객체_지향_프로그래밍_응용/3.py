import turtle
wn = turtle.Screen()
wn = turtle.bgcolor('lightyellow')

color = ['blue', 'red']

for i in range(2):
    step = 20
    angle = 40
    
    t = turtle.Turtle()
    t.shape('turtle')
    t.color(color[i])
    t.penup()

    t.forward(step*i)
    for _ in range(26):
        t.stamp()
        step += 5
        t.forward(step)
        t.right(angle)

wn.mainloop()