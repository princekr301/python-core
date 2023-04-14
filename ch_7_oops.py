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