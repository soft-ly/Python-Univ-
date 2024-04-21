x = int(input("숫자를 입력하시오"))
for prime in range(2,x):
    if x % prime == 0:
        print(f"{x}는 소수가 아니다.")
        break
    if prime == x-1:
        print(f"{x}는 소수다.")