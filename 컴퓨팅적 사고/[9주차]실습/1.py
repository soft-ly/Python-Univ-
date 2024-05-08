def calculate(x, y,z):
   if z == "+":
      return x + y
   elif z == "-":
      return x - y
   elif z == "*":
      return x * y
   elif z == "/":
      return x/y
num1 = int(input("숫자 1 입력"))
num2 = int(input("숫자 2 입력"))
opt = input("연산자 입력")
res = calculate(num1, num2, opt)
print(f"정답은: {res}")