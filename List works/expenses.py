
expenses=[12000,13000,11000,14000,15000,21000,22000,13000]


# find lenght of objects in expenses
# print all expenses
# print expenses>15000
# print total expenses
# average expenses


length=len(expenses)
total_expenses=0
print(f"Count={length}")
for i in range(0,length):
    if expenses[i]>15000:
        print(expenses[i])
    total_expenses=total_expenses+expenses[i]
print(f"Total expenses={total_expenses}")
average=total_expenses/length
print(f"Average={average}")