#write a function to two take two numbers and print their sum
def sum(a,b):#passing arguments in function
    return a+b

a=int(input("Enter the number "))
b=int(input("Enter the number "))
x=sum(a,b)#passing paramters in main function
print(x)


#WAF to take list from user and print the element of the list
def plist(list1):
    for item in list1:
        print(item,end=" ")
    
    
list1=[]    
n=int(input("Enter the length of list "))
for i in range(n+1):
    a=int(input("Enter the number "))
    list1.append(a)
plist(list1)  


#WAF to take number from the user and print its factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        
    print("Factorail of number is ",fact)
    
n=int(input("Enter the number to check factorial "))
factorial(n)


#WAF to take number from the user and check wtehter the no is even or odd
def check_even_odd(n):
    if n%2==0:
        print("No is even ")
    else:
        print("No is odd ")
    
n=int(input("Enter the number "))
check_even_odd(n)


#WAF to input a word and print it in reverse order 
def reverse_word(word):
    
    for char in word[::-1]:
        print(char)
    
    
    
word=input("Enter the word ")
reverse_word(word)

#WAF to check wether the no is prime or not
def check_prime(n):
    count=0
    for i in range(1,n+1):
        if n%2==0:
            count+=1
    if count<=2:
        print("No is prime ")
    else:
        print("No is not prine ")
    
    
    
n=int(input("Enter the number "))
check_prime(n)

#WAF to take marks of 3 subject print total and percentage of student
def student(m1,m2,m3):
    total=m1+m2+m3
    per=(total/300)*100
    print("Total marks of student ",total)
    print("Percentage of student is ",per)
    
    
    
    
m1=int(input("enter the marks of 1 subject "))
m2=int(input("enter the marks of 2 subject "))
m3=int(input("enter the marks of 3 subject "))

student(m1,m2,m3)


#WAF to remove duplicate value from the list using set
def duplicate(list1):
    set1=set()#declare empty set
    for char in list1:
        if char not in set1:
            set1.add(char)
    print(set1)
    
    
list1=[1,2,1,3,2,4,5,3,6,7]
duplicate(list1)
        

#WAF to sort elment of list without using built in sort() function
def sort(list1):
    a=len(list1)
    for i in range(0,a):
        for j in range(i+1,a):
            if list1[i]>list1[j]:
                list1[i],list1[j]=list1[j],list1[i]
    return(list1)        
    
    
    
list1=[2,4,3,1,6,5,8,7]
a=sort(list1)       
print(a)

#WAF to count even and odd number in the list
def count(list1):
    a=len(list1)
    count_even=0
    count_odd=0
    for char in list1:
        if char%2==0:
            count_even+=1
        else:
            count_odd+=1
        
    return count_even,count_odd#return multiple values from the function to main function
            

list1=[1,2,1,4,5,7,7]
a=count(list1)
print(a)#print output in the form of list


#WAF to return largest word from the string and print its length
def largest(str1):
    str1=str1.split()
    a=str1[0]
    for word in str1:
        if len(a)<len(word):
            a=word
    return a ,len(a)       
    
    

str1=input("Enter any sentence ")
a=largest(str1)
print(a)    

#WAF to count how many times word comes in string
def count_word(str1,a):
    str1=str1.split()
    count=0
    for word in str1:
        if word==a:
            count+=1
    return count       
    
    

str1=input("Enter any sentence ")
a=input("Enter the word to check in sentence ")
x=count_word(str1,a)
print(x)  


#WAF to find maximum value in dicitinary and prints its key
def max_key(dict1):
    max_value=max(dict1.values())
    
    for key, value in dict1.items():
       if value==max_value:
           return key
    
dict1={"Abhinav":80,"Sahil":90,"Akshat":75}
a=max_key(dict1)
print(a)

#Write a function to take list as a paramter and retrun its value and print it
def min_value(list1):
    return min(list1)
    
    
list1=[]
n=int(input("Enter the length of list "))
for i in range(0,n):
    a=int(input("Enter the number in the list "))
    list1.append(a)
x=min_value(list1)  
print("The minimum element of list is ",x)