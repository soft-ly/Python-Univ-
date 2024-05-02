from pathlib import Path
student_scr= []
name=''
with open(Path()/"student_scores.txt","r",encoding='utf-8') as f:
    for line in f:
        if line.find("이름") >= 0:
            name= line.split()[1]
        elif line.find("과목") >= 0:
            continue
        else:
            scr_name = line.split()[0]
            scr_scr = line.split()[1]
            group = [name,scr_name,scr_scr]
            try:
                student_scr.append(group)
            except:
                continue
scr_list = []   
for name, score in student_scr:
    scr_list.append(score)
total_score=0
avg_score=0
for score in scr_list:
    s = int(score)
    total_score+=s
avg_score = total_score / 5
print(round(avg_score, 2))
