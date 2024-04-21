a=[]
c=0
a.append(int(input("")))
print(a)
while True:
    b=int(input(""))
    for num in a:
        if b > num:
            a.insert(c,b)
        if b < num:
            a.insert(c-1,b)
        c+=1
    c=0
    print(a)

    
