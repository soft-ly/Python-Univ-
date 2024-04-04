rate = 0.05

def term_deposit(principal, period, rate):
    savings = principal*(1+rate*period)
    return savings

print(term_deposit(input("원래 금액, 기간, 금리")))