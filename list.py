
#Write a program to return a list of negative numbers , you have given positive number of
#list from the user
list1=[1,4,6,8,10]
b=[]
for i in list1:
    b.append(-1*i)
    
print(b) 

#Write a program to print the largest element of list
list1=[1,45,4,68,7]
a=list1[0]
for i in range(0,len(list1)):
    if a<list1[i]:
        a=list1[i]
    
print("The largest element in the list is ",a)  

#Write a program to print and count odd and even numbers in the list
list1=[1,45,4,68,7]
count_odd=0
count_even=0

for i in list1:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1

print(count_even) 
print(count_odd)

#Write a program to remove duplicate value from the list
list1=[1,45,4,68,1,7]
list2=[]

for i in list1:
    if i not in list2:
        list2.append(i)

print(list2)  

#Write a progrmm to print and calculate the sum of element and avg
list1=[1,45,4,68,1,7]
sum1=0
avg=0


for i in list1:
    sum1+=i
    
avg=sum1/len(list1)    
print(sum1)
print(avg)     

#Write a program to sort the list without using built in function sort()
list1 = [5, 2, 8, 1, 3]

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] > list1[j]:
            # Swap elements
            list1[i], list1[j] = list1[j], list1[i]

print("Sorted list:", list1)


#Wrtie a program to reverse element of list without using built in
#function
l=[1,45,6,78,9,10]
n=len(l)
for i in range(n//2):#loop sirf half length takh chlyga list ke
    l[i],l[n-i-1]=l[n-i-1],l[i]#swapping process
    
print(l)
#Second method using slicing
l=[1,45,6,78,9,10]
l1=l[::-1]
print(l1)

#Third Method
l1=eval(input("enter list of integer separated by white spaces"))
l2=[]
for i in range(1,len(l1)+1):
    l2.append(l1[-i])
    
print(l2)    


#Write to print to merge two list and sort after merge
l1=[1,2,3,4,6]
l2=[5,7,8,9,10]
l1.extend(l2)#Doo list ko merge krta ha
l1.sort()
print(l1)

#Write to print index of maximum value in the list

list1=[1,45,4,68,7]
a=list1[0]
for i in range(0,len(list1)):
    if a<list1[i]:
        a=list1[i]#a ma maximum number aa chuka ha
        c=i#index store huu rha ha maximum value ka
    
print("The largest element index  is ",c)

#Write to print the second largest element of list
list1=[45,2,3,67,78]
c=max(list1)#remove largest element of list
list1.remove(c)
a=list1[0]
for i in range(0,len(list1)):
    if a<list1[i]:# a ma aab second largest element aa chuka ha
        a=list1[i]
    
print("The second largest element in the list is ",a) 

#Write to program count and print using dictionary,how many times each element of list comes
list1=[1,2,1,3,2,5,4,10]
freq={}

for i in list1:# i ma ek ek krka sara element ayga
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
        
print(freq)  

# qyes input list1=['apple','cat','banana','dog']
# output list1=['cat', 'dog', 'apple', 'banana']

list1=['apple','cat','banana','dog']

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if len(list1[i])>len(list1[j]):
            list1[i],list1[j]=list1[j],list1[i]
        
print(list1) 

#Write to program to check whether the list is palindrome or not
list1=[1,2,3,4,5,2,1]
list2=[]

for i in range(1,len(list1)+1):
    list2.append(list1[-i])#Negative index slicing
    
if list1==list2:
    print("The list is palindeome ")
else:
    print("List is not palindrome ")

#Write to program to print the most frequent element of a list
list1=[3,3,4,2,3]
freq={}#Empty dictionary

for i in list1:
    if i in freq:#count how many times each word comes in dictionary
        freq[i]+=1
    else:
        freq[i]=1

print(max(freq.values()))  

#Find the pair of numbers whose sum is equal to a given target
#Example: Input: [2,7,11,15], target=9 → Output: [2,7]
list1=[2,7,11,19] 
list2=[]
target=9

for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if (list1[i]+list1[j]==target):
            list2.append(list1[i])
            list2.append(list1[j])

print(list2) 


#list1 = [1, 2, 3, 2, 4, 5, 1]
# Output: [1, 2]
#Find all duplicate element of the list
list1=[2,7,7,2,11,19] 
freq={}

for i in list1:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

for key,value in freq.items():
    if value>1:
        print(key)

#list1 = [1, 2, 3, 2, 4, 2]
#element = 2
# Output: [1, 3, 4]
#Remove all ocurrence of the given element from the list

list1=[2,7,7,2,11,19] 
for i in range(2):
    list1.remove(2)
print(list1)


#Write to check all occurence of element in the list and print index where no come
a=[2,5,2,7,2]
n=int(input("Enter the number to check in list "))
for i in range(len(a)):
    if a[i]==n:
        print(i)#Index print


#Merge two sorted lists into one sorted list 
l1 = [1, 3, 5]
l2 = [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]

l1 = [1, 3, 5]
l2 = [2, 4, 6]

l1.extend(l2)  # dono list merge ho gayi
# ab l1 = [1, 3, 5, 2, 4, 6]

for i in range(len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] > l1[j]:   # yahan l1 hi use karna hai
            l1[i], l1[j] = l1[j], l1[i]

print("Sorted merged list:", l1 )      

#find all common elements between two list
#list1 = [1,2,3,4,5]
#ist2 = [3,4,5,6,7]
# Output: [3,4,5]


list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
for i in list1:
    for j in list2:
        if i==j:
            print("The common elements are", i)

#Move all zeros at the end of the list

list1 = [0, 2, 0, 4, 0, 5, 7, 0]
list2=[]
for i in list1:
    if i!=0:
        list2.append(i)
        
for i in list1:
    if i==0:
        list2.append(i)
    
print(list2)              

#orr second method
a=[0,2,3,0,4,5,0]
for i in a:
    if i==0:
        a.remove(i)#first remove
        a.append(i)#Than add at the end of the list
print(a) 

#Rotate a list by k steps from right side
#Enter the value of k 2
#Rotated list: [4, 5, 1, 2, 3]


list1 = [1, 2, 3, 4, 5]
k =int(input("Enter the value of k "))

k = k % len(list1)  # agar k list length se bada ho
rotated = list1[-k:] + list1[:-k]

print("Rotated list:", rotated)