temp= int(input("입력하시오"))
humi= int(input("입력하시오"))

if temp >= 25 and humi >= 70:
    print(f"현재 온도: {temp}, 현재 습도: {humi}, 에어컨 스위치: ON")
elif 23<=temp < 25 and humi >= 70:
    print(f"현재 온도: {temp}, 현재 습도: {humi}, 에어컨 스위치: ON")
elif temp < 23 and humi < 70:
    print(f"현재 온도: {temp}, 현재 습도: {humi}, 에어컨 스위치: OFF")