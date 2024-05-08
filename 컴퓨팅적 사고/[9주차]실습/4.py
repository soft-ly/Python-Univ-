a = int(input("숫자"))
def IsPrime(x):
    for i in range(2,a+1):
        prime=0
        for x in range(2,i):
            if i%x == 0 :
                print(f"{i}는 소수가 아님")
                prime=1
                break
        if prime == 0:
            print(f"{i}는 소수임.")
IsPrime(a)
