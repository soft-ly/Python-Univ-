coffeeamount = 10
coffeeprice = 300
inputmoney = int(input("돈을 넣으시오"))
while True:
    if coffeeamount == 0:
        print("남아있는 커피가 없습니다")
        break
    if coffeeprice <= inputmoney:
        print("커피 하나 출력")
        inputmoney = inputmoney - 300
        print("거스름돈:", inputmoney)
        coffeeamount= coffeeamount- 1
        if coffeeprice > inputmoney:
            print("더이상 커피를 뽑을 수 없습니다")
            break  
    elif coffeeprice > inputmoney:
        print("더이상 커피를 뽑을 수 없습니다")
        print("거스름돈:", inputmoney)
        break
    