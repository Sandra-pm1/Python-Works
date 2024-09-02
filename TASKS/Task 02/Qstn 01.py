# Python Program to Find LCM



num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
new_1=[]
new_2=[]
for i in range(1,num1+1):
    n1=num1*i
    new_1.append(n1)
    n2=num2*i
    new_2.append(n2)
for i in new_1:
    if i in new_2:
        print(i)
        break