# print all the leap year frm 1800 to 2024

for year in range(1800,2025):
    if(year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
        print(year)