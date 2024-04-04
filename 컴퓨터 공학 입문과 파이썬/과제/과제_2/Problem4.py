
a = int(input("첫 점수를 입력하시오"))
b = int(input("두 번째 점수를 입력하시오"))
c = int(input("세 번째 점수를 입력하시오"))
d = int(input("네 번째 점수를 입력하시오"))
e = int(input("다섯 번째 점수를 입력하시오"))
score_list = [a,b,c,d,e]
def print_score_list(x, y, z):
    print(f"평균 점수 : {x} / 가장 높은 점수 : {y} / 가장 낮은 점수 : {z}")
avg = (a+b+c+d+e)/5
high = max(score_list)
low = min(score_list)
print_score_list(avg, high, low)



