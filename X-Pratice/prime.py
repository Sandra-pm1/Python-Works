num=int(input("enter a number "))
isPrime=True
for i in range(2,num):
    if num%2==0:
        isPrime=False
        break
print(f"Prime number" if isPrime==True else f"Not a prime number ")