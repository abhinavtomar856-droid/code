#Write to print the length of tuple without using built in function

t1=(1,2,3,4,5)
a=0
for i in t1:
    a+=1
print("The length of tuple is ",a)

#Write a program to check whether the given number exists or not

t1=(1,2,3,4,5)
a=int(input("Enter the number to be check "))

for i in t1:
    if i==a:
        print("Number exsits ")
        break#Break eseleya lagya kyo ke jo number nhi aye usma bar bar number not exist print hu
else:
    print("Number not exists ")

#Find index of given element without using index() method

t1=(1,3,46,7,89)
n=int(input("Enter the element to check index of "))

for i in range(len(t1)):
    if t1[i]==n:
        print("Index of element is ",i)
        break
else:
    print("Element not found ")    

#Convert list into tuple and vice-versa
t1=(1,3,46,7,89)
l1=[1,2,3,4,5]
t2=tuple(l1)
l2=list(t1)
print(t2)
print(l2)


#Concentate two tupples without using "+" operator
#Note
#we use extra tupple to concentate two tuple, in single tuple variable it can not possible

t1=(1,3,46,7,89)
t2=(2,56,31)

t3=()
for i in t1:
    t3+=(i,)
    
for i in t2:
    t3+=(i,)
    
print("Concated tuple ",t3)   

#Revrse a tuple using slicing and loop both method
t1=(1,3,46,7,89)
rev_tuple=t1[::-1]#Using slicing
print(rev_tuple)

#Note  if you do to with loop method it can only if you convert tuple into list else it will give error
# tuple object does not support item assignment
t = (1, 3, 46, 7, 89)
t_list = list(t)
n = len(t_list)

for i in range(n // 2):
    t_list[i], t_list[n - i - 1] = t_list[n - i - 1], t_list[i]

t = tuple(t_list)
print("Reversed tuple:", t)

#Repeat a tuple n times (simulate * operator logic manually).
#(1, 2, 3) * 3  →  (1, 2, 3, 1, 2, 3, 1, 2, 3)


t1=(1,2,3)
n=int(input("Enter the value of n "))
t2=()
for i in range(n):
    for j in t1:
        t2+=(j,)
        
print(t2) 
#Swap two tupples without using third variable
#Input tuples
t1 = eval(input("Enter first tuple: "))
t2 = eval(input("Enter second tuple: "))

print("\nBefore swapping:")
print("Tuple 1:", t1)
print("Tuple 2:", t2)

# Swapping without third variable
t1, t2 = t2, t1#Swapping process

print("\nAfter swapping:")
print("Tuple 1:", t1)
print("Tuple 2:", t2)

#Remove all repeated value in the tuple

t1=(1,2,3,1,2,5,6,7)
t2=[]

for i in t1:
    if i not in t2:
        t2.append(i)
        
t2=tuple(t2)
print("The tupple without deplicated value is",t2) 

#Sort a tuple without using sort() method
t1 = (5, 1, 4, 2, 3)

# Step 1: convert to list
lst = list(t1)

# Step 2: manual bubble sort logic
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

# Step 3: convert back to tuple
sorted_tuple = tuple(lst)
print(sorted_tuple)

#Count how many tuples in a list containing given element
#lst = [(1, 2, 3), (4, 5), (2, 7, 2), (9,), (2, 3)]
#element = 2
#Number of tuples containing 2 is: 3


lst = [(1, 2, 3), (4, 5), (2, 7, 2), (9,), (2, 3)]
element = 2
count=0
for i in lst:
    if element in i:
        count+=1

print(count)  

#Write a program to print the longest word in the tuple
#enter a tuple of words: ('apple', 'banana', 'kiwi', 'watermelon')
#The longest word is: watermelon

# Input tuple
words = eval(input("Enter a tuple of words: "))

# Assume first word is longest initially
longest = words[0]

# Loop through each word
for word in words:
    if len(word) > len(longest):
        longest = word   # update longest if bigger word found

print("The longest word is:", longest)


#Important point to remeber
#print("The longest word is:", longest)
#👉 longest ek normal variable hai — usme assignment allowed hai
#👉 Hum tuple ke elements ko modify nahi kar rahe, bas compare kar rahe hain
#So no item assignment is happening inside tuple → no error ✅

#Question
#t = (1, (2, 3), (4, (5, 6)))
# print 5

t = (1, (2, 3), (4, (5, 6)))
print(t[2][1][0])

#Given a list of tuples like [(1, 2), (3, 4), (5, 6)], return a tuple of all first elements → (1,3,5).

def elment(a):
    return a[0][0],a[1][0],a[2][0]#return multiple values from function
    

a=[(1, 2), (3, 4), (5, 6)] 
x=elment(a)
print(x)

#Rotate a tuple by k steps from right side
t = (10, 20, 30, 40)
k=int(input("Enter the value of k "))
k=k%len(t)

t=t[-k:]+t[:-k]
print(t)

#Given tuple of tuples → filter out all inner tuples whose sum is even.
#First method
t=((1,3),(2,5),(2,8))
for pair in t:
    if sum(pair) % 2 == 0:
        print(pair)

#second method
t = ((1,2), (4,6), (8,9))

for x, y in t:
    if (x + y) % 2 == 0:
        print(x, y)

#Not get exact output, we get only 4,6 instead of (4,6)
#so we use first method  

#Flatten a nested tuple → ((1, 2), (3, (4, 5))) → (1, 2, 3, 4, 5)
t=((1, 2), (3, (4, 5)))
b=[]
def flatten(x):
    if type(x)==tuple:# or if ininstance(x,tuple), it check the value in x is tuple or not?
        for y in x:
            flatten(y)
    else:
        b.append(x)
        
for x in t:
    flatten(x)
print(tuple(b))   


#Given tuple of strings, sort by string length, return as new tuple
# input case t = ("apple", "kiwi", "banana", "mango", "fig")
# output case t= ('fig', 'kiwi', 'mango', 'apple', 'banana')


t = ("apple", "kiwi", "banana", "mango", "fig")  

sorted_tuple=tuple(sorted(t,key=len))
print(sorted_tuple)
    
#✅ sorted(t)
#sorted() function tuple ko sort karta hai.
#But sorted hamesha list return karta hai, tuple nahi.
#Default sorting alphabetical hoti hai, lekin yaha humne rule change kiya hai ↓
#✅ key=len
#key batata hai kis cheez ke basis par sort karna hai.
#len ka matlab → string ki length.
#So sorting will be based on string length, not alphabetical order.    

#Given a tuple of integers, find all pairs whose sum equals k.

t=((1,2),(2,1),(3,0),(4,2))
k=int(input("Enter the value of k "))

for pair in t:
    if (sum(pair)==k):
        print(pair)


#Write to print the maximum pair of tuple

t = ((1, 2), (3, 4), (6, 1), (2, 1))
max_pair="none"
max_product=float("-inf")#stores negative infinty value 

for x,y in t:
    product=x*y
    if product>max_product:
        max_product=product
        max_pair=(x,y)
        
print(max_pair)  

#Given a tuple of tuples → find sum of each inner tuple and store in a new tuple.
# input case t = ((1, 2, 3), (4, 5), (10, 20, 30, 40), (7,))
# output case t=(6, 9, 100, 7)


t = ((1, 2, 3), (4, 5), (10, 20, 30, 40), (7,))
result=[]
for pair in t:
    sum_=0
    for i in pair:
        sum_+=i
    result.append(sum_)

result=tuple(result)
print(result)

#Given a tuple of tuples of integers, find the tuple with the highest average value
# input case= t = ((1, 2, 3), (10, 20), (4, 5, 6, 7), (100,))
# output case t=(100,)


t = ((1, 2, 3), (10, 20), (4, 5, 6, 7), (100,))
max_avg=float('-inf')
max_pair=None

for pair in t:
    avg=sum(pair)/len(pair)
    if avg>max_avg:
        max_avg=avg
        max_pair=pair
        
print("The pair with highest maxium avg is ",max_pair)


#Given t = (1, 2, 3, 4, 5, 6, 7, 8) and n=3, split into equal size chunks
#((1,2,3), (4,5,6), (7,8)).


t = (1, 2, 3, 4, 5, 6, 7, 8)
n=3
result=[]
for i in range(0,len(t),n):
    equ_parts=t[i:i+n]
    result.append(equ_parts)
    
result=tuple(result)
print(result)


#Input case= t=((1,2,3),(4,5,6),(7,8,9))
#Output case= t=((1, 4, 7), (2, 5, 8), (3, 6, 9))

t=((1,2,3),(4,5,6),(7,8,9))
t1=[]
t2=[]
for i in range(len(t)):
    for j in range(len(t)):
        t1.append(t[j][i])
for k in range(1,len(t)+1):
    t2.append(tuple(t1[(k-1)*len(t):k*len(t)]))
    
print(tuple(t2))