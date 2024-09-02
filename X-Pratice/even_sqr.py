
sum=0
squr=1
for i in range(1,101,1):
    if i%2==0:
        squr=i**2
        sum=sum+squr
print(squr)