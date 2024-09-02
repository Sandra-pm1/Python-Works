# Write a program to check if a person is eligible for voting or not
# Conditions : Age greater than or equal to 18 the person is eligible
#              Age less than 18 not eligible for voting




age=int(input("Enter the age : "))
if age>=18:
    print("Person is eligible for voting")
else:
    print("Person is not eligible for voting")