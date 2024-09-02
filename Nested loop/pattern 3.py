# print the given pattern

# @ @ @ @
# @ @ @
# @ @
# @


for row in range(1,5):
    for col in range(row,5):  # for col in range(1,6-row) 
        print("@",end="\t")
    print()