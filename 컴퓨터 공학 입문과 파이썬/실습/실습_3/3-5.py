n = 2
while n <11:
    is_prime = True #이값이 계속 유지되면 소수임

    for x in range(2,n):
        if n % x == 0: #곱하기가 가능한 숫자 다 찾는것
            is_prime = False
            print("-", n, "=", x, "*", n//x)
            break
            print("따라서", n, "은(는) 소수 아님!") #이건 절대 프린트 안됨! 위의 break 때문

    n += 1
    continue #때문에 밑의 조건문은 안됨...
    if is_prime:
        print("-", n, "은(는) 소수다")
    else:
        print(" ",n, "은(는) 소수가 아니다.")