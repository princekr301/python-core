

#		cheptor:- function in python 

'''
1. What is function?
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



# Two time print hello world
'''
def x():
	print("hello world")

x()
x()

# print one time hello mom

def x():
	print("hello mom")

x()	# it is pass when i will pass then print hello mom


def y():
	print("welcome back")
	print("i m  prince")
y()
y()
y()	'''


# default perameter value by user defined function
'''def fun(name="prince kumar"):
	print("Good morning "+name)
fun()								# Good morning prince kumar
fun("chhotu kumar")	'''				# Good morning chhotu kumar



# note perameter=arrgument

# this is my additonal program
'''
def add(a,b):
	print(a+b)

add(7,5)
add(78,45)'''

#Default function
def add(x=5,y=15):
	print(x+y)

add()
add(45,40)



# this is my simplification program.
'''
def simp(a,b,c,d,e):
	print("this is my simlification =",a+b*c/d-e)

simp(12,20,45,5,10)'''



#write a function two or more aggrument and apply all airthmeric opreration on it.
'''def simp(a,b,c,d,e):
	print(a+b-c*d/e)

simp(41,78,56,14,7)

'''


# create a function with the help of user input.
'''def add():
	a=int(input("enter a number:-"))
	b=int(input("enter a number:-"))
	print(a+b)

add()
add()'''


# apply all method in function by user input
'''def x():
	a= int(input("enter a number: -"))
	b= int(input("etner a number:-"))
	print(a-b)
	print(a*b)
	print(a/b)
	print(a%b)		# modules
	print(a**b)		#exponentation
	print(a//b)		# floor divison

x()'''



#********************************************************************************************************
'''
# perameter or arguments ?
The terms pereameter and argument can be used for the same thing: 
information that are passed into a function.


# From a functions to perspsctive:
A perameter  is the variable listed inside the parentheses in the function
definition.
An argument is the value that is sent to the function when it is two argument.


# Number of arguments
By default , a function must be called with the correct number of arguments.
Meaning that if your functione expects two argument, you have to call he function
with argument,no more ,and not less


# Arbitatry arguments, *args
If you do not know how many arguments that will be passed into your function,
add astrick * before the perameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the 
item in the index:
'''

# arbitatry arguments (*name)
'''def x(*names):
	print("i am a good",names[1])
	print("I am", names[0])
	print("hello dear",names[5])
	print("Good morning",names[3])
	print("I am indian my name is",names[2])
	print("sita is a friend of ",names[1])

x("prince","chhotu","ankit","rani","riya","priyanshu","ankita","manu")
#	 0		  1		   2	  3		  4		  5			  6		 7


def x(*y):
	print("hello",y[0])
	print("good morning",y[1])
	print("i am a",y[2])

x("prince","brother","data scientist","mother")'''


# Keyword arguments
'''You can also send arguments with the key= value syntax
this way the order of the arguments does not matter.'''

'''
def x(name, Age, Class):
	print("My name is ",name)
	print("I am",Class,"with math honors")
	print("I am",Age,"year old")

x(name="prince kumar", Age=22, Class="graduate")



def n(state,dist,post,village):
	print("my state name is",state)
	print("my district name is",dist)
	print("my post office is",post)
	print("i live in",village)

n(village="chakkapar",post="nawada",dist="begusarai",state="bihar")
'''

# Arbitatry keyword Argumetns,	**kwargs
'''if you do not know how many arguments that will be passed into your
function, add two  astrisk ** before the parameter name in the function definition.

this way the function will receive a dictionary of arguments, and can access the
 items accordingly 

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
def p(**j):
	print("we all are",j["name"])
	print("i like",j["food"])
	print("his favorate",j["color"])

p(color="white",name="indian",food="cold coffe")'''


# python *argument
'''def myFun(*argv):
    #print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)
 
 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')'''



# 				///////////*argument//////////////
'''def x(*y):
	for i in y: 
		print("argument throught :",i)
x('hello','prince','i','am','happy')
x("hii","this","is","prince","here")'''

'''def myFun(**kwargs):
	for key, value in kwargs.items():
		#print("%s == %s" % (key, value))
		print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')'''




#  *argument and **kwargument
'''def myFun(**kwargs):
	#print("args: ", args)
	print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun(first="Geeks", mid="for", last="Geeks")'''


'''def x(**a):
	print("a",a)

x(First="prince",second="kumar",third="sharma")'''



'''def x(*a):
	for p in (a):
		print(p)

x("prince","kumar","sharma")'''



#************************************************************************************************************
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



#4.  create a function and make a list with the eight items and remove two items and add
#    only one item on the place of the items without method.


'''
# it is eight list of function
def list(a,b,c,d,e,f,g,h):
# it is a list in eight str
	mylist=[a,b,c,d,e,f,g,h]
# here we removing two str and adding one str on the place
	mylist[0:2]=["prince"]
#  pinting the mylist
	print(mylist)

# passing the arguments in the function
list(a="january",b="february",c="march",d="april",e="may",f="june",g="july",h="august")
'''

#*****************************************************************************************************************************

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
'''function definitions can not be empty, but if you for sume reason have a function
definition
with no content ,put in the pass statement to avoid getting an NameError

def x():
	pass
'''

# Return values
# To let a function return a value , use  the return statements:

'''def x(y):
	return 7*y
print(x(5))


def cv(t,r):
	return 3*t,4*r
print(cv(4,2))


def pk(x,y,z):
	return 4*x,3*y,8*z
print(pk(2,5,8))'''


# Python program to illustrate cube of a number
# showing difference between def() and lambda().


'''def cube(y):
	return y*y*y


def g(x): return x*x*x


print(g(7))

print(cube(5))'''

#  by internet
# A Python program to generate squares from 1
# to 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1
'''def nextSquare():
	i = 1

	# An Infinite loop to generate squares
	while True:
		yield i*i				
		i += 1 # Next execution resumes
				# from this point	

# Driver code to test above generator
# function
for num in nextSquare():
	if num > 200:
		break	
	print(num)'''

'''def x():
	i=1
	while True:
		yield i*i
		i+=1

for y in x():
	if y>150:
		break
	print(y)'''


# python Anonymous / Lambda function

# the anonymous function , also known as lambda function.
'''in puthon , an anonymous function is a function that is defined without a name 

while normal function are defined using the def keeyword in python,
anonymous function are defined using the lambda keyword.

Hence , anonymous  function are also called lambda function.

a lambda function is small  anonymous function.
a lambda function can take any number of arguments , but can only have one expression.
'''
'''
x= lambda a,b:a+b
print(x(45,40))


x=lambda a,b: a*b
print(x(5,6)) 


x=lambda a,b,c:a+b+c
print(x(5,6,4))


x= lambda a,b,c,d:a+b*c/d

print(x(6,8,10,4))


p=lambda a:a
print(p("ram"))


prince= lambda a,s,d,f:a*s-d/f*d+a+s+d+f
print(prince(12,45,78,13))

def x(a,b):
	return 4*a,8*a,7*b
print(x(4,5))				'''


#*************************************************************************************

# python  zip function 
# join two tuple together
# it is used to join list ,set,dict,tuple


'''x=("sun","mon","tue")
y=("wed","thu","fri",)
z=zip(x,y)
#print(tuple(z))
print(list(z))'''

'''
x=("jan","feb","maarch")
y=("april","may","june","july")
z=zip(x,y)
print(list(z))

'''


'''x=["jan","feb","maarch"]
y=["april","may","june","july"]
z=zip(x,y)
print(set(z))'''





'''
x=["jan","feb","maarch"]
y=["april","may","june","july"]
z=zip(x,y)
print(dict(z))
'''


'''x=["prince","ankit","ram"]
y=[4,6,7]
z=zip(x,y)
print(dict(z))	'''	




# Pectice time

#1. create a function and take six argument s and perform any arithmetic operation within a single line

'''x=lambda a,b,c,d,e,f:a+b/c*d+e-f
print(x(12,10,5,10,20,5))
'''
'''
expression
2. create a function with the help of two tuple make a dictionary.
'''
'''x= ("ram","sita","ravan","krishna")
y=("god","devi","evil","avtar")
z=zip(x,y)
print(dict(z))'''

'''
3. create four function and perform arithmetic opreration as want to in each function,
    and call these function is a suffling wayss'''
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
4. create two function and find the 10 even number in the first function and find 10 odd number in functionin a suffling ways.

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
5. create three function and find the 10 whole number do the sum of these whole number in first 
function and find the exponents in second function,

'''
'''
def whole(x):
	z=0
	for y in range(0,x):
		print(y)
		z+=y
	print("sum of 10 whole number is ",z)	

whole(int(input("enter whole number")))
'''
#def x(a,b):
#	return 2**a,3**b
#print(x(2,4))		# it means 2*2=4 and 3*3*3*3=81

#Default function in perameter
'''def fun(a=10,b=23):
	return 2*a,4*b

print(fun())		#(20, 92)
print(fun(5,4))		#(10, 16)'''
