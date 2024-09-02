# create a function is_fibonacci_number(number) to return true if the number is fibonacci and false if the number is not fibonacci


def is_fibonacci_number(num):
    previous=0
    current=1
    next=current+previous
    while(next<=num):
        next=previous+current
        if num==next:
            return True
        previous=current
        current=next
    return False
print(is_fibonacci_number(8))