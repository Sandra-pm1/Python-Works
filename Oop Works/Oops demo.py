# object oriented programming
# key components   : class  [design pattern,template,blue print]
#                    object [real world entity]



class Student:
    name:str
    age:int
    id:int
    contact:int
    course:str
    gender:str

    def set_student(self,name,age,id,contact,course,gender):
        self.name=name
        self.age=age
        self.id=id
        self.contact=contact
        self.course=course
        self.gender=gender

    def display_student(self):
        print(self.name,self.age,self.id,self.contact,self.course,self.gender)

# creating objects

student_instance=Student()
student_instance.set_student("sandra",24,100001,9947743089,"python django","female")
student_instance.display_student()