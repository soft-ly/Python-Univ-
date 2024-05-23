from pathlib import Path
with open(Path()/"student_scores.txt","r",encoding="utf-8") as f:
    for _ in range(2):
        f.readline()
    for _ in range(1):
        print(f.readline().strip())
    