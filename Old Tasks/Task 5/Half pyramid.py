# print the following pattern given below

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *

for row in range(0,6):
    for col in range(0,row+1):
        print("*",end=" ")
    print()