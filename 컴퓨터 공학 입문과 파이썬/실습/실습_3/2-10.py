print("수 알아맞히기 게임에 오신것을 환영합니다")
secret = 17
guess =-1
while guess != secret:
    guess = int(input("1부터 100사이의 정수 하나를 입력하세요: "))
    if guess == secret:
        print("맞았습니다!")
    elif guess <secret:
        print("너무 작습니다!")
    else:
        print("너무 큽니다!")
print("게임 종료!")