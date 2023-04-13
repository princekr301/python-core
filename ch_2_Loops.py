

'''
Python Loops
Python has two primitive loop commands:


1. while loops
2. for loops


1. The while Loop : -
With the while loop we can execute a set of statements as long as a condition is true.

'''

'''									Python For Loops
									
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).


This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.


With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
'''


				# python loops

#while loop

'''x=0
while x<10:
	print("prince")
	x+=1'''




# counting program

'''x=0
while x<10:
	x+=1
	print(x)'''
	
	
# back counting program

'''x=0
y=10
while x<y:
	y-=1
	print(y)
	'''

# 1 to 10  sum print

'''x=0
y=10
z=0
while x<y:
	x+=1
	print(x)
	z+=x
print("This is my sum of 10 numbers", z)'''

'''x=0
y=10
z=0
while x<y:
	x+=1
	print(x)
	z+=x
	print(z)'''

#find even number
'''x=0
y=20
while x<y:
	print(x)
	x+=2'''



#find 10 odd number 
'''x=1
while x<20:
	print(x)
	x+=2'''



#find the table of three
'''x=3
while x<=30:
	print(x)
	x+=3'''



# find the table of four
'''x=4
while x<=40:
	print(x)
	x+=4'''



#find the table of five 
'''x=5
while x<=50:
	print(x)
	x+=5'''



# find the table of 6
'''x=0
while x<=60:
	print(x)
	x+=6'''



#TAKE USER INPUT AND WRITE COUNTING FROM 1 TO 100
'''x=0
y=int(input("enter a number: "))
z=0
while x<y:
	x+=1
	print(x)
	z+=x
print("This is the sum of",y,"=", z)'''





# take a user input and reverse counting

'''x=int(input("enter a number"))
y=1
while x>y:
	print(x)
	x-=1
print("sum of",x,"=",y)'''


#table of 2 programing

'''x=0
y=int(input("enter a number"))
z=0
while x<y:
	x+=2
	print(x)
	z+=x
print("sum of table two","=",z)'''



# take user input and show the even number
'''x=int(input("enter a number"))
y=0
z=0
while x>y:
	y+=2
	print(y)
	z+=y
print("sum of ten even number is","=",z)'''



# take user input and show the odd number
'''x=int(input("enter a number"))
y=1
while x>y:
	print(y)
	y+=2'''

# using operator in loop for even number
'''x=int(input("enter a number"))
y=0
z=0
while x>y:
	y+=1
	if y%2==0:
		print (y)
		z+=y
print("sum of total y is",z)'''



# using operator in loop for odd number
'''x=int(input('enter a number='))
y=0
z=0
while x>y:
	y+=1
	if y%2!=0:
		print(y)
		z+=y
print("sum of total odd number=",z)'''


# second type to get even number

'''x=int(input("enter a number="))
y=0
z=0
while x>y:
	z+=1
	if z%2==0:
		print(z)
		y+=1'''

# third type to get even number

'''x=int(input("enter a number"))
y=0
z=0
while x>y:
	z+=1
	if z%2==0:
		print(z)
		y+=1
print("sum of total even number=",y)'''


# user input to table
'''x=int(input("enter a number"))
y=0
z=0
while x>y:
	y+=5
	print(y)'''
	
# the break statement
# the break statement we can stop the loop even if the while condition is true :

#break statement
'''x=1
while x<10:
	if x==8:
		break
	print(x)
	x+=1'''

'''y=1
while y<20:
	if y==10:
		break
	print(y)
	y+=1'''



# continue statement
# With the continue statement we can stop the current iteration, and continue with the next:

'''x=0
while x<10:
	x+=1
	if x==7:
		continue
	print(x)'''

'''y=0
while y<8:
	y+=1
	if y==4:
		continue
	print(y)'''


#make a program and print 1 to20 counting and counting should be break 14 and 14 should not print


'''x=0
while x<20:
	x+=1
	if x==14:
		continue
	print(x)'''

# make a second program  and 1 to 20 counting and 18 number should be skip in this cpounting

'''p = 0
while p < 20:
	p+=1
	if p==18:
		continue
	print(p)'''


# take user input and print table

'''x=int(input("enter a number: "))
y = 0
while y<10:
	y+=1
	print(y*x)

#table of 11,12,13'''

'''p=int(input('enter a number:-'))
y=0
while y<10:
	y+=1
	print(y*p)'''


#*****************************************************************************

# Factorial program
'''x=int(input("enter a number"))
z=1
while x>0:
	z=x*z
	x-=1
	print(z)'''

'''p=int(input("enter a number:-"))
r=1
while p>1:
	r=p*r
	p-=1
	print("this is my factorial answer:-",r)'''


# factorial user input programing

'''a=int(input("enter the number"))
b=1
while a>0:
	b=a*b
	a-=1
print(b)'''
#write table of 4
'''x=int(input("enter table number:-"))
y=0
while y<10:
	y+=1
	print(y*x)'''

	#find even number
'''p=int(input("please enter how much even number need :- "))
q=0
r=0
while p>q:
	r+=1
	if r%2==0:
		print(r)
		q+=1'''

# find odd number
'''x=int(input("please how much you need odd number : -  "))
y=0
z=0
while x>y:
	z+=1
	if z%2!=0:'''
'''x=int(input("enter a number:-"))
y=0
z=0
while x>y:
	print(x)
	x-=1
	z+=x
print('sum of all',z)'''


'''x=int(input("enter number"))
y=0
while x>y:
	y+=1
	if y==5:
		continue
	print(y)'''

	#factorial program in loop python

'''x=int(input("enter a number:- "))
y=1
while x>0:
	y=x*y
print(y)
x-=1'''


'''x=0
while x<10:
	print("prince")
	x+=1'''




# counting program

'''x=1
while x<=10:
	print(x)
	x+=1'''
	
	
# back counting program

'''x=1
y=10
while x<=y:
	print(y)
	y-=1'''

# 1 to 10  sum print

'''x=0
y=10
z=0
while x<y:
	x+=1
	print(x)
	z+=x
print("This is my sum of 10 numbers", z)'''

'''x=0
y=10
z=0
while x<y:
	x+=1
	print(x)
	z+=x
	print(z)'''

#find even number
'''x=0
y=20
while x<y:
	print(x)
	x+=2'''



#find 10 odd number 
'''x=1
while x<20:
	print(x)
	x+=2'''



#find the table of three
'''x=3
while x<=30:
	print(x)
	x+=3'''



# find the table of four
'''x=4
while x<=40:
	print(x)
	x+=4'''



#find the table of five 
'''x=5
while x<=50:
	print(x)
	x+=5'''



# find the table of 6
'''x=0
while x<=60:
	print(x)
	x+=6'''



#TAKE USER INPUT AND WRITE COUNTING FROM 1 TO 100
'''x=0
y=int(input("enter a number: "))
z=0
while x<y:
	x+=1
	print(x)
	z+=x
print("This is the sum of",y,"=", z)'''





# take a user input and reverse counting

'''x=int(input("enter a number"))
y=1
while x>y:
	print(x)
	x-=1
print("sum of",x,"=",y)'''


#table of 2 programing

'''x=0
y=int(input("enter a number"))
z=0
while x<y:
	x+=2
	print(x)
	z+=x
print("sum of table two","=",z)'''



# take user input and show the even number
'''x=int(input("enter a number"))
y=0
z=0
while x>y:
	y+=2
	print(y)
	z+=y
print("sum of ten even number is","=",z)'''



# take user input and show the odd number
'''x=int(input("enter a number"))
y=1
while x>y:
	print(y)
	y+=2'''

# using operator in loop for even number
'''x=int(input("enter a number"))
y=0
z=0
while x>y:
	y+=1
	if y%2==0:
		print (y)
		z+=y
print("sum of total y is",z)'''



# using operator in loop for odd number
'''x=int(input('enter a number='))
y=0
z=0
while x>y:
	y+=1
	if y%2!=0:
		print(y)
		z+=y
print("sum of total odd number=",z)'''


# second type to get even number

'''x=int(input("enter a number="))
y=0
z=0
while x>y:
	z+=1
	if z%2==0:
		print(z)
		y+=1'''

# third type to get even number

'''x=int(input("enter a number"))
y=0
z=0
while x>y:
	z+=1
	if z%2==0:
		print(z)
		y+=1
print("sum of total even number=",y)'''


# user input to table
'''x=int(input("enter a number"))
y=0
z=0
while x>y:
	y+=5
	print(y)'''
	
# the break statement
# the break statement we can stop the loop even if the while condition is true :

#break statement
'''x=1
while x<10:
	if x==8:
		break
	print(x)
	x+=1'''

'''y=1
while y<20:
	if y==10:
		break
	print(y)
	y+=1'''



# continue statement

'''x=0
while x<10:
	x+=1
	if x==7:
		continue
	print(x)'''

'''y=0
while y<8:
	y+=1
	if y==4:
		continue
	print(y)'''


#make a program and print 1 to20 counting and counting should be break 14 and 14 should not print


'''x=0
while x<20:
	x+=1
	if x==14:
		continue
	print(x)'''

# make a second program  and 1 to 20 counting and 18 number should be skip in this cpounting

'''p = 0
while p < 20:
	p+=1
	if p==18:
		continue
	print(p)'''


# take user input and print table

'''x=int(input("enter a number: "))
y = 0
while y<10:
	y+=1
	print(y*x)

#table of 11,12,13'''

'''p=int(input('enter a number:-'))
y=0
while y<10:
	y+=1
	print(y*p)'''
#*****************************************************************************

# Factorial program
'''x=int(input("enter a number"))
z=1
while x>0:
	z=x*z
	x-=1
	print(z)'''

'''p=int(input("enter a number:-"))
r=1
while p>1:
	r=p*r
	p-=1
	print("this is my factorial answer:-",r)'''


# factorial user input programing

'''a=int(input("enter the number"))
b=1
while a>0:
	b=a*b
	a-=1
print(b)'''
#write table of 4
'''x=int(input("enter table number:-"))
y=0
while y<10:
	y+=1
	print(y*x)'''

	#find even number
'''p=int(input("please enter how much even number need :- "))
q=0
r=0
while p>q:
	r+=1
	if r%2==0:
		print(r)
		q+=1'''

# find odd number
'''x=int(input("please how much you need odd number : -  "))
y=0
z=0
while x>y:
	z+=1
	if z%2!=0:
		print(z)
		y+=1'''


# find factories
'''x=int(input('enter number'))
y=1
z=0
while x>z:
	y=x*y
	y+=1
	print(y)
	z+=1'''

#counting
'''x=int(input("enter counting to "))
y=0
while x>y:
	y+=1
	print(y)'''

#back counting
'''x=int(input("enter a number:-"))
y=0
while x>y:
	print(x)
	x-=1'''
#write 23 odd number
'''x=int(input("enter odd number : -"))
y=0
z=0
while x>y:
	z+=1
	if z%2!=0:
		print(z)
		y+=1'''

#write twenty even number 
'''x=int(input("enter a number"))
y=0
z=0
while x>y:
	z+=1
	if z%2==0:
		print(z)
		y+=1'''




# write table
'''x=int(input("enter table"))
y=0
while y<10:
	y+=1
	print(y*x)'''

#use break
'''x=100
y=0
while x>y:
	if y==12:
		print(y)
		y+=1'''


#******* *******************************************************************************************
# date  20/06/2022
#***********************************************************************************
# prime number program


'''x=int(input("enter a number"))
y=2
if x<2:
	print("number is not prime")
elif x==2:
	print("number is the prime number")
else:
	while y<x:
		if x%y==0:
			print("not a prime number")
			break
		y+=1
	else:
		print('number is prime')'''

#**************************************************************

# uses of (python for loops ) program

'''x= "prince kumar"
for y in x:					
	print(y)			# vertical line 
x="prince kumar"
for y in x:
	print(y,end=" ")'''		#horizontal line


'''days=["sunday","monday","tuesday","wednesday","thursday","friday",
"saturday"]
for x in days:
	if x=="wednesday":
		break
		print(x)'''


'''days=["sunday","monday","tuesday","wednesday","thursday","friday",
"saturday"]
for x in days:
	if x=="friday":
		continue
	print(x)'''

# table print

'''for x in range(5,51,5):
	print(x)'''

# take user input to counting

'''x=int(input("enter a number"))
for y in range(1,x):
	print(y)'''



'''x=int(input("enter a number"))
x=x+1
for y in range(1,x,):
	print(y)'''

# back counting by user input

'''x=int(input("enter a number:-"))
for y in range(x,0,-1):
	print(y)'''


# sum of counting

'''x=int(input("enter a number"))
x=x+1
z=0
for y in range(1,x):
	print(y)
	z+=y
print("sum of all",z)'''


#print table to user input

'''x=int(input("enter a number"))
for y in range(1,11):
	print(x,"*",y,"=",y*x)'''

#******************************************************************
# date 21/06/2022


#print even number
'''x=int(input("enter even number:-"))
x=x+1
x=x*2
for p in range(2,x,2):
	print(p)'''

#print odd number
'''x=int(input("enter a number:-"))
x=x*2
for y in range(1,x,2):
	print(y)'''

#factorial program
'''x=int(input("enter a number"))
y=1
for z in range(0,x,1):
	y=y*x
	x=x-1
print(y)'''


# nested loop
'''days=["sun","mon,"tue","wed"]
months=["jan","feb","march"]'''




# print this type of program
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *

'''x=int(input("enter a number:-"))
x=x+1
for y in range(x):
	for z in range(y):
		print("*",end=" ")
	print()'''






#print this type of program
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
'''x=int(input("enter a number:-"))
x=x+1
for y in range(x):
	for z in range(y):
		print(y,end=" ")
	print()'''





#print this type of program
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6

'''x=int(input("enter a number:-"))
x=x+2
for y in range(1,x):
	for z in range(1,y):
		print(z,end=" ")
	print()'''
		



#print this type of program
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6

'''x=int(input("enter a number:-"))
x=x+1
for i in range(1,x):
	for j in range(1,i+1):
		print(j,end=" ")
	print()'''


'''x=int(input("enter a number:- "))
x=x+1
for k in range(x):
	for p in range(1,k):
		print(p,end=" ")
	print()'''

#****************************************************************
#	date 22/06/2022

# print this type of program
#5 5 5 5 5
#4 4 4 4
#3 3 3
#2 2
#1
'''x=int(input("enter a number:- "))
for y in range(x,0,-1):
	for z in range(y):
		print(y,end=" ")
	print()'''



# print this type of program

#1 2 3 4 5
#1 2 3 4
#1 2 3
#1 2
#1
'''x=int(input("enter a number:- "))
x=x+1
for y in range(x,1,-1):
	for z in range(1,y):
		print(z,end=" ")
	print()'''


# * * * * *
# * * * *
# * * *
# * *
# *
'''x=int(input("enter a number:- "))
for y in range(x,0,-1):
	for z in range(y):
		print("*",end=" ")
	print()'''


'''a="good morning"
print(type(a))
print(len(a))'''



'''x="arunachal pradesh"
for y in x:
	#print(y)		
	print(y,end=" ")'''


'''x="Arunachal pradesh"
y=len(x)
z = 0


while z<y:
	#print(x[z])
	print(x[z],end=" ")
	z+=1'''



'''x="bihar,begusarai" 
y=len(x)
z=0
while y>z:
	print(x[z])
	z+=1'''

'''x=str(input("enter any name: -"))
y=len(x)
z=0
while y>z:
	print(x[z])
	z+=1'''

'''x=str(input("enter any name: -"))
y=len(x)
z=0
while y>z:
	print(x[z],end=" ")
	z+=1'''

'''x=str(input("write any name:- "))
for y in x:
	print(y,end=" ") '''

#print by while vertical line

'''x=str(input("write any name:- "))
y=len(x)
z=0
a=y-1
while a>=z:
	#print(x[a])
	print(x[a],end=" ")
	a-=1'''


#print any name in horizontal line

'''x=str(input("write any name:- "))
y=len(x)-1
z=0
while z<=y:
	print(x[y])
	y-=1'''


#reverse name print by for loop


'''x=str(input("write any name:- "))
y=len(x)
for z in range(y-1,-1,-1):
	#print(x[z])
	print(x[z],end=" ")
'''
#	or

'''x=str(input("write any name:- "))
for z in range(len(x)-1,-1,-1):
	#print(x[z])
	print(x[z],end=" ")'''

'''x="honesty is the best policy"
print("best" in x)
'''
'''x="honesty is the best policy"
print("ravi" not in x)
'''
'''x="honesty is the best policy"
if "best" in x:
	print("best, in present.")'''







# create a prime number with the help of for loop by user.
 
'''num=int(input("enter any number:- "))
prime = True
for i in range(2,num):
	if (num%i==0):
		prime=False
		break
if prime:
	print("this number is prime")
else:
	print("this number is not prime")
'''



# create a factorail program with the help of for loop

'''num=int(input("enter any number: -"))
factorial=1
for i in range(1,num+1):
	factorial=factorial*i
print("the factorail of",num,"is",factorial)'''





#  	  *
#    ***
#   *****
#  *******
# *********


'''x=5
for i in range(5):
	print(" "*(x-i-1),end=" ")
	print("*"*(2*i+1),end=" ")
	print(" "*(x-i-1))'''





# leap year finding program  which year is leap year
'''def leap(year):
	if (year%400==0) or (year%100!=0 and year%4==0):
		print("leap year")
	else:
		print("not leap year")
    
    # Write your logic here
    

leap(year = int(input("write")))'''

'''# find a program from 1900 to 2020 how many leap year
x=0
for i in range(1900,2021):
	if (i%400==0) or (i%4==0 and i%100!=0):
		print("leap year :",i)
		x=x+1
print("from 1900 to 2020 in",x,"leap year")'''

'''
x= int(input("enter year: "))
if (x%400==0) or (x%100!=0 and x%4==0):
	print(f"{x} is leap year")
else:
	print(f"{x} is not leap year")'''

'''x=0
for i in range(1990,2022):
	if (i%400==0) or (i%100!=0 and i%4==0):
		#print(i)
		x+=1
print(x)'''



# How many leap year between 1990 to 2022 by while loop
'''x=1990
y=2022
z=0
while x<y:
	x+=1
	if (x%400==0) or (x%100!=0 and x%4==0):
		z+=1
print(z)'''


# find the prime number by for loop and while while loop

n=int(input("enter any number :"))
if n>1:
	for i in range(2,int(n/2)+1):
		if n%i==0:
			print(f"not prime")
			break
	else:
		print(f"prime number")
else:
	print(f"not prime")


n=int(input("enter any number :"))
m=2
if n>1:
	while m<int(n/2):
		m+=1
		if n%m==0:
			print("not prime")
			break
	else:
		print("prime number")
else:
	print("not prime number")


#find the factorial by for loop and while loops

x=int(input("enter a number"))
y=1
fact=1
while x>y:
	y+=1
	fact=fact*y
print(fact)

n=int(input("enter the number : "))
fact=1
for i in range(1,n+1):
	fact=fact*i
print(fact)








