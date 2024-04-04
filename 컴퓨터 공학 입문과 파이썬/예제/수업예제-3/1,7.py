a=int(input("입력하시오"))
def dmas(x):
    if x == "*":
        print(a*10)
    elif x == "/":
        print(a/10)
    elif x == "+":
        print(a+10)
    elif x == "-":
        print(a-10)
     
if a >= 100:
    dmas("*")
elif 50 <= a < 100:
    dmas("/")
elif 20 <= a < 50:
    dmas("+")
elif 0 <= a < 20:
    dmas("-")
