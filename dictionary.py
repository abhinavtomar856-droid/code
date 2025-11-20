#✅ Main Functions / Methods of Dictionary
#Method / Operation	Description	Example
#dict[key]	Access value by key	student["age"]
#get()	Access value safely (no error)	student.get("age")
#keys()	Returns all keys	student.keys()
#values()	Returns all values	student.values()
#items()	Returns key-value pairs	student.items()
#update()	Add/modify items	student.update({"city": "Delhi"})
#pop()	Remove key and return value	student.pop("age")
#clear()	Remove all items	student.clear()
#len()	Number of items	len(student)


#Write a program to input roll no and marks of student and store data in dictionary and print their
#average
a=int(input("Enter total number of students"))  
d={}
for i in range(1,a+1):
    b=int(input(f"Enter roll no of {i}th student "))
    c=int(input(f"Enter marks of {i}th student "))
    d[b]=c
    
f=sum(d.values())/a
print("The average of student marks is ",f)


#Create a dictionary of 3 students with name as key and marks as value. Print all names.

student={"Abhinav":90,"Arnav":85,"Akshat":70}

for key in student.keys():
    print(key)

#print values
student={"Abhinav":90,"Arnav":85,"Akshat":70}

for value in student.values():
    print(value)


#Count frequency of each character in a string using dictionary.
#Example: "banana" → {b:1, a:3, n:2}

s="Banana"
freq={}

for i in s:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
    
print(freq)    

#Write a program to check if a key exists in dictionary or not?

d={1:"Abhinav",2:"Arnav",3:"sahil"}
check_key=int(input("Enter the key to check "))

for i in d:#iss loop sa dictionary ke sare key ayge one by one i ma
    if i==check_key:
        print("Key exist ",check_key)
        break
else:
    print("Key not exists ")

#Add key value pair in the existing dictionary

d={1:"Abhinav",2:"Arnav",3:"sahil"}
d.update({4:"Akshat"})
print(d)

#Remvoe key from the dictinoary using pop() method
d={1:"Abhinav",2:"Arnav",3:"sahil"}
d.pop(3)#pop function remove key and return its value
print(d)

#WAP to print key with maximum value

a={"A":50,"D":90,"C":40}
max_value=a["A"]#Asume first value is maximum
max_key=None#Default set none

for key,value in a.items():
    if max_value<value:
        max_value=value
        max_key=key

print("The key with maximum value is ",max_key) 

#Sort a dictionary on the basis of value in ascending and descending order

#Ascending order

a={"A":50,"B":90,"C":40}

sorted_dict=dict(sorted(a.items(),key=lambda item:item[1]))
print(sorted_dict)

#Descending order

a={"A":50,"B":90,"C":40}

sorted_dict=dict(sorted(a.items(),key=lambda item:item[1],reverse=True))
print(sorted_dict)

#Second Method using loop(Ascending order)

a={"A":50,"B":60,"C":80}

sorted_dict={}
for key,value in sorted(a.items(),key=lambda item:item[1]):
    sorted_dict[key]=value
    
print(sorted_dict) 


#WAP to store name and marks of student and print top 3 scorer marks

a={"Abhi":80,"Sahil":75,"Akshat":90,"Arnav":100}

sorted_dict=dict(sorted(a.items(),key=lambda item:item[1],reverse=True))
print("Top 3 scorer are")
count=0
for value in sorted_dict.values():
    print(value)
    count+=1
    if count==3:
        break

#Count word frequency in a sentence. Example: "this is a test this is" 
#{"this":2,"is":2,"a":1,"test":1}
sentence = "this is a test this is"

words = sentence.split()    # sentence ko words me tod diya
freq = {}                   # empty dictionary

for w in words:
    if w in freq:
        freq[w] += 1        # agar word already hai → count badhao
    else:
        freq[w] = 1         # pehli baar mila → count 1

print(freq)

#Dictionary comprehension: Create dict of numbers 1 to 5 where value = square of number.
#Output: {1:1, 2:4, 3:9, 4:16, 5:25}

n=int(input("Enter the value of n "))
d={}

for i in range(1,n+1):
    a=int(input("Enter the value of a "))
    b=a*a#Square of the number 
    d[a]=b#assinging value in the dictionary

print(d) 


#Convert two lists into dictionary.
#Example: keys=["a","b"] and values=[1,2] → {"a":1,"b":2}

key=["a","b"]
value=[1,2]

d={}#Empty dictionary

for i in range(len(k)):
    d[key[i]]=value[i]

print(d)

#Check whether two dictionary are equal or not without using == operator

d1 = {1: "Abhinav"}
d2 = {2: "Arnav"}

# Step 1: Check length
if len(d1) != len(d2):
    print("Dictionary not equal")
else:
    is_equal = True   # assume equal

    for key in d1:
        if key not in d2:
            is_equal = False
            break
        if d1[key] != d2[key]:
            is_equal = False
            break
    
    if is_equal:
        print("Dictionary equal")
    else:
        print("Dictionary not equal")

#Write a program to print common key in the dictionary

d1={1:"Abhinav",2:"Sahil"}
d2={3:"Akshat",4:"Arnav"}

for i in d1:
    for j in d2:
        if i==j:
            print("The common key are ",i)


#Two Sum using dictionary
#Input: nums=[2,7,11,15], target=9
#Output: [0,1] (because 2 + 7 = 9)

nums=[2,7,11,15]
list=[]
target=int(input("Enter the value of target "))
for i in range(len(nums)):
  for j in range(i+1,len(nums)):
    if nums[i]+nums[j]==target:
      list.append(i)
      list.append(j)

print(list)

#Most frequent element in list using dictionary
l=[1,2,1,3,1,4,1]
freq={}

for i in l:
  if i in freq:
    freq[i]+=1
  else:
    freq[i]=1

print(max(freq)) 

#Find duplicate elements using dictionary (return elements that appear more than once)
l=[1,2,1,3,2,4,1]
freq={}

for i in l:
  if i in freq:
    freq[i]+=1
  else:
    freq[i]=1

for key,value in freq.items():
  if(value)>1:
    print(key)