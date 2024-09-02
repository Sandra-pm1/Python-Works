# read two numbers from the user num1 and num2
# print largest of two numbers 
# if both are equal print equal


num1=int(input("Enter first number "))
num2=int(input("Enter second number "))
if num1>num2:
    print(f"largest number is {num1}")
elif num2>num1:
    print(f"largest number is {num2}")
else:
    print(f"Both {num1} and {num2} are equal")