from pathlib import Path
student_scr= []
student_intscr =[]
name=[]
score = []
with open(Path()/"student_scores.txt","r",encoding='utf-8') as f:
    for line in f:
        x = line.split()
        student_scr.append(x)
        student_score = []
        for y in range(0,6):
            if y==0:
                name.append(x[y])
            elif y >= 1:
                score.append(x[y])
                student_score.append(x[y])
        student_intscr.append(student_score)         

print(student_intscr)
kor = []

for i in student_intscr:
    

