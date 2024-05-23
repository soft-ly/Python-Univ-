import math
from random import randint
baskinsthirtyone = 0
for x in range(0,100):
    a = int(input("1과 3 사이의 숫자를 입력하시오: "))
    if 0<a<4:
        for _ in range(0,a):
            baskinsthirtyone += 1
            print(baskinsthirtyone)
            if baskinsthirtyone >= 31:
                break
        if baskinsthirtyone >= 31:
            print("컴퓨터의 승리! 게임 오버")
            break
        print("다음! 컴퓨터의 차례!") 
    else:
        print("오류:3 이상의 숫자 불가능. 다시 시작하시오.")
        break

    pc = randint(1,3)
    print("컴퓨터의 숫자 선택:", pc)
    for _ in range(0,pc):
        baskinsthirtyone += 1
        print(baskinsthirtyone)
        if baskinsthirtyone >= 31:
            break
    if baskinsthirtyone >= 31:
        print("사용자의 승리! 게임 오버")
        break
    print("다음! 사용자의 차례")
    
