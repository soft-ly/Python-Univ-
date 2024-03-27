def avg_numbers(name=[]):
    result = 0
    for i in name:
        result += i 
    print(result/len(name))
a = input("예제 답? Y - N .... <N은 계산기>")
if a == "Y":
    avg_numbers([1,2])
    avg_numbers([1,2,3,4,5])
elif a == "N":
    x=int(input("과목 수?"))
    y=0
    score = []
    while y < x: 
        a= int(input())
        score.append(a) 
        y += 1
    avg_numbers(score)
else:
    print("오류... 대문자 확인")