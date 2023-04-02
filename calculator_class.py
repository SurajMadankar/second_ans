class Calculator:
    x=10
    y=94
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return (self.x+self.y)
    def subtract(self):
        return (self.y-self.y)
    def multiply(self):
        return(self.x*self.y)
    def divide(self):
        return(self.x/self.y)
    
obj = Calculator(10, 94)
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.divide())