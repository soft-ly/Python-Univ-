from pathlib import Path
with open(Path()/"student_scores.txt","r",encoding="utf-8") as f:
    for line in f:
        list = line.split()
        print(list[3])