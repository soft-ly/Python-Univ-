a = input("지역을 입력하시오")
b = int(input("온도를 입력하시오"))
if a == "안성":
    print(f' 지역은: {a} \n 온도는: {b} \n "걸어서 등교합니다"')
elif a == "서울" and b > 0:
    print(f' 지역은: {a} \n 온도는: {b} \n "통학버스를 타고 등교합니다"')
elif a =="서울" and b <= 0:
    print(f' 지역은: {a} \n 온도는: {b} \n "자가용을 타고 등교합니다"')
else: 
    print(f' 지역은: {a} \n 온도는: {b} \n "시외버스를 타고 등교합니다"')