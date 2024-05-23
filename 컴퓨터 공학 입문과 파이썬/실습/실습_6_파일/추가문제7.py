from pathlib import Path
ult_list = []
with open(Path()/"student_scores(원래파일).txt","r",encoding="utf-8") as f:
    for line in f:
        list = line.split()
        ult_list += [list]
ult_list.pop(10)
ult_list.insert(10, ['최진수', '85','95','89','96','85'])
with open(Path()/"student_scores.txt","w",encoding="utf-8") as f:
    for line in ult_list:
        full_line= line[0] + ' ' + line[1] + ' ' + line[2] + ' ' + line[3] + ' ' + line[4] + ' ' + line[5] + '\n'
        f.write(full_line)