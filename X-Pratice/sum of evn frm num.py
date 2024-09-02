# read a number frm the user and print the sum of the even numbers in the readed number


num=int(input("enter a number "))
sum=0
while(num!=0):
    digit=num%10
    if digit%2==0:
        sum=sum+digit
    num=num//10
print(sum)