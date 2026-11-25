def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

a = int(input("First number: "))
op = input("Operator (+, -, *, /): ")
b = int(input("Second number: "))

if op == "+": print(add(a, b))
elif op == "-": print(sub(a, b))
elif op == "*": print(mul(a, b))
elif op == "/": print(div(a, b))
