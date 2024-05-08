a = int(input("?"))
def Sum_N(A):
    x=0
    res =0
    while x <= A:
        res += x
        x += 1
    return res

print(Sum_N(a))