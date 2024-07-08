import turtle
color = ['red','orange', 'yellow','green','blue','indigo','purple']
wn = turtle.Screen()
n = int(input("몇개의 원을 넣고 싶나요?"))
a = turtle.Turtle()
a.speed(0)
b = 0
for i in range(n):
    a.color(color[b])
    a.circle(100)
    a.right(360/n)
    b+=1
    if b == 7:
        b = 0

wn.mainloop()
