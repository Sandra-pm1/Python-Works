# FUNCTION


# syntax

# def fuction_name(para1,para2,para3...paran)
# function definition
# return value


def is_leap_year(year):
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        return True
    else:
        return False
print(is_leap_year(2026)) 