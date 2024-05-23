class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    #이걸 쓰면 그냥 FourCal(x,x)

    # def setdata(self, first, second):
    #     self.first = first
    #     self.second= second
    # 이걸 쓰면, 
    # a = FourCal()
    # a.setdata(x,x)를 해줘야함


    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result    


a = FourCal()
b = FourCal()
a.setdata(1,2)
b.setdata(2,5)
print(a.add())
print(a.sub())
print(a.div())
print(a.mul())
print("--------")
print(b.add())
print(b.sub())