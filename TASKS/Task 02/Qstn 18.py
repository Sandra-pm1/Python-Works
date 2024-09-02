# Python Program to Find Armstrong Number in an Interval


start=int(input("Enter the starting limit : "))
end=int(input("Enter the ending limit : "))
for num in range(start,end+1):
    sum=0
    org_num=num
    count=len(str(num))
    while(num!=0):
        digit=num%10
        expo=digit**count
        sum=sum+expo
        num=num//10
    if sum==org_num:
        print(org_num)
