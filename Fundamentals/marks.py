# program to read student name and three marks
# print total marks and avg


stud_name=input("Enter student name ")
m1=input("Enter mark1 ")
m2=input("Enter mark2 ")
m3=input("Enter mark3 ")

total=int(m1)+int(m2)+int(m3)
avg=(total/3)

print(f"Student name={stud_name}   Total marks={total}  and Average marks={avg}") 