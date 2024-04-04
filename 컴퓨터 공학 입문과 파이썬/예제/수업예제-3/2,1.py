a = int(input("첫 숫자"))
b = int(input("두번째 숫자"))
c = input("무슨 계산?")

if c=="+":
    print(a+b)
else:
    if c == "-":
        print(a-b)
    else:
        if c == "*":
            print(a*b)
        else:
            if c == "/":
                print(a/b)