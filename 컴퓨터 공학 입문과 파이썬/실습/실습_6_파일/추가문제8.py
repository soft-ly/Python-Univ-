from pathlib import Path
ult_list = []
kor_total=0
eng_total=0
math_total=0
sci_total=0
with open(Path()/"student_scores(원래파일).txt","r",encoding="utf-8") as f:
    for line in f:
        list = line.split()
        kor_total += int(list[1])
        eng_total += int(list[2]) 
        math_total += int(list[3]) 
        sci_total += int(list[4])
        ult_list += [list]

for line in ult_list:
    line.pop(5)
kor_avg= round(kor_total /15,2)
eng_avg= round(eng_total /15,2)
math_avg= round(math_total /15,2)
sci_avg = round(sci_total /15,2)
with open(Path()/"student_scores(심화2).txt","w",encoding="utf-8") as f:
    for line in ult_list:
        full_line= line[0] + ' ' + line[1] + ' ' + line[2] + ' ' + line[3] + ' ' + line[4] + ' ' + '\n'
        f.write(full_line)
    f.write(f'국어평균: {kor_avg}\n')
    f.write(f'영어평균: {eng_avg}\n')
    f.write(f'수학평균: {math_avg}\n')
    f.write(f'과학평균: {sci_avg}\n')
