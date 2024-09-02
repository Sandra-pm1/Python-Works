# create a function is_palindrome(number) to return true if the number is palindrome and false if the number is not palindrome


def is_palindrome(num):
    org=num
    result=0
    while(num!=0):
        digit=num%10
        result=result*10+digit
        num=num//10
        if org==result:
            return True
    return False
print(is_palindrome(123)) 