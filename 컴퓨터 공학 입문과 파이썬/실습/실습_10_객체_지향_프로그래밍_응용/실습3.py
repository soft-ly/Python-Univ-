import turtle
import math
wn = turtle.Screen()

t = turtle.Turtle()
t.shape("turtle")


n = int(input("몇각형을 그릴까요?"))

angle = 360/n
anglerad = math.pi/180
otherangle= (180 - angle)/2
otheranglerad = otherangle * anglerad
length = 10/math.cos(otheranglerad)

print(length)
for _ in range(n):
    t.forward(20)
    t.right(angle+otherangle)
    t.forward(length)
    t.right(180-angle)
    t.forward(length)
    t.right(angle+otherangle)
    t.forward(20)
    t.right(angle)




wn.mainloop()