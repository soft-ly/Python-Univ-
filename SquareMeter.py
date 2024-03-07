
per_koreanmeter = 1.3025
var = input("평수를 미터로? 아니면 미터를 평수로?")

if var == "미터를 평수로":
    x = input("몇 미터?")
    a = float(x)
    answer = a/per_koreanmeter
    print(answer)

if var == "평수를 미터로":
    x = input("몇 평수?")
    a = float(x)
    answer1 = a*per_koreanmeter
    print(answer1)

