# find the missing positive numbers

arr=[0,1,2,4]
for n in arr:
    sum_of_num=n*(n+1)//2
    current_sum=sum(arr)
    missing_num=sum_of_num-current_sum
print(missing_num)