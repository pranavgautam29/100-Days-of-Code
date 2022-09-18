def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1 - n2
def prod(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : prod,
    "/" : div
}
def calculator():
    
    num1 = float(input("Enter first number:"))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        op_symbol = input("Pick an operation:")
        num2 = float(input("Enter next number:"))
        func = operations[op_symbol]
        answer = func(num1 , num2)
        print(f"{num1} {op_symbol} {num2} = {answer}")
        if input(f"Type 'y' for further calculation and 'n' to start begin new calculation:") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()



