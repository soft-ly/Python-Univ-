a = int(input())
print(a, "의 약수: ",end='')
for item in range(1,a+1):
    if a % item ==0:
        print(item,", ",end='',sep='')