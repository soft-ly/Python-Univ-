
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
    pass

a = MoreCal(10, 12)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())