answer = int(input("몇X몇으로?"))

pm = "+ - - " 
ps = "|     " 
plus_sign = "+"
pipe_sign = "|"
def print_pm(y):
    print(pm * y + plus_sign)
def print_ps(x):
    ps_line = ps * x + pipe_sign
    print(ps_line, ps_line, sep="\n")
def grid(n):
    count = 0
    while count < n:
        print_pm(n)
        print_ps(n)
        count += 1
    print_pm(n)
    return n**2
print(grid(answer))
