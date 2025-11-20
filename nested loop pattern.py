#write a program to print this pattern

#    *
#   **
#  ***
# ****
#*****

n=int(input("Enter number of rows "))
for i in range(1,n+1):#for outer loop or to print rows
    for j in range(n-i):# this loop for to print spaces
        print(" ",end='')
    for k in range(i):#this loop to print for stars
        print("*",end="")
    print()  

#write a program to print this pattern

#*****
#*****
#*****
#*****
#*****

for i in range(1,6):
    for j in range(1,6):
        print("*",end="")
    print()   

#Write a program to print this pattern

#*
#**     
#***
#****

for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print()   


#Write a program to print this pattern

#****
#***
#**
#*

for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()  


#Write a program to print this pattern

#1
#12
#123
#1234        

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()

#Write a program to print this pattern

#1
#22
#333
#4444

for i in range(1,5):
    for j in range(1,i+1):
        print(i,end="")
    print() 

#Write a program to print floyod pattern

#1
#23
#456
#78910

num=1
for i in range(1,5):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()           

#Write a program to print this pattern

#   *
#  ***
# *****
#*******

for i in range(1,5):
    for j in range(4-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end='')
    print() 

#Write a program to print this pattern

# *******
#  *****
#   ***
#    *

for i in range(1,5):
    for j in range(i):
        print(" ",end="")
    for k in range(2*(4-i)+1):
        print("*",end='')
    print()   


#Write a program to print this pattern

#    *
#   ***
#  *****
# *******
#*********

for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end='')
    print() 


#Write a program to print this pattern

#   *
#  ***
# *****
#*******
# *****
#  ***
#   *

n = 4  # upper wale pyramid ki rows

# Upper pyramid
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()

# Lower inverted pyramid
for i in range(n-1, 0, -1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()

#Write a pogram to print this pattern
# 1 2 3 4
# 5 6 7 8 
# 9 10 11 12 


num=1
for i in range(1,4):
    for j in range(1,5):
        print(num,end=" ")
        num+=1
    print()  

#Write a program to print this pattern

#   *
#  ***
# *****
#*******
#*******
# *****
#  ***
#   *

n = 4  # upper wale pyramid ki rows

# Upper pyramid
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()

# Lower inverted pyramid
for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()