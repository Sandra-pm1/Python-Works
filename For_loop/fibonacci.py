# write a pgrm to print fibannaci series



previous=0
current=1
print(f"{previous} {current}",end=" ")
for i in range(1,11):
    nxt=previous+current
    print(f"{nxt}",end=" ")
    previous=current
    current=nxt
