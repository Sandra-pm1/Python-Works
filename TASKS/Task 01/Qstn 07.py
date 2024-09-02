# Write a program for simple calculator


num1=int(input("Enter first number  : "))
num2=int(input("Enter second number : "))
operator=input("Enter an operator [+,-,/,*,%] : ")

if operator=="+":
    add_result=num1+num2
    print(f"{num1} + {num2} ={add_result}")
elif operator=="-":
    sub_result=num1-num2
    print(f"{num1} - {num2} = {sub_result}")
elif operator=="*":
    mul_result=num1*num2
    print(f"{num1} * {num2} = {mul_result}")
elif operator=="/":
    div_result=num1/num2
    print(f"{num1} / {num2} = {div_result}")
elif operator=="%":
    mod_result=num1%num2
    print(f"{num1} % {num2} = {mod_result}")
else:
    print("Invalid operator") 