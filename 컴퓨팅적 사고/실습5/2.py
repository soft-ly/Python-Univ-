# user_action : 사용자의 선택
# user_choice : 사용자가 할 수 있는 모든 선택

import random
def winner(x):
    if x=="승리":
        print(f"'{translatorforuser()}'을 선택하였고, 컴퓨터의 선택은 '{translatorforpc()}' 이므로, {x}하셨습니다!")
    elif x=="패배":
        print(f"'{translatorforuser()}'을 선택하였고, 컴퓨터의 선택은 '{translatorforpc()}' 이므로, {x}하셨습니다!")
def translatorforpc():
    if pc_action == "1":
        return "가위"
    elif pc_action == "3":
        return "보"
    elif pc_action == "2":
        return "바위"
def translatorforuser():
    if user_action == "1":
        return "가위"
    elif user_action == "3":
        return "보"
    elif user_action == "2":
        return "바위"
user_action=input("\n 아래 표시된 숫자로 가위 바위 보 중 선택하십시오! \n 가위: 1 \n 바위: 2 \n 보: 3 \n  \n")

pc_choice = ["2","3","1"]
pc_action=random.choice(pc_choice)

if user_action==pc_action:
    print(f"둘다 {pc_action}을 선택하셨네요! 무승부 입니다!")
    
elif user_action == "1":
    if pc_action == "3":
        winner("승리")   
        
    elif pc_action == "2":
        winner("패배")
        
elif user_action == "2":
    if pc_action == "3":
        winner("패배")
        
    elif pc_action == "1":
        winner("승리")
        
elif user_action == "3":
    if pc_action == "2":
        winner("승리")
        
    elif pc_action == "1":
        winner("패배")

        
            
            
            



                
            
    

