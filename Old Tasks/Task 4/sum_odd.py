# print sum of all odd numbers frm 1 to 100

sum=0
for num in range(1,101,1):
    if num%2!=0:
        sum=sum+num
print(sum)