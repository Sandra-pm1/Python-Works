# pgrm to swap first and last elements in a list

num=[1,2,3,4,5,6,7]

# num[-1],num[0]=num[0],num[-1]

a=num.pop()
b=num.pop(0)

num.insert(0,a)
num.insert(-6,b)
print(num)
