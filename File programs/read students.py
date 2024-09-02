
f=open("C:\\Users\\uttohs\\Desktop\\PythonJuneWorks\\File programs\\students.txt","r")

student=[]

for stud in f:

    student.append(stud.rstrip("\n"))
    
print(student)