a= int(input("입력하시오"))
x =10
def mult():
    print( x * a)
def div():
    print( x / a)
def add():
    print( x + a)
def sub():
    print( x - a)
if a >= 100:
    mult()
elif 50 <= a < 100:
    div()
elif 20 <= a < 50:
    add()
elif 0 <= a < 20:
    sub()
