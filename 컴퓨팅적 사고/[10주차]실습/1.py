import turtle
angle= int(input(""))
for idx in range(angle):
    turtle.forward(50)
    turtle.right(360/angle)
if angle <= 2:
    print("Error")