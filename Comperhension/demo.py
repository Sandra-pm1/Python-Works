

# Syntax
#       
#      [return iteration condition]

# find the squares

lst=[10,2,3,4,5,6]
squares=[n**2 for n in lst]
# print(squares)

# print even numbers

even=[n for n in lst if n%2==0]
# print(even)

# print odd numbers

odd=[n for n in lst if n%2!=0]
# print(odd)


# print words starts with fly

words=["fly","flyin","flyout","flyoff","out","in"]
