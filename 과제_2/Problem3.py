wordlist = ['수학', '과학', '영어', '고구마', '감자', '컴퓨터', '딸기'] #데이터 지정
num=int(input("몇 번째 단어를 뽑고 싶으신가요?")) #숫자 입력하는 기능
def func(x): #함수 만들어서 
    return wordlist[x]
print(func(num)) #이렇게 출력할 수 있고

print(wordlist[num]) #이렇게 더 좀 더 간단하게 할 수 있다. 