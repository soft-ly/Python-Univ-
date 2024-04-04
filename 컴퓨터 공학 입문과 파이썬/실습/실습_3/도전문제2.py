principal = float(input("원금 입력"))
rate = float(input("이자 입력"))
period = float(input("예치기간 입력"))
date =0
total_rate=0
def total():
    global principal
    global total_rate
    ovr = principal + total_rate
    return ovr

while date < period:
    total_rate = total_rate + principal*rate
    date += 1

answer=total()
print(answer)

