listoflocations = ['서울', '수서', '평택', '나주', '대전', '부산']
onlocation = 2
class KTX_Train:
    global listoflocations
    global onlocation
    def go(self):
        global onlocation
        onlocation += 1
        print(f"KTX가 {listoflocations[onlocation]}(으)로 진입 했습니다.")
    
    def back(self):
        global onlocation
        onlocation -= 1
        print(f"KTX가 {listoflocations[onlocation]}(으)로 진입 했습니다.")

ktx1 = KTX_Train()
ktx1.go()
ktx1.back()
ktx1.back()