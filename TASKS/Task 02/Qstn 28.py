# Write a Python function to find the maximum of three numbers


def max_value(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3
print(max_value(10,30,20))



# max_value=max(10,30,27)
# print(max_value)