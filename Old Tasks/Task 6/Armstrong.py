# print armstrong number from numbers

numbers=[151,153,154,370,371,372,373,16341,1635]

length=len(numbers)

for i in range(0,length):
    sum=0
    count=len(str(numbers[i])) 
    org=numbers[i]  
    while(numbers[i]!=0): 
        digit=numbers[i]%10     
        expo=digit**count         
        sum=sum+expo               
        numbers[i]=numbers[i]//10  
        if sum==org:
            print(org)
