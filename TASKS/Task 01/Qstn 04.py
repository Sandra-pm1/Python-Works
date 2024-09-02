# Write a program for grade classification based on percentage
# Condition : percentage greater or equal 90               (grade A)
#             percentage in between 80-90                  (grade B)
#             percentage in between 70-80                  (grade C)
#             percentage less than 70                      (fail)


percentage=int(input("Enter the percentage : "))
if percentage>=90:
    print("A Grade")
elif percentage >=80:
    print("B Grade")
elif percentage >=70:
    print("C Grade")
else:
    print("Failed")