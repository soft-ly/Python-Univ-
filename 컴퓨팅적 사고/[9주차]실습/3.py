def Average_3(one, two , three):
    return (one+two+three)/3
kor= int(input("국어 성적을 입력하시오"))
math = int(input("수학 성적을 입력하시오"))
eng = int(input("영어 성적을 입력하시오"))
res = round(Average_3(kor, math, eng), 2)
print(f"3 과목의 평균은 {res}점 입니다")
