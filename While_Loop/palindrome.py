# check given number is palindrome or not

num=int(input("enter a number"))
orginal=num
result=0
while(num!=0):
    digit=num%10
    result=result*10+digit
    num=num//10
print(result)
print(f"is palindrome" if result==orginal else f"not palindrome" )
