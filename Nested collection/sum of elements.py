# find the sum of elements

arr=[[10,20],[20,30],[30,40]]
# numbers=[]
# for lst in arr:
#     for num in lst:
#         numbers.append(num)
# print(sum(numbers))


numbers=[num for lst in arr for num in lst]
print(sum(numbers))
