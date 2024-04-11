x = int(input("크리스마스 트리의 층(단)수를 입력하시오:"))
star = "*"
space = " "
for num in range(1,x+1):
    print(f"{(x-1)*space}{(num*2-1)*star}")
    x -= 1