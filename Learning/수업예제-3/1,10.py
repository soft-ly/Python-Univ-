A=int(input("입력하시오"))
B=int(input("입력하시오"))
def newA():
    return A*5/3
def newB():
    return B*4/2
if newA() < newB():
    print(newB())
elif newA() > newB():
    print(newA())
elif newA() == newB():
    print(f"두 영역이 {newA()}로 같습니다.")