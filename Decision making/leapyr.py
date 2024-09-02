# write a program to find the given year is leap year or not
# read the year frm the user


year=int(input("Enter an year  "))
if(year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year") 