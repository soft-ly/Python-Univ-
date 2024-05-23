import turtle
turtle.clearscreen()
turtle.setup(400,400)
turtle.shape('arrow')
turtle.color('green')

def turtle_up(distance):
    turtle.left(90)
    turtle.forward(distance)
    turtle.right(90)

def turtle_down(distance):
    turtle.right(90)
    turtle.forward(distance)
    turtle.left(90)

def turtle_forward(distance):
    turtle.forward(distance)

def turtle_backward(distance):
    turtle.right(180)
    turtle.forward(distance)
    turtle.right(180)

while True:
    a = int(input('방향을 입력하세요 (앞: 1 / 뒤: 2 / 위: 3 / 아래: 4) '))
    b = int(input('이동할 거리를 입력하세요: '))
    if a == 1:
        turtle_forward(b)
    elif a == 2:
        turtle_backward(b)
    elif a == 3:
        turtle_up(b)
    elif a == 4:
        turtle_down(b)
    else:
        print("Error: 잘못입력하셨습니다")
        break
