# Python program to print the smallest element in an array


arr=[9,4,8,1,7,12,0]
current=arr[0]
previous=arr[0]
for i in arr:
    if i<current:
        previous=current
        current=i
print(current)