def inttostr(a):
    newstr = str(a)
    return newstr
def strtoint(b):
    newint = int(b)
    return newint

x = 10
print("기존 자료형: ", type(x))
x=inttostr(x)
print("입력받은 값: ", x)
print("변환 자료형: ", type(x))


y = "10"
print("기존 자료형: ", type(y))
y=strtoint(y)
print("입력받은 값: ", y)
print("변환 자료형: ", type(y))