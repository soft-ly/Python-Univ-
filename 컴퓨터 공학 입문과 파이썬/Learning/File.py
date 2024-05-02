#about directories
#상대경로 : ../../Documents
#절대경로 : D:\Users\user\Documents\Github\Python-Univ-\컴퓨터 공학 입문과 파이썬

#rel_path\main\sub\main.py
#rel_path\modules\reader.py
#rel_path\config\hello.txt
# .\sub\main.py
# ..\modules\reader.py
# ..\config\hello.txt

from pathlib import Path
from urllib.request import urlretrieve

baseurl= "https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/data/"
file_name = "results5m.txt"
file_url = baseurl + file_name

data_path= Path()
target_path = data_path / file_name 

urlretrieve(file_url, target_path)
filename=open("./results5m.txt",encoding="utf-8")

for line in filename:
    print(line.strip())

filename.close()