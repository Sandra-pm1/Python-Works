# read a number frm the user and check the given number is fibonaci or not




num=int(input("Enter a number "))
previous=0
current=1
nxt=1
Isfib=False
if num in range(0,1):
    Isfib=True
else:
    nxt=previous+current
    while(nxt<=num):
        nxt=previous+current
        previous=current
        current=nxt
        if num==nxt:
            Isfib=True
            break
print(Isfib)