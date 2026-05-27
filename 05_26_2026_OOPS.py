# # # # # # # 

# # # # # # # Multiple Inheritance in Python
# # # # # # class Parent1:
# # # # # #     def test1(self):
# # # # # #         print("This is a method in the Parent1 class.")

# # # # # # class Parent2:
# # # # # #     def test(self):
# # # # # #         print("This is a method in the Parent2 class.")

# # # # # # class Child2 (Parent1, Parent2):
# # # # # # #    def test(self):
# # # # # # #        print("This is a method in the Child2 class.")
# # # # # #     pass 

# # # # # # child = Child2()
# # # # # # child.test()  # This will call the test method from Parent1 due to method resolution order



# # # # # #Polymorphism in Python

# # # # # class Parent:
# # # # #     def test(self):
# # # # #         print("This is a method in the Parent class.")

# # # # # class Child(Parent):
# # # # #     def test(self):
# # # # #         print("This is a method in the Child class.")   

# # # # # c1 =Child()
# # # # # c1.test()  # This will call the test method from the Child class due to method overriding


# # # # #Overloading in Python

# # # # class Overload:
# # # #     def add(self,a,b=5,c=10):
# # # #         return a+b+c

# # # # obj = Overload()
# # # # print(obj.add(2))  # This will use the default values for b and c
# # # # print(obj.add(2,3))  # This will use the default value for c 
# # # # print(obj.add(2,3,4))  # This will use the provided values for a, b, and c

# # # class Test:
# # #     def __init__(self,value):
# # #         self.value = value
    
# # #     def __add__(self,other):
# # #         return self.value + other.value 
    
# # #     def __str__(self):
# # #         return f"Test object with value: {self.value}"
    
# # # obj1 = Test(10)
# # # obj2 = Test(20)
# # # print(obj1 + obj2)  # This will call the __add__ method and return the sum of the values

# # # print (obj1)

# # from abc import ABC,abstractmethod

# # class Business (ABC):
# #     @abstractmethod
# #     def profit(self):
# #         pass

# # class ITCompany(Business):
# #     def profit(self):
# #         return "IT Company is making a profit of 20%."  

# # it_company = ITCompany()
# # print(it_company.profit())  # This will call the profit method defined in the ITCompany


# class parent:
#     def __init__(self, name):
#         self.name=name
#     def displayName (self):
#         print("Parent Display Name Method Invoked")

# class child(parent):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age=age

#     def displayInfo(self):
#             super().displayName()
#             print(f"Child Display Info Method Invoked. Name: {self.name}, Age: {self.age}")

# child_obj=child("PV",38)
# child_obj.displayInfo()


class Test:
    cmpName ="Oracle"
    def __init__ (self,name):
        self.name=name

    def instanceMethod(self,name):
        print(f"Instance method called with name: {name}")

    @staticmethod
    def staticMethod(num):
        print(f"Static method called with num: {num}. Squared value: {num**2}")
    @classmethod
    def classMethod(cls,newCmpnyName):
        cls.cmpName = newCmpnyName
        print(f"Class method called. Company Name: {cls.cmpName}")

    @classmethod
    def displayCompanyName(cls):
        print(f"Current Company Name: {cls.cmpName}")

test_obj = Test("PV")
test_obj1 = Test("John")
test_obj.instanceMethod("PV")  # This will call the instance method and print the name  
Test.staticMethod(5)  # This will call the static method and print the squared value of num
Test.classMethod("Google")  # This will call the class method and update the company name   
test_obj.classMethod("Microsoft")  # This will also call the class method and update the company name, demonstrating that class methods can
print(Test.cmpName)  # This will print the updated company name, which is now "Microsoft" due to the last call to classMethod
test_obj1.displayCompanyName
#Test.instanceMethod("John")  # This will call the instance method and print the name "John"
test_obj1.staticMethod(10)  # This will call the static method and print the squared value of num (100)