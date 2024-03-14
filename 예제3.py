Option=input("예제 답 or 계산기?")
perMilk = 820
perIC= 1500
if Option == "예제 답":
    AmtMilk = 2
    AmtIC= 3
    SaleIC = 0.95*perIC*AmtIC
    print(SaleIC + AmtMilk*perMilk)
elif Option == "계산기":
    AmtMilk = input("우유 개수?")
    AmtIC = input("아이스크림 개수?")
    SaleIC = 0.95*perIC*AmtIC
    if AmtIC > 2:
        print(SaleIC + AmtMilk*perMilk)
    else:
        print(perIC*AmtIC+ AmtMilk*perMilk)