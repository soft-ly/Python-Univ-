class Calculator:
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
    
    def pow(self):
        result = self.first ** self.second
        return result

a = Calculator(4, 5)
print(a.add(), a.sub(), a.mul(), a.div(), a.pow())

