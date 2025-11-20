
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    def power(self, a, b):
        return a ** b
    def sqrt(self, a):
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return a ** 0.5

    def modulus(self, a, b):
        return a % b
    def floor_divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a // b
  def percentage(self, a, b):
    def percentage(self, a, b):
        return (a / b) * 100    
    