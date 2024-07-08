pin = '881120-1068234'
a=pin.split('-')
yyyymmdd=a[0]
num = int(a[1])
if 2000000> num > 1000000:
    print('주민등록 번호 "1"에 따르면, 남자입니다')
elif 2000000< num < 3000000:
    print('주민등록 번호 "2"에 따르면,여자입니다')