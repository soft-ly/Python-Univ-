n = int(input("2부터 9 사이의 자연수를 입력하시오"))
list=[1,2,3,4,5,6,7,8,9]
for item in list:
    ans = n * item
    if 2<=n<=9:
        print(f"{n} * {item} = {ans}")
