#전역함수 지정
a = int(input())
b = int(input())

#A: 더하기 함수
def add(x,y):
    return x+y
print(add(a,b))

#B:빼기 함수
def subtract(x,y):
    return x-y
print(subtract(a,b))

#C: 곱하기 함수
def mult(x,y):
    return x*y
print(mult(a,b))

#D: 나누기 함수 (몫과 나머지 각각 출력)
def div(x,y):
    return x//y, x%y
print(div(a,b))
