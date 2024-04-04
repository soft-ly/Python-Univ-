n = int(input("2부터 9 사이의 자연수를 입력하시오"))
list=[1,2,3,4,5,6,7,8,9]
index=0
while index < 9:
    ans = n * list[index]
    index = index + 1
    if 2<=n<=9:
        print(f"{n} * {list[index]} = {ans}")
    
