vowels = ['a','e','i','o','u','A','E','I','O','U']
a=input()
result=0
for vow in vowels:
    result += a.count(vow)
print(result)

def count_vowels():
    global b
    global c
    global vowels
    for let in b:
        for vow in vowels:
            if vow == let:
                c += 1
    return c
b=list(a)
c=0
print(count_vowels())
