import random
password = random.randrange(0,99)
print(password)
passwordinput = ""
trypassword = 0
while trypassword < 5:
    passwordinput = int(input("비밀번호를 맞추어보시오"))
    if password == passwordinput:
        print("맞추셨습니다!")
        break
    else:
        print("틀리셨습니다")
    trypassword += 1