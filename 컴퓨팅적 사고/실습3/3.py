measure = input("무슨 단위를 사용하시나요? 리터 vs 갤런")
howmuch = int(input("얼마나 넣고 싶나요?"))
litre = howmuch
gallon = howmuch
priceg = gallon * 2.89
pricel = litre *2.89 *0.264
if measure == "리터":
    print(f" 단위: {measure} \n 주유량: {howmuch} \n 가격은 {pricel}")
elif measure == "갤런":
    print(f" 단위: {measure} \n 주유량: {howmuch} \n 가격은 {priceg}")
