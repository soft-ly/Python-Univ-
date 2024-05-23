from pathlib import Path
list_name=["최진수"]
list_kor=[85]
list_eng=[95]
list_math=[89]
list_sci=[96]
list_soc=[85]
with open(Path()/"s_scores.txt","w",encoding="utf-8") as f:
    f.write(" 이름 | 국어 | 영어 | 수학 | 과학 | 사회 \n")
    for x in range(len(list_name)):
        line = list_name[x]+ "   " + str(list_kor[x]) + "    " + str(list_eng[x]) + "    " + str(list_math[x]) + "    " + str(list_sci[x]) + "    " + str(list_soc[x]) + "\n"
        f.write(line)