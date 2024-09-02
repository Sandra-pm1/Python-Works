
# print even numbers frm the list
arr=[[10,20],[21,30],[40,53]]
evens=[num for lst in arr for num in lst if num%2==0]
print(evens)


# numbers greater than 15

numbers=[num for lst in arr for num in lst if num>15]
print(numbers)
