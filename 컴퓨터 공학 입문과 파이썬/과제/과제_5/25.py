import pathlib
with open(pathlib.Path()/'test1.txt','w+') as f:
    body = f.write('java is a good program')
    body = 'python'
    f.seek(0)
    x = f.readline()
    x = str(x)
    fin = x.split()
    f.close()


with open(pathlib.Path()/'test1.txt','w+') as f:
    c = 0
    for i in fin:
        if i == 'java':
            f.write('python ')
        else:
            f.write(f'{i} ')
        c += 1
        