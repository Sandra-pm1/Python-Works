# print the following pattern given below

# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


for row in range(0,6):
    for col in range(row,6):
        print("*",end=" ")
    print()