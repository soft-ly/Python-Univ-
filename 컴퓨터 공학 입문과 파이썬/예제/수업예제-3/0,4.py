Python = int(input("파이썬 점수를 입력하시오"))
DataStructure = int(input("자료구조 점수를 입력하시오"))
AI = int(input("인공지능 점수를 입력하시오"))
print("합격") if (Python+DataStructure+AI)/3 >= 85 else print("불합격")
