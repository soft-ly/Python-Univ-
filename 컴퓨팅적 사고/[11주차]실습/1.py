from random import randint
def dice_image(a):
    one = f"\n|   |\n| O |\n|   |\n"
    two = f"\n|O  |\n|   |\n|  O|\n"
    three = f"\n|O  |\n| O |\n|  O|\n"
    four = f"\n|O O|\n|   |\n|O O|\n"
    five = f"\n|O O|\n| O |\n|O O|\n"
    six = f"\n|O O|\n|O O|\n|O O|\n"
    if a == 1:
        print(one)
    elif a == 2:
        print(two)
    elif a == 3:
        print(three)
    elif a == 4:
        print(four)
    elif a == 5:
        print(five)
    elif a == 6:
        print(six)
total = 0
a = int(input())
for x in range(0,a):
    dice_number=randint(1,6)
    print(dice_number)
    dice_image(dice_number)
    total += dice_number
print(f"모든 주사위 결과를 더한 값은 '{total}'입니다.")