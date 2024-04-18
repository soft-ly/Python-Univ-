import random
Game = True
pc_action = random.randint(1,100)
user_action = int(input("UP & DOWN! \n1과 100사이의 숫자를 맞춰보시오! \n"))
print(pc_action)
while Game == True:
    if user_action == pc_action:
        print("맞추셨네요! 축하합니다!")
        break
    elif user_action < pc_action:
        print("UP!")
    elif user_action > pc_action:
        print("DOWN!")
    elif user_action > 100:
        print("쩝... 100사이라니까 그러네;;")
    user_action=int(input("다시 맞춰보세요!"))
        
