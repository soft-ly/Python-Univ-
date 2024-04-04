a=int(input("입력하시오"))
def dmas(x):
    if x == "*":
        print(a*10)
    elif x == "/":
        print(a/10)
    elif x == "+":
        print(a+10)
    else:
        print(a-10) #문제가 발생하긴 하는데, 그냥 아무것도 안 입력해도 사용되어서, 정확성 떨어짐.
     
if a >= 100:
    dmas("*")
elif 50 <= a < 100:
    dmas("/")
elif 20 <= a < 50:
    dmas("+")
elif 0 <= a < 20:
    dmas()
