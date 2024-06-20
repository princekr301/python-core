
#Variable :- it is a sort name of any values
# or 
#Variable are used to store the data 
#or
#Variable is a container where we store the values.

'''
x = "India"
print(x) 

1. Single Variable 

x = 45
y = 60

2. Multipule Variable

x,y = 45,60

print(x)


Comments :- It is a statement that we want to show
    but don't want to execute in python Code
1. single comments  #
2. Multipule Comments( """      """ or  

'''
#Country

# x = "India"
# print(x)

# x = 1500
# y = 2000

# print(x,y)
# print(y)


# ---------------------------------------

'''Limitation of Variable
1. variable should be start with alphabets
2. Variable cane be alphanumeric (x2)
3. variable is case sencetive
4. Here you can not insert any special charactor
		(@$%^&*)
5. Here you can use (_) under_score in variable
'''
'''
A = "HELLO WORLD!"
print(A)		

b2 = 4561
print(b2)

name = "prince sharma"
print(name)


Country_name = "India"
print(Country_name)
'''


#IndentationError:- 
# It is a extraa space starting of code


# print("Welcome")
# print("Python classes")

# print("Hello world!")


# Additionn, substraction,multiplication,Division

'''
x = 12
y = 40
print(x+y)
print("Add ",x+y)'''


#print the sum of three number that given Below
# x = 45
# y = 60
# z = 80

# a = x+y+z
# print(a)





#print the multiplication of four number
# a,b,c,d = 5,4,8,9

# m = a*b*c*d
# print(m)




# 1.Variable
# 2. commments
# 3. Limitation of variable
# 4. type of variable
# 5. IndentationError

# print("Hello world!")



# x = 10
# y = 20

# m = x * y
# print(m)

'''
Data type:
--------------------------------------------------------------------
1. Numerical Data   :-  1. integer  int,  2. float   3.complex  21j
2. Text type Data   :-  strings   str
3. Sequence Data 	:-   list [] ,tuple  (), range()
4. Mapping Data     :- Dictionary  {key:values}
5. set data         :-  set  {}
6. Boolen Data      :- True, False
7. None				:- None
--------------------------------------------------------------------
x = {key : values}
--------------------------------------------------------------------
list  :- List always written in square bracket
x = ["data","science",343,45.55]

tuple :- Tuple are written in Round Bracket.
x = ("data","science",343,45.55)

range() :- it is used to print the number in a sequence
range(starting,ending,step_size)
range(1,100,2)
set :- set are written in curly bracket.
Dictionary :- dict are written in curly bracket and pair of key and values.
'''

# Numerical Data  

# x = 45

# # How to check the data type
# t = type(x)
# print(t)

# or

# print(type(x))
'''
x = 789
y = 456.89
z = 21j
a = "prince sharma"

print(x)
print(type(x))

print(y)
print(type(y))


print(z)
print(type(z))

print(a)
print(type(a))

'''

# x = "Data Science"
# # How to find the length of the text
# #len()
# print(x)
# print(len(x))


# x = "12000"
# print(len(x))


# x = "10"
# y = "20"

# print(x + y)


# x = "data"
# y = "science"
# print(x+y)

# Forcasting of Data :- 
# It is used to change the data type.


# x = 456
# print(type(x))

# x = str(x) #changed into string
# print(x)

# print(type(x))
# print(x*5)


# x = "125"
# print(type(x))

# # change into float  
# f = float(x)
# print(f)
# print(type(f))


# # change into complex
# c = complex(x)
# print(c)
# print(type(c))



# change in list
# l = list(x)
# print(l)
# print(type(l))

# change in int




# number  to string
# string to number


# x = 1466465
# list
# tuple
# set


# string


#x = 'data analysis'
# x = 456789
# print(x)

# t = tuple(x)
# print(t)

#-------------------------------------------------------

# variables :- it is a sort name of any values.


# comments :-

# limitation of variable :-

# IndentationError :-

# data type 

# Forecasting



# x = "100"
# y = "200"

# a = int(x)
# b = float(y)

# print(x + y)  #100200


# x = "data"
# y = list(x)
# print(y)


# x = 12
# y = 12
# z = x/y
# print(type(z))



# x = 120.789

# print(len(x))



# Operators
'''Types of Operators
---------------------------
1.Airthmatic Operators
2.Assignment Operators
3.Comperision Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
--------------------------------


Airthmatic Operators
--------------------------------
+ : Addition
- : substraction
* : multiplication
/ : Division
% : Modules  :- Its show the reminder
**: Exponentation :- it is used to add the power on number.
//: Floor Division :- It show the values before the decimal.'''


# x = 45
# y = 20

# print("Modules :-",x%y)
# print("The Reminder of ",x,"and",y,"is :",x%y)


# x = 5
# y = 3

# print(x*y)
# print(x**y)


# x = 19
# y = 5
# print(x//y)

#print(19%4)

# x = 13
# y = 7
# z = x%y
# print(type(z))

# x = 100
# y = 7
# z = x//y

# print(z)


# x = 2

# #print(x**4)
# print(3**3)

#--------------------------------
# 2. Assignment Operators
# --------------------------------
# = : Assign        
# ==: equal to 
# != :Not Equal to 
# +=: 			 (or)     x = x + 1
# -=:				 (or)     x = x - 1
# *=:				 (or)     x = x * 1
# /=:				 (or)     x = x / 1


# x = 45
# y = 45

# #Equal
# print(x==y)

# Not Euqal to
# x = 100
# y = 200
# print(x==y)
# print(x!=y)


#Plus equal to  (+=  or x = x + 1)
# x = 50
# x = x + 5
# x+=10  #or x = x + 10
# x+=10
# print(x)


# 3. Comperision Operators
# >  : Greater than
# <  : Less than 
# >= : Greater than equal to 
# <= : Less than equal to 
# == : Equal to 
# != : Not equal to 


# x = 45
# y = 10
# print(x>y)
# print(x<=y)


# x = 100
# y = 100
# print(x==y)
# print(x<=y)

# if____else statement


# if _else  :- it is used to divide
# the data in different different 
# category.



# write a python program to show the number 
# if number is greater than 10 then print 
# Yes else print No


# x = 8
# if x>10:
# 	print("Yes")
# else:
# 	print("No")




# x = 100

# if x>50:
# 	print("Yes it is greater than 50")

# else:
# 	print("It is not greater than 50")




# write a python program to check the Number is 
# even or odd

# x = 11

# if x%2==0:
# 	print("Even Number")
# else:
# 	print("Odd Number")


# write a python program to check 
# Number is odd 
#x = 19

# check the Number is Divisible of 9 or not



x = 40

if x%9==0:
	print("Divisible of 9")


# User input :- it is a input where you enter 
# the values in Outuput screen


# int 
# float
# str

# x = int(input("Enter any Number :-"))

# if x%2==0:
# 	print("Even Number")
# else:
# 	print("Odd Number")



# Write a python program with the help of 
# user input and show the Number is greater 
# than 200 the print "Yes greater than 200"
# else print "Less than 200"


# x = int(input("Enter Number :-"))

# if x>200:
# 	print("Greater than 200")
# else:
# 	print("Less than 200")



# check the text is equal to 
# Delhi then print Yes else print No

# x = str(input("Enter Any text :-"))
# if x=="Delhi":
# 	print("Yes")

# else:
# 	print("No")


# Write a python Program to show the 
# state and Capital According to user input

# x = str(input("Enter the state name  :- "))
# if x=="Bihar":
# 	print("Patna")
# else:
# 	print("Other")

# Logical Operators
# and :- it return True when both condition arer True 
# or :- It return True when at leat one Condition is True
# not :- its reverse the Output of   (and or)


x = 15
y = 10

#print(x>10 or y>15)

# if x>10 and y>5:
# 	print("Both Condition are True")
# else:
# 	print("Wrong Condition")



# write a python Program to check the Number 
# is between 20 to 30 than print "Yes"
# else print "No"
'''
x = 25
if x>20 and x<30:
	print("Yes")
else:
	print("No")

'''

# Write a python Program to check if
# Number is Divisible of 10 or 5 then 
# print Yes else Print No


# x = int(input("Enter Number :- "))
# if x%5==0 or x%10==0:
# 	print("Yes")
# else:
# 	print("No") 




# write a python program to check and compare two
# who is greatest Number.

# x = int(input("enter First Number :-  "))
# y = int(input("enter Second Number :- "))

# if x > y:
# 	print(x,"is Greater than ",y)
# else:
# 	print(y,"is Greater than ",x)


# write a python program to check the number is Divisible
# by 5 and 10.
# x = int(input("enter Number :- "))
# if x%5==0 and x%10==0:
# 	print("Divisible of 10 and 5")

# else:
# 	print("Not divisible")



# write a python program to print the last digit of any number
# if number is odd

# x = int(input())
# if x%2!=0:
# 	print("Last Digit of NUmber :- ",x%10)




# write a python program with the help of user input to check
# if password is Eaual the print "Correct password" else print
# "Wrong Password"

p = 1234

# x = int(input("Enter your pin :- "))

# if x==p:
# 	print("Correct Password")
# else:
# 	print("Wrong Password")


# write a python program to print the discout and Discounted Amount
# if Amount is less 5000 than 20% else 30%

'''
amount = float(input("enter amount :- "))


if amount<500:
	d = amount*0.2
	a = amount-d

else:
	d = amount*0.3
	a = amount-d

print("Discount :- ",d)
print("After Discount :-",a)
'''


# x = int(input("enter Number :-"))

# if x>=1 and x<10:
# 	print("FIrst")

# elif x>=10 and x<20:
# 	print("Second")

# elif x>=20 and x<30:
# 	print("Third")

# else:
# 	print("Forth")



# write a python program to show the Division
# if percentage is greater than equal to 60 then print First Division
# if percetnage is greater than equal to 45 then print Second Division
# if percetnage is greater than equal to 33 then print Third Division
# else print Fail
# per = float(input("enter percentage :- "))

# if per>=60:
# 	div = "First Division"
# elif per>=45:
# 	div = "Second Division"
# elif per>=33:
# 	div = "Third Division"
# else:
# 	div = "Fail"
# print(div)

# per = float(input("enter percentage :- "))

# if per>=60:
# 	print("First Division")
# elif per>=45:
# 	print("Second Division")
# elif per>=33:
# 	print("Third Division")
# else:
# 	print("Fail")

# write a python program with the help of user input
# to check number with three variable 
# who is the greatest Number



# x = int(input("enter first Number :-"))
# y = int(input("enter Second Number :- "))
# z = int(input("Enter third Number :- "))

# if x>y and x>z:
# 	print("Gretest Number :- ",x)
# elif y>x and y>z:
# 	print("Gretest Number :- ",y)
# elif z>x and z>y:
# 	print("Gretest Number :- ",z)

# else:
# 	print("Equal",x,y,z)

#---------------------------------------------------
# ---------------------------------------------------
# Swapping in python
# membership operators
# identity Operators
#---------------------------------------------------


# 1. What is swapping in Python 
# in when we exchage the values to other variable
# that is called swapping in python.


# x = 45
# y = 10

# print("x :-",x)
# print("y :- ",y)


# print("After the Update")


# x,y = y,x

# print("x :-",x)
# print("y :- ",y)


# x = 20
# y = 30
# z = 40
# #-------------------
# x,y,z = z,x,y


# print(x)
# print(y)
# print(z)



# x = 100
# y = 200
# z = 300

 
# x = 300
# y = 100
# z = 200

# x,z = z,x
# y,z = z,y

# print("x",x)

# print("Y",y)

# print("Z",z)


# x,y,z = 10,20,30

# x,z,x = z,x,y
# y=x

# print(x)  #30  20   error



# A,B,C,D = 10,20,30,40
# A = B
# C = D
# A,C,D = B,A,C
# print(A)
# print(B)
# print(D)



# x,y = "59"
# z = 12

# x,y = z,x
# z,x = z,y
# x = y
# print(x)
# print(y)
# print(z)


# x = "sceince"

# print("i" in x)
# print("I" in x)
# print("z" not in x)
# print("s" not in x)


# x = [23,4,5,6,7,8,10]

# check 24 in list or not
# check 10 in list

# Write a python program with the help of user
# input to print
# if name contain a or i then print "Yes"
# else print "No"
'''
x = str(input("Enter Name :-"))
if ("a" in x) or ("i" in x):
	print("Yes")
else:
	print("No")



x = ["Sunday","Monday","Tuesday","Wednesday"]
if "sunday" in x:
	print("Present")
else:
	print("Not Present")


# WRITE A PYTHON PROGRAM TO show THE GRADE
# IF NUMBER IS GREATER THAN 90 THEN PRINT "A+"
# IF NUMBER IS GREATER THAN 80 THEN PRINT "A"
# IF NUMBER RIS GREATER THAN 70 THEN PRINT "B+"
# IF NUMBER IS GREATER THAN 60 THEN PRINT "B"
# IF NUMBER IS GREATER THAN 50 THEN PRINT "C"
# ELSE PRINT "D"


# WRITE A PYTHON PROGRAM TO SHOW YEAR AND LEAP YEAR
# WITH THE HELP OF USER input


x = 10
y = 20
if x>y:
	print(x,"is larger")
elif x==y:
	print("Equal")
else:
	print(y,"Larger")


7.

x = int(input("enter Number :- "))
if x>0:
	print("Positive Number")
else:
	print("Negative Number ")

8.
x = str(input("Enter any alphabets :-"))
if x in ("a","i","e","o","'u"):
	print("Vowel")
else:
	print("Consonents")

# 9. ==  3.

11.


x = int(input("Enter Time In Whole Number :- "))

if x < 1200:
	print("Good Morning")

elif x>=1200 and x<1700:
	print("Good Afternoon")

elif x>=1700 and x<2100:
	print("Good Evening")

elif x >=2100 and x<2359:
	print("Good Night")




x = int(input("Enter Time In Whole Number :- "))

if x < 1200:
	print("Good Morning")

elif x<1700:
	print("Good Afternoon")

elif x<2100:
	print("Good Evening")

elif x<2359:
	print("Good Night")

'''


# x  = "Data science"

# #show the data type of x
# #show the length of the x


# a = len(x)
# print("Length of X :",a)

# b = type(x)

# print("data type of x :",b)


# print("Phone Pay :")
# print("-"*50)

# loc = 1234
# u = 7894

# x = int(input("Enter PIn :- "))

# if x==loc:
# 	print("First PIN is Correct")
# 	y = int(input("Enter UPI Pin :- "))

# 	if y==u:
# 		print("Unlocked")

# 	else:
# 		print("UPI pin is Wrong")

# else:
# 	print("Wrong PIN")








# print("-"*50)
# x = str(input("Name of Borad :- "))
# print("-"*50)

# if x=="bseb":
# 	print("Welcome to Bihar Board!")
# 	print("-"*50)
# 	cl = int(input("Enter Class Number :- "))
# 	print("-"*50)
# 	if cl == 9:
# 		print("Welcome to Class 9th")
# 	elif cl == 10:
# 		print("Welcome to Class 10th")
# 	else:
# 		print("Not Found")

# elif x == "cbse":
# 	print("Welcome to Central Board")
# 	print("-"*50)
# 	cl = int(input("Enter Class Number :- "))
# 	if cl == 11:
# 		print("Welcome to Class11th")
# 		print("-"*50)

# 	elif cl == 12:
# 		print("Welcome to Class 12th")
# 		print("-"*50)

# 	else:
# 		print("Not Found")

# else:
# 	print("You entered Wrong Board")


# print("-"*50)




# #semi final matches
# ind=int(input("india score is:-"))
# aus=int(input("australia score is:-"))

# if ind>aus:
# 	x = "india"
# 	margin = ind-aus
# else:
# 	x = "Australia"
# 	margin = aus-ind
# print(x,"Won the match")
# print(x,"win by ",margin,"run")

# str(input("now second semi final pakistan vs england"))
# pak=int(input("pakistan score is:-"))
# eng=int(input("england score is:-"))

# if pak>eng:
# 	y = "pakistan"
# 	margin = pak-eng
# else:
# 	y = "england"
# 	margin = eng-pak
# print(y,"Won the match")
# print(y,"win by",margin,"runs")




# print("The final match will play with",x,"vs",y)
# finalx = int(input(f" {x} Score is :-"))
# finaly = int(input(f" {y} Score is :-"))

# if finalx > finaly:
# 	winner = x
# 	m = finalx - finaly
# else:
# 	winner = y
# 	m = finaly-finalx

# print("The Winner of the final match is Team",winner)
# print(winner,"won by ",m,"runs")
# print("Congraatulations Team :",winner)




# ind = int(input("enter the Score of India :- "))
# aus = int(input("etner the score of Australia :- "))

# if ind >aus:
# 	w = "India"
# 	m = ind - aus
# else:
# 	w = "Australia"
# 	m = aus - ind
# print("Winner is :-",w)
# print(w,"Won by :",m,"runs")

# pak = int(input("enter the Score of pakistan :- "))
# eng = int(input("etner the score of england :- "))

# if pak >eng:
# 	w2 = "pakistan"
# 	m2 = pak - eng
# else:
# 	w2 = "england"
# 	m2 = eng - pak
# print("Winner is :-",w2)
# print(w2,"Won by :",m2,"runs")


# print("-"*50)
# print(f"The final match between {w} and {w2}")

# print("-"*50)

# x = int(input(f"Score of {w} :"))
# y = int(input(f"Score of {w2} :"))


# if x>y:
# 	win = w
# 	ma = x - y
# else:
# 	win = w1
# 	ma = y - x

# print("-"*50)
# print("final winner is :",win)
# print(win,"Won by :",ma)

#------------------------------------------------
#    strings
#------------------------------------------------


# Data type :-

# 1. Numerical
# 2. text
# 3. Sequence
# 4. Mapping
# 5. set
# 6. Boolen
# 7. None


# numrical :- float,complex int
# sequence : - list range() tuple
# boolen :- True False
# mapping :- Dictionary



# int :- whole Number 

# float :-  decimal
# complex:-34j


# list :- list are written in square bracket
# tuple :- tuple are written in round bracket 




# operators :
# 1. Airthmatic
# 2. Assignment
# 3. Comperision
# 4. membership
# 5. identity
# 6. Logical
# 7. Bitwise


# or :- Logical

# += Assignment

# is :- identity

# not in :- membership




# x = 45
# y = 45

# print(x is y)





# find the Area of Circle :
# r = 7
# pie = 22/7

# area = pie*r**2

# #show the average of first five Number

# x = 1+2+3+4+5
# print(x/5)


#string :- it is always written dual qutation or single qutation

# x = "4546#$%%%$"
# print(x)

# print(type(x))

# print(len(x))


# x = "data science"

# -----------------------------------------------
# Strings function
#-----------------------------------------------
# x = 'prince'
# if x == "PRINCE":
# 	print("yes")
# else:
# 	print("No")


# upper :-it is used to convert the text in capital letter
# lower :- it is used to convert the text in small letter
# title :- it is used to capitalize the first alphabets of text

# capitalize :- convert first alphabet in capital letter 

# upper
# x  = "Patna"
# x = x.upper()
# print(x)


# # lower
# x = "DELHI"
# x = x.lower()
# print(x)


# # title
# x = "delhi"
# x = x.title()
# print(x)


# x = "prince sharma"
# y = x.title()
# z = x.capitalize()

# print("title :- ",y)
# print("capitalize :- ",z)


#write a python program to check the text is equal or not

# x = "science"
# y = "scIENCE"


# if x==y.lower():
# 	print("Yes")
# else:
# 	print("No")



# x = str(input("Enter Any Name :-  ")).title()

# if x == "Rohit":
# 	print("Yes")

# elif x == "Ranjan":
# 	print("Yes")

# else:
# 	print("No")



# swapcase :- 

# x = "scIENCE"

# x = x.swapcase()
# print(x)


# print("-"*50)

# Code	Result	Try it
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed


# -------------------------------------------
#   strings :- it is written in single quatation or dual quatation 
# x = "345345"
# print(type(x))
# print(len(x))
# -------------------------------------------------------------


# string function 

# 1. upper :- CONVERT IN CAPITAL LETTER

# x = "prince"
# y = x.upper()
# print(y)


# 2.lower :- convert in small letter
# x = "DATA SCIENCE"
# y = x.lower()
# print(y)


# 3.title :- 

# x = "pRINce kuMAr sharMA"
# y = x.title()
# print(y)

# 4.capitalize :-
# X = 'PRINCE KUMAR SHARMA'
# a = X.capitalize()
# print(a)

# 5. swapcase :- 
# x = "pRInCE"
# y = x.swapcase()
# print(y)


#----------------------------------------
# Indexing :- it show the  position of each alphabet 
# Slicing :-


# x = "D  E  L  H  I"
# 	   0  1  2  3  4   :- Positive Indexing
# 	  -5 -4 -3 -2 -1	 :- Negative Indexing

# x = "himachal"

# #extract "m" form text

# print(x[2])

# print(x[4])


# x = "Arunachal Pradesh"

# Extract :-
# Positive Indexing
# r
# a
# A
# P
# h

# Negative Indexing
# e
# s
# d
# P

# ------------------------------------------------------------------------
# indexing :- it is used to extract the single alphabet from the text.
# ------------------------------------------------------------------------
# Slicing :- it is used to extract the range of charactor from the text.
# ------------------------------------------------------------------------

x = "Airthmatic"
# Slicing
#x[starting position : ending position : step size]
# print(x[0:3])
# #mat
# print(x[5:8])
# print(x[0::1])

# x = "himachal pradesh"
# mach
# desh
# him
# mac
# rade
# # step size 
# mca
# x[2:7:2]
# hmca
# x[0:7:2]
# aap
# x[3:10:3]

# x = "haryana"
# # Negative Slicing
# rya
# na
# arya
# hary

# # x = "h  a  r  y  a  n  a"
# # 	-7 -6 -5 -4 -3 -2 -1  Negative index

# x[-5:-2]  #rya
# x[-2:]    # na
# x[-6:-2]
# x[-7:-3]

#x = "himachal Pradesh"
#x = "Delhi"

#output :- ihleD
# reverse the text with the help of slicing

#x = "Arunachal pradesh"

# 1. arun  X[0:4]
# 2. anu   X[4:1:-1]
# 3. nac   X[3:6]
# 4. can    X[5:2:-1]
# 5.pradesh  X[-7:]
# 6.hsedarp  X[-1:-8:-1]
# 7. runa	   X[1:5]
# 8. anh		X[0:8:3]
# 9.hna       X[6::-3]
# 10.DESH    X[-4:].upper()

#--------------------------------------------------------
x = "data analyst"

# show the index of space

# index() :- it is used to show the position or index of alphabet
# find()  :- same

# a = x.index(" ")
# print("Index of space : ",a)
# print(f"index of space : {a}")


# x = "data analyst"

# y = x.index("a")
# print("First a :-",y)


# a2 = x.index("a",y+1)
# print("Second a :-",a2)

# a3 = x.index("a",a2+1)
# print("Third a :",a3)


# a4 = x.index("a",a3+1)
# print("Forth index :-",a4)


# find the position of 3rd a and 4th a



x = "india"

# Second value of i

# i2 = x.find("i",x.find("i")+1)
# print(i2)

x = "data analysaat"

# count total Number of a from the text.

# count() :- it is used to count the particular 
# 			alphabet from the text.


# y = x.count("a")

# print("total Numeber of a :",y)

# --------------------------------------------
# x = "Arunachal"
# #1. count total Number of a
# x = x.lower()  # aruncahal
# a = x.count("a")
# print("Total NUmber of a :",a)







# x = "python is A Programming LAnguage"
# # 2. count total length without space
# # a = len(x)-x.count(" ")
# # print("Length without space :",a)



# # 3. count total number of a and p
# x = x.upper()
# a = x.count("A") + x.count("P")
# print("Total Number of A and P :",a)




# # 4. Extract the first five alphabet form the text.
# a = x[0:5]

# print("First FIve Alphabet : ",a)
# # 5. Extrac the last 3 alphabet from the text.
# b = x[-3:]
# print("Last three alphabet : ",b)


# replace :- it is used to replace the value 
# from old text or alphabet to new text or alphabet.

# x = "data analyst"
# y = x.replace("at","*")
# print(y)

# x = "python is a program"
# y = x.replace(" ","")
# print(len(y))


# split :- it is used to convert string to list base 
#        of a delimiter

# x = "python is a Programming language"

# y = x.split(" ")

# print(y)
# print(type(y))



# join :- it is used to convert the list to string
# x = ['python', 'is', 'a', 'Programming', 'language']
# print(x)
# print(type(x))

# print("-"*60)

# y = ",".join(x)

# print(y)

# print(type(y))





# x = ["a","b","c"] # to "abc"
# print(x)
# print(type(x))


# y = "".join(x)
# print(y)


# x = ["a","b","c"]
# y = ",".join(x)
# print(y)


# strip :- it is used to delete the extra space from 
#			starting and ending of the text.


# x = "         data sciene        "

# print(x)

# y = x.strip()
# print(y)

x = "science"


# format :- it is used to feel the values according to position

# x = "Hello {}"

# y = x.format("Good Morning")
# print(y)

# x = "Hii {} My name  is {} i am {} old"

# y = x.format("good morning","prince sharma",25)
# print(y)


#startswith :- it is used to check the first alphabet from the text.
# x = "rohit sharam"
# y = x.startswith("r")
# print(y)

# if name start with r then print yes else print no

#x = input().lower()
# if x.startswith("r"):
# 	print("Yes")
# else:
# 	print("No")


# endswith :- it is used to check the last alphabet ends with 
# particular alphabet or not

# write a python program to check if name endswith r and a then 
# print the name else print "not found"

# x = str(input("Enter any Name:- "))
# if x.endswith("a") or x.endswith("r"):
# 	print(x)
# else:
# 	print("Not Found")





# capitlize the first and last alphabet in capital 
#  letter.

# x = "india"

# x = x.title()
# print(x)

# a = x[0:-1]
# b = x[-1].upper()
# print(a+b)


# x = "brillica"

# # reverse the string
# print(x[-1::-1])

# # print first and last aplphabet from the text
# print(x[0]+x[-1])

# # count total number of i

# y = x.count("i")
# print("Total Number of i :",y)


#  find the length of the text without "i"

#replace   #len





x = "python is an object oriented programming language"

# Reverse this text

# Expected Output :-
# language programming oriented object an is python

# x = x.split(" ")
# a = x[-1::-1]
# a = " ".join(a)
# print(a)

 

# isupper :-
# islower
# isdigit
# isdecimal
# isalpha()
# isalnum()
# isspace()
# istitle()


# x = "data"
# y = x.isupper()
# print(y)


# print(x.islower())

# x = "10a"
# print(x.isdigit())


# x = "@#$234dfsd"
# print(x.isalnum())

# x = " "
# print(x.isspace())

# x = "Prince Kumar sharma"
# print(x.istitle())

# x = "1"
# print(x.isdecimal())





# x = "34534d"

# y = int(x)
# print(y)
# print(type(y))


# 1. write a python program with help of user input
# to check the text is in capital or not

# x = str(input("Enter Text :-  "))
# if x.isupper():
# 	print("Yes")
# else:
# 	print("No")


# 2. Write a python program with help of user input
# 	to print yes if first alphabet of name is upper else print no
# x = str(input("Enter Text :-  "))
# if x.isupper():
# 	print("Yes")
# else:
# 	print("No")


# 3. write a python program with the help of user input
# 	to print the first 3 aplphabet in capital letter
# 	if length of text is greater than 5

# x = str(input("Enter Text :-  "))
# if len(x)>5:
# 	print(x[0:3].upper())





# 4. create a program to print the data type of text or number
# if input is digit then print number
# if input is space then print space
# if input is text then print text
# if input is special charactor then print special charactor


# x = str(input("Enter any text : "))

# if x.isdigit():
# 	print("Number",x)

# elif x.isspace():
# 	print("Space",x)

# elif x.isalpha():
# 	print("Text",x)

# elif x.isalnum():
# 	print("Text or Number or both",x)

# else:
# 	print("special Charactor",x)



# --------------------------------------------------------------------------

# x = "brillica"

# y = x.replace("i","")
# print(len(y))




# Loop :- loop are used to run the set of statement.
# 	 :- 	Block of Code


# type of loop
#  1 while loop
#  2.for loop
#  3. Nested Loop


# while loop :- it is used to iterate the set of statemnet
#				for infinite time.



# x = 20
# while x>1:
# 	print("Hello World")
# 	print(x)
# 	x-=1



# print the name 10 times

# x = 10
# while x>0:
# 	print("Prince sharma")
# 	x-=1


# x = 10
# y = 0
# while x > y:
# 	print("Data science")
# 	y +=1



# x = 10
# while x>0:
# 	print("Yes")
# 	x = x - 1



# print the counting from 1 to 50 with the help of while loop


# x = 1
# y = 51

# while x < y:
# 	print(x)
# 	x+=1



# print counting from 10 to 40
# print backward counting from 30 to 1
# print counting with the help of user input to print the counting



# x = int(input("Enter Any Number : "))+1
# y = 1
# while x>y:
# 	print(y)
# 	y+=1


# x = int(input("Enter Any Number : "))
# y = 0
# while x>y:
# 	print(x)
# 	x-=1


# print table of 5



# x  = 5
# y = 51
# while x<y:
# 	print(x)
# 	x+=5


# z = int(input("enter any table Number :- "))
# x = 11
# y = 1

# while x>y:
# 	print(y*z)
# 	y+=1


# x = int(input("enter table name :- "))
# print("-"*70)
# y = 1

# while y<11:
# 	print(f"{x} X {y} = {x*y}")
# 	y+=1



# print hello world 15 times
# x = 15
# y = 0
# while x > y:
# 	print("Hello world!",y)
# 	y+=1

# print counting from 40 to 50
# x = 40
# y = 50

# while y >= x:
# 	print(x)
# 	x = x + 1




# print backward Counting from 60 to 40 
# x = 60
# y = 40
# while x>=y:
# 	print(x)
# 	x = x - 1


# x = 15
# while x>1:
# 	print("Hello world")

# 	x-=1

#  even Number   1 to 20

# x = 0
# y = 20

# while y >= x:
# 	print(x,"Even Number")
# 	x+=2

# 31 to 50


# x = 31
# y = 50

# while x<=y:
# 	if x%2==0:
# 		print("Even No :",x)
# 	x+=1

# print all odd number bwtween 1 to 30
# x = 1
# y = 30
# while x<=y:
# 	if x%2!=0:
# 		print("Odd number :- ",x)
# 	x+=1


# print all number from 58 to 89 who is divisible of 7
# x = 58
# y = 89
# while x<=y:
# 	if x%7==0:
# 		print(x)
# 	x+=1



# 1. print all number from 1 to 100 who is
# 	 divisible of 5 and 8

# 2. print all number from 100 to 200 who is divisible of
# 			10 or 5.

# x = 100
# y = 200
# while x <= y:
# 	if x%5==0 or x%10==0:
# 		print(x)
# 	x+=1

# 3. print square value  from 1 to 10

# x = 1
# y = 11
# while x<y:
# 	print(x,"square :- ",x**2)
# 	x+=1

# 4. print all even number from 340 to 300
#-----------------------------------------------------

# 1.find the sum of first 10 number 1 to 10
# 2. Find the average of first 5 number
# 3. Count total Number of even Number from 1 to 25
# 4. Count total Number of odd Number from 20 to 36
# 5. Cuont total number who is divisible of 7 from 1 to 80.


# x = 1
# y = 10
# s = 0
# while y >= x:
# 	#print("Counting : ",x)
# 	s+=x
# 	x+=1

# print("Sum of First 10 Number :-",s)

# # 1--20

# x = 1
# y = 9
# c = 0
# while x <= y:
# 	if x%2==0:
# 		#print(x)
# 		c+=1
# 	x+=1

# print("Total Number of Even Number :- ",c)

#------------------------------------------
#------------------------------------------



# 1.find the sum of first 10 number 1 to 10y

# x = 10
# y = 1
# s = 0
# while x >= y:
# 	print("No. ",y)
# 	s+=y
# 	print(s)
# 	y+=1

# print("sum of first 10 Number :- ",s)


# 2. Find the average of first 5 number


# x = 5
# y = 1
# add = 0
# while x >= y:
# 	add = add + y
# 	y+=1

# avg = add/x
# print("Average of First Five Number :- ",avg)


# 3. Count total Number of even Number from 1 to 25

# x = 25
# y = 1
# c = 0
# while x>=y:
# 	if y%2==0:
# 		#print("Even Number :",y)
# 		c=c+1
# 	y+=1

# print("total Even Number :- ",c)


# 4. Count total Number of odd Number from 20 to 36

# x = 36
# y = 20
# c = 0
# while x>=y:
# 	if y%2!=0:
# 		c+=1
# 	y+=1
# print("total odd number :- ",c)


# 5. Cuont total number who is divisible of 7 from 
# 1 to 80.
# x = 80
# y = 1
# c = 0
# while x>=y:
# 	if y%7==0:
# 		c+=1
# 	y+=1
# print("Divisible of 7 :- ",c)



# statement
# Break :- Break statement are used to Break the loop According
# 			condition.
# Continue :- It is used to skip the number of text according to 
# 			condition.

# x = 10
# y = 1

# while x >=y:
# 	if y==5:
# 		break
# 	print(y)
# 	y+=1


# continue

# x = 10
# y = 0
# while x > y:
# 	y+=1
# 	if y==4 or y==7:
# 		continue
# 	print(y)



# print number from 50 to 80
#  and skip 60 to 70


# x = 80
# y = 49
# while x > y:
# 	y+=1
# 	if y>=60 and y<=70:
# 		continue
# 	print(y)

#-------------------------------------------------------------
# For loop :- it is used to run set of statement.
# 			or
# 			it is used to iterate the block of code



# for variable in range(10):
# 	print(variable) 

#1 to 20
# for a in range(1,11):
# 	print(a)


# 1. print number from 100 to 140

# for i in range(100,141):
# 	print(i)


# 2. print backward Counting from 20 to 10
# for i in range(20,9,-1):
# 	print(i)

# 3. print all even number from 1 to 15
# for i in range(1,15):
# 	if i%2==0:
# 		print(i)

# 4. print all odd number from  25 to 40.

# for i in range(25,41):
# 	if i%2!=0:
# 		print(i)

# 5. print all leap year from 1947 to 2024.
# for i in range(1947,2025):
# 	if i%4==0:
# 		print(i)













# cheak="y"
# while cheak=="y":
# 	try:
# 		print("ıllıllı⭐🌟 R͙e͙s͙u͙l͙t͙ 🌟⭐ıllıllı")
# 		result={
# 		"prince kumar":{"hnd":98,"math":90,"eng":86,"sc":94,"sst":82},
# 		"ankit kumar": {"hnd":88,"math":60,"eng":96,"sc":94,"sst":92},
# 		"manu singh":  {"hnd":79,"math":81,"eng":66,"sc":64,"sst":78},
# 		"kumod kumar": {"hnd":89,"math":91,"eng":56,"sc":54,"sst":68},
# 		"anmol asha":  {"hnd":70,"math":85,"eng":63,"sc":54,"sst":70},
# 		"priya sharma":{"hnd":40,"math":55,"eng":53,"sc":54,"sst":68},
# 		"chhotu kumar":{"hnd":20,"math":35,"eng":53,"sc":24,"sst":18},
# 		"priyanshu kumar":{"hnd":30,"math":35,"eng":35,"sc":46,"sst":59}
# 		}
# 		#if you want to update the marks of student then use this method
# 		#result["prince kumar"]["hnd"]=30
# 		#result["Ankit kumar"].update({"hnd":50})
# 		#result.pop("chhotu kumar") # to delete the marksheet


# 		name=input("Name of student:")
# 		ob_marks=sum(result[name].values())
# 		#per=(sum(result[name].values())/500)*100
# 		per=ob_marks/5	
# 	#print(result["prince"].values())
# 		print(f"Full marks     : 500")
# 		print("Obtained marks :",ob_marks)
# 		print(f"percentage     :{per}%")
# 		if ob_marks>300:
# 			div="First Divison"
# 		elif ob_marks>225:
# 			div="Second Divison"
# 		elif ob_marks>200:
# 			div="Third Divison"
# 		else:
# 			div="Fail"
# 		print(f"Divison        : {div}")
# 	except:
# 		print("please enter student name correctly !")
# 		print("There is no student by this name!")
# 	else:
# 		print("★彡[ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴ ᴅᴇᴀʀ ꜱᴛᴜᴅᴇɴᴛ!]彡★")
# 	finally:
# 		print("★彡[ᴛʜɪꜱ ᴘʀᴏᴊᴇᴄᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ ★ᴘʀɪɴᴄᴇ ᴋᴜᴍᴀʀ★]彡★")
# 	cheak=input("If you want to cheak another student of result then press y  else n :")




x = [45,78,89,56,253,23]
# a = x[-1::-1]
# print(a)
# 1. 253
# x[4]  or x[-2]
# # [45,78]
# x[0:2]
# # [23,253]
# x[-1:-3:-1]
# # [89,78,45]
# x[2::-1]

# # [56,89]
# x[3:1:-1]



x = [45,78,89,56,23,20,100]
#output = [20,23,45,56,78,89,100]


# sort() :- it is used to arrange the data in ascending or 
# 			descending order.


# sorted :-it is used to arrange the data in ascending or 
# 			descending order.


x = [45,78,89,56,23,20,100]


# Ascending order
# x.sort()
# print(x)


# Descending order
# x.sort(reverse=True)
# print(x)


# x = [45,78,89,56,23,20,100]

# # Ascending order
# y = sorted(x)
# print(y)
# print(x)


# # Descending order
# y = sorted(x,reverse=True)
# print(y)



x = [45,89,56,25,41,10,96,35,78]

# 1. arrange the data in ascending order
#x.sort()

# 2. extract the maximum value from the list
# x.sort()
# print(x[-1])


# 3. extract the minimum value from the list
# x.sort()
# print(x[0])


# 4. find the second highest value from the list
# x.sort()
# print(x[-2])

# 5. Show the second lowest value from the list
# x.sort()
# print(x[1])


# 6. show the top 3 number from the list
# x.sort()
# print(x[-1:-4:-1])


# 7.  show the bottom 3 number from the list
# x.sort(reverse=True)
# print(x[-1:-4:-1])




x = [45,89,56,25,41,10,96,35,78]


print(max(x))

print(min(x))























































































# Reverse words in a given String in Python
# Ways to remove i’th character from string in Python
# Find length of a string in python (4 ways)
# Python – Avoid Spaces in string length
# Python program to print even length words in a string
# Python – Uppercase Half String
# Python program to capitalize the first and last character of each word in a string
# Python program to check if a string has at least one letter and one number
# Python | Program to accept the strings which contains all vowels
# Python | Count the Number of matching characters in a pair of string
# Python program to count number of vowels using sets in given string
# Python Program to remove all duplicates from a given string
# Python – Least Frequent Character in String
# Python | Maximum frequency character in String
# Python – Odd Frequency Characters
# Python – Specific Characters Frequency in String List
# Python | Frequency of numbers in String
# Python | Program to check if a string contains any special character
# Generating random strings until a given string is generated
# Find words which are greater than given length k
# Python program for removing i-th character from a string
# Python program to split and join a string
# Python | Check if a given string is binary string or not
# Python | Find all close matches of input string from a list
# Python program to find uncommon words from two Strings





# x = str(input("enter any text :- "))

# # first and last two alphabet should be capital


# a = x[0:2].upper()
# b = x[2:-2].lower()
# c = x[-2:].upper()

# print(a+b+c)







# 1. Write a program to find the given number is positive or negative.
# x = 10
# if x>0:
# 	print("Positive")
# else:
# 	print("Negative")






# # 2. Write a program to find a minimum of three numbers.
# # x = 45
# # y = 30
# # z = 60

# # if x<y and x<z:
# # 	print(x,"is smallest number")
# # elif y<x and y<z:
# 	print(y,"is smallest number")
# else:
# 	print(z,"is smallest number")






# 3. write a program with the help of user input to find index of any alphabet form the Given text.
# x = "himachal Pradesh"

# a = str(input("etner alphabet :- "))

# print("Index number :-  ",x.find(a))








# 4. Write a program to find the sum of three number that is given below.
# x = "78"
# y = "24"
# z = "12"

# x = int(x)
# y = int(y)
# z = int(z)

# print(x+y+z)  # 782412



# 5. Write a python program to find the factorial of any number with the help of user input.

# x = int(input("enter any number :-  "))
# f = 1
# for i in range(1,x+1):
# 	f = f*i
# print("Factorial :- ",f)









# 6. write a python program to print the last two digit of any number with the help of user input.
# x = int(input("enter any number :- "))
# print(x%100)


# 7. write a unit convertor program with the help of two user input. if first input is foot then second input convert to foot if 
# first input id cm then second input convert in centimeter else print Not converted





# 8. Write a python program with the help of user 
# input to check the entered number is three digit number or not ?
# x = int(input("enter any number :- "))
# if x>=100 and x<=999:
# 	print("Yes")
# else:
# 	print("No")
# #----------------------
# y = str(x)
# if len(y)==3:
# 	print("Yes")
# else:
# 	print("No")

# 9. Write a python program to calculate the Actual Amount after discount.
# if amount is greater than 5000 then 30% Discount if amount is greater 
# than 3000 then 20% Discount else 10% Discount.
# x = float(input("enter any Amount :-  "))
# if x>5000:
# 	print(x - x*0.3)
# elif x>=3000:
# 	print(x - x*0.2)
# else:
# 	print(x - x*0.1)



# 10. Find the Middle elements from the string. 

# x = "Chennai"
# y = int(len(x)/2)
# print(x[y])




# 11. Extract all the text from strings given Below
# x = "Welcome to Delhi"
# # 1. come
# # 2. del
# # 3. wloe
# # 4. last four alphabet
# x[-4:]
# # 5. First three alphabet
# x[0:3]



# # 12. Solve all these Questions.
# x = "Losing doesn’t define you. it refines you"
# # 1. Count total Number of "o"
# a = x.count("o")
# print(a)

# # 2. find the length without "n"
# print(len(x)-x.count("n"))

# print(len(x.replace("n","")))


# # 3. Replace "+" at the place of "o"
# # 4. Reverse this text.
# a = " ".join(x.plit()[-1::-1])
# print(a)

# # 5.concatenate this text and "?"
# print(x+"?")

# # 13. Write a python program to print First 10 Natural Number.
# for i in range(10):
# 	print(i)


# # 14. Write a python program to reverse first 10 Even Number.
# x = 20
# while 0<=x:
# 	if x%2==0:
# 		print(x)
# 	x-=1



# # 15. Write a python program to print the square and cube According to 
# #  condition with the help of while loop from 1 to 20.
# # if number is even then print square root of number if number is odd
# #   then print cube of number

# for i in range(1,21):
# 	if i%2==0:
# 		print(i**2)
# 	else:
# 		print(i**3)



# # 17 write a python program to print number from 20 to 60 and skip all number who is divisible of 5 and 3.
# for i in range(20,61):
# 	if i%5==0 and i%3==0:
# 		continue
# 	else:
# 		print(i)


# # 18 Write a python program to count all even number form 100 to 150.
# x = 150
# y = 100
# c = 0
# while x>=y:
# 	if y%2==0:
# 		c+=1
# 	y+=1


# # 19 Find the average of First 20 Number.
# s = 0
# for i in range(1,21):
# 	s+=i
# print(s/20)


# x = 20
# s = 0
# while 0<20:
# 	s+=x
# 	x-=1
# print(s/x)


# # 20 print the table with the help of user input properly.
# x = int(input("Enter table Name :-  "))
# for i in range(1,11):
# 	print(f"{x} X {i} = {x*i}")


# # 21 Define : 
# # 1. Strings
# # 2. List
# # 3. Indentation Error
# # 4. loops
# # 5. variable


#----------------------------------------------------------


# x = input("enter unit convert :- ")
# y = float(input("enter number in inches :- "))

# if x == "foot":
# 	f = y/12
# 	#print(str(f) + " Foot")
# 	print(f"{f} foot")

# elif x =="cm":
# 	c = y*2.54
# 	#print(str(c) + "cm")
# 	print(f"{c}cm")
# else:
# 	print("Invaild Input")


# For Loop


# for i in range(20,31,2):
# 	print(i) 

# x = range(100,49,-1)
# for i in x:
# 	print(i)


# print the number from 10 to 80
# step size should be 5


# for i in range(10,80,5):
# 	print(i)



# Count total number of odd number from 
# 1 to 15

# c = 0
# for i in range(1,16):
# 	if i%2!=0:
# 		c+=1

# print("Total Odd Number :",c)


# write a python program to print the number 
# from 100 to 50 who is divisible of 3 or 7
# and number should  even

# for i in range(100,49,-1):
# 	if i%3==0 or i%7==0:
# 		if i%2==0:
# 			print(i)

#    ------------or----------------
# for i in range(100,49,-1):
	
# 	if (i%3==0 or i%7==0) and i%2==0:
# 		print(i)




#----------------
# Text in Loop
#----------------

# for i in range(10):
# 	print("Hello world!")

# import time

# x = "PriNce"

# for i in x:
# 	print(i)
# 	time.sleep(1)




# x = "prince sharma"
# y = len(x)

# for i in range(y):
# 	print(x[i])


# x = "Kunal"
# y = len(x)  # 5
# z = 0

# while y>z:
# 	print(x[z])
# 	z+=1



# print the number from 20 to 40 and 
# break the number when number is 30


# for i in range(20,41):
# 	print(i)
# 	if i==30:
# 		break


# print counting from the 1 to 10
# but print the number in Horizontally.



# for i in range(1,11):
# 	print(i,end=" * ")
# 	# to print the number horizontally



# x = "prince"
# for i in x:
# 	print(i)

# x = "prince"
# y = len(x)
# for i in range(len(x)):
# 	print(x[i])


# show the index number of each alphabet
# form the text
x = "rohit sharma"

# for i in range(len(x)):
# 	print(x[i],"index number :- ",i)


# show the index number of each alphabet from
# the text in negative index


# y = len(x)
# a = 0
# for i in range(y):
# 	print(x[i],"Negative index :",i-y)

# while y>a:
# 	print(x[a],"  : ",a-y)
# 	a+=1


x = "programming123"
# extract all number from text
# extract all alphabet from the text.
#-----------------------------------
# isdigit
# isalpha
#-----------------------------------
x = "prog3r4a5m6ming123"

# y = 0
# for i in x:
# 	if i.isdigit():
# 		#print(i)
# 		y = y + 1

# print(y)


# print(y)
# print(type(y))
# y = int(y)
# print(y)
# print(type(y))
#---------------------------------------------------------
#---------------------------------------------------------
#10 9 8 7 6 5 

# for i in range(10,4,-1):
# 	print(i,end=" ")


#1 to 20

# for i in range(1,21):
# 	if i%2==1:
# 		print(i)




x = "programming"

# 1. Extract all vowel alphabet.
# a =  ["a","e","i","o","u"]

# for i in x:
# 	if i in "aeiou":
# 		print(i)

# 2. print the alphabet who is repeated more than one time



# x = "programming"

# for i in x:
# 	if x.count(i)>1:
# 		print(i)











# 3. print all even index of value from text

# x = "programming"

# y = len(x)  #12

# for i in range(y):
# 	if i%2==0:
# 		print(x[i],end = "  ")



# x = "PrinceKR"

# for a in x:
# 	if a.isupper():
# 		print(a)



# 1 to 20  square value

# for i in range(1,21):
# 	print(i,"square : ",i*i)


# 1 to 20 :- cube


# 2 = 2*2*2 = 8
# 3 = 3*3*3 = 27


# for a in range(1,21):
# 	print(a,"Cube :",a**3)


x = "prog3r4a5m6ming123"

# extract all number
'''c = 0
for i in x:
	if i.isdigit():
		print(i)
		c+=1
		print("Counting :- ",c)
'''


# find the average of first 10 number
'''
sum1 = 0
for i in range(1,11):
	#print(i)
	sum1 = sum1+i
avg = sum1/i
print("sum of 10 number :-",sum1)
print("Total Number :- ",i)
print("average :-",avg)
'''


x = "p34ert345j4j34534j"

# #1. find the sum of number 
# s = 0
# for i in x:
# 	if i.isdigit():
# 		i = int(i)
# 		s = s + i
# print(s)

# x = "p34ert345j4j34534j"

# a = ""
# b = ""
# for i in x:
# 	if i.isdigit():
# 		a = a + i

# 	elif i.isalpha():
# 		b = b + i

# print(a)
# print(b)

# #-------------------------------------------
#  ---------------    List    ---------------
# #-------------------------------------------
# list :- list always written in square bracket.
# 		list are used to store the multipule value in a single variable.

# # main uses of list
# 1. List are ordered
# 2. list are changable or mutable
# 3. list are indexed
# 4. list allow duplicate values.
# 5. list written in square bracket.
# 6. here you can store the multiple type of data

# ---------------------------------------------------------------
#----------------------------------------------------------------
# Storing the multuple data type of values
# x = [100,"Friday",78.23,45j,True,None,200,855]
# print("List : ",x)
# print("Data Type : ",type(x))
# print("Length of List : ",len(x))


# # string the duplicate values.
# x = [45,45,45,45,4,54,4,54,54,45]
# print(x)



# List Manipulation

x = ["sunday","Monday","tuesday","wednesday","thursday","Friday","saturday"]
#print(x)

# How to delete the value from the list.



# 1. delete the sunday from the list
#x.pop(0)


# x.pop()
# print(x)








# 2. delete the last value from the list.

# 1. pop :- 
# 2. remove :- 

# x.remove("sunday")
# x.remove("Monday")
# print(x)


# 3. del


# x = ["sunday","Monday","tuesday","wednesday","thursday","Friday","saturday"]
# #print(x)
# # 1.pop :-
# # it is used to delete the value from the list
# # with the help of indexing and 
# # by default delete the last value form list.

# x.pop()  # delte the last value
# x.pop(2)  # delte the 2nd index of value
# print(x)


# 2. remove :- its delete the value from list by values


# x = [12,45,78,12,55,45]
# x.remove(78) # delete 78 from list
# print(x)


#3. clear :- its delete all values from the list.

# x = ["prince",78,456,78,89,8,56,56,56]
# print("Before -----------")
# print(x)

# x.clear()

# print("after---------------")
# print(x)


# 4. del :- del is a keyword that is used to delete
# the value according to index and according variable.


#x = [23,45,78,89,56,23,23]

#del x[-1]  # indexing
#del x[0:3]  # slicing

# del x
# print(x)


#  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#-----------------------------------------------------------------------

# 1. ordered
# 2. duplicate allow
# 3. changable
# 4. indexed
# 5. store multipule type of data
# 6. []


# delete

# 1. pop :- 
# 2. remove :- 
# 3.clear :- 
# 4. del :-


# x = [12,45,78,"fri",89,8,"thu",56,62,3,32,"sun"]


# # 1. delete the last value with the help of pop
# x.pop()
# print(x)
# # 2. delete "Fri" with remove
# x.remove("fri")
# print(x)
# # 3. delete first three elements

# del x[0:3]

# print(x)

# # 4. delete  all values from list
# x.clear()
# print(x)

# # 5. delete variable of list
# del x
# print(x)



# How to add the value in a list

# 1. insert :- it is used to add the value accoridng to index number.
# 2. append :- it is used to add the value.
# 3. extend :- it is used to add the multiple value in a list.


# x = [12,45,78,89,23,23]

# x.insert(2,"prince")
# x.insert(0,250)

# print(x)


# append
#------------------------------------------

# x = [12,45,78,89,23,23]

# x.append("ram")
# x.append(4564)
# print(x)


# Extend 
#------------------------------------------


# x = [1,2,3]
# y = [4,5,6]

# x.extend(y)
# print(x)


# x = "prince"
# print(list(x))


# x = [1,2,3,4,5]
# y = [45,34,56,6,77,88,100]
# x.extend(y)
# print(x)




# x = [1,2,3,4,5]
# x.extend(["prince"])

# print(x)


# x = ["virat","rohit","anikul","rakesh"]

# y = [VIRAT,ROHIT,ANIKUL,RAKESH]
# # Create a new list and add all value of x and convert in capital letter.

# for i in x:
# 	i = i.upper()
# 	y.append(i)

# y = []
# for i in range(1,11):
# 	y.append(i)
# print(y)


# x = [45,78,89,56,12,25,47,69,10]

# 1. delete third value 

# 2. add 200 in 2nd index

# 3. add 500 in last of list

# 4. delete 4th and 5th position of value

# 5. add [1,1,1] in list

# 6. add "python " last of list

# 7. delete 89 from list

# 8. delete all vaule from list

# 9. show the length of list

# 10.show the data type of x





















































