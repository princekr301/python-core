
#print("i am prince")
#print("from bihar")



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
	pri nt("true")


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
# there are type of logical opertor
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

x=int(input("enter a number:- "))
y=1
while x>0:
	y=x*y
print(y)
x-=1






















































































































