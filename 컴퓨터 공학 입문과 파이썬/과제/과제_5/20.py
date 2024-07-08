def avg_numbers(args):
    result = 0
    for i in args:
        result+=i
    return result / len(args)

a= [1,2]
b= [1,2,3,4,5]

print(avg_numbers(a))
print(avg_numbers(b))