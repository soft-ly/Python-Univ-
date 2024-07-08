import turtle
wn = turtle.Screen()

t = turtle.Turtle()
t.shape("turtle")

length = int(input("얼마나 앞으로 갈까요?"))
n = int(input("몇각형을 그릴까요?"))
angle = 180 - 180*(n-2)/n
def shape():
    global step
    global n
    global angle
    for i in range(n):
        t.forward(length)
        t.right(angle)

shape()


wn.mainloop()