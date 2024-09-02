# Write a Python program to check whether the n-th element exists in a given list


lst=[23,12,34,53,45,20,46,1]
nth_ele=int(input("Enter the position : "))
length=len(str(lst))
if nth_ele<=length:
    print("Element exists")
else:
    print("Element not exists")
