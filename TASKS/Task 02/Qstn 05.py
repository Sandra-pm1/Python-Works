# Python program to check if the given number is a Disarium Number



num=int(input("Enter a number : "))
org_num=num
sum=0
while(num!=0):
    count=len(str(num))
    digit=num%10
    expo=digit**count
    sum=sum+expo
    num=num//10
if org_num==sum:
    print(f"{org_num} is a disarium number")
else:
    print(f"{org_num} is not a disarium number")