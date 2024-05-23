class Family():
    lastname = '신'

a = Family()
b = Family()

Family.lastname = '최'

print(Family.lastname)


print(a.lastname)
print(b.lastname)