a = int(input("당신의 근무일수를 입력하시오"))
b = input("당신의 직책을 입력하시오")
calcy= a // 365
lefty= a% 365
calcm= lefty // 30
leftm= lefty % 30
calcw= leftm // 7
leftw= leftm % 7
if b == "본부장":
    print(f"총 {calcy}년 {calcm}월 {calcw}주 {leftw}일을 근무했습니다. \n 그에 따른 퇴직금은 15,000,000원 입니다")
elif b == "실장":
    print(f"총 {calcy}년 {calcm}월 {calcw}주 {leftw}일을 근무했습니다. \n 그에 따른 퇴직금은 10,000,000원 입니다")
elif b == "팀장":
    print(f"총 {calcy}년 {calcm}월 {calcw}주 {leftw}일을 근무했습니다. \n 그에 따른 퇴직금은 5,000,000원 입니다")
elif b == "파트장":
    print(f"총 {calcy}년 {calcm}월 {calcw}주 {leftw}일을 근무했습니다. \n 그에 따른 퇴직금은 3,000,000원 입니다")
elif b == "일반사원":
    print(f"총 {calcy}년 {calcm}월 {calcw}주 {leftw}일을 근무했습니다. \n 그에 따른 퇴직금은 1,000,000원 입니다")