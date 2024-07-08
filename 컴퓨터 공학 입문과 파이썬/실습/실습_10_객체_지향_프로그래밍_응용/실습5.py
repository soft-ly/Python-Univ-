import turtle
import math
wn = turtle.Screen()
x = int(input("첫 변수: 한 원의 반지름 당 정해진 라디안"))
y = int(input("두번째 변수: 돌리고 싶은 횟수"))
a = turtle.Turtle()
a.speed(0)
result = 360/x*y
intresult = int(round(result, None))
for i in range(intresult):
    a.circle(i,x)

wn.mainloop()