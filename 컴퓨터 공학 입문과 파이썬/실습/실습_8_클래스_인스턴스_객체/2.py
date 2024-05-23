listoflocations = ['서울', '수서', '평택', '나주', '대전', '부산']
onlocation = 2
class KTX_Train:
    global listoflocations
    global onlocation

    def go(self, num):
        global onlocation
        onlocation += num
        if 0<=onlocation<=6:
            print(f"KTX가 {listoflocations[onlocation]}(으)로 진입 했습니다.")
        elif onlocation < 0:
            print(f"KTX가 서울(으)로 진입 했습니다. 더 이상 운행이 불가합니다, 죄송합니다.")
        elif onlocation > 6:
            print(f"KTX가 부산(으)로 진입 했습니다. 더 이상 운행이 불가합니다, 죄송합니다.")
            
    
    def back(self, num):
        global onlocation
        onlocation -= num
        if 0<=onlocation<=6:
            print(f"KTX가 {listoflocations[onlocation]}(으)로 진입 했습니다.")
        elif onlocation < 0:
            print(f"KTX가 서울(으)로 진입 했습니다. 더 이상 운행이 불가합니다, 죄송합니다.")
        elif onlocation > 6:
            print(f"KTX가 부산(으)로 진입 했습니다. 더 이상 운행이 불가합니다, 죄송합니다.")

ktx1 = KTX_Train()
ktx1.go(3)
ktx1.back(2)
ktx1.back(1)