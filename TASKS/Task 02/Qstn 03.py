# Python Program to Make a Simple Calculator


operator=input("Enter an operator (+,-,/,*,%) : ")
num1=int(input("Enter first number  : "))
num2=int(input("Enter second number : "))

if operator=="+":
    add=num1+num2
    print(f"{num1} + {num2} = {add}")
elif operator=="-":
    sub=num1-num2
    print(f"{num1} - {num2} = {sub}")
elif operator=="/":
    div=num1/num2
    print(f"{num1} / {num2} = {div}")
elif operator=="*":
    mul=num1*num2
    print(f"{num1} * {num2} = {mul}")
elif operator=="%":
    mod=num1%num2
    print(f"{num1} % {num2} = {mod}")
else:
    print("Invalid Operator")