operator = input("연산기호를 입력하시오")
num1 = int(input("첫 숫자"))
num2 = int(input("두번째 숫자"))
print(f" 연산기호: {operator} \n 숫자1: {num1} \n 숫자2: {num2} \n")

if operator =="+":
    print("결과는", num1 + num2)
if operator =="-":
    print("결과는", num1 - num2)
if operator =="*":
    print("결과는", num1 * num2)
if operator =="/":
    print("결과는", num1 / num2)
if operator =="%":
    print("결과는", num1 % num2)
if operator =="//":
    print("결과는", num1 // num2)
if operator =="**":
    print("결과는", num1 ** num2)