num=int(input("Enter a number "))
previous=0
current=1
nxt=previous+current
while(nxt<=num):
    nxt=previous+current
    previous=current
    current=nxt
print(nxt)