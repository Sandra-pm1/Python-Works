# find the number count

numbers=[12,4,56,79,10,11,13,15]

number_count={}
for n in numbers:
    if n in number_count:
        number_count[n]+=1
    else:
        number_count[n]=1
print(number_count)