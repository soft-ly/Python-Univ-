from pathlib import Path
list_1=['홍길동','이순신','세종대왕']
list_2=[20,40,15]

with open(Path() / "text.txt","w",encoding='utf-8') as f:
    f.write("이름 : 나이\n")
    for i in range(len(list_1)):
        line = list_1[i] + " : " + str(list_2[i])+"\n"
        f.write(line)