# find the second smallest frm the list

numbers=[2,3,5,7,1,9,10,4]
smallest_num=numbers[0]
second_smallest=numbers[-1]
for i in numbers:
    if i<smallest_num and i<second_smallest:
        second_smallest=smallest_num
        smallest_num=i
    else:
        if i<second_smallest and i>smallest_num:
            second_largest=i
print(second_smallest)