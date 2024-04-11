#속담이 10번 찍어 안넘어간다면, 10번 안에서도 넘어갈수도 있다고 생각해,
#재미로 좀 더 추가해봤습니다 ㅎㅎ

import random
a = random.randint(0,10)
b=1
while b<=a:
    print(f"나무를 {b}번 찍었습니다.")
    b+=1
if b>a:
    print("나무가 넘어갔습니다")


