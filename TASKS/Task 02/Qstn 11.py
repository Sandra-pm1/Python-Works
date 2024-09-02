# Python program to print the duplicate elements of an array

arr=[1,4,2,3,1,2,5,7,3]
duplicate_ele={}
for i in arr:
    if i in duplicate_ele:
        print(i)
    else:
        duplicate_ele[i]=1