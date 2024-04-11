money=int(input("커피 자판기입니다. 돈을 입력하세요!"))
coffeeprice=300
amountofcoffee=10
while amountofcoffee != 0:
    if money >= 300:
        print("커피 한잔 뽑음")
        money = money - coffeeprice
        print(f"거스름돈: {money}원")
        amountofcoffee = amountofcoffee - 1
        continue
    elif money < 300:
        print("더 이상 커피를 뽑을수 없습니다.")
        if money >0:
            print(f"넣으신 {money}을 드리겠습니다.")
        break
if amountofcoffee == 0:
    print("남아있는 커피가 없습니다.")
    if money >0:
        print(f"남으신 {money}원을 드리겠습니다.")
        
    
    


