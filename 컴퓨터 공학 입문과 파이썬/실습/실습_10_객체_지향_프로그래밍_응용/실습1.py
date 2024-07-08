import turtle
wn = turtle.Screen()

colors = ['black', 'magenta']

t = turtle.Turtle()
t.shape("turtle")

step = int(input("얼마나 앞으로 갈까요?"))

def rectangle():
    global step
    for i in range(4):
        
        angle = 90
        t.forward(step)
        t.right(angle)

rectangle()


wn.mainloop()