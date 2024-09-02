# create a function is_armstrong(number) to return true if the number is armstrong and false if the number is not armstrong


def is_armstrong(num):
    org=num
    count=len(str(num))
    sum=0
    while(num!=0):
        digit=num%10
        expo=digit**count
        sum=sum+expo
        num=num//10
        if org==sum:
            return True
    return False
print(is_armstrong(153))
