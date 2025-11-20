#Exception handling


#Built in exception
try:
    a=int(input("Enter first number "))
    b=int(input("Enter second number "))
    c=a/b
    print("Divison = ",c)
except:
    print("Dividing by zero not possible pls provide non zero values ")
else:
    print("Programm run successfully  ")
finally:
    print("I am always executed ")   


#User defined Exception
age=int(input("Enter age "))

if age<0:
    raise Exception("Age cannot be negative ")
elif age>18:
    print("Person eligible for voting ")
else:
    print("Eligible for voting ")    