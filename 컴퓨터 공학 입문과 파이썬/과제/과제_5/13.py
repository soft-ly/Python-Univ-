a = "Life is too short, you need python"

if 'wife' in a:
    print('wife')
elif 'python' in a and 'you' in a:
    print('python') #이것만 프린트 됨. a에 있는 정확한 스트링 값을 찾아야함.찾으면 if문의 조건이 충족되어 프린트됨.
elif 'shirt' not in a:
    print('shirt')
elif 'need' in a :
    print('need')
else:
    print('none')