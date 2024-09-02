# Program to Check Armstrong Numbers in Python

num=int(input("Enter a number : "))
org_num=num
sum=0
length=len(str(num))
while(num!=0):
    digit=num%10
    expo=digit**length
    sum=sum+expo
    num=num//10
print(f"{org_num} is Armstrong number" if org_num==sum else f"{org_num} is not Armstrong number")