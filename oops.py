#Class and object basic problem and concept


#Declaring class
class Student:
    name="Abhinav"
    cllg="Bennett"

s1=Student() #Make object(instance of class) 
print(s1.name)
print(s1.cllg)  

#Let s make another simple program for better understanding

class Car:
    color="Blue"
    brand="BMW"

car1=Car()
print(car1.color)
print(car1.brand)    


#Multiple classes and object we can also use in oops

class Car:#class 1
    color="Blue"
    brand="BMW"

class Customer:#Class 2
    name="Abhinav"
    add="Merrut"
    

car1=Car()#Class 1 object
c1=Customer()#Class 2 object
print(car1.color)
print(car1.brand)   
print(c1.name)
print(c1.add)


#Concept of constructor
class Student:
    #Defaualt constructor
    def __init__(self):
        pass
    #Parameterizsed constructor
    def __init__(self,name,marks):#Self is an object that evoked automatically during object creation,it points object(s1,s2)
        #from main function
        self.name=name#Attributes(The data stored in classes and objects are called attrbutes)
        self.marks=marks#Attributes
        
s1=Student("Abhinav",90)
print(s1.name)
print(s1.marks)

s2=Student("Sahil",85)
print(s2.name)
print(s2.marks)

#Class attribute and object attribute

class Student:
    cllg_name="Bennett"#Class attribute(The variable which declared within the class )

    def __init__(self,name,marks):
        self.name=name#Object attribute or instance attribute
        self.marks=marks#Object attribute(The attribute which declared within constructor)

s1=Student("Abhinav",90)
print(s1.name)
print(s1.marks) 
print(s1.cllg_name)#Or print(Student.cllg_name) they both are same thing       

#Method concept in oops
#The functions which  are decalred within the class are called methods

class Student:

    def __init__(self,name,marks):#constructor
        self.name=name#object attributes
        self.marks=marks
        
    def data(self):#Function or methods
        print("Welcome",self.name)
        print("Your marks is",self.marks)
        
s1=Student("Abhinav",90)
s1.data()#Calling function using object creation 

#Ques 1
#Create a student class that takes name and marks of 3 subject as argument in constructor and print their avg using function 
class Student:

    def __init__(self,name,m1,m2,m3):#constructor
        self.name=name#object attributes
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.avg=(m1+m2+m3)/3
        
    def avg_student(self):#Function or methods
        print("Average of student",self.avg)
        
        
s1=Student("Abhinav",90,80,85)
s1.avg_student()#Calling function using object creation 

#Static Method
#The method which do not use self parameter(Work at class level) are called static methods

class Student:
    @staticmethod #Decorator
    def college():
        print("Bennett University ")

s1=Student()
s1.college()        

#Four important pillars in object oriented programing are:
#1 Abstraction 
#Hiding the implementation details of class and showing only the essential features to the user

#2 Encapsulation
#wrapping of the data and function into single unit that is object,is called encapsulation

#Ques Create Account class with 2 attributes balance and account no. Create a method for debit,
# credit and printing the balance
class Account:
     
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
         
    def debit(self, amt):
        self.balance -= amt
        print("Rs", amt, "was debited")
      
        
    def credit(self, amt):
        self.balance += amt
        print("Rs", amt, "was credited")
       
        
    def print_bal(self):
        print("The final balance was ",self.balance)
         
a1 = Account(10000, 12345)
a1.debit(1000)
a1.credit(500)
a1.print_bal()

#OOPS part 2
#del keyword
#use to delete object or object properties

#In this case it delete object properties
class Student:
    
    def __init__(self,name):
        self.name=name
        
s1=Student("Abhinav")
print(s1.name)#Output Abhinav
del s1.name
print(s1.name)#But in this case it will through the error s1 has no attribute "name"

#In this case it delete object
class Student:
    
    def __init__(self,name):
        self.name=name
        
s1=Student("Abhinav")
print(s1.name)#Output Abhinav
del s1
print(s1.name)#But in this case it will through error "s1" not defined

#Private attribute & methods
#Private attribute and method are used within the class and are not accesible from outside the
#->class

class Student:
     
     def __init__(self,name):
         __self.name=name#Private attribute
         
s1=Student("Abhinav")
print(s1.name)

#In this hello method is private it would not call outside,but we call it from inside the class
#using another function name welcome()
class Student:
     
    def __hello(self):#Private Method
         print("Hello person")
         
    def welcome(self):
        self.__hello()

s1=Student()
s1.welcome()

#Third pillar of OOPS that is inheritence
#Define -> When one class(child) derive the properties and method of another class(parent),is called inheritence

#Inheritance Concept
#Type of inheritance
#1) Single level inheritance
#2) Multi level inheritence
#3) Multiple level inheritance


#Type 1 Single inheritance
#Parent class
class Car:
    color="black"
    @staticmethod
    def start():
        print("Car started ")
        
    @staticmethod   
    def stop():
        print("Car stoped ")
#Child class       
class Toyota(Car):#Here toyota car class  inherit the properties of above class(that is Car)
    def __init__(self,name):
        self.name=name
        
    
c1=Toyota("Fortuner")
print(c1.start())
print(c1.color)

#Type 2 Multi-level inheritance

class Car:
    color="black"
    @staticmethod
    def start():
        print("Car started ")
        
    @staticmethod   
    def stop():
        print("Car stoped ")
    
class Toyota(Car): 
    def __init__(self,brand):
        self.brand=brand

class Type(Toyota):
    def __init__(self,type):
        self.type=type
        
    
c1=Type("Disel")
print(c1.start())
print(c1.color)


#Multi level Inheritence
class Akshat:
    a="Hi Akshat"

class Sahil:
    s="Hi Sahil"

class Abhinav(Akshat,Sahil):#It take two classes 
    d="Hi Abhinav"
    
a1=Abhinav()
print(a1.d)
print(a1.s)
print(a1.a)

#Super Method
#super method is used to access the methods of parent class

class Car:
    
    def __init__(self,type):
        self.type=type
        
    @staticmethod
    def start():
        print("Car started")
        
    def stop():
        print("Car stoped ")
        
class Toyota(Car):
    
    def __init__(self,name,type):
        super().__init__(type)#Here super method call the type function from parent class(Car),We have to call the type function
        #of parent class not the child class so we use super() function
        self.name=name

#Note super() method always call constructor not function        
        
car1=Toyota("Prius","Electric") 
print(car1.type)

#Another Example of super() Method
class Car:
    
    def __init__(self,type,amount):
        self.type=type
        self.amount=amount
        
    @staticmethod
    def start():
        print("Car started")
        
    def stop():
        print("Car stoped ")
        
class Toyota(Car):
    
    def __init__(self,amount,type):
        super().__init__(amount,type) 
        
car1=Toyota("1000000","Electric") 
print(car1.type)
print(car1.amount)

#Class Method
#Define-> A class method is bound to the class and receives its first arguement as class

class Person:
    name="Abhinav"
    
    @classmethod
    def changename(cls,name):#class method ,takes first arguement as class
        cls.name=name
        
p1=Person()
p1.changename("Sahil")
print(p1.name)#Here p1 point class variable(cls.name) 
#p1.name actually class ke variable se hi value le raha hai.
print(Person.name)

#Instance method
#Which takes first arguement as object which we study above they all are instance methods

#Static Methods
#Which takes no arguement 

#How to use class method basic example
class Person:
    name="Abhinav"
    
    @classmethod
    def changename(cls,name):
        cls.name=name
        
p1=Person()
p1.changename("Sahil")
print(p1.name)#Here p1 point class variable(cls.name) 
#p1.name actually class ke variable se hi value le raha hai.
print(Person.name)

#static method

#Property decorator 
#Define-> we use property decorator on any method in the class to use the method as property

#Property decortator Concept

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
        
s1=Student(60,80,67)    
print(s1.percentage)

s1.phy=70
print(s1.percentage)


#Polymerpism
# 📘 Definition of Polymorphism:

#Polymorphism is an OOPs concept that allows the same function or method name to behave differently based on the object or data type that is calling it.

#🔹 In Hindi:

#Polymorphism ka matlab hota hai "ek hi naam, alag-alag kaam" —
#Matlab ek function ya method alag-alag classes me alag tarike se kaam karta hai.
 
#Polymerpism Overloading Concept
#When the same operator is allowed to have different meaning according to context

#Operator Overloading and dunder function
#a+b   a__add__(b)
#a-b   a__sub__(b)
#a*b   a__mul__(b)
#a/b   a__truediv__(b)
#a%b   a__mod__(b)


class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def showNumber(self):
        print(self.real,"i+", self.img,"j")
        
    def __add__(self,num2):#Dunder Function
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return complex(newReal,newImg)
        
num1=Complex(1,4)
num1.showNumber()

num2=Complex(4,5)
num2.showNumber()

num3=num1+num2
num3.showNumber()

#Ques
#Define a class Circle to create circle with radius r using constructor
# define a function to calculate its area
# define a function to calculate its perimeter


class Circle:
    def __init__(self,rad):
        self.rad=rad
        print("Circle radius is ",self.rad)
         
    def area(self):
        a=3.14*self.rad*self.rad
        return a
    
    def perimeter(self):
        b=3.14*self.rad*self.rad*2
        return b
        
c1=Circle(56)
print("Area of cirlce is",c1.area())
print("Perimeter of circle is" ,c1.perimeter())

#Define a class Employee with attribute role,departement,salary.This class has function showDetails() to print the details
# of the employee

class Employee:
    
    def __init__(self,role,depart,salary):
        self.role=role
        self.depart=depart
        self.salary=salary
        
    def showDetails(self):
        print("Role of the person is",self.role)
        print("Departemnt of the person is",self.depart)
        print("Salary of the person is",self.salary)
        
e1=Employee("Professor","CS",50000)
print(e1.showDetails())

#Ques Create an engineer class that inherits the properties of employee class. Engineer class has two attributes name and age

class Employee:
    def __init__(self, role, depart, salary):
        self.role = role
        self.depart = depart
        self.salary = salary
        
    def showDetails(self):
        print("Role of the person is", self.role)
        print("Department of the person is", self.depart)
        print("Salary of the person is", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Accountant","CS",50000)

E1 = Engineer("Abhinav", 18)
print(E1.showDetails())


#Write a program to create class name rectangle and make two attributes length and breadth and also create function area and perimeter method to calculate area and
#perimeter 
class Rectangle:
    def __init__(self,length,breadth):
         self.length=length
         self.breadth=breadth
    
    def area(self):
        area=self.length*self.breadth
        return area
    
    def perimeter(self):
        per=2*(self.length+self.breadth)
        return per
        
r1=Rectangle(15,20)
print(r1.area())
print(r1.perimeter())

#Create a class employee with name and salary.Add a method to calculate to calculate 10% bonus and show updated salary

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def add_bonus(self):
        sal=self.salary+(self.salary*0.10)
        print("Updated salary is ",sal)
        
e1=Employee('Abhinav',50000)
e1.add_bonus()

#Define a class student with attributes name and marks.Print whether the student is passsed or failed(passing marks=40)
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def check(self):
        if self.marks>=40:
            print("Student is passed Congrats ")
        else:
            print("Student is failed Better luck next time ")
    
s1=Student("Abhinav",85)
s1.check()

