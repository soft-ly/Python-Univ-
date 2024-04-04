a=int(input("입력하시오"))
b=int(input("입력하시오"))
def sub():
    return a-b
def add():
    return a+b
if sub()<0 and add() < 0 :
    print("두 가지 결과가 음수로 나왔습니다.")
elif sub()<0 or add()<0:
    print("두 가지 결과 중 하나만 음수로 나왔습니다.")
elif sub()>0 and add()>0:
    print("두 가지 결과가 양수로 나왔습니다.")
    