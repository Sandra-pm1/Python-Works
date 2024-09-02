arr=[10,11,12,13,14,15,16,17]

# expected output
#       arr=[10,17,12,15,14,13,16,11]

left=1
length=len(arr)-1
if length%2==0:
    right=length-1
else:
    right=length
while(left<right):
    arr[left],arr[right]=arr[right],arr[left]
    left+=2
    right-=2
print(arr)