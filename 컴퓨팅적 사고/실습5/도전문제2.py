import datetime
def today():
    d = datetime.date.today()
    if d.weekday() == 0:
        weekday="일"
    elif d.weekday() ==1:
        weekday="월"
    elif d.weekday() ==2:
        weekday="화"
    elif d.weekday() ==3:
        weekday="수"
    elif d.weekday() ==4:
        weekday="목"
    elif d.weekday() ==5:
        weekday="금"
    elif d.weekday() ==6:
        weekday="토"
    return f"{d.year}년 {d.month}월 {d.day}일 {weekday}요일"

print("오늘은",today(), "입니다.")