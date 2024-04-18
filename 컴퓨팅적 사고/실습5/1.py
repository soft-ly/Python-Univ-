import math
functionwanted=input("원하시는 함수는? ")
number=float(input("숫자 입력! "))

if functionwanted == "abs":
    print(abs(number))
elif functionwanted == "cos":
    print(math.cos(number))
elif functionwanted == "sin":
    print(math.sin(number))
elif functionwanted == "log":
    print(math.log(number))
elif functionwanted == "exp":
    print(math.exp(number))
    