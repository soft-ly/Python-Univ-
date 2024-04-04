a=int(input("입력하시오"))
if a >= 90:
    print(f"{a} 점수는 A학점입니다")
elif 90 > a >= 80:
    print(f"{a} 점수는 B학점입니다")
elif 80 > a >= 70:
    print(f"{a} 점수는 C학점입니다")
else:
    print(f"{a} 점수는 D학점입니다") if 70 > a >= 60 else print(f"{a} 점수는 F학점입니다")