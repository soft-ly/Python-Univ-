number = 17
square = 3 #우선 3으로 저장됨
def square_return(number):
 square = number ** 2 #square를 number의 제곱으로 저장시키고
 return square + 1 #이 함수의 값을 square 의 값과 1을 더한 값으로 만든다
square = square_return(number) #함수를 부른다
print(square) #17**2 = 289 ==> 289+1= "290"