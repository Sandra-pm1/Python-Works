num=int(input("enter a number "))
org=num
count=len(str(num))
result=0
while(num!=0):
    digit=num%10
    expo=digit**count
    result=result+expo
    num=num//10
print(result)
print(f"{org} is armstrong" if result==org else f"{org} is not armstrong")
