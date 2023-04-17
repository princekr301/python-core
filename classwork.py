#-------------------------------------------------------------------------------
# Name:        prince kumar
# Purpose:      Learn data science
#
# Author:      programe collection
#
# Created:     05-08-2022
# Copyright:   (c) princ 2022
# Licence:     <madrid software training center>
#-------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

#print("i am prince")
#print("from bihar")

#print('''hii this is princce here
#	and we all are indian we love our country
#	my teacher name is pooja sharma ''')

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

#this is my addition program
'''x=15
y=10s
z=x+y
print(z)'''


# this is my substraction program
'''x=23
y=22
z=x-y
print(z)'''


#python syntax
'''x=24
if x>20:
	print("true")


if x>15:
	print("this is true")'''

#**********************************************************************************************************************************

#2nd days class

#python indentation
#indetation is refers to the begning of a code line indentation rule mean of
#single line comments
#multiline comments



'''x, y, z, = "sunday", "monday", "tuesday"
print(x)
print(y)
print(z)'''


'''x=y=z= "sunday"
print(x)
print(y)
print(z)'''

#type of conservation
'''x = "hello bihar"
print(type(x))


x=34
print(type(x))

x=23.6
print(type(x))

x=2j
print(type(x))'''

'''x=45
print(float(x))
x=3.14
print(complex(x))
x=35
print(complex(x))
x=3.12
print(int(x))
x=3.14
print(type(x))
x=3j
print(type(x))'''


# make a program and do the type of conservation in these numbers

#Q1 change 765 into the complex number
'''x=765
print(complex(x))'''

#Q2 change 876 into float number
'''x=876
print(float(x))'''

#Q3 change 345.67 into integer numbber
'''x=345.67
print(int(x))'''
#Q4 change -3454 into complex number
'''x=-3454
print(complex(x))'''
#Q5 change -876.45 into complex number
'''x=-876.45
print(complex(x))'''
#Q6 change -876.45 into integer number
'''x=-876.45
print(int(x))'''

#Q7 change -3454 into float number
'''x=-3454
print(float(x))'''

#******************************************************************************************************************************

#THIRD DAYS OF CLASS IN WE LEARN THAT 


#				Python operater
# there are seven type of operetor 
'''1.arithmetic operators
	operators     	 		name
		+				addition
		-				substraction
		*				multiplication
		/				dividon
		**				exponentiation
		//				floor divison
		%				modules'''


#example additional operator
'''x=12
y=16
z=x+y
print(z)
# substraction operator
x=23
y=22
z=x-y
print(z)
#multiplication operator
x=12
y=12
z=x*y
print(z)'''
#divison operator
'''x=625
y=25
z=x/y
print(z)
#exponentiation operators 	**(ye any no. ko square karti secon wale se)
x=4
y=3
z=x**y
print(z)
#floor division  //        (ye divison me quotient ka sirf point se pahle ka ans deti hai)

x=40
y=6
z=x//y
print(z)
#modules operators 			(ye divison me reminder ko answer deta hai)
x=78
y=8
z=x%y
print(z)'''


'''python relational operators comparison operator
 		operator 				name
 		>						greater than
 		<						less than
 		==						equal to
 		!=						not equal to
 		>=						greater than or equal to
 		<=						less than or equal to'''

#greator than  (>)
'''x=12
y=10
if x<y:
	print("true")
elif x<y:
	print("this is right")
else:
	print("nothing is true")'''

#less than  (<)
'''x=45
y=15
if x<y:
	print("this is true")
elif x>y:
	print("prince is right")'''


# equal to (==)
'''x=67
z=67
y=67
if x==y==z:
	print("chhotu")'''
# not equal to  (!=)
'''x=23
y=23
z=34
if x==y==z:
	print("yes")
elif x==y!=z:
	print("true")
#greator than or equal to /less than or equal to
x=10
y=12
z=12
if y>x and y==z:
	print("this is true")'''
#[note:- we can use elif or else on condition]


'''Python assigment operators
 =	assign
+=	add and assign
-=	substract and assign
*=	multiplication and assign
/= 	divide and assign
%=	modules and assign
**= exponentation and assign
//= floor divison and assign'''

 # assign   (=)
'''x=13
x+=12
print(x)
#sbstraction and assign
x=25
x-=30
print(x)
#multiplication and assign
x=10
x*=15
print(x)
#divison and assign
x=15
x/=5
print(x)
#modulus and assign
x=30
x%=8
print(x)
#Floor divisiable and assign
x=45
x//=8
print(x)
#Exponentation and assign
x=6
x**=3
print(x)'''

#python logical operators
# there are 3 type of logical opertor
#1 and = both condition should be true
#2 or = either one condition should be true
#3 NOt = reverse the decision of and , or

#Example

'''x=34
y=23
z=56
if x>y and y<z:
	print("this is true")


x=12
y=10
z=8
if x>y or x==z:
	print("true") 

x=5
y=5
z=1
if not x==y and y>z:
	print("false")
elif not x>y or y<z:
	print("prince")'''

# python membership operators-they are used to test if a sequence is present in an object
#htere are two type of membership operator
#	1.in operator
#	2.not in operator

#define
# in 				returns true if a sequence with the specified value is presnt in the object
# not in 			Returns True ia a sequence with the specified value is not pesent in the object
# Example


'''x = ["sunday" , "Monday" , "Tuesday" , "wednesday" "thursday"]
if "Monday" in x:
	print("This is true")


x = ["sunday" , "Monday" , "Tuesday" , "wednesday" "thursday"]
if "friday" not in x:
	print("this is true")'''
#python identity operator
#there are two type of identity
#	1 is
#	2 is not


#*******************************************************************************************************************

#4th days of class



# user input
'''x=int(input("enter a number"))
if x>20:
	print("this is true")
elif x<20:
	print("x is less than number")
else:
	print("all are equal")'''


#  find the eligibility of  a person is eligible to vote or not
#if 18  and 18 plus htan person is eligible other wise not

'''x=int(input("enter an age"))
if x>18:
	print("it is eligible for vote")
elif x<18:
	print("not eligible for vote")
elif x==18:
	print("eligible for vote")
else:
	print("all are not eligible for vote")'''

# take three inputs and find the greatest number among the three

'''x=int(input("enter a number"))
y=int(input("enter a number"))
z=int(input("enter a number"))'''
'''if x>y>z:
	print("x is greater than all",x)
elif x<y>z:
	print("y is greater than all",y)
elif x<z>y:
	print("z is greater than all",z)
elif x==y==z:
	print("its all are equal",x,y,z)
elif x==z>y:
	print(" x and z is equal",x,z)
else:
	print("not satisfy")
if x>z and y<x:
	print("x is a greater than all",x)
elif x<y or x>y:
	print ("one condition is true")
elif not(x==y or y>z):
	print("x is not greater then all")
elif x==y and y==z:
	print('all are equal')'''


# find the odd and even number

'''if x%2==0:
	print("even number")
elif x%42!=0:
	print("odd number")
else:
	print("rational number")'''

#**************************************************************************************
#	5th day class
#******************************************************************************************

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

#---------------------------------------------------------------------------------------------------------------------------
#		Date  15-06-2022
#--------------------------------------------------------------------------------------------------------------------


#print("hello")

#set user position of a student if student get more than 90 marks, then select on A+grade
#if student get more than  88 marks; then select on  A grade
#if student get more than  60 marks; then select on first position
#if student get more than  55 marks; then select on second position
#if student get more than  45 marks; then select on third position
#if student get more than  33 marks; then select on pass


'''if x>88 or x==88:
	print("A grade")
elif x>60<88 or x==60:
	print("first div")
elif x==55:
	print("first div")
elif x>55 and x<60:
	print("second div")
elif x==55:
	print("second div")
elif x>45 and x<55:
	print("third div")
elif x==45:
	print("third div")
elif x>33 and x<45:
	print("pass")
elif x==33:
	print("pass")
else:
	print("fail")'''

#take user input and make program to cheak number is positive, negative or zero

'''x=int(input("enter a number"))
if x>0:
	print("positive number")
elif x<0:
	print("negative number")
else:
	print("zero")'''

#take a user input if number is less than an equal to 23 so enter into the
 #if block and if number number is equal to 14 than print number is equal to 14
#if number is less then 13 then print then number is less then 13 and equal
 #to 13 if number is greater than and equal to 20 then print number is greater
# than or equal to 20, else print number doesn't match with 13 and 20  and if all conditions are not satisfied then print number out of range.'''


'''x=int(input("enter a number"))
if x>=20:
	if x==25:
		print("number is equal")
	elif x>25:
		print("number is greater than x")
	elif x<25:
		print("number is less than x")
	else:
		print("number is less than zero")'''



'''x=int(input("enter a number"))
if x<=23:
	if x==14:
		print("number is equal to 14")
	elif x<=13:
		print("number is less then or equal to 13")
	elif x>=20:
		print("no is greater than or equal to 20")
	else:
		print("doesn't match")

else:
	print("number out of range")'''



#take user input and make a program if number is less than or equal to 25 to enter into the if block , and nummber is equal to 15 so
#print the number is equal to 15, if number is les than 15 so print  number is less than , and if number is greater than 15 so print number is greater than 15. otherwise
#print number is out of range



'''x=int(input("enter a number"))
if x<=25:
	if x==15:
		print('number is equal to 15')
	elif x<15:
		print("number is less than 15")
	elif x>15:
		print('number is greater than 15')
	else:
		print('out of range')
else:
	print('false')'''






#+**+*/+*/+*/+*/+*/+*/+*/++*/+*/+*/+*/+*//////*+/**+*+/*/*/+*/+**+*/*/*/*/*/
						# python loops
#******************/////////////////////*//////////************************

					#	while loop



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

#		(self prectice from instragram)

'''x=("prince","chhotu","pappu")
for item in x:
	print(x)
x=["apple", "bat", "cat"]
for item in x:
	print(x)'''


'''print("welcome to prince home")
pin=int(input("please enter a password:- "))
if pin==8873:
	print("you entered your correctly")
	x=int(input("enter your mobile number"))
	if x==8873276380:
		if 5200==x:
			print(x)'''


#=====================================================================
# self Quiz prectice
#========================================================================
'''x=[1,2,3,4,5]
value=[y&1 for y in x ]
print(value)'''

#priting
'''x=0
while x<=18:
	x=x+3
print(x)'''


'''x=[[0],[1]]
print(("".join(list(map(str,x))),))'''

'''a=4/5
b=5//4								#ans 0.8
print(a*b)
'''

'''a=100
b=5
print(a//b*a/b)	'''					#answer	400.0


'''a=100/5
b=20//3
print(a*b)'''							#answer 120.0

'''a=~4
b=a+4
print(b)'''								#answer -1

#==================================================================

#table printing


'''x=int(input("please enter table number :-"))
y=0
while y<10:
	y+=1
	print(x,"*",y,"=",x*y)'''


'''x = int(input("enter a number"))
fact = 1
while (x>1):
	fact =fact*1
	x=x+1
print("factorial+",fact)'''


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

#******************************************************************************************


#x="Arunachal pradesh"
#print(len(x))
#print(x[5])
#print(x[-4])


#return second item
#print(x[2])
#return 17th item
#print(x[16])
#return 12 item
#print(x[12])
#return fourth item
#print(x[4])
#return 3rd item
#print(x[3])
#return 15th item
#print(x[15])
#return 1st item
#print(x[1])
#return second item
#print(x[2])
#return ninth item'''
#print(x[9])

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#	Date = 27/06/2022

#////////////////////////////////////////////////////////////////////////////


'''x="hello delhi"
print(x[0:5])
print(x[-11:-6])
print(x[6])
print(x[-5])'''

'''x="Himachal pradesh"		# 0  1  2  3  4  5  6  7 8 9 10 11 12  13 14 15
print(len(x))				# H  i  m  a  c  h  a  l   p  r  a  d  e  s  h
print(x[3])
print(x[-14])					#
print(x[4])
print(x[-13])
print(x[5])
print(x[-12])
print(x[3:15])
print(x[-14:])
print(x[5:8])
print(x[-12:-8])
print(x[7:8])
print(x[-9:-8])
print(x[-6:-5])
print(x[10:11])
print(x[-16:-2])
print(x[9:16])
print(x[14])
print(x[-16:])
'''
#x= "Himachal pradesh"
#print(x[0::2])
#print(x[2:14:3])
#print(x[-16:-1:2])
#print(x[-16:-1:-2])

'''x="Himachal pradesh"
print(x[0:2])'''


'''x="prince kumar"
y=len(x)
z=0
while y>z:
	print(x[z],end="   ")
	z+=1'''

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////
#	28-06-2022
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#x="Himachal pradesh"
#print(x.upper())		# PRINT WILL ALL IN CAPITAL LETTER
#x="HIMACHAL PRADESH"
#print(x.lower())		#PRINT WILL ALL IN SMALL LETTER

#x=" BIHAR"
#print(x.strip())	# ye start ke backspace ko kam karta hai


'''x=" we all are students"		# its will the old to new word
print(x.replace("students","indian"))

x="Good morning"
print(x.split())'''		#it will be print in ['good','morning']like this

'''x="one two three four five"
print(x.split())'''



# python-string concatenation
'''x="Good"
y="morning"
z=x+" "+y
print(z)

x="Good"
y="morning"
z=x+y
print(z)

x="good"
y="morning"
z=x,y
print(z)
'''

'''x="Good"
y="morning"
print(x,y)

 Escape sequence : -
	\n ----  for new line
	\t ----  for a tab
	\''----	 for single quote
	\\ ----	 for back slash
	\r ----  Replace at a place
'''
# \n its take a new page

'''x="welcome to, \ndata science"
print(x)
'''
# \t its take a one tab
'''x="my name is \tprince kumar sharma"
print(x)
'''

# \b its take a backspace
#x="good    \bmorning"
#print(x)

# python string swapcase = its convert the capital to small and small to capital
#x="hONESTY IS THE BEST policy"
#y=x.swapcase()
#print(x.swapcase())
#print(y)
#====================================================================================
'''age=23
x="my name is prince ,and i am {} old"
print(x.format(age))
'''
#
'''quantity= 3
item= 45
price= 78.45
x=" i want {} pieces pf item {} for {} price."
print(x.format(quantity,item, price))'''


'''quantity= 3
price= 45
item= 78.45
x=" i want {} pieces pf item {} for {} price."
print(x.format(quantity,item, price))
'''

'''My name is prince i am 23 year old and i passed 12 in 2017,
i purachase 20 oranges and  the price of these oranges are 60.50
'''

'''age=23
passed= 12
oranges=20
price=60.50
x="My name is prince, i am {} old and i passed {} in 2017 purachase {} oranges and  the price of these oranges are {}"
print(x.format(age,passed,oranges,price))
'''

'''age=input("enter age")
passed=input("date")
graduation=input("gradution date")
x="hii this is prince, when i was {} old then i passed {} 12th exam and completed my graduation {} "
print(x.format(age,passed,graduation))
'''


#**********H.W******HW********HW*********HW***********


#1. reverse the string with the help of for loop
'''x="himachal pradesh"
y=len(x)-1
for a in range(y,0,-1):
	print(x[a],end=" ")'''
#print(x[5:8])

#2. find the length of this string
#x="Himachal pradesh"
#print(len(x))

#3.return seventh item
#x="Himachal pradesh"
#print(x[6])

#4.return fifth to eeight item
#x="Himachal pradesh"
#print(x[4:8])

#5. take the user input reverse this string with the help of for loop
'''x=str(input("write any name:-\n"))
y=len(x)-1
for z in range(y,-1,-1):
	print(x[z],end=' ')'''

'''x=input("write any name:-\n")
for z in x:
	print(z,end=' ')'''

#6. Take the user input print this string with help of while loop
'''x="Himachal pradesh"
y=len(x)
z=0
while y>z:
	print(x[z],end=" ")
	z+=1'''

#7. print the ** place of a
'''x="Himachal pradesh"
print(x.replace("a","**"))'''


#8. swapcase the string
'''x="Himachal PRADESH"
print(x.swapcase())'''

#9. take a user input and split this string
'''x=input("enter anything below\n:-")
print(x.split())'''


#///////////////////////////////////////////////////////////////////
#	29-06-2022
#////////////////////////////////////////////////////////////

#	List
# string type data
'''Days=["sun","mon","tues","wed"]
print(Days)
print(type(Days))
print(len(Days))'''


# integer typr data

'''x=[1,2,3,4,5,6]
print(x)
print(len(x))
print(type(x))
'''
'''x=["true", "false"]
print(x)
print(len(x))
print(type(x))'''

'''x=list(("sunday","monday", "tuesday"))
print(x)'''


# Indexing

#create an eight item of list and extract the item with the helpp of the
#negative and positive indexing

'''days=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
print(days[3])
print(days[-4])
print(days[5])
print(days[-6])
print(days[6])
print(days[-7])
print(days[5:6])
print(days[-6:])
print(days[3:5])
print(days[2:7])
print(days[0:6])
print(days[3:8])
'''


#print a list with the help of while loop and for loop
#print a reverse list with the help of while loop and for loop

'''x=["one","two","three","four","five"]
for y in x:
	print(y)
	#print(y,end=" ")'''


'''x=["one","two","three","four","five"]
y=len(x)
z=0
while y>z:
	print(x[z])
	z+=1 '''
'''
x=["one","two","three","four","five"]
y=len(x)-1
z=0
while y>=z:
	#print(x[y])
	print(x[y],end=" ")
	y-=1 '''



'''x=["one","two","three","four","five"]
y=len(x)-1
for z in range(y,-1,-1):
	#print(x[z])
	print(x[z],end=" ")'''


'''x=str(input("write any name"))
for y in x:
	print(y,end=" ")'''

'''x=input("enter any number or name : -")
w= x.split()
#print(w)
y=len(w)
#print(y)
z=0
while y>z:
	print(w[z])
	#print(w[z],end=" ")
	z+=1'''

'''print(x)
print(type(1))'''

# list
'''x=input("enter any thing : -")
y=x.split()
z=len(y)-1
while z>=0:
	#print(y[z])
	print(y[z],end=" ")
	z-=1'''



'''x=input("hii prince write anything: -")
y=x.split()
print(y)
print(len(y))'''

#//////////////////////////////////////////////////////////////////////
# date 30-06-2022
#/////////////////////////////////////////////////////////////

			# cheak if item exists

'''x=["sunday","monday","tuesday","wednesday"]
print("monday" in x)	# cmd will print "true"
print("saturday" in x)			# cmd will print "false"
print("friday" not in x)		# cmd will print "true"
print("monday" not in x)		# cmd will print "false"'''

'''x=["one","two","three","four","five"]
if "one" in x:
	print("this is true")
	if "two" in x:
		print("this is true")
'''



'''x=["sun","mon","tue","wed"]
print(x.copy())
'''


'''x=[1,2,3,4,5,6,7]
print(x.reverse())'''


'''x=[12,23,45,56,78,16,25]
x.sort()
print(x)'''



'''x=[34,56,21,23,87,89]
x.sort(reverse=true)
print(x)'''


'''x=["a","c","b","f","e"]
x.sort()
print(x)'''



'''x=["sunday","monday","tuesday","wednesday"]
y=x.index("tuesday")
print(y)'''




'''x=[1,2,5,4,6,8]
y=x.index(5)
print(y)'''


				# change the second item


'''x=["sunday","monday","tuesday"]
x[1]="prince"
print(x)'''




''''x=["january","february","march","april","may"]
x[1:3]=["prince","kumar"]
print(x)'''

'''

x=["january","february","march","april","may","june","july"]
x[0:2]=["hiii","bro"]
print(x)
'''
'''x=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
x[1:4]=['january']
print(x)'''

'''x=["january","february","march","april","may","june","july","august"]
x.clear()
print(x)


x=[1,5,8,6,4,7,9,3,5,8,8]
y=x.count(8)
print(y)'''



'''x=["january","february","march","april","may","june","july","august"]
x.append("september")
print(x)'''



'''x=["sun","mon","tue","wed","thu"]
x.insert(1,"fri")
print(x)'''



'''x=["sun","mon","tue","wed","thu"]
y=[1,2,3,4,5]
x.extend(y)
print(x)'''


'''x=["sun","mon","tue","wed","thu"]
x.remove("mon")
print(x)



x=[35,45,66,77,88,99]
x.remove(66)
print(x)
'''
'''x=["sun","mon","tue","wed","thu"]
x.pop()
print(x)'''


'''x=[45,12,56,78,12,45,15]
x.pop(2)
print(x)'''


'''x=["sun","mon","tue","wed","thu","fri"]
del x[1]
print(x)'''



# create a five items list and apply add elements as you want with the the help of append
#,extend and insert method


#x=["ant","axe","air","aro","ass"]
#x.insert(1,"all")
#print(x)
#y=[2,5,4,6]
#x.extend(y)
#print(x)
#x.append("accurate")
#print(x)




'''y=["ball","bat","bag","boy","buy","both","bike","blog"]
del y[]
print(y)
'''
#///////////////**********************////////////////*****************///////////////////*************

# 04-07-2022

# nested list

#x=['apple','banana',['charry','orange','kiwi'],'melon','mango']
#print(x)
#print(x[2][0])
#(x[3])
#print(x[1:4])
#print(x[2][0:2])


#insert papaya and index should be 1 on of the second list.
'''x[2].insert(0,"papaya")
print(x)
x[2].clear()
print(x)'''
#y=[0,1,2,3,4]
#x[2].extend(y)		# list


'''x[2].extend([1,2,3])
print(x)
'''
'''x[2].append(0,1,2,3)
print(x)'''






# prectice question no 2

#x=[1,2,['sun','mon',['apple','banana'],'tues'],5,6]
# 1.reverse the third list
# x[2][2].reverse()
# print(x)

# 2.extract this 'sun'
#print(x[2][0])

#extract 'mon'to 'tues'
# 3.print(x[2][1:])

# 4.extract 5 to 6
# print(x[3:])

# 5.add one item in the second list and index should be 2
# x[2].insert(2,"prince")
# print(x)

# 6.remove third item in the second the list
# x[2].pop(2)
# print(x)


#************//////////////////////*****************////////////////////****************///////////////////****************//////////
# 								date 05-07-2022
# 		cheptor tupple in python


# tuple : - a tuple is collection which is odered and allow duplicate.


'''
x=("sunday","monday","tuesday","wednesday","thursday","sunday")

print(x)
print(len(x))
print(type(x))'''



'''x=("prince")
print(type(x))
'''



'''x=tuple("prince")
print(type(x))
print(x)			# return <class tuple>

x=("prince",)
print(type(x))		# return <class tuple>
print(x)'''


# create a tuple in eight item
'''
x=("jan","feb","mar","apr","may","jun","jul","aug")

# reeturn 3rd item
print(x[2])
print(x[-6])'''


#return 4th item
'''print(x[3])
print([-5])


#return fifth to seventh item
print(x[4:8])
print(x[-4:-1])


#return 2nd to 5th item
print(x[1:5])
print(x[-7:-3])


# return 2nd to last item
print(x[1:])
print(x[-7:])
'''

#return second last to first item
#print([6:0])

# all program done with the help of negative and positive indexing



# create a tuple with eight values
# typecasting

'''x=("jan","feb","mar","apr","may","jun","jul","aug")
y=list(x)
y[1:4]=("prince",)
z=tuple(y)
print(z)


'''

# add a item in tuple
#creat a new tuple with the value "wednesday" and add that tuple.


'''x=("sunday","monday","tuesday","thursday")
y=list(x)
y[2]=("wednesday",)
z=tuple(y)
print(z)
'''

'''x=("sunday","monday","tuesday","thursday")
y=("wednesday",)
x += y
print(x)'''			#print ('sunday', 'monday', 'tuesday', 'thursday', 'wednesday')




# remove from tuple
'''x=("one","two","three","four","five")
y=list(x)
y.remove("three")
x=tuple(y)
print(x)'''


# unpacking tuple

'''x=("fruits","birds","animals")
a,b,c=x
print(a)
print(b)
print(c)
print(x)'''


#astick coading

'''x=("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
(jan, feb, *march)=x
print(jan)
print(march)'''

'''x=("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
(jan, *feb, march)=x

print(feb)'''


# create a tuple with eight elements and iterate with for loop and while loop
# in for , looop through  the index  number.
#reverse this tuple with help of for loop and while loop

# while loop 

'''x=("one","two","three","four","five","six","seven","eight")
y=len(x)
z=0
while y>z:
	print(x[z],end=" ")
	z+=1'''

# reverse from while loop

'''x=("one","two","three","four","five","six","seven","eight")
y=len(x)-1
while y>=0:
	#print(x[y])
	print(x[y],end=" ")
	y-=1'''


# for loop


'''x=("one","two","three","four","five","six","seven","eight")
for y in x:
	print(y,end=" ")
	#print(y)'''


# reverse for loop

'''x=("one","two","three","four","five","six","seven","eight")
y=len(x)-1
for z in range(y,-1, -1):
	#print(x[z])
	print(x[z],end=" ")'''


'''x=("one","two","three","four","five","six","seven","eight")
y=set(x)
print(y)'''

# ******************* //////////////////////////***********************************

# 				 		date  06-07-2022

#///////////////////////////++++++++++++++++++///////////////////////////////////+

# join tuple
'''
x=(1,2,3,4,5)
y=("a","b","c","d")
print(x+y)
'''

# multiply tuples

'''x=(1,2,3,4,5)
y=x*2
print(y)'''

'''
x=("a","v","c")
y=x*4
print(y)

'''
# count method in tuple
'''x=("a","b","a","r","a","t","a")
y=x.count("a")
print(y)		# this method is used to count the number of int or str.

x=(1,2,4,5,7,8,1,5,4,9,6,5,4,1,2,5,4,1,2,8,1)
y=x.count(1)
print(y)	'''	# counting how much 1 is present in this tuple.

# x.index method
'''
x=(1,2,3,4,5,6,7,8,9)
y=x.index(5)
print(y)'''


'''x=("a","b","c","d","e","f")
y=x.index("c")
print(y)'''





# prectice set of tuple python

#create a tuple eight elements and replace this one item with two item.
'''x=(1,2,3,4,5,6,7,8)
y=list(x)
y[2:3]=(45,84)
x=tuple(y)
print(x)'''

'''x=(1,2,3,4,5,6,7,8)
y=list(x) 
y.remove(1)
y[0]=(45,54,)
x=tuple(y)
print(x)'''

#create a tuple eight elements and add one item at the list of tuple
'''x=("sun","mon","tue","wed","thu","thu","fri","sat")
y=list(x)
y.append("prince")
x=tuple(y)
print(x)
'''
# create a tuple eight elements and remove the last list item of the tuple

'''x=("sun","mon","tue","wed","thu","thu","fri","sat")
y=list(x)
y.pop()		# its delete last index of str
x=tuple(y)
print(x)'''


#create a tuple eight elements and unpack the tuple.
'''x=("one","two","three","four","five","six","seven","eight")
a,b,c,d,e,f,g,h=x
print(a)
print(b)
print(c)
print(d)
print(h)'''

#create a tuple eight elements and add one item in this tuple ,item index should be 4
'''x=("one","two","three","four","five","six","seven","eight")
y=list(x)
y.insert(3,"prince")
x=tuple(y)
print(x)'''



#create a tuple eight elements and reverse this tuple
'''x=("one","two","three","four","five","six","seven","eight")
y=list(x)
y.reverse()
x=tuple(y)
print(x)'''









# set in python

#  set in python : -
#  set : - set is collection of non repitative elements


# properties of set

# 1. set are unorderd => elements order does not matter .
# 2. set are unindexed => can't acses elements by index .
#3. there is no way to change items in set.
#4. set can't contain dublicate values.


'''x={"sunday","monday","tuesday","wednesday","sunday"}
print(x)
print(type(x))
print(len(x))


x={"one","two",1,2,3}
print(x)

#The set constructor to make a set

x=set(("sunday","monday","tuesday","wednesday"))
print(x)
'''

'''x={"sunday","monday","tuesday","wednesday"}
for y in x:
	print(y)


# x.add method
x={"sunday","monday","tuesday","wednesday"}
x.add("prince")
x.add("kumar")
print(x)'''




'''x={"sunday","monday","tuesday","wednesday"}
if "monday" in x:
	print("this is true")
'''

# update methord

'''x={"sunday","monday","tuesday","wednesday"}
y={1,2,3,4,4,5}
x.update(y)
print(x)



x={"sunday","monday","tuesday","wednesday"}
y={1,2,3,4,4,5}
z={"prince","kumar"}
x.update(y)
x.update(z)
print(x)
'''


# how can we fill an empty set()

'''x=set()
y=[1,2,3,4]
x.update(y)
x.add("prince")
print(x)'''



# Remove meethod

# remove "tuesday" by using the remove()

'''x={"sunday","monday","tuesday","wednesday","thursday"}
x.remove("tuesday")
print(x)
'''

# discard methord
'''x={"sunday","monday","tuesday","wednesday","thursday"}
x.discard("sunday")
print(x)'''		# this methord is used to delete any str


'''x={"sunday","monday","tuesday","wednesday","thursday"}
#x.remove("saturday")
x.discard("prince")
x.add("prince kumar sharma")
print(x)'''


# while loop in set
'''x={"sunday","monday","tuesday","wednesday","thursday"}
a=list(x)
y=len(a)
z=0
while y>z:
	x=set(a)
	print(a[z],end=" ")
	z+=1 '''


# trying to reverse print in whiile loop.

'''x={"sunday","monday","tuesday","wednesday","thursday"}
a=list(x)
y=len(a)-1
z=0
while y>=z:
	x=set(a)
	print(a[y],end=" ")
	y-=1 '''
				# but not succses because set is unorderded


#*//////////******************///////////////////////***********//
#		Date	: -		07-07-2022
#**************************************************************************

# pop method: - remove the last item by using is the removed item.

'''x={"sunday","monday","tuesday","wednesday","thursday","friday","saturday"}
y=x.pop()
print(y)		# its show which string has removed
print(x)		# removed the last item in set


x={"sunday","monday","tuesday","wednesday","thursday","friday","saturday"}
x.clear()
print(x)

# set completely deletd
x={"sunday","monday","tuesday","wednesday","thursday","friday","saturday"}
del x
print(x)'''


# join two set
'''x={"sunday","monday","tuesday","wednesday","thursday","friday","saturday"}
y={1,2,3,4}
z=x.union(y)
print(z)



x={"sunday","monday","tuesday","wednesday","thursday","friday","saturday"}
y={1,2,3,4}
a={"prince","kumar"}
z=x.union(y,a)
print(z)'''


'''x={"sunday","monday","tuesday","wednesday","thursday","friday","saturday"}
y={1,2,3,4}
a={"prince","kumar"}
x.update(y,a)
print(x)'''

# keep the item that exits in both set x and set y

'''x={"sunday","monday","tuesday","wednesday","thursday","friday","saturday"}
y={"sunday","monday","tuesday","january","february","march"}
x.intersection_update(y)
print(x)				# its take duplicate str in both set



x={"sunday","monday","tuesday","wednesday","thursday","friday","saturday"}
y={"sunday","monday","tuesday","january","february","march"}
z=x.intersection(y)
print(z)



# keep all , but not present in both sets:
# return a set
x={"sunday","monday","tuesday","wednesday","thursday","friday","saturday"}
y={"sunday","monday","tuesday","january","february","march"}
x.symmetric_difference_update(y)
print(x)		# its print only the string that is not in both


x={"sunday","monday","tuesday","wednesday","thursday","friday","saturday"}
y={"sunday","monday","tuesday","january","february","march"}
z=x.symmetric_difference(y)
print(z)
'''


# precice set of set

#1. create two sets with six elements and print all common values in dirsst set
'''x={"one","two","three","four"}
y={1,2,3}
x.update(y)
print(x)



#2. create two sets with six elements and print all uncommon values in third set
p=set()
x={"one","two","three","four"}
y={1,2,3}
z=p.union(y,x)
print(z)'''


#3. print an empty set and fill it.
'''x=set()
y=(1,2,3,4)
x.add(y)
print(x)''' # it is not sucsses

'''x={'prince',"kumar","sharama"}
x.clear()
x.add("priyanshu",)
x.add("roy")
print(x)'''


# 4.create a set with six elements and delete any value in
# this set with the hlp of pop() and try  to show which elements
# is deleted
'''x={"one","two","three","four","six"}
y=x.pop()
print(y)
print(x)
'''

#5. join two set with the help of any two methods.
'''x={"one","two","three","four"}
y={1,2,3}
x.update(y)
print(x)


x={"one","two","three","four"}
y={1,2,3}
p={"hiii","students"}
z=x.union(y,p)
print(z)'''


# 6. create set with six elements and add two item in this set
'''x={"jan","feb","mar","apr","may","jun"}
x.add("prince",)
x.add("kumar")
print(x)'''


# 7.  create a set with eight elementes and remove one item
# with the help of discard method. remove method,pop method
# in pop show which item you have deleted

'''x={"one","two","three","four","five","six","sesven","eight"}
x.discard("one")
x.remove("two")
print(x)

y=x.pop()
print(y)
print(x)'''

#***********************************************************************************************


 #					new cheptor in python
#					 python dictionaries


# Dictionary are written with curly brackets, and have keys and values
#dictionay are odered , changable  and does not allow duplicate
# dictionary item are presented in keys:values pairs, and can be reffered to by using the key name.

'''students={"name": "prince kumar","home": "bihar","age": 23}
print(students)
print(type(students))
print(len(students))'''


'''myDoc={
"number": "one two three four",
"boolen": ["true", "false"],
"floating": (12.4,45.8)
}
print(myDoc["number"])
print(myDoc["boolen"])
print(myDoc)'''

# make a dynamic list with the help of user input,
# take empty list
'''x=eval(input("enter a number"))
take user input and

'''


# Make a program so that when enter a state by user ,
# its capital will be shown
'''
state_capital={
"bihar": "patna",
"assam": "dispur",
"uttar pradesh": "lucknow",
"rajsthan": "jaipur",
"goa": "panji",
"kerala":"trivandrum",
"manipur": "imphal",
"gujrat": "gandhinagar",
"jharkhand": "ranchi",
"madhya pradesh": "bhopal",
"punjab": "chandigarh",
"tamil nadu": "chennai",
"west bengal": "kolkata",
"uttarakhand": "dehradun",
"odisha":"bhubaneswar",
"Arunachal pradesh": "itanagar",
"chhatisgarh": "raipur",
"haryana": "chcandigarh",
"himachal pradesh": "shimla",
"karnatka": "bengaluru",
"meghalaya": "shillong",
"mizoram": "aizawl",
"nagaland": "kohima",
"sikkim": "gangtok",
"telangana": "Hyderabad",
"tripura": "Agartala"
}
x=input("enter state name :-\n")
print("the capital of",x,"is",state_capital[x])'''







#******************************************************************************
# 11-07-2022

'''myDict={
"name" : "prince sharma",
"age": "22",
"state" : "bihar",
"district": "begusarai",
"Days": ["sun","mon","tues"]
}'''

#print(myDict)
#print(len(myDict))
#print(type(myDict))
#print(myDict["name"])
#print(myDict["Days"])
#print(myDict["age"])
#print(myDict["state"])



# get the value of the dictionary
'''print(myDict.get("Days"))
print(myDict.get("name"))
print(myDict.get("state"))

'''
# this keys method will return a list of all the keys in the dictionary.

'''myDict={
"name" : "prince sharma",
"age": 22,
"state" : "bihar",
"district": "begusarai",
"Days": ["sun","mon","tues"]
}
#print(myDict.keys())
# this values method will return a list of all the values in the dict.

#print(myDict.values())

x=myDict.keys()
print(x)

y=myDict.values()
print(y)
'''

# we adding item in the dict without method

'''myDict={
"name" : "prince sharma",
"age": "22",
"state" : "bihar",
"district": "begusarai",
"Days": ["sun","mon","tues"]
}

myDict["class"]=10
myDict["subject"]="math"
print(list(myDict))

'''
# we adding item in the dict without method

# opposite word
'''myDict={
"man": "woman",
"water": "fire",
"up" : "down",
"white": "black",
"day": "night"

}'''
'''myDict["string"]="integer"

x=myDict.items()
print(x)'''


# update method : -this method is used to add item in the dictionary.

'''myDict={
"man": "woman",
"water": "fire",
"up" : "down",
"white": "black",
"day": "night"
}

myDict.update({"inter": "out"})
print(myDict.items())'''		# to print keys and value in one item in dict.



# this method is used to delete  the keys and values

# pop("key")
# popitem()

'''myDict={
"man": "woman",
"water": "fire",
"up" : "down",
"white": "black",
"day": "night"

}
myDict.pop("man")
myDict.popitem()
print(myDict)'''

# del x["key"] method

'''myDict={
"man": "woman",
"water": "fire",
"up" : "down",
"white": "black",
"day": "night"

}

del myDict["day"]
print(myDict)'''


'''myDict={
"man": "woman",
"water": "fire",
"up" : "down",
"white": "black",
"day": "night"

}
del myDict		# this method is used to delete the dictionary.
print(myDict)'''

#output of del myDict method
# print(myDict)
#NameError: name 'myDict' is not defined

# for loop in dict

'''myDict={
"man": "woman",
"water": "fire",
"up" : "down",
"white": "black",
"day": "night"
}

for x in myDict:
	print(x)
for y in myDict:
	print(myDict[y])'''


# print kays and values with the help of x.items() method

'''myDict={
"man": "woman",
"water": "fire",
"up" : "down",
"white": "black",
"day": "night"
}

for x in myDict.items(): 		 # to print with the keys and values
	print(x)
'''

'''myDict={
"man": "woman",
"water": "fire",
"up" : "down",
"white": "black",
"day": "night"
}

for x in myDict.keys():			# to print keys with the help of loop
	print(x)
for x in myDict.values():		# to print vlues with the help  of loop
	print(x)'''


# copy() method

'''myDict={
"man": "woman",
"water": "fire",
"up" : "down",
"white": "black",
"day": "night"
}

#x=myDict.copy()			#to copy the dict
#print(x)

x=dict(myDict)
print(x)'''


#create a employee name dictionary and add  one item  in a  dictionary
#and delete last item of this dictionary. add item should be age : 30
#delete item should be "salary" :40000


'''myDict={
"name": "xyz",
"company": "abcd",
"state" :"delhi",
"post": "manager",
"salary": 40000
}

myDict["age"]=40
myDict.pop("salary")
print(myDict)'''

#create a dictionary and print the all keys and values with the help of method
#create a dictionary and iterate all the values of the dictionary with the help of update method.

'''myDict={
"name": "xyz",
"company": "abcd",
"state" :"delhi",
"post": "manager",
"salary": 40000
}
myDict.pop("name")
myDict.popitem()
del myDict["post"]
myDict.update({"time":10})
myDict["title"]="sahrma"

print(myDict)
print(myDict.keys())
print(myDict.values())
print(myDict.items())
print(myDict.get("state"))'''

#create a dictionary with the help of dict

'''myDict={
"name": "xyz",
"company": "abcd",
"state" :"delhi",
"post": "manager",
"salary": 40000
}
x=dict(myDict)
print(x)'''

#***********************************************************************
# 12-07-2022
#**************************************************************

#Nested dict
'''
myfamily = {
  "mummy" : {
    "name" : "mamta sahrma",
    "job" : "nurse"
  },
  "brother" : {
    "name" : "pappu sharma",
    "age" : 27
  },
  "sister" : {
    "name" : "priya sharma",
    "age" : 25
  }
}

print(myfamily)

'''
# student details

'''
students={
"student1":{"name": "prince", "class": "data sc"},
"student2": {"name" : "ankit","calss" : 12},
"student3": {"name" :"priyanshu","class": 11}
}

print(students)
'''

# student dict

'''student1={
"name": "abcd",
"class": "b.tech",
"age": 24
}

student2={
"name": "xydb",
"class": 8,
"age": 18
}

student3={
"name": "poiu",
"class":"mba",
"age": 25
}


students={
"student1" : student1,
"student2": student2,
"student3" : student3
}

print(students)
'''

# create an employee dict that contain four dictionaties.
'''company={
"employee1": {"name":"harsh","age":34,"post": "labour"},
"employee2": {"name": "adarsh","age":36,"post":"superwiser"},
"employee3": {"name":"rakesh","age":40,"post":"manager"},
"employee4": {"name":"mohan","age":45,"post":"ceo"}
}
print(company)
'''



# add four dict into a new dictionary.


'''employee1= {
"name":"harsh",
"age":34,
"post": "labour"
}

employee2= {
"name": "adarsh",
"age":36,
"post":"superwiser"
}

employee3= {
"name":"rakesh",
"age":40,
"post":"manager"
}

employee4= {
"name":"mohan",
"age":45,
"post":"ceo"
}

company={
"employee1":employee1,
"employee2":employee2,
"employee3":employee3,
"employee4":employee4
}

print(company)
'''

#   *********   h.w   ************
#print a dict with help of uer input

'''favlang={}
a=input("enter your favorate language prince\n")
b=input("enter your favorate language kumod\n")
c=input("enter your favorate language ankit\n")
d=input("enter your favorate language priyanshu\n")
favlang["prince"]=a
favlang["kumod"]=b
favlang["ankit"]=c
favlang["priyanshu"]=d
print(favlang)'''

#  *************** or+*****************

'''z={}
x = int(input("Enter any number: "))
y = 0
while y<x:
	keys=str(input("Enter any key: "))
	values = eval(input("Enter any value: "))
	z[keys]=values
	y+=1
print(z)'''

'''

#print a tuple with help of uer inputs
x=input("wrtite any name or number:-\n")
x=x.split()
y=tuple(x)
print(y)



#print a set with help of uer input
x=input("wrtite any name or number:-\n")
x=x.split()
y=set(x)
print(y)



#print a list with help of uer input
=input("wrtite any name or number:-\n")
x=x.split()
print(x)
'''



#***************************************************************************

# python in Function
'''
what is function?

A function is a back of code which only runs when it is called.
You can pass data , known as perameter , into a function.
a functioncan return data a result.


 creating a  function
  in pythoon  Function  is defined using the def keyboard:


  There are mainly two fuctions.

  1.  user defined function : the user  defined function by the user to perform
   the specific  task

  2.  Built in function :  the Built in function are those function that  are
  pedefinied in python

'''

'''def x():
	print("hello world")
	print("wlcome back")

x(),(),()
x()
'''


# note perameter=arrgument


'''def add(a,b):
	print(a+b)

add(2,5)
add(45,78)
add(24,5)
add(4,7)'''


'''def sub(a,b):
	print(a-b)

def mul(a,b):
	print(a*b)

def add(a,b):
	print(a+b)

def div(a,b):
	print(a/b)

add(4,5)
mul(4,5)
sub(4,5)
div(4,5)
'''


#write a function two or more aggrument and apply all airthmeric opreration on it.

'''def simp(a,b,c,d,e):
	print(a+b-c*d/e)

simp(41,78,56,14,7)

'''


# create a function with the help of user input
'''def add():
	a=int(input("enter first number:-\n"))
	b=int(input("enter second number:-\n"))
	print(a+b)
	print(a*b)
	print(a/b)
	print(a%b)
	print(a//b)
add()
'''

'''z={}
x = int(input("Enter any number: "))
y = 0
while y<x:
	keys=str(input("Enter any key: "))
	values = eval(input("Enter any value: "))
	z[keys]=values
	y+=1
print(z)'''





#		args

'''def x(*names):
	print("i am good",names[0])
	print("good morning", names[7])
	print("hello world" + " " + names[5])
	print("i am indian officer" +" " + names[2])
	print("i am army officer" + " " + names[4])
	print()

x("ABC","XYZ","IBM","GOOGLE","REF","INDIAN","MICROSOFT","AMAZON")
'''


'''key word agruments
you can also send agruments with the key = value syntax
this way the order of the agruments does not matter
'''
'''def x(name,age,Class):
	print("my name is",name)
	print("my class name is",Class)
	print("my age is",age)
x(name="prince",age="19",Class="b.sc")
'''


#Arbitrary keyword agruments,   **kwargs



'''def x(**a):
	print("my name is",a["name"])
	print("my class is",a["Class"])
	print("my age is",a["age"])

x(name="prince",age="34",Class="12th")

'''

#create three functions and find the exponent in first function,
#find floor divison in second
'''def x(a,b):
	print(a**b)

def x(a,b):
	print(a//b)

def x(a,b):
	print()
x(12,8)

'''

# create three functions and find the exponents  in first function, find floor divison
# in second
# function and find the modulus in third function, take two agruments,
# and call first function to three times, call second function to one time and
# third function to two items, call it in suffling way, take diffrent perameters,
# when you call the function.

'''def y(a,b):
	print(a**b)

def floor(a,b):
	print(a//b)

def module(a,b):
	print(a%b)

y(2,3)
y(4,3)
y(5,3)

floor(14,10)

module(45,12)
module(100,7)
'''

#**********************home  prectice********************

'''
1 substraction
2 multiply
3 divison
4 module
5 floor divison
6 exponentation


perform a function with the help of user input
create a function with the help of user input and apply all airthmetic operator.
'''
'''def x():
	a=int(input("a = "))
	b=int(input("b = "))
	c=int(input("c = "))
	d=int(input("d = "))
	print("The simplification of a*b+c*d is 	:-",a*b+c*d)
	print("the sum of all number is 		    :-",a+b+c+d)
	print(" the simplify of a+b-c*d is 		    :-",a+b-c*d)
	print("the module  and after add of a%b+c is :- ",a%b+c)

x()'''

'''


Arbitarary arguments, *args


if you do not know how many arguments that will be passed into your
function, add an astrisk before the parameter namein the function definition.

this way the function will receive a tuple of arguments, and can access the
 items accoringly index
'''
'''
def x(*names):
	print("I am", names[0])
	print("hello dear",names[5])
	print("Good morning",names[3])
	print("I am indian my name is",names[2])
	print("sita is a friend of ",names[1])

x("prince","chhotu","ankit","rani","riya","priyanshu","ankita","manu")
#	 0		  1		   2	  3		  4		  5			  6		 7

'''

'''
keyword arguments

You can also send arguments with the key = value syntax.
this way the order of the arguments does not matter.
'''


'''
def x(name, Age, Class):
	print("My name is ",name)
	print("I am",Class,"with math honors")
	print("I am",Age,"year old")

x(name="prince kumar", Age=22, Class="graduate")
'''


'''
Arbitarary arguments, **kwargs


if you do not know how many arguments that will be passed into your
function, add two  astrisk ** before the parameter name in the function definition.

this way the function will receive a dictionary of arguments, and can access the
 items accoringly

if the number of keyword agruments is known, add a double  ** before the perameter
name'''

'''
def x(**a):
	print("my name is",a["name"])
	print("i study in class", a["Class"])
	print("my age is ",a["Age"],"year")

x(name="prince", Age= 20,Class="xth")
'''

'''
def a(**x):
	print(x["name"])
	print(x["age"])
	print(x["state"])
	print(x["country"])

a(name="prince", age="23", state="bihar",country="India")
'''

'''
def t(**m):
	print(m["prince"])
	print(m["delhi"])
	print(m["bihar"])
	print(m["boy"])
t(boy="larka",prince="chhotu",bihar="state",delhi="capital of india")
'''




# prectice set  question

#1. create three functions and find the exponent in first function,
#   find floor divison in second

'''def exp(a,b):
	print(a**b)

def x(a,b):
	print(a//b)

exp(3,4)
x(70,8)
'''


# 2. create three functions and find the exponents  in first function, find floor divison
#   in second
#  function and find the modulus in third function, take two agruments,
#  and call first function to three times, call second function to one time and
#  third function to two items, call it in suffling way, take diffrent perameters,
#  when you call the function.

'''
def y(a,b):
	print("The a**b  of exponents is : -",a**b)
	print("The sum of a+b is :-",a+b)

def floor(a,b):
	print("the floor divison is: -",a//b)

def module(a,b):
	print("the module of a%b is:-",a%b)

y(2,3)
y(4,3)
y(5,3)

floor(14,10)

module(45,12)
module(100,7)'''



#3. create three functions find divison in the first function, and
#	print table of any random number with the help of loop in ssecond function,
#	and find the multiplication
#   in third function. take two agruments in first and third functionand take user
#   inputin second function and call it in shuffling way.

# it is my 1st function
'''def div(a,b):
	print("the divison of a/b is :-",a/b)


# it  is my 2nd funcion
def table(x):
	y=10
	z=1
	g=0
	while z<=y:
		m = x*z
		print(m)
		z+=1
#		g+=m
#	print("the sum of total table: -",g)


# it is my 3rd function
def mul(p,q):
	print("the multiply of p*q is : -",p*q)

# passing Arguments
div(8,2)
div(120,24)
table(int(input("Enter a number: ")))
mul(2,3)
'''






#2nd function print table with the help of while loop
'''
def table(x):
	y=1
	while y<=10:
		print(y,"x",x,"=",y*x)
		y+=1

table(int(input("enter table name:-")))
'''





# funtion in print table with the help of for loop

'''def  table(tn):
	s=0
	for i in range(1,11):
		x=i*tn
		print(i,"x",tn,"=",x)
		s+=x
	print("the sum of table",tn,"is:-",s)


table(int(input("enter table :-")))
'''



#4.  create a function and make a list with the eight items and remove two items and add
#    only one item on the place of the items without method.


'''
# it is eight list of function
def list(a,b,c,d,e,f,g,h):
# it is a list in eight str
	mylist=[a,b,c,d,e,f,g,h]
# here we removing two str and adding one str on the place
	mylist[0:2]=["prince"]
# prpinting the mylist
	print(mylist)

# passing the arguments in the function
list(a="january",b="february",c="march",d="april",e="may",f="june",g="july",h="august")
'''

#***************************************************************************************************************

# 14-07-2022

#******************************************************************************************

#default perameter : - the following exampe shown how to use a default pearmater value.
# if we call the function without zgrument ,it uses the default value.


'''
def x(city="delhi"):
	print("I am from",city)

x("punjab")
x()
x("rajsthan")
x()
x("bihar")
x()
x("chandigarh")

'''

# the pass statement
'''
function definitions can not be empty, but if you for sume reason have a function
definition
with no content ,put in the pass statement to avoid getting an NameError



def x():
	pass


return values

To let a function return a value, use the return statment:
'''
'''
def A(x):
	return 5*x
print(A(3))
print(A(5))
print(A(9))
'''


# python Anonymous / Lambda function

# the anonymous function , also known as lambda function.
'''in puthon , an anonymous function is a function that is defined without a name



a lambda function is small  anonymous function.
a lambda function can take any number of arguments , but can only have one expression.
'''
'''
x=lambda a,b: a*b
print(x(5,6))


x=lambda a,b,c:a+b+c
print(x(5,6,4))


x= lambda a,b,c,d:a+b*c/d

print(x(6,8,10,4))


p=lambda a:a
print(p("ram"))
'''



# python  zip function

#join two tuple  together
'''
x=("sun","mon","tue")
y=("wed","thu","fri","sat")
z=zip(x,y)
print(tuple(z))


x=("jan","feb","maarch")
y=("april","may","june","july")
z=zip(x,y)
print(list(z))




x=["jan","feb","maarch"]
y=["april","may","june","july"]
z=zip(x,y)
print(set(z))






x=["jan","feb","maarch"]
y=["april","may","june","july"]
z=zip(x,y)
print(dict(z))
'''

'''
x=["prince","ankit","ram"]
y=[4,6,7]
z=zip(x,y)
print(dict(z))
'''
'''
key=str(input("enter key:-"))		# not coompletd
value=eval(input("enter value:-"))
x=zip(key,value)
print(dict(x))

'''

# Pectice time

#create a function and take six argument s and perform any arithmetic operation within a single line
'''x=lambda a,b,c,d,e,f:a+b/c*d+e-f
print(x(12,10,5,10,20,5))

'''
'''
expression
create a function with the help of two tuple make a dictionary.
'''
'''x= ("ram","sita","ravan","krishna")
y=("god","devi","evil","avtar")
z=zip(x,y)
print(dict(z))'''

'''
create four function and perform arithmetic opreration as want to in each function,
and call these
function is a suffling wayss'''
'''
def x(a,b,c):
	print(a+b*c)


def y(p,q,r):
	print(p*q-r)


def z(f,g,h):
	print(f*g/h)


def avg(j,k,l,m):
	print((j+k+l+m)/4)


x(4,5,6)
x(7,4,1)

y(8,5,2)
y(4,2,3)

z(4,45,9)
z(78,100,10)


avg(45,56,12,10)


'''

'''
create two function and find the 10 even number in the first function and find 10 odd number in functionin a suffling ways.

'''
'''

def even(x):
	y=0
	z=0
	while x>y:
		z+=1
		if z%2==0:
			print(x,"even number",z)
			y+=1



def odd(x):
	y=0
	z=0
	while x>y:
		z+=1
		if z%2!=0:

			print(x,"odd number",z)
			y+=1

even(10)

odd(10)
'''
'''
create three function and find the 10 whole number do the sum of these whole number in first
function and find the exponents in second function,

'''
'''
def whole(x):
	z=0
	for y in range(0,x):
		print(y)
		z+=y
	print("sum of 10 whole number is ",z)


whole(10)'''

#****************************************************************************************************************************
#			19-07-2022
#*******************************************************************************************************************************

	#create nested dictionary by user input
'''myDict={}
				x= int(input("enter any number:-"))
				for i in range(0,x):
					key=str(input("erite key:"))
					value=eval(input("enter value"))
					myDict.append(key)'''


#********************************************************************************************************
#								class

#	A class is an objeective oriented prograamming , almost everything is python
'''is an objective with its properties and methods.

A class like an objecte constroctor or a "blue print" for creating an object
objects are related to real wntities such as phone , mobile car extract
Major principeles of objects oriented prograamming


Class
objects
methods
inheritance
polymorphism
Data abstraction
Encapsulation.
'''



'''class x:
	a=5
b=x()
print(b.a)


class x:
	a=4
	b=3
	z=a*b
mul=x()
print(mul.z)
print(mul.a)'''


'''class x:
	def c(self):
		print("hello")
a=x()
a.c()'''



'''class x:
	def c(self,a,b):
		self.a=a
		self.b=b
		self.z=a+b
p=x()
p.c(4,5)
print(p.z)'''


'''class x:
	def c(self,a,b,c,d):
		self.a=a
		self.b=b
		self.c=c
		self.d=d
		self.z=a+b+c+d
		self.k=a*b+c-d
p=x()
p.c(4,5,9,6)
print(p.z)
print(p.k)'''

#create a class and make two method in this calss in first method do multipliication
#and second method do substraction
'''class y:
	def x(self,a,b):
		self.a=a
		self.b=b
		self.p=a*b

	def sub(self,c,d):
		self.c=c
		self.d=d
		self.k=c-d

mul=y()
mul.x(8,4)
mul.sub(12,10)
print(mul.p)
print(mul.k)'''



'''class a:
	def div(prince,b,c):
		prince.b=b
		prince.c=c
		prince.d=b/c

	def mod(prince,b,c):
		prince.b=b
		prince.c=c
		prince.e=b%c

	def exp(prince,d,e):
		prince.d=d
		prince.e=e
		prince.f=d**e


x=a()
x.div(42,5)
print("divison :",x.d)
x.mod(12,5)
print("module :",x.e)
x.exp(3,3)
#print("divison :",x.d)
#print("module :",x.e)
print("exponents :",x.f)



class a:
	def div(prince,b,c):
		prince.b=b
		prince.c=c
		prince.d=b/c

	def mod(prince,b,c):
		prince.b=b
		prince.c=c
		prince.e=b%c

	def exp(prince,d,e):
		prince.d=d
		prince.e=e
		prince.f=d**e


x=a()
x.div(42,5)
print("divison :",x.d)
x.mod(12,5)
print("module :",x.e)
x.exp(3,3)
#print("divison :",x.d)
#print("module :",x.e)
print("exponents :",x.f)

'''

#To understand the meaning of classes we have to understand the built-in __init__
#function.
#All classes have a function
'''
class person:
	def __init__(self,name,age):
		self.name=name
		self.age=age

x=person("prince",45)
print(x.name)
print(x.age)
'''

'''
class person:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def x(self):
		print("mu name is",self.name)


p1=person("prince",34)
p1.x()
print("my name is",p1.name)
print("my age is",p1.age)
'''

#create a class and make  two method in this class and in first method print
#any statement, in second use __init__ function  and do addition.
'''
class x:
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		self.d=a+b+c
	def pk(self):
		print("addition :",self.d)

p1=x(6,5,4)
p1.pk()
print(p1.d)'''
'''
class x:
	def __init__(self,number):
		self.number=number
p1=x(12)
#print(p1.number)
o=p1.number
for i in range(o+1):
	print(i)
'''



'''class math:
	def x(self):
		print(self.d)
	def __init__(self,d,e):
		self.d=d
		self.e=e
		self.f=d*e
	#def x(self):
	#	print(self.d)
p=math(4,6)
p.x()
p.x()
#p.x(9,7)
#print(p.c)
print(p.f)'''

#****************************************************************************************************
# 		Date 	20-07-2022
#************************************************************************************************************


# Modify object properties
#You can modify properties on objects like this
'''
class person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
				
	def x(self):
		print("My name is",self.name)

p1=person("prince",45)
p1.x()
print(p1.name)'''
'''
class person:
	def __init__(self,a,b):
		self.a=a
		self.b=b

	def x(self):
		print(self.b)

x1=person("ram",45)
#x2=person("mohan",12)
del x1
print(x1)'''


'''creat a class and make three method in this class in first method do exponents
in second method print any statement and in third method find the modules. take diffrent arguments for
all method , and __init__function in this use
'''
'''
class math:
	def __init__(self,a,b,c,d):
		self.a=a
		self.b=b
		self.c=c
		self.d=d
		self.e=a**b
		self.f=a+b*c-d
		self.g=c%d

	def x(self):
		print("Hii \nThis is prince here")
		print("exponent :",self.e)


	def y(self):
		print("simplification :",self.f)

p=math(3,4,12,10)
p.x()
p.y()
#p.x()
print("modules :",p.g)
'''


'''create a class and make two method with the help of user input in first method
print a table with the help of while loop in and second in multipliication.
'''


'''
class math:
	def x(self,a):
		self.a=a
		p=1
		while p<=10:
			print(p,"x",a,"=",p*a)
			p+=1
	def y(self,b,c):
		self.b=b
		self.c=c
		self.d=b*c
z=math()
z.x(int(input("enter table")))
z.y(12,10)
print("\nmultiplication : ",z.d)'''




# class in table by user input with __init__ function
'''
class math:
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		self.d=b*c

	def x(self):
		y=self.a
		z=1
		while z<=10:
			print(y,"x",z,"=",z*y)
			z+=1

x1=math(int(input("table :")),12,10)
x1.x()
print("\n\nmultiplication",x1.d)
'''


#Example of single level inheritance

'''class parents():
	def first(self):
		print("apple is good for helath")

class child(parents):
	def second(self):
		print("Honesty is the best policy")

x=child()
x.first()
x.second()'''



#create two classes and use single level in inheritance and make one method in each class
#in first do multiplication in second class find the modules. use __init__ constroctur
#in each case
'''
class parents():
	def p(self,e,f):
		self.e=e
		self.f=f
		self.g=e*f
		print(x.g)


class child(parents):
	def q(self,e,f):
		self.e=e
		self.f=f
		self.g=e%f
		print(x.g)

x=child()
x.p(6,8)
x.q(18,7)'''



# with the use of __init__function
'''class parents():
	def __init__(self,e,f):
		self.e=e
		self.f=f
		self.g=e*f
		self.h=e%f


class child(parents):
	def l(self):
		print("multiplication :",x.g)

x=child(5,6)
x.l()
print("modules : ",x.h)'''

#		OR
'''
class parents():
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a*b
class child(parents):
	def x(self,c,d):
		self.c=c
		self.d=d
		self.e=c%d

y=child(12,10)
print("multipication :",y.c)

y.x(15,4)
print("modules :",y.e)'''


'''
create two classes and use single level inheritance and make two methods  in each class
do addition
in first class find the exponents and in second method print any statement
in second class find the floor divison and in second method print any statement
use __init__ constructor in each class

'''


#****************************************************************************************************************
# 		DATE 21-07-2022
#***********************************************************************************************************************

# super function uses super()


'''class parents():
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a*b
	#	print(self.c)


class child(parents):
	def __init__(self,a,b,g,d):
		super().__init__(a,b)
		self.g=g
		self.d=d
		self.e=g+d

x=child(4,6,8,2)
print(x.c)
print(x.e)'''



'''
create two classes AND MAKE TWO methodsIN EACH CLASS IN FIRST METHOD DO SNY SRITHMETIC
OPERRSTOR AND SECOND IN METHOD PRNT SNY statement, IN IN SECOND, IN SECOND CLASS  PRINT
A LIST WITH THE HELP OF WHILE LOOP AND INN SECOND METHOD DO ANY CALUCULATION.
USE __INIT__ constructor AND SUPER Function AS PER YOUR QEQUIRMENT.
'''



'''ok=[]
class parents():
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		self.d=a+b+c

	def x(self):
		p=self.a
		q=0

		while q<p:
			ok.append(q)
			q+=1
		print(ok)

class child(parents):
	def __init__(self,a,b,c,g,e):
		super().__init__(a,b,c)
		self.g=g
		self.e=e
		self.f=g+e

	def o(self):
		print("\nhii i am prince sharma")


x1=child(12,5,7,9,6)
print("addition :",x1.d)

x1.x()

print("\nadd :",x1.f)
x1.o()
'''

#	prectice question set of class, inheritance,super(). function

'''
1. create three classes and make two methods in first class in first method print a list
with help of while loop and in second method find modules. in second class create
three method  and in first
method  print this string in lower case "ARUNACHAL PREADESH", in second method print
a tuple in reverse order
and in third method print a table, of any random number

use __init__function and super() function as per your requirment	'''

'''
class parents():
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a%b
		#x=["prince","kumar","sharma"]

	def  mod(self):

		x=[12,21,14,15,16,]
		z=len(x)
		y=0
		while z>y:
			print(x[y],end=" ")			# this question is solved
			y+=1


class child(parents):
	def __init__(self,a,b):
		super().__init__(a,b)
		z= "ARUNACHAL PRADESH"
		p=z.lower()
		print(p)

	def second(self):
		jk=(5,14,25,36,7,8)
		kk=list(jk)
		kk.reverse()
		jk=tuple(kk)
		print("\nreverse order :",jk)

	def third(self,c):
		s=self.c
		for ii in range(1,11):
			print(ii*s)


pk=child(12,8)
print(pk.c)
pk.mod()
#print("mod :",pk.c)

pk.second()

pk.third(5)
'''

#2. create two class and make two methods in first class ,in first method
#find the person is eligible for vote or not,in second method
# find the exponent, and second class print this statement
# "Honesty is the best policy" in first method
# and in second method do any caluculation  as u want u can use
#  __init__ and super function per your.

'''
class parents:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a**b

		age=int(input("enter your age :"))
		if age>=18:
			print("eligible for vote")
		else:
			print("not eligible for vote")
	def exp(self):
		print("exponent :",self.c)


class child(parents):
	def __init__(self,a,b,d,e,f):
		super().__init__(a,b)
		self.d=d
		self.e=e
		self.f=f
		self.g=d+e*f
		print("Honesty is the best policy")

	def cal(self):
		print("simplification :",self.g)



x=child(4,5,11,10,8)
x.exp()
x.cal()	'''

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#												multilevel inheritance


'''
# Multilevel inherritance

class grandent():
	def first(self):
		print("\napple is good for health")

class parents(grandent):
	def second(self):
		print("\nHonesty is the best policy")

class child(parents):
	def third(self):
		print("\nmy name is prince kumar")

ob=child()
ob.first()
ob.second()
ob.third()

'''



# example of multilevel inheritance
'''
class grand():
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a+b

	def first(self):
		print("hello python i will finish you")

class parent(grand):
	def __init__(self,a,b,d,e):
		super().__init__(a,b)
		self.d=d
		self.e=e
		self.f=d-e

	def second(self,g,h):
		self.g=g
		self.h=h
		self.i=g%h

class child(parent):
	def __init__(self,a,b,d,e,j,k):
		super().__init__(a,b,d,e)
		self.j=j
		self.k=k
		self.l=j**k

	def third(self,m,n):
		self.m=m
		self.n=n
		self.o=m+n-m*n/m


x=child(12,45,78,23,25,2)
print("add :",x.c)
print("sub :",x.f)
print("exponent : ",x.l)

x.first()
x.second(19,4)
print("module :",x.i)
x.third(12,4)
print("simplification : ",x.o)
'''


# prectice question of multilevel inheritance

#1. create three classes with the help of multilevel inhertitance and use __init__
# constructor each class and create two method in each class in one method print
# any statement and in another method perform any aithmetic operation.
# use super function.


'''
class grand:
	def first(self):
		print("\nif you born in poor faimly \nits not your problem \nbut you die in poor \nits your problem \n\t\t\tby prince")

	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		self.cc=a*b-c

class parents(grand):
	def second(self):
		print("\nFailure is the not opposite of sucsses \nI'ts part of sucsses \n\t\t\tby prince")

	def __init__(self,a,b,c,d,e,f):
		super().__init__(a,b,c)
		self.d=d
		self.e=e
		self.f=f
		self.ff=d%e*f

class prince(parents):
	def third(self):
		print("\nFailure is the best part of our sucssesful life \ni feel this")

	def __init__(self,a,b,c,d,e,f,g,h):
		super().__init__(a,b,c,d,e,f)
		self.g=g
		self.h=h
		self.hh=g/h


x=prince(12,10,8,45,14,23,22,11)
x.first()
x.second()
x.third()
print("\n frist def :",x.cc)
print("second def :",x.ff)
print(" third def :",x.hh)

'''


#3. create a program with help of multilevel inheritance and make three class, in
#first class
#make two method and first method do any caluculation and in second method print any statement.
#second class
#make one method and first method in do simplification.
#third class
#make two method and first in print a table of any random numner and second in any statement.
#use
#__init__ constructor and super(). function in this program
'''
print("\n\nwelcome to oops\n")
class prince:
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		self.avg=(a+b+c)/3

	def first(self):
		print("\n\nfailure is succses in progress")

class kumar(prince):
	def __init__(self,a,b,c,d,e,f):
		super().__init__(a,b,c)
		self.d=d
		self.e=e
		self.f=f
		self.simp=d+e/f*d-e+f

class sharma(kumar):
	def __init__(self,a,b,c,d,e,f,g):
		super().__init__(a,b,c,d,e,f)
		self.g=g
		k=self.g
		for i in range(1,11):
			print(g,"x",i,"=",i*g)


	def second(self):
		print("\nSelf-Belive & hard work will always \nearn you sucsses\n\tit's my thought")

x=sharma(12,8,10,4,2,16,int(input("enter table")))
x.first()
x.second()
print("\n\naverage :",x.avg)
print("simplification :",x.simp)

'''


#4. create three classes and use multilevel inheritance and
#first class
#create two method in first any caluculation and second in prnit any satatment
#second class
#create only one method and use __init__ constructor and permform any airthmetic operation
#third class
#create two methods in first method print any statement and second method in perform caluculation

'''
class one:
	def first(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		self.math=a+b*c/b-a+c

	def second(self):
		print("\n\nNothing is impossible")

class two(one):
	def __init__(self,e,f,g):
		self.e=e
		self.f=f
		self.g=g
		self.math2=e*f*g

class three(two):
	def third(self):
		print("\nStart where you are")

	def forth(self,h,i):
		self.h=h
		self.i=i
		self.math3=h**i

x=three(12,4,3)
x.second()
x.third()
x.first(9,7,3)
print("\n\nsimp :",x.math)
x.forth(6,5)
print("exponent :",x.math3)
print("bracket q :",x.math2)
'''



'''class prince:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a*b
		print("hiii",self.c)

	def x(maa,d,e):
		maa.d=d
		maa.e=e
		maa.f=d+e
		print(maa.f)
class kumar(prince):
	def __init__(self,a,b,g,h):
		super().__init__(a,b)
		self.g=g
		self.h=h
		self.i=g/h
		print(self.i)

	def y(maa,j,k):
		maa.j=j
		maa.k=k
		maa.l=j**k
		print(maa.l)

xx=kumar(1,2,13,4)
#print(xx.c)
print(xx.i)
xx.x(5,6)
#print(xx.f)
xx.y(4,6)
#print(xx.l)'''





'''
class x:
	def __init__(self,a):
		self.a=a
		z=1
		while z<=10:
			print(z*a)
			z+=1

	def first(self,b,c):
		self.b=b
		self.c=c
		self.d=c*b
		#print("mul : ",self.d)

x1=x(int(input("table number")))
x1.first(4,12)
print(x1.d)'''


#*******************************************************************************************************
#	DATE :-	25-07-2022
#*******************************************************************************************************
'''
create a program in three classes and create two method in each class first
method take a user input and find the factorial and in second method print
any statment
second class first method take two veeriable and perform any airthmetic operations and
second in print any statememt
third class first method in print sum any number by user input in second metthod
take two arguments and perform any airthmetic operator
'''

'''class grandent():
	def first(self):
		a=int(input("enter"))
		fact =1
		for i in range(1,a+1):
			fact=fact*i
		print("factorial","=",fact)


	def second(self):
		print("\nfailure is the part of succses")

class parents(grandent):
	def third(self,d,e):
		self.d=d
		self.e=e
		self.f=d+e*d

	def forth(self):
		print("\nbelive your self")


class child(parents):
	def fifth(self):
		j=int(input("enter a number"))
		k=0
		for i in range(1,j+1):
			k+=i
		print("summ of :",k)

		#self.m=j+k

	def sixth(self,p,q):
		self.p=p
		self.q=q
		self.r=p**q


x=child()
x.first()
#print("\nfactoral :",x.c)

x.second()
x.third(8,6)
print("simplification :",x.f)

x.forth()
x.fifth()
#print("\nsumm : ",x.m)
x.sixth(3,3)
print("exponents : ",x.r)

'''








'''
n=int(input("enter"))
fact =1
for i in range(1,n+1):
	fact=fact*i
print("factorial","=",fact)

'''
'''x=int(input("enter a number"))
y=1
z=0
while x>y:
	print(y)
	y+=1
#print("sum of all :",z)
	z+=y
print("sum of all :",z)'''


#**************************************************************************************
# 		next type of multipule inheritance
'''
class parent_1:
	def first(self):
		print("principeles")

class parent_2:
	def second(self):
		print("good morning")

class child(parent_1,parent_2):
	def third(self):
		print("welcome to my pc")

x=child()
x.first()
x.second()
x.third()'''


'''
make three class with the help of multipule inhertitance and make two method in
each class perform any airthmetic operator and print any statement in each classes
'''

'''
class parent_1:
	def __init__(self,a,b):		# this program is completed
		self.a=a
		self.b=b
		self.c=a+b

	def first(self):
		print("honesty is the best policy")

class parent_2:
	def __init__(self,d,e):
		self.d=d
		self.e=e
		self.f=d*e

	def second(self):
		print("i like mangoes")

class child(parent_1,parent_2):
	def __init__(self,a,b,d,e,g,h):
		parent_1.__init__(self,a,b)
		parent_2.__init__(self,d,e)
		self.g=g
		self.h=h
		self.i=g**h

	def third(self):
		print("hii this is prince here")

x=child(4,6,5,8,7,3)
x.first()
x.second()
x.third()

print(x.c)
print(x.f)
print(x.i)'''


#**********************************************************************************************************************
#		DATE 26-07-2022
#*********************************************************************************************************************

'''
create  three classes and use multilevel inheritance in this program and use __init__
constactor and super function in this program perform any airthmetic operation in all
classes
'''
'''
class parents:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a+b

	def first(self):
		print("try yourself")

class child:
	def mul(self,d,e):
		self.d=d
		self.e=e
		self.f=d*e

	def sec(self):
		print("congratulation prince")

class prince(parents,child):
	def __init__(self,a,b,g,h):
		super().__init__(a,b)
		self.g=g
		self.h=h
		self.i=g**h
	def third(self):
		print("hello world")


x=prince(12,8,3,4)

print(x.c)
print(x.i)

x.mul(8,5)
print(x.f)
x.first()
x.sec()
x.third()'''


'''
class prince:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a+b

class kr:
	def __init__(self,d,e):
		self.d=d
		self.e=e
		self.f=d*e

class sharma(prince,kr):
	def __init__(self,a,b,d,e,g,h):
		prince.__init__(self,a,b)
		kr.__init__(self,d,e)
		self.g=g
		self.h=h
		self.i=g-h

x=sharma(4,5,3,6,9,8)
print(x.c)
print(x.f)
print(x.i)
'''


'''
class prince:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a/b

class kr:
	def mod(self,d,e):
		self.d=d
		self.e=e
		self.f=d%e

class sharma(prince,kr):
	def __init__(self,a,b,d,e,g,h):
		super().__init__(a,b)
		super(). mod(d,e)
		self.g=g
		self.h=h
		self.i=g**h

x=sharma(45,5,19,4,6,3)
print(x.c)
print(x.f)
print(x.i)'''





'''
class x1:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a-b+b+8

	def first(self):
		print("hii  i a prince kr")

class x2:
	def __init__(self,d,e):
		self.d=d
		self.e=e
		self.f=d**e

	def second(self):
		print("honesty is the best policy")

class x3:
	def __init__(self,g,h):
		self.g=g
		self.h=h
		self.i=g+h*g/2

	def third(self):
		print("we all are indian")

class prince(x1,x2,x3):
	def __init__(self,a,b,d,e,g,h,j,k):
		x1.__init__(self,a,b)
		x2.__init__(self,d,e)
		x3.__init__(self,g,h)
		self.j=j
		self.k=k
		self.l=j%k
	def forth(self):
		y=int(input("table :"))
		for i in range(1,11):
			print(f"{y} x {i} = {y*i}")

x=prince(4,3,2,6,45,15,27,4)
print("substact :",x.c)
print("exponent :",x.f)
print("addition :",x.i)
print("modules :",x.l)
x.first()
x.second()
x.third()
x.forth()'''



'''
Q1. create three classes with the help of multipule inheritanceand make a two method
each class and use init function in each class and use super function as per your
requirmentin first take two arguments and perform any airthmetic operator and
second method print a list with the help of while loop
second class take argumment print any arithmetic operation and second print a dictionary
with the help of loop
third class in take two argumment and perform any airthmetic operator and second
in take user input and print a table.
'''

'''
class c1:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a+b
	def first(self):
		list1=[]
		for i in range(10):
			list1.append(i)
		print(list1)

class c2:
	def __init__(self,d,e):
		self.d=d
		self.e=e
		self.f=d-e
	def second(self):
		x1={
		"ram":"sita","mohan":"mira","mother": "father","up":"down"
		}
		for i in x1.keys():
			print(i,end=" ")

class prince(c1,c2):
	def __init__(self,a,b,d,e,g,h):
		c1.__init__(self,a,b)
		c2.__init__(self,d,e)
		self.g=g
		self.h=h
		self.k=g**h

	def third(self):
		l=int(input("table :"))
		for m in range(1,11):
			print(m*l)

y=prince(4,5,6,9,7,3)
print(y.c)
y.first()
print(y.f)
y.second()

print(y.k)
y.third()'''

'''
Q2. create two class first paarents class and second child class and do single level
inheritance use init and super function
first class in first method do caluculation in first method and second in do any
2nd class first method do caluculation and second do anything
'''


'''class parents:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a+b*a/b
	def first(self):
		print("we feel happy when you stay with me")
class child(parents):
	def __init__(self,a,b,d,e):
		super().__init__(a,b)
		self.d=d
		self.e=e
		self.h=d//e
	def second(self):
		print("i want to spend with you mom every time")


x=child(14,7,67,12)
print("simplification :",x.c)
x.first()
x.second()
print("floor division :",x.h)	'''

'''
Q3. create two class and make two methods in first class print a list with the help
of while loop and second method find modules.
in second class create three methods in first
method print this string in lower case"ARUNACHAL PRADESH", in second method print a
tuple in reverse order. and  in third method print a table  of any random number
use __init__ function and super() as per your requirments.
'''

'''class parents:
	def first(self):
		list1=[]
		x1='ram','mohan','sita','gita','prince',4,34,45.6
		y=0
		while len(x1)>y:
			list1.append(x1[y])
			y+=1
		print(list1)


	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a%b

class child(parents):
	def second(self):
		x2="ARUNACHAL PRADESH"
		y1=x2.lower()
		print(y1)

	def third(self):
		x3=("sunday","monday","tuesday","wednesday","thursday")
		x4=list(x3)
		x4.reverse()
		x3=tuple(x4)
		print(x3)

	def __init__(self,a,b,d):
		super().__init__(a,b)
		self.d=d
		for i in range(1,11):
			print(f"{d} x {i} = {d*i}")

x=child(23,4,12)
x.first()
print("modules :",x.c)

x.second()

x.third()'''

#print(f"{d}x{i}={x.d*i}")


'''
Q4. create two class make two methods in first class, in first method find the
person is eligible for vote or not , in second method find the exponent, and
2nd class print the statement "Honesty is the best  policy",in first method and
second method in do any caluculation
as u want u can use __init__ and super()super function as per you requirment.
'''
'''class parents:
	def first(self):
		age=int(input("if age is :-"))
		if age>=18:
			print("\n\t\t\teligible for vote")
		else:
			print("\n\t\t\tnot eligible for vote")

	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a**b

class child(parents):
	def second(self):
		print("\n\t\t\tHonesty is the best policy")
	def __init__(self,a,b,d,e,f,g):
		super().__init__(a,b)
		self.d=d
		self.e=e
		self.f=f
		self.g=g
		self.h=d+e-g*f/d

x=child(5,4,12,20,40,8)
x.first()
x.second()
print("\n\t\t\texponent :",x.c)
print("\t\t\tsimplification :",x.h)		'''


#**************************************************************************************************************
'''
class q1:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a+b
	def first(self):
		for i in range(10):
			for t in range(1,i):
				print("*",end=" ")
			print()

class q2:
	def __init__(self):
		w=[5,7,8,9,6,2,4,16,5,1]
		w.sort()
		print(w)

	def second(self):
		p=34
		r=26
		self.i=p+r

class prince(q1,q2):
	def __init__(self,a,b,d,e):
		q1.__init__(self,a,b)
		q2.__init__(self)
		self.d=d
		self.e=e
		self.f=d-e

	def third(self):
		n=["prince1","kumar","sharma"]
		#n[0]="mamta"
		n.insert(1,"devi")
		n.insert(0,"mamta")
		print(n)

x=prince(3,4,12,10)
print(x.c)
x.first()
x.second()
print(x.i)
print(x.f)
x.third()'''

#****************************************************************************************************
#		DATE 27-07-2022
#****************************************************************************************************
						  # polymorphism in oops

'''class parrot:
 	def fly(self):
 		print("parrot can fly")
 	def swim(self):
 		print("parrot can't fly")


class pegwin:
	def fly(self):
		print("pegwin can't fly")

	def swim(self):
		print("pegwin can swim")

def flying_test(self):
	self.fly()
	self.swim()

bird=parrot()
peggy=pegwin()

flying_test(bird)
flying_test(peggy)'''


'''
create two classes and use polymorphism in these classes , in class make two method
in ,first
method do any caluculation and in second method print any statement. for both classes
'''
'''class math:
	def add(self,a,b):
		self.a=a
		self.b=b
		self.c=a+b

	def first(self):
		print("hello world")

class math2:
	def add(self,d,e):
		self.d=d
		self.e=e
		self.h=d-e

	def first(self):
		print("welcome to this world")

def math_test(self):
	self.add(2,3)
	self.first()

x=math()
y=math2()

math_test(x)
math_test(y)
print(x.c)
print(y.h)
'''


'''
create three classes and use polymorphism in these classes, in each class
make two methods, iin first in do any caluculation and  second in print
any statement for both classes'''
'''
class A:
	def x1(self,a,b):
		self.a=a
		self.b=b
		self.c=a**b

	def x2(self):
		print("today is wednesday")
class B:
	def x1(self,d,e):
		self.d=d
		self.e=e
		self.f=d+e

	def x2(self):
		print("this month is july")

class C:
	def x1(self,g,h):
		self.g=g
		self.h=h
		self.i=g**h

	def x2(self):
		print("tommorow is thursday")
def math_test(self):
	self.x1(6,3)
	self.x2()

y1=A()
y2=B()
y3=C()

math_test(y1)
math_test(y2)
math_test(y3)
print(y1.c)
print(y2.f)
print(y3.i)'''

'''
create two classes and make two methods in each class. in first
method do exponent and in second method print any statement
in second class first method print a list with the help of while
loop, and second in do addition method.apply polymorphism in this
program.'''

'''class A:
	def x1(self,a,b):
		self.a=a
		self.b=b
		self.c=a**b

	def x2(self,k,m):
		print("india is my country")

class B:
	def x1(self,i,j):
		pk=[]
		k=[4,5,8,7,6]
		l=0
		while len(k)>l:
			pk.append(k[l])
			l+=1
		print(pk)

	def x2(self,d,e):
		self.d=d
		self.e=e
		self.h=d*e

def math_test(self):
	self.x1(4,3)
	self.x2(2,3)

u=A()
v=B()

math_test(u)
math_test(v)
print(u.c)
print(v.h)'''

# data encapsulation
#encapsulation mean in python describe the concept of building data
#and method within a single units.
#for example when you create a class , it means you are imlemting
#encapsulation a class is an example



'''
class employee:
	def __init__(self,name,salary,project):
		self.name=name
		self.salary=salary
		self.project=project

	def show(self):
		print("name:",self.name,'salary',self.salary)
	def work(self):
		print(self.name, "is working on",self.project)

emp=employee('prince',45000,"deep learning")
emp.show()
emp.work()'''
'''
import datetime
x=datetime.datetime.now()
print(x)	'''

# ************************hw***********************************
#Q1. create three classes and use polymorphism in in these clases
#in each class make two methods in first methods print a list
#with the while loop and second in print any statement, in second
#class do any caluculation in first method print any statement
#in second method as in third classes
'''
class A:
	def x1(self,a,b):
		list1=[]
		k="sun","mon","tues","wed","thu","fri","sat"
		r=0
		while r<len(k):
			list1.append(k[r])
			r+=1
		print(list1)

	def x2(self):
		print("honesty is the best policy")

class B:
	def x1(self,c,d):
		self.c=c
		self.d=d
		self.e=c+d
	def x2(self):
		print("failure is the part of succses")

class C:
	def x1(self,f,g):
		self.f=f
		self.g=g
		self.h=f*g

	def x2(self):
		print("i will be a rich person")

def math(self):
	self.x1(12,8)
	self.x2()

y1=A()
y2=B()
y3=C()

math(y1)
math(y2)
math(y3)

print(y2.e)
print(y3.h)'''



'''
Q2.create three class and use inheritance in this as you want and
in first class perform two method in first method find the factorial
and second in print any statement
in second class first method find the exponent and second method print
one to ten countinig.
in third class create two method in first a dictionary with five elements
and print only values of the dictionary withaout method and second in perform
addition.'''

'''
class A:
	def fact(self):
		a=int(input("enter number"))
		b=1
		for i in range(1,a+1):
			b=b*i
		print("factorial :",b)

	def first(self):
		print("The capital of bihar is patna")

class B:
	def __init__(self,b,c):
		self.b=b
		self.c=c
		self.d=b**c
	def second(self):
		for i in range(1,11):
			print(i)

class C(A,B):
	def __init__(self,b,c):
		super().__init__(b,c)
		myDict={"name": "prince", "age" :24, "gender": "male", "height":5.9}
		print(myDict.values())

	def third(self,e,f):
		self.e=e
		self.f=f
		self.g=e+f

x=C(2,5)

x.fact()
x.first()
x.second()
x.third(25,25)
print("exponent :",x.d)
print("addition :",x.g)		'''


#******************************************************************************************************************
#		DATE 28-27-2022
#******************************************************************************************************************
# Abstract methods
'''
an abstract method is a method that is declear d, but contains no implementation.
abstract classes may not be instantiaated and its abstract  methods must be implemnted
by its subclaesses.
what is abstract base class python?
in python , abstract base classes provide a blueprint for concrete classes.
they don tcontain implementation. instead ,they provide an interface and make
sure that derived concrete are
propeerly  implementated. abstract base classes cannot be '''

'''
from abc import ABC,abstractmethod
class employee(ABC):
	def emp_id(self,id,name,age,salary):
		pass


class employee_1(employee):
	def emp_id(self,id):
		print("emp_id is 12345")

emp1=employee_1()
emp1.emp_id(8)'''

'''
from abc import ABC,abstractmethod
class x(ABC):
	def y(self,name,age,salary):
		pass

class x1(x):
	def y1(self,name,age):
		self.name=name
		self.age=age
		print(self.name, self.age)
w=x1()
w.y1("prince",15)'''






#create a class with the help of abstract method and do multiplication in this program.
'''from abc import ABC,abstractmethod
class prince(ABC):
	def x1(self,a,b):
		pass
class kumar(prince):
	def x2(self,a,b):
		self.a=a
		self.b=b
		self.c=a*b
y=kumar()
y.x2(5,4)
print(y.c)'''

'''
create three classes with the help of abstract method , in second class create two
function , in first function create a set and add two elementes in this set .
in second function print any statement .
in third class first function find the factorial of any random
number, and in second method print any statement'''
'''
from abc import ABC
class prince(ABC):
	def x(self,a):
		pass

class kr(prince):
	def x1(self):
		set1={"ram","mohan","sita"}
		set1.add("mira")
		set1.add("arjun")
		print(set1)
	def x3(self):
		print("belive yourself")

class kr1(prince):
	def x4(self,a):
		self.a=a
		k=1
		for i in range(1,a+1):
			k=k*i
		print("factorial :",k)

	def x5(self):
		print("good morning")

y=kr()
y.x1()
y.x3()
y1=kr1()
y1.x4(int(input("enter any number:-")))
y1.x5()
'''
'''
from abc import ABC
class prince(ABC):
	def x1(self,a,b,c,d):
		pass
class kr(prince):
	def x2(self,a,b):
		self.a=a
		self.b=b
		self.g=a+b
	def x3(self):
		print("Honesty is the best policy but we all are not honest")

class kr1(prince):
	def x3(self):
		k=int(input("enter any nummber"))
		for i in range(1,11):
			print(f"{k} x {i} = {k*i}")

	def x4(self,c,d):
		self.c=c
		self.d=d
		self.h=c**d
ob=kr()
ob.x2(5,6)
print(ob.g)
ob.x3()

ob1=kr1()
ob1.x3()
ob1.x4(3,5)
print(ob1.h)
print("done")
'''



'''from abc import ABC
class main(ABC):
	def x(self,a,b,c,d):
		pass
class prince(main):
	def x1(self,a,b):
		self.a=a
		self.b=b
		self.j=a**b
	def x2(self):
		n=[]
		for i in range(10):
			n.append(i)
		print(n)

class kumar(main):
	def x3(self,c,d):
		self.c=c
		self.d=d
		self.k=c+d
	def x4(self):
		print(f"failure is the part of succses we \nhave to fight against the failure")

y=prince()
y.x1(14,12)
print(y.j)
y.x2()

y1=kumar()
y1.x3(10,24)
print(y1.k)
y1.x4()'''

'''class parents:
	def __init__(self):
		a=5
		b=4
		self.c=a+b
	def y(self):
		print("hii this is prince here")

class child(parents):
	def __init__(self):
		super().__init__()
		d=3
		e=9
		self.f=d*e
x=child()
print(x.c)
print(x.f)
x.y()'''

#multilevel inheritance
'''class grandent:
	def __init__(self):
		print("i love you")


class parents(grandent):
	def __init__(self):
		super().__init__()
		print("i love you too")

class child(parents):
	def __init__(self):
		super().__init__()
		print("i can't leave without you")

x=child()'''


'''class per1:
	def __init__(self):
		print("i like you")
class per2:
	def __init__(self):
		print("but as a friend")
class prince(per1,per2):
	def __init__(self):
		per1.__init__(self)
		per2.__init__(self)
		print("do you like me ")

x=prince()'''


#polymorphism




'''class A:
	def first(self):
		print("you will becoome a powerful")
class B:
	def first(self):
		print(" it is my wish")
class C:
	def first(self):
		print("and will complete this wish")

def prince(self):
	self.first()

x=A()
x1=B()
x2=C()

prince(x)
prince(x1)
prince(x2)'''


#data encapsulation
'''class x:
	def __init__(self,name,age,salary):
		self.name=name
		self.age=age
		self.salary=salary

	def first(self):
		print(f"my name is {self.name}")
	def second(self):
		print(f"my age is {self.age}")
	def third(self):
		print(f"my salary is {self.salary}")
	def forth(self):
		print(f"currently learning python")
y=x("prince",23,34000)
y.first()
y.second()

y.third()
y.forth()'''

#abstractmethod
'''from abc import ABC
class body(ABC):
	def dad(self):
		pass

class prince(body):
	def first(self):
		print("good morning")

class prince1(body):
	def second(self):
		print("good after noon")

x=prince()
x.first()

x1=prince1()
x1.second()'''

#polymorphism
'''class A:
	def one(self):
		print("i want to fly in the sky")
	def two(self,a,b):
		self.a=a
		self.b=b
		self.c=a**b
	def three(self):
		x="iNDIA IS MY COUNTRY"
		print(x.swapcase())

class B:
	def one(self):
		print("but i am trying but i think is so hard")
	def two(self,a,b):
		self.a=a
		self.b=b
		self.c=a+b+a+b+a+b+a+b+a+b
	def three(self):
		x=(1,2,3,4,5,6,7)
		print(x[0:4])

def test(self):
	self.one()
	self.two(5,4)
	self.three()
a1=A()
b1=B()

test(a1)
test(b1)
print(a1.c)
print(b1.c)'''

#abstractmethod
'''from abc import ABC
class main(ABC):
	def IQOO(self):
		pass

class A(main):
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a+b+a*b

class B(main):
	def __init__(self):
		print("i feel very sad because my second grand mother gone")
x=A(5,4)
print(x.c)

y=B()'''

'''class parents():
	def first(self):
		x=["one","two","three","four","five"]
		y=len(x)-1
		for i in range(y,-1,-1):
			print(x[i])

	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a%b

class child(parents):
	def __init__(self,a,b):
		super().__init__(a,b)
		p="ARUNACHAL PRADESH"
		print(p.lower())

	def second(self):
		a=(5,28,25,2,11,9)
		b=list(a)
		b.reverse()
		a=tuple(b)
		print("\nreverse order :",a)

	def third(self,a):
		self.a=a
		z=0
		while z<10:
			z+=1
			print(f"{a} x {z} = {z*a}")
ob=child(39,10)
ob.first()
ob.second()
ob.third(int(input("enter any number: ")))
print("\nmodules :",ob.c)
'''
'''
class India():
	def capital(self):
		print("New Delhi is the capital of India.")

	def language(self):
		print("Hindi is the most widely spoken language of India.")

	def type(self):
		print("India is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def type(self):
		print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
	country.capital()
	country.language()
	country.type()


# Python program showing
# abstract base class work

from abc import ABC, abstractmethod
class Animal(ABC):

	def move(self):
		pass

class Human(Animal):

	def move(self):
		print("I can walk and run")

class Snake(Animal):

	def move(self):
		print("I can crawl")

class Dog(Animal):

	def move(self):
		print("I can bark")

class Lion(Animal):

	def move(self):
		print("I can roar")

# Driver code
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()


# Python program showing
# implementation of abstract
# class through subclassing

import abc

class parent:
	def geeks(self):
		pass

class child(parent):
	def geeks(self):
		print("child class")

# Driver code
print( issubclass(child, parent))
print( isinstance(child(), parent))



# Python program invoking a
# method using super()
import abc
from abc import ABC, abstractmethod

class R(ABC):
	def rk(self):
		print("Abstract Base Class")

class K(R):
	def rk(self):
		super().rk()
		print("subclass ")

# Driver code
r = K()
r.rk()'''
#***************************************************************************************
#		01-08-2022
#************************************************************************************************

'''
Exception Handling

When an error occurs, or exception as we call it ,python will normally stop
and generate an error
message. these exceptions can be handled using the try statement:
the try block lets you test a block of code for errors.
the except block lets you handle the error.
the else block lets you execute code when there is no error.
the finally block lets  you execute code , regardless of the result of the
try -and except block.
'''


#print(x)
'''
try:
	print(x)
except:
	print("x should be defined")'''
'''
x=3
y=0
z=x/y
print(z)'''
'''
try:
	x=3
	y=0
	z=x/y
	print(z)
except ZeroDivisionError:
	print("zero should not be required")
finally:
	print("have a nice day")'''


'''try:
	x=12
	y=4
	z=x/y
	print(z)
except:
	print("okay")
else:
	print("prince")
finally:
	print("good")'''
'''
x=3
y="hello"
z=x+y
print(z)'''

'''
try:
	x=3
	y="hello"
	z=x+y
	print(z)
except:
	print("put intger here")
finally:
	print("have a nice day")'''

#Else block: you can use the else keyword to define  a block of code to be
#executed if no errors were raised:
'''
try:
	print("honesty is the best policy")
except:
	print("every thing is good")
else:
	print("nothing is wrong")'''

'''Finally block:
the finally block , if specified, will be executed regardless if the try block
raises an erroror not'''

'''try:
	print("good morning mom")
except:
	print("everything is good")
else:
	print("nothing is wrong")
finally:
	print("good luck")'''

#take a user input .
#create a program in try block, find the voter is eligible or not.
'''
try:
	age=int(input("enter age:"))
	if age>=18:
		print("voter is eligible for vote")
	else:
		print("voter is not eligible for vote")
except:
	print("please enter correct age in integer")
else:
	print("nothing is wrong")
finally:
	print("create by prince")'''


#take user input
#create a program in try block ,find the odd and even number
'''
try:
	x=int(input("enter a number"))
	if x%2==0:
		print("even number")
	else:
		print("odd number")
except:
	print("enter number correctly in integer ")
else:
	print("nothing is wrong")
finally:
	print("good")'''


'''Raise an exception
As a python you can choose to throw an exception if a condition occurs.
to throw (or raise) an exception, use the raise keyword.
example : Raise an error an and stop the program if x is lower than 0:'''

'''x=-1
if x<0:
	raise Exception("sorry no numbers executed below zero")'''


'''the raise keyword is used to raise an exception .
you can define what kind of error to raise , and the text to print the user.
example
raise a typeerror if x is not an integer:'''

'''a=5
if a%2 !=0:
	raise Exception("the number should't be an odd integer")'''


'''take user input and print any random number of even number or any random number
or any random number of odd number
and show the sum of these even numbers and odd numbers'''
'''
try:
	x=int(input("enter a number"))
	y=0
	z=0
	a=0
	while x>y:
		z+=1
		if z%2==0:
			print(f"even : {z}")
			y+=1
			a+=z
	print(f"sum of {x} even number is: {a}")
except:
	#raise Exception
	print("the number should be in integer")
else:
	print("nothing is wrong")
finally:
	print("good")'''
'''
try:
	x=int(input("enter a number :"))
	y=0
	for i in range(2,(x*2)+1,2):
		print(f"even number :{i}")
		y+=i
	print(f"sum of {x} even number is {y}")
except:
	print("please enter number in integer")
else:
	print(f"everything is okay")
finally:
	print(f"good")'''


'''x=(False,-2,-5)
y=(x,2,7)
print(y)'''
#print("\U0001F917")
#print("\U0001F62A")
'''
try:
	x=int(input("enter a number :"))
	y=x+8-4
	print(y)
except:
	print(f"write number in integer there is something went wrong :")
else:
	print(f"good")
finally:
	print(f"best of luck")'''


#x="123prince"
#raise Exception(f"there is some mistake please care this")


'''try:
	income=int(input("please enter annual income :"))
	if income <=1000:
		tax=(income*10)/100
		print(f"{income} of 10% is {int(tax)}Rupees")
	elif income>1000 and income<2000:
		tax=(income*25)/100
		print(f"{income} of 25% is {int(tax)}Rupees")
	else:
		print("no tax")
except:
	print("enter number is in integer form")
else:
	print("thank you for paying tax")
finally:
	print("best of luck")
'''

#create program to caluculate of income tax by our anual package
'''
try:
	income=int(input("enter amount :"))
	if income<=250000:		#2 lakh 50 thousands
		tax=0
	elif income<=500000:	#5lakh
		tax=(income-250000)*0.10+12500
	elif income<=750000:	# 7 lakh 50 thousands
		tax=(income-500000)*0.15+37500
	elif income<=1000000:	# 10 lakh
		tax=(income-750000)*0.20+75000
	elif income<=1250000:	#12 lakh 50 thousands
		tax=(income-1000000)*0.25+125000
	elif income<=1500000:	#15 lakh
		tax=(income-1000000)*0.30+187500
	else:
		tax=(income-1500000)*0.30+187500
	print("You owe",tax,"Rupees in tax!")
except:
	print("please enter amoount correctly in integer !")
else:
	print("Thank you for paying the tax on time !")
finally:
	print("best of luck for you progress !")
'''

'''
try:
	class main:
		def first(self):
			income=int(input("enter amount :"))
			if income<=250000:		#2 lakh 50 thousands
				tax=0
			elif income<=500000:	#5lakh
				tax=(income-250000)*0.10+12500
			elif income<=750000:	# 7 lakh 50 thousands
				tax=(income-500000)*0.15+37500
			elif income<=1000000:	# 10 lakh
				tax=(income-750000)*0.20+75000
			elif income<=1250000:	#12 lakh 50 thousands
				tax=(income-1000000)*0.25+125000
			elif income<=1500000:	#15 lakh
				tax=(income-1000000)*0.30+187500
			else:
				tax=(income-1500000)*0.30+187500

			print("You owe",tax,"Rupees in tax!")
	class main_1(main):
		def __init__(self):
			super().first()
			try:
				age=int(input("enter age"))
				if age>=18:
					print("Person is eligiable for vote")
				else:
					print("not eligiable for vote")
			except:
				print("please number correctly in integer")
			else:
				print("every thing is good")
			finally:
				print("have a nice day")
	class main_2(main_1):
		def __init__(self):
			super().__init__()
			try:
				x=int(input("enter a number"))
				y=0
				for i in range(2,(x*2)+1,2):
					print(f"even number :{i}")
					y+=i
				print(f"sum of {x} even number is :{y}")
			except:
				print("please enter number correctly")
			else:
				print("thank god every thing is good")
			finally:
				print("thanks for taking the intrest")
	ob=main_2()
except:
	print("please call correctly in lower the class !")
else:
	print("this program is working properly")
finally:
	print("weldone prince")'''

'''
class A:
	def first(self):
		score=map(int,input("enter the score").split())
		x=list(score)
		x.sort(reverse=True)
		print(x)
		print("winner in this team",x[0])
		print("Runner up in this team",x[1])
	def second(self):
		x=int(input("enter number :"))
		y=int(input("enter number :"))
		z=int(input("enter number :"))
		n=int(input("enter number :"))
		list1=[]
		for i in range(x+1):
			for j in range(y+1):
				for k in range(z+1):
					if i+j+k!=n:
						list1.append([i,j,k])
		print(list1)

ob=A()
ob.first()
ob.second()'''

#***************************************************************************
#	date 02-08-2022
#****************************************************************************
'''file Handling

File handling is an important part of any web application
python has several function for creating ,reading,updating and deleting files.

file handling

The key function for working with files in python is the open()function
The open function takes two perameter; filename and mode.
There are four diffrent methods (mode) for opening a file.

"r" - Read - Default value. opens a file for reading ,error if the file does not exists
"a" - append - open a file for appending, creates the file if it does not exists
"w" -write- opens a file for writing,creates the file if it does not exist
"x" - create -creates the specified file return an error

'''
	#syntax
	#	To open a file for rading it is enough to specify
	#	the name of the file:

'''x=open("pri.py","r")
print(x.read())'''

#y=open("prectice.py","r")
#print(y.read())
'''
file=open("pri.py", "r")
print(file.read(15))'''		# its read the charactor of line

'''x=open("pri.py","r")
print(x.readline())		# its print one line in one time
print(x.readline())
'''

'''x=open("pri.py","a")
x.write("\n\nHonesty is the best policy")
x=open("pri.py","r")
print(x.read())
'''

'''x=open("xyz.py","a")
x.write("\n\nHonesty is the best policy")
x.write("i am prince ")
x=open("xyz.py","r")
print(x.read())'''		# its creat a new file with the text

'''x=open("xyz.py","w")
x.write("failure id the part of sucsses")
x=open("xyz.py","r")
print(x.read())	'''	# its replace the file inter the text
'''
x=open("wxyz.py","x")
x=open("wxyz.py","w")
x.write("apple is good for health")
x=open("wxyz.py","r")
print(x.read())'''


'''python delete file

To delete a file , you must import the os  module, and run its os . remove() function()
example
remmove the file"xyz.py":'''

#import os
#os.remove("xyz.py")	# if you want to delete permanenet file then use this method




#x=open("yt.py","r")
#print(x.read())
'''
x=open("wxyz.py","a")
x.write("\nwhat is python ?")
x.write("\npyrhon is a high level interpated oriented language")
x=open("wxyz.py","r")
print(x.read())'''


#***********************************************************************************************************
#	date 	03-08-2022
#******************************************************************************************************************


#import datetime
#x=datetime.datetime.now()
#print(x)

'''delete folder
to delete folder an entire , use the os .rmdir() method:
Example'''
'''import os
os.rmdir("chhotu")
'''
# you can remove only empty folder:


#delete the folder of your your desktop but folder should emepty
#import os
#os.rmdir("killer")
#folder has been deleted from your desktop
'''
import datetime
x=datetime.datetime.now()
print(x)'''

'''some important commands

#cd stand for change directory.
cd.. "come back on c one by one".
cd/.. 'we come back on direct c prompot'
pushd drive_name: "we can change the drive"

pushd D:

popd "we can come back on previous drive"'''

'''
first print amsg in a file with the help of append "a",msg should be
this is my program.
with the help of try  exceeption method ,find the number is even or
odd.'''
'''x=open("abc.py","a")
#x.write("\nthis is my program")
x.write("\nx=int(input('enter a number'))\ny=0\nwhile x>y:\n\tprint(y)\n\ty+=1")
x=open("abc.py","r")
print(x.read())
'''

#take three user input find which one is greater.
'''try:
	a=int(input("enter a number :"))
	b=int(input("enter a number :"))
	c=int(input("enter a number :"))
	if a>b and a>c:
		largest=a
	elif b>a and b>c:
		largest=b
	elif c>a and c>b:
		larget=c
	else:
		largest="all are equall"
	print(largest)
except:
	print("please number in integer form")
else:
	print("proggram is working properly")
finally:
	print("best of luck")'''


'''
with the help of "w" or write(), create a file and print a msg this is my
program and print a
table with the help of while loop, use try and exception block'''
'''
x=open("abc2.py","a")
x.write("\n this is my program")
x=open("abc2.py","r")
print(x.read())
'''
'''try:
	x=int(input("enter a number :"))
	y=1
	while y<10:
		y+=1
		print(f"{x} x {y} = {x*y}")
except:
	x=float(input("enter a number :"))
	y=1
	while y<10:
		y+=1
		print(f"{int(x)} x {y} = {int(x*y)}")
else:
	print("good")
finally:
	print("best of luck for your prectice")
'''
#*********************************************************************************************************
#	Date 04-08-2022
#*********************************************************************************************************

#  	Python Modules

'''What is module?
Consider a module to be the same as a code library

a file containing a set of function  you want to include  in your application

create a moduleto creeate a module just save the code you want in a file the
teh file extaince.py:'''
# how can create a module


'''def a(x):
	print("Hello, "+x)

x=[45,12,78,89,56,23]'''

'''y=[]
while True:
	n=eval(input("enter the number :"))
	y.append(n)
	choice=input("if you want to stop write yes  :")
	if choice=="yes":
		break'''

'''
class A:
	def first(self):
		print("failure is the part of sucsses")
	def second(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		self.d=a+b+c'''
#x=A()
#x.first()


'''per1={
"name":"prince",
"age":45,
"country":"india"
}'''

class gradent:
	def second(self):
		print("python is a deneral object orient high level language")
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		self.d=a+b+c
class parents(gradent):
	def first(self):
		print("Honesty is the best policy")
	def __init__(self,a,b,c,e,f):
		super().__init__(a,b,c)
		self.e=e
		self.f=f
		self.g=e**f

x=parents(12,8,10,4,5)

#print(x.d)


#***********************************************************************************
# some functions
'''abs() function
The abs() function return the absolute the values ot the specified number '''
'''x=-987
print(abs(x))#return the absolute value of the

x=6+56j
print(abs(x))'''


#pow()  function

#x=pow(4,3)
#print(x)		#give his exponent

'''x=pow(3,3,4,5)
print(x)'''
#return the value of 3 to the power of 3 modules 4(same as(2*2*2)%4)

#dir() function



#sorted() function
#the sorted function return a sorted list of the specified iterable object.

#x=['a','c','e','b']
'''x=[45,12,78,45,89,47,15,48,10,23,45]
print(sorted(x))
print(sorted(x,reverse=True))
y=sorted(x)
print(y)
y=sorted(x,reverse=True)
print(y)'''

'''max() function
the max() function  returns the item with the maximum value or the item with
the maximum values'''

#x=[12,45,78,56,89,23,56,48,15,10]
#x=(12,78,45,89,56,23,47,12)
#x=["prince","kumar","sharma"]
#x=("prince","kumar","sharma")
#print(max(x))	# its return highest value of x
#print(min(x))	# its return lowest value of x
#print(f"highest number of x is :{max(x)}")
#print(f"Lowest number of x is {min(x)}")

#import os
#os.remove("pri.py")#it is used to delete the file by name in module function

try:
    for i in range(5):
        print("Welcome this home")
except:
    print("plese write correct word")
else:
    print("good job")
finally:
    print("weldone")































































































































































































































































































