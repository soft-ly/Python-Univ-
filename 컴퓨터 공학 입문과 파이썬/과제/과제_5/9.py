a = dict()
a['name']='python'
a['a',]='python'
a[[1]]='python'#이게 안됨: 이유는 [[]]를 사용하면 안의 []가 리스트형으로 인식되기 때문에.
a[250]='python'
print(a)