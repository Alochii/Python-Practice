#the calculator!

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
def calculator():
    num1 = float(input("number 1\n"))
    result = num1
    while True:
        num1 = result
        symbol = input("symbol (+, -, * or /\n")
        num2 = float(input("number 2\n"))
        displaymsg = "type "
        result = round(operations[symbol](num1,num2),2)
        print(f"{num1} {symbol} {num2} = {result}")
        if input("type 'y' to continue, or 'n' to start a new operation") == 'n':
            calculator()


calculator()