# user_action : 사용자의 선택
# user_choice : 사용자가 할 수 있는 모든 선택

import random
print("* 코딩이 전반적으로 한국어를 사용하면 에러가 자주 뜹니다. 되도록이면 영어로 적어주세요!*")
print("* 혹시나 잘못 입력하신게 있다면 언제나 N을 치시면 뒤로 가게했습니다.*")
user=input("안녕하세요! 당신의 이름은? ")

ThisGame=True

def GameError(): 
    X=True
    global user_choice
    global user_action
    while X==True:
        for Y in user_choice:
            if user_action != Y: 
                user_action=input("에러! 제대로 하시지를 않으셨네요! 다시 입력해주세요... \n")
            elif user_action == Y:
                X=False
def GameDone(): 
    B= input("\n 어떻게 하실래요 \n 1: 모든 게임 끝 \n 2: 처음부터 다시 시작 \n 3: 동일 게임 다시 시작 \n")
    X=True
    global ThisGame
    global Game
    while X==True:
        
        if B == "1":
            X=False
            Game = False
            ThisGame = False
        elif B == "2":
            X=False
            Game = False
        elif B == "3":
            X=False
        else: 
            B=input("? 다시 쳐보시오")
            
def Cancel():
    global Game
    B = input("N을 누르셨어요! 나가고 싶으신가요?[Y/N]")
    if B=="Y":
        Game = False


while ThisGame == True:
    User_Choice_of_Game=input(f"안녕하세요 {user}님! 아래의 게임 중 하고 싶으신 것을 숫자로 입력하세요! \n 1. 가위 바위 보 \n 2. 숫자 맞추기 \n 3. 생각중... \n (주의! 실수했다간 다시 해야할 수도 있으니 주의해 주세요!)\n")
    Game=True
    while Game==True:
        if User_Choice_of_Game == "1":
            
            def winner(x):
                if x=="승리":
                    print(f"{user}님은 '{translatorforuser()}'을 선택하였고, 컴퓨터의 선택은 '{translatorforpc()}' 이므로, {x}하셨습니다!")
                elif x=="패배":
                    print(f"{user}님은 '{translatorforuser()}'을 선택하였고, 컴퓨터의 선택은 '{translatorforpc()}' 이므로, {x}하셨습니다!")
            def translatorforpc():
                if pc_action == "S":
                    return "가위"
                elif pc_action == "P":
                    return "보"
                elif pc_action == "R":
                    return "바위"
            def translatorforuser():
                if user_action == "S":
                    return "가위"
                elif user_action == "P":
                    return "보"
                elif user_action == "R":
                    return "바위"
            
            user_choice = ["R","P","S"]
            user_action=input("\n가위 바위 보를 선택하셨네요! \n 아래 표시된 영어로 가위 바위 보 중 선택하십시오! \n 가위: S \n 바위: R \n 보: P \n")
            
            pc_choice = ["R","P","S"]
            pc_action=random.choice(pc_choice)
            
            if user_action==pc_action:
                print(f"{user}님과 컴퓨터가 둘다 {pc_action}을 선택하셨네요! 무승부 입니다!")
                GameDone()
            elif user_action == "S":
                if pc_action == "P":
                    winner("승리")   
                    GameDone()
                elif pc_action == "R":
                    winner("패배")
                    GameDone()
            elif user_action == "R":
                if pc_action == "P":
                    winner("패배")
                    GameDone()
                elif pc_action == "S":
                    winner("승리")
                    GameDone()
            elif user_action == "P":
                if pc_action == "R":
                    winner("승리")
                    GameDone()
                elif pc_action == "S":
                    winner("패배")
                    GameDone()
            elif user_action == "N":
                Cancel()
            else:
                GameError()

        elif User_Choice_of_Game == "2":

            def winner(t,r): 
                global pc_action
                global user_action
                global user_choice
                global pc_choice
                if user_action > r or user_action <t:
                    GameError()
                elif t<= user_action <= r and user_action != pc_action: 
                    DoneorRetry = input("아... 틀리셨군요... 한번 더 시도 해보실래요? [Y/N] ")
                    if DoneorRetry != "Y":
                        Check = input("확실하십니까?[Y/N]")
                        if Check == "Y":
                            GameDone()
                    if DoneorRetry == "Y":
                        user_action=int(input("오! 다시 한번 찍어보세요! "))
                        winner(t,r)
                elif user_action==pc_action:
                    print("축하합니다! 숫자를 맞추셨습니다!")
                    GameDone()
                elif user_action=="N":
                    Cancel()

            print(f"숫자 맞추기를 고르셨네요! 이 단순 게임은 입력하신 범위에서 랜덤으로 컴퓨터가 숫자를 골라 {user}님께서 숫자를 맞추는 게임입니다. \n ")
            instructions=input(f"위의 내용을 이해하셨다면 N을 제외한 아무 키나 눌러 주세요!")
            if instructions == "N":
                Cancel()

            x=int(input("시작합니다! 범위의 첫 수를 입력해주세요! (두 숫자의 대소비교는 컴퓨터가 합니다! 정수 아무거나 넣어주시면 됩니다)"))
            y=int(input("다음 숫자를 정해주세요! (두 숫자의 대소비교는 컴퓨터가 합니다! 같은 수가 아닌 정수 아무거나 넣어주시면 됩니다)"))
            user_action=int(input("숫자를 고르시오!")) 

            if x < y :
                pc_action = random.randint(x,y)
                user_choice = [x,...,y]
                winner(x,y)
            elif x > y:
                pc_action = random.randint(y,x)
                user_choice = [y,...,x]
                winner(y,x)

        elif User_Choice_of_Game == "3":
            print("3번 까지 만들려다가 아직은 생각이 안나서 고민중...")

print("Game Over")
        
            
            
            



                
            
    



        

    
    
            
