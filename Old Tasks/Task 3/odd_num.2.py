# read start_limit and end_limit frm the user and print all the odd numbers frm the start_limit to end_limit

start=int(input("Enter the starting number "))
end=int(input("Enter the ending number "))
while(start<=end):
    if start%2!=0:
        print(start)
    start=start+1
