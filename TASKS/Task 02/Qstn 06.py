# Python program to determine whether the given number is a Harshad Number



num=int(input("Enter a number : "))
org_num=num
base=0
while(num!=0):
    digit=num%10
    base=base+digit
    num=num//10
if org_num%base==0:
    print(f"{org_num} is Harshad number")
else:
    print(f"{org_num} is not Harshad number")