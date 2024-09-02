# pgrm to print the sum of cubes of each digits

num=int(input("Enter the number "))
sum=0
while(num!=0):
    digit=num%10
    cube=digit**3
    sum=cube+sum
    num=num//10
print(sum)