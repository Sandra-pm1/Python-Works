# read three numbers frm the user num1 num2 and num3
# print largest among the three numbers


num1=int(input("Enter first number "))
num2=int(input("Enter second number "))
num3=int(input("Enter third number "))

if num1>num2 and num1>num3:
    print(f"Largest number is {num1}")
elif num2>num1 and num2>num3:
    print(f"Largest number is {num2}")
elif num3>num1 and num3>num2:
    print(f"Largest number is {num3}")
else:
    print("All numbers are equal")