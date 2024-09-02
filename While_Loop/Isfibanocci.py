# read a number frm the user and check the number is fibonacci or not



num=int(input("Enter a number "))
previous=0
current=1
Isfib=False
nxt=previous+current
while(nxt<=num):
    nxt=previous+current
    if num==nxt:
        Isfib=True
        break
    previous=current
    current=nxt
print(f"Fibonacci number" if fib==True else f"Not fibonacci number")