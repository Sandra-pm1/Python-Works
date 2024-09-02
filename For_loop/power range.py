# print the power range of a number

sum=0
pattern=0
num=int(input("enter a number"))
for i in range(1,num+1): 
    pattern=pattern*10+num
    sum=pattern+sum
print(sum)