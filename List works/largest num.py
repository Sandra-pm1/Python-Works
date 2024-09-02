# to find the largest number without using methods


numbers=[1,3,2,5,7,9,10,4]
# largest_number=numbers[0]
# for i in numbers:
#     if i>largest_number:
#         largest_number=i
# print(largest_number)


# to  find the smallest number without using method

# smallest_number=numbers[0]
# for i in numbers:
#     if i<smallest_number:
#         smallest_number=i
# print(smallest_number)


# second largest number

# numbers.sort()
# print(numbers[-2])

# without methods

# largest_number=numbers[0]
# second_largest=numbers[0]
# for i in numbers:
#     if i>largest_number and i>second_largest:
#         second_largest=largest_number
#         largest_number=i
#     else:
#         if i>largest_number and i<second_largest:
#             second_largest=i
# print(second_largest)


# sum of odd numbers

sum=0
for i in numbers:
    if i%2!=0:
        sum=sum+i
print(sum)