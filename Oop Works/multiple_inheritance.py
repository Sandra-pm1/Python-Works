class Grandparent:

    def m1(self):
        print("m1 method")

class Parent:

    def m2(self):
        print("m2 method")

class Child(Grandparent,Parent):

    def m3(self):
        print("m3 method")

child_instance=Child()
child_instance.m1()
child_instance.m2()
child_instance.m3()