allday = int(input("근무일수를 입력하시오."))
year= allday // 365
allday1 = allday % 365
month = allday1 // 30
allday2 = allday1 % 30
week = allday2 // 7
day = allday2 % 7
print("근무일수:", allday)
print(f"{year}년 {month}월 {week}주 {day}일")