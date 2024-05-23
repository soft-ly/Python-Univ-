class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
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
    
class MoreCal(FourCal):
    def pow(self):
        result = self.first**self.second
        return result
    
class SafeCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first/self.second
    #메서드 수정/override

a = SafeCal(4,0)
print(a.div())

