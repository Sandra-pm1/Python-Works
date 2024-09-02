# pgrm to check the given number is prime or not

num=int(input("enter a number "))

isprime=True

for i in range(2,num):

    if num%i==0:

        isprime=False

        break

print(f"is prime" if isprime==True else f"not prime")