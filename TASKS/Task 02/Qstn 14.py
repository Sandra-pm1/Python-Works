# Python program to print the largest element in an array

arr=[9,7,2,4,8,1]
for i in arr:
    current=arr[0]
    previous=arr[0]
    if i>current:
        previous=current
        current=i
print(current)