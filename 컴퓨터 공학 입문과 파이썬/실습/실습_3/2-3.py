list = [70,80,55,61,59,95,100, 20,23,45]
sum = 0
index = 0 
while index<10:
    sum = sum + list[index]
    index = index + 1
print("A학급의 중간고사 점수의 평균은", round(sum/10,2), "입니다")
