class room:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("CLASS ROOM")
        a=self.length*self.breadth
        print("Area of room: ",a)
class hall(room):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)

    def show(self):
        print("CLASS HALL")
        a=self.length*self.breadth
        print("Area of Hall: ",a)

# l=int(input("Enter Length :"))
# b=int(input("Enter Breadth :"))
# r=hall(l,b)
# r.show()

# l=int(input("Enter Length :"))
# b=int(input("Enter Breadth :"))
# r=room(l,b)
# r.area()

class A:
    def __init__(self):
        print("A init")
    def feature_1(self):
        print("Feature 1")
    def feature_2(self):
        print("Feature 2")

class B():
    def __init__(self):
        print("B init")
    def feature_3(self):
        print("Feature 3")
    def feature_4(self):
        print("Feature 4")

class C(A,B):
    def __init__(self):
        print("C init")
    def feature_5(self):
        print("Feature 5")
    def feature_6(self):
        print("Feature 6")

obj=C()
obj.feature_1()
obj.feature_2()
obj.feature_3()
obj.feature_4()
obj.feature_5()
obj.feature_6()

# obj2=B()
# obj2.feature_1()