# print all non_century years frm 1800 to 2024

for year in range(1800,2024,1):
    if year%100!=0:
        print(year)