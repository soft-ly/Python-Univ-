from pathlib import Path
first_answer=''
second_answer=''
third_answer=''
with open(Path()/"student_scores.txt","r",encoding="utf-8") as f:
    for line in f:
        list = line.split()
        if list[0] == "남궁기연":
            first_answer = list[4]
        elif list[0] == "윤종하":
            second_answer = list[1]
        elif list[0] == "탁인숙":
            third_answer = list[5]
print(f'{first_answer}\n{second_answer}\n{third_answer}')