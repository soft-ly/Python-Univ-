from random import randint, randrange
print(randrange(5)) # 시작 없이 5까지의 숫자를 불러옴
print(randrange(4,5)) #마지막 수 5를 포함하지 않음. 즉, 수학에서 말하는 [1,5)인것이다. randrange(x,x)일때는 공간이 사라져서 에러뜸. randrange(x-1,x)면 x밖에 없음.
randint(1,5) #수학에서 닫힌 구간 같이 [1,5]면 1부터 5까지 고른다.
