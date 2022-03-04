# #magic method
# import function
# def sub(a,b):
#     z=a-b
#     print(z)
# # sub(5,2)
# # print(__name__)

# #class and object 

# class Person:
#     def speak(self):
#         print("I'm Speaking.....")
#     def walk(self):
#         print("I'm Walking.....")
#     def write(self):
#         print("I'm Writing.....")
#     def sleep(self):
#         print("I'm Sleeping.....")

# obj_1=Person()  #instance 



# obj_1.speak()
# obj_1.walk()
# obj_1.write()
# obj_1.sleep()
# # print(id(obj_1))
# # print(type(obj_1))


# class Student:
#     def __init__(self,name):
#         self.name=name
#     def greet(self):
#         print("Hello "+self.name)
# p1=Student("Alan")
# print(p1.name)
# p1.greet()


# class Example:
#      def __init__(self,name,age):
#         self.name=name
#         self.age=age
#      def greet(self):
#         print("Hello "+self.name)

# s1=Example("Alan",21)
# print(s1.age)
# print(s1.name)

# s1.greet()

class StudentMark:
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def get_name(self):
        print("Name: "+self.name)
    def get_mark(self):
        print("Subject 1:",self.m1,"\nSubject 2:",self.m2,"\nSubject 3:",self.m3)
    def get_total(self):
        print("Total: ",self.m1+self.m2+self.m3)
    def details(self):
        print("Name: "+self.name,"\nsubject 1: ",self.m1,"\nsubject 2: ",self.m2,"\nsubject 3: ",self.m3,"\nTotal: ",self.m1+self.m2+self.m3,"\n---------------------------------------------------------------")
    def set_name(self,name):
        self.name=name
    def set_mark(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
        


sm=StudentMark("Alan Xavier",96,87,69)
# sm.get_name()
# sm.get_mark()
sm.get_total()
sm.get_total(9)

sm.details()
sm.set_name("Xavier")
sm.set_mark(78,87,65)
sm.details()
