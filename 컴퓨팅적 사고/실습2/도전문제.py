moneyinput = int(input("투입한 돈 입력"))
price = int(input("물건의 값 입력"))
leftover = moneyinput - price
leftover5 = leftover % 500
leftover1 = leftover5 % 100
leftover11 = leftover1 % 50

print("투입한 돈 :", moneyinput)
print("물건의 값 :", price)
print(f"거스름돈은 500원 짜리 {leftover // 500}개와 100원짜리 {leftover5 // 100}개와 50원 짜리 {leftover1 // 50}개와 10원짜리 {leftover11 // 10}개")