print("Hi") #"Hi"를 출력해라는 명령
def funcA(): #새로운 A함수(일종의 명령 집합소) 생성
    print("A") #함수 내용: "A"를 출력해라는 명령

def funcB(): #새로운 B함수 생성
    print("B") #함수 내용: "B"를 출력해라는 명령
    funcA() #            기존의 A함수를 실행시키는 명령

def funcC(): #새로운 C함수 명령
    print("C") #함수 내용: "C"를 출력해라는 명령
    funcA() #            기존의 A함수를 실행시키는 명령
    funcB() #            기존의 B함수를 실행시키는 명령
print("D") #"D"를 출력해라는 명령
funcC() #C함수를 실행시키는 명령