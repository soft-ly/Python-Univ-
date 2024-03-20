rate = 0.05

def term_deposit(principal, period, rate):
    savings = principal*(1+rate*period)
    return savings

print(term_deposit())