# read a number frm the user and extract digits frm the number

num=int(input("Enter a number "))
while(num!=0):
    digit=num%10
    print(digit)
    num=num//10
  
