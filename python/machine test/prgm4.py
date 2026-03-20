class Calculator:
    def add(akheedha, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b



c = Calculator()

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", c.add(a, b))
elif op == "-":
    print("Result:", c.subtract(a, b))
elif op == "*":
    print("Result:", c.multiply(a, b))
elif op == "/":
    if b != 0:
        print("Result:", c.divide(a, b))
    else:
        print("Error: Division by zero not allowed")
else:
    print("Invalid operator")