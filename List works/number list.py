
numbers=(10,11,12,34,43,54,19,78,42)

# print number of objects in numbers
# print even number frm this numebrs
# print total of numbers
# print total of odd numbers


length=len(numbers)
total=0
odd_total=0
print(f"Length={length}")
for i in range(0,length):
    total+=numbers[i]
print(f"Total of numbers={total}")

for i in range(0,length):
    if numbers[i]%2==0:
        print(f"Even numbers : {numbers[i]}")
    else:
        odd_total+=numbers[i]
print(f"Total of odd numbers={odd_total}")

