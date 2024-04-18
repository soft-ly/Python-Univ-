import math
a=int(input("이차항계수 입력"))
b=int(input("일차항계수 입력"))
c=int(input("상수항 입력"))
def Polynomial_Discriminant():
    global a
    global b
    global c
    global answer
    return (b**2-4*a*c)
answer= Polynomial_Discriminant()
def quadratic_formula_p():
    global a
    global b
    global c
    return (-b+math.sqrt(pow(b,2)-4*a*c))/2*a
def quadratic_formula_n():
    global a
    global b
    global c
    return (-b-math.sqrt(pow(b,2)-4*a*c))/2*a
if answer<0:
    print("이 식의 실수 해는 존재하지 않음.")
elif answer == 0:
    print("이 식의 실수 해는 1개 (중근)이고, 해의 값은:", -b/2*a)
elif answer > 0:
    print(f"이 식의 실수 해는 2개 이고, 해의 값은:\n첫 해: {quadratic_formula_p()}\n두번째 해: {quadratic_formula_n()}")