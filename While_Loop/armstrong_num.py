# find the given number is armstrong


num=int(input("Enter a number "))
original=num
sum=0
count=len(str(num))
while(num!=0):
    digit=num%10
    expo=digit**count
    sum=sum+expo
    num=num//10
print(sum)
print("Given number is armstrong" if sum==original else "Given number is not armstrong")

