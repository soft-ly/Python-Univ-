from pathlib import Path
list_name=["홍길동", "김나희", "이진성", "박하나"]
list_kor=[80, 85, 67, 89]
list_eng=[92, 90, 53, 90]
list_math=[100, 95, 70, 95]
list_sci=[81, 86, 71, 92]
list_soc=[72, 85, 72, 93]
with open(Path()/"s_scores.txt","w",encoding="utf-8") as f:
    f.write(" 이름 | 국어 | 영어 | 수학 | 과학 | 사회 \n")
    for x in range(len(list_name)):
        line = list_name[x]+ "   " + str(list_kor[x]) + "    " + str(list_eng[x]) + "    " + str(list_math[x]) + "    " + str(list_sci[x]) + "    " + str(list_soc[x]) + "\n"
        f.write(line)