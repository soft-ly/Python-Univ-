lan1 = int(input("국어 : "))
lan2 = int(input("영어 : "))
sci = int(input("과학 : "))
soc = int(input("사회 : "))
def ave(a,b,c,d):
    total_score=a+b+c+d
    avg_score = total_score/4
    return total_score, avg_score
print(ave(lan1, lan2, sci, soc))