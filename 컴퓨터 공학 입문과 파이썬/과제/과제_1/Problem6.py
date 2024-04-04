x="  "
y="* "
i=1
z = [x,x,x,x,y]

while i <=5 :
    for all in z:
        print(all, end=' ')
    del z[0]
    z.append(y) 
    i = i + 1
    print("\n")

while i > 1 :
    del z[4]
    z.insert(0,x)
    i = i - 1
    for all in z:
        print(all, end=' ')
    print("\n")
