print("insert the first number")
num1 =float(input())
print("insert operation")
operation= input()
print("insert the second number")
num2 =float(input())

if (operation == "+"):
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    print(num1/num2)
else : 
    print("error")