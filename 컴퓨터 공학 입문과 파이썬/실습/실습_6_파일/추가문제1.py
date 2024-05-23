from pathlib import Path
with open(Path()/"student_scores.txt","r",encoding="utf-8") as f:
    line = f.read()
    print(line)
    f.seek(0)
    print("")
    for x in range(15):
        print(f.readline().strip())
    print("")
    f.seek(0)
    lines=f.readlines()
    print(lines)
    