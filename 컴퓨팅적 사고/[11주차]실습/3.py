from random import sample
WholeGame=1
while WholeGame:
    lottery = input("미니로또(1 입력), 로또 6(2 입력), 로또 7(3 입력) 중에 고르시오")

    a = int(input("원하시는 만큼 로또 번호를 추천: "))
    
    if lottery == "1":
        선택지 = range(1,32)
        선택결과 = sample(선택지,a)
        print(선택결과)
            
    elif lottery == "2":
        선택지 = range(1,44)
        선택결과 = sample(선택지,a)
        print(선택결과)
    elif lottery == "3":
        선택지 = range(1,38)
        선택결과 = sample(선택지,a)
        print(선택결과)
    b= input("더 고르실래요? Y/N")
    if b == "N":
        
        WholeGame=0