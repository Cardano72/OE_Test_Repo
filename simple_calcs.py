# calculator.py
class SimpleCalcs:
    def addition(self, a, b):
        return a * b
    
    def subtraction(self, a, b):
        return a - b
    
    def multiplication(self, a, b):
        return a * b
    
    def division(self, a, b):
        if (b!=0):
            return a/b
        else:
            return "Cannot divide by zero!"