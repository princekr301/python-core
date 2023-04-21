

'''print("hello world!")

from datetime import date
def jk(birthday):
	today=date.today()
	age=today.year-birthday.year-((today.month,today.day)<(birthday.month,birthday.day))
	print(age)
a=int(input("Year:- "))
b=int(input("Month:- "))
c=int(input("Birthday:- "))
jk(date(a,b,c))'''


'''
import random
while True:

	def game(comp,you):
		if comp==you:
			return None
		if comp=="w":
			if you=="s":
				return True
			elif you=="g":
				return False
		elif comp=="s":
			if you=="g":
				return True
			elif you=="w":
				return False
		elif comp=="g":
			if you=="w":
				return True
			elif you=="s":
				return False

	c=random.randint(1,3)
	if c==1:
		comp="s"

	elif c==2:
		comp="w"
	elif c==3:
		comp="g"
	print("computer turns sanke (s) water(w) gun(g) :")

	you=input("your turn choose sanke(s) gun(g) water(w) :")

	a=game(comp,you)
	print("your choose is :", you)
	print("computer chhoice is :",comp)

	if a==None:
		print("game is tie!")
	elif a:
		print("You won the game!")
	else:
		print("You lose the game!")

	x=input("Would you like to exit the game then press yes/No :")
	if x=="yes":
		break
	else:
		continue
'''
'''import time
question="when was python was invented"
print("\n",question)
time.sleep(2)
print("\n\ta==1994\n\tb==1948\n\tc=1991\n\td=None of these")
time.sleep(2)
opt=input("enter option :")
if opt=="a":
	#opt1=wrong_(x)
	print("wrong_(x)")
elif opt=="c":
	#opt1=Correct_(v)
	print("Correct_(t)")
elif opt=="b":
	#opt1=wrong_(x)
	print("wrong_(x)")
else:
	#opt1=wrong_(x)
	print("wrong_(x)")
#print(opt1)'''

'''a,b,c,d=4,5,6,7
print(c)'''
'''input
x={"yellow","green"}
y={"green","black"}
z=x-y
a=y-x
print(z)
print(a)'''

'''Output
{'yellow'}
{'black'}
print(x[0])'''


'''z=x-y
a=y.symmetric_difference(x)
print(a)'''
'''
x=int(input("enter a number:"))
y=2
if y>x:
	print("number is not prime")
elif x==y:
	print("number is prime!")
else:
	while y<x:
		if x%y==0:
			print("number is not prime!")
			break
		y+=1
	else:
		print("number is prime!")
			#print("number is prime!")'''


'''n=int(input("enter a number:"))
c=0
For i in range(1,n+1):
	if n%i==0:
		c=c+1

if n==0 or n==1:
	print("number is not prime !")
elif c<3:
	print("numbmer is prime!")
else:
	print("number is not prime!")'''



'''fruits=["apple","orange","lichi","lemon","plum"]
newlist=[]
For i in range(len(fruits)):
	if fruits[i].startswith("l"):
		newlist.append(fruits[i])
print(newlist)'''

'''fruits=["apple","orange","lichi","lemon","plum"]
newlist=[]
For i in (fruits):
	if i.startswith("l"):
		newlist.append(i)
print(newlist)'''


'''
def cheak(x):
	if x>1:
		For i in range(2,x+1):
			if x%i==0:
				print("number is not prime!")
				break
			else:
				print("number is prime!")
				
			
	else:
		print("number is not prime!")

cheak(int(input("enter a number :")))'''


'''
import random

upper="PRINCEKUMAR"
lower="princekumar"
num="123456789"
log="@#$%&*"

mix=upper+lower+num+log
size=8

password="".join(random.sample(mix,size))
print(password)'''

'''class math:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a+b
	def first(self):
		print("Honesty is the best policy!")
class eng(math):
	def __init__(self,a,b,d,f):
		super().__init__(a,b)
		self.d=d
		self.f=f
		self.g=d-f
	def second(self):
		print("Failure is the part of sucsses!")

h1=eng(12,45,48,20)
h1.first()
h1.second()
print(h1.c)
print(h1.g)'''

'''
class math:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a+b
	def first(self):
		print("Honesty is the best policy!")
class eng:
	def __init__(self,d,f):
		self.d=d
		self.f=f
		self.g=d-f
	def second(self):
		print("Failure is the part of sucsses!")
	def Forth(self):
		print("today  is numpy is completed we all are very happy!")
class main1(math,eng):
	def __init__(self,a,b,d,f,j,k):
		math.__init__(self,a,b)
		eng.__init__(self,d,f)
		self.j=j
		self.k=k
		self.m=j**k
	def third(self):
		print("i love my mother!")

x=main1(12,45,47,41,12,2)
x.first()
x.second()
x.third()
print(x.c)
print(x.g)
print(x.m)
x.Forth()'''

'''x=input("entr first number :")
y=input("enter operator( +,-,*,/,**,//,% ) : ")
z=input("enter the second numner :")
a=float(x)
b=float(z)

if y== "+":
	m=(a+b)
elif y== "-":
	m=(a-b)
elif y=="*":
	m=(a*b)
elif y=="/":
	m=(a/b)
elif y=="**":
	m=(a**b)
elif y=="//":
	m=(a//b)
else:
	m=(a%b)
print(f"The output is {m}")'''
'''
x=int(input("enter the table :"))
y=0
while y<10:
	y+=1
	print(f"{x} x {y} = {x*y}")'''


'''x=int(input("enter number :"))
y=0
z=0
while x>y:
	z+=1
	if z%2==0:
		print(z,"Even number")
		y+=1
x=int(input("enter odd number"))
y=0
z=0
while x>y:
	z+=1
	if z%2!=0:
		print(z,"Odd number")
		y+=1'''


'''x=20
t=0
while x>t:
	print(x)
	x-=1'''

import numpy as np
import pandas as pd
'''class nump:
	def __init__(self):
		x=np.arange(20).reshape(4,5)
		print(x)
		print(np.diag(x))

	def one(self):
		y=np.linspace(40,60,num=15,dtype=int)
		z=y.reshape(5,3)
		print(z)
class pand(nump):
	def __init__(self):
		super().__init__()
		a=pd.DataFrame({"Number":[1,2,3,4,5,6,7,8,9],"name":["one","two","three","four","five","six","seven","eight","nine"]})
		print(a)
	def two(self):
		print("this is my first program from numpy to pandas")
m=pand()
m.one()
m.two()'''

'''x=int(input("enter the number:"))
y=np.arange(1,x+1)
print(np.prod(y))'''

import math
'''print(math.factorial(int(input("enter number of factorial"))))
print(math.sqrt(int(input("enter number"))))
print(int(input('number'))**2)'''

#For i in range(20):
#	print(f"{i} of square root is {(i**2)}")

'''For i in range(201):
	a=math.sqrt(i)
	print(i,"",a)'''
'''
For i in range(1,21):
	print(i,"Table\n")
	For j in range(1,11):
		print(j*i)'''

'''with open("table.txt","a") as f:

	For i in range(1,21):
		#with open(f"cd table table.txt {i}","w") as f:
			For j in range(1,11):
				f.write(f"{i} x {j} = {i*j}\n")'''
				#if f!=10:
					#f.write("\n")
'''
import pandas as pd
with open("pandas.txt","a") as f:
	a={"Company":["HCL","HCL","HCL","LG","LG","MI","MI"],
	"employer":["prince","anshu","Priya","annu","ankit","mayur","mahi"],
	"Profit":[1000,800,600,500,400,1200,200]}
	x=pd.DataFrame(a)
	#print(x)
	y=x.groupby("Company")
	print("describe")
	f.write(f"{y.describe()}")
	f.write(f"{y.describe().T}\n {y.sum()},\n{y.count()}")'''


#Now aggrigating the gruop
'''print("\nsum method with total profit of Company")
print(y.sum())

print("\n minimum profit of company ")
print(y.min())

print("\n mean of company profit")
print(y.mean())

print("\nfind the maximum profit of this company")
print(y.max())

print("\n show how many employer and number of profit")
print(y.count())

print("\n describe the detalis of company")
print(y.describe())'''
import numpy as np
'''
with open("pks.txt","w") as f:
	class  math:
		def __init__(self):
			x=np.linspace(48,200,num=400,dtype=int).reshape(4,10,10)
			f.write(f"{x}")
			print("done")
	a=math()'''
'''
with open("pks.txt") as f:
	p=f.read()
	p=p.replace("mamta devi","prince kumar sharma")
with open("pks.txt","w") as f:
	f.write(p)
	print("done")'''
'''
with open("pandas.txt","a") as f:	
	x=np.array([[[[[[45,78,89,56,461,1,4,49,89,78,56,2315,49,449,65,6,626,65,95,94,1,62,6,]]]]]])
	For i in np.nditer(x):
		f.write(f" {x} ")
		f.write(f" {i} ")
		print("done")'''

'''
x={"prince":{"a":100,"b":200,"c":400}}
#print(x)
#y=x["prince"][sum(values.())]
print(sum(x["prince"].values()))'''


'''with open("prince.xl","a") as f:
	x=int(input("enter a number:"))
	For i in range(1,11):
		print(x*i)
		f.write(f"{x*i}")


x=10
if x==1: print(x)
else: print("hii")'''
import time

#x=int(input("enter the number :"))
#time.sleep(4)
#if x==5: print("hii boy"),time.sleep(5),print("hello guy"),time.sleep(3),print("welcome to this show!")
#else: time.sleep(3),print("good morning dear prince"),time.sleep(3),print("i hope your all are cool"),time.sleep(3),print("how is your classes are going on")


'''x=[]
while True:
	a=eval(input("enter number:"))
	x.append(a)
	b=input("woul you like to stop this list then press 's' or 'stop':")
	if b=="s" or b=="stop":
		break
print(x)'''

'''q=4
x=[]
while q!=0:
	a=eval(input("enter number:"))
	x.append(a)
	b=input("woul you like to stop this list then press 's' or 'stop':")
				if b=="s" or b=="stop":
					break
	q-=1
print(x)'''

'''chances=4
while chances!=0:
	pin=int(input("enter four digit pin :"))
	if pin!=1234:
		print("incorrect pin \nTry again\nEnter correct pin:")
		chances-=1
		print(f"left chances {chances}")

	else:
		print("welcome to this game!")
print("blocked")'''

'''
import time
print("----------------------------------------------------------------")
print("Welcome to the Prince Tutorial!")
print("----------------------------------------------------------------")
time.sleep(2)
print("----------------------------------------------------------------")
print("\nPlease choice which subject do you want to learn\nFor english press == 1\nFor math press == 2\nFor science press == 3\nFor social studies press == 4")
time.sleep(3)
try:
	print("----------------------------------------------------------------")
	x=int(input("\nplease press your choice subject wise :"))
except:
	time.sleep(2)
	print("----------------------------------------------------------------")
	print("\nyou have enterd incorrect input\nPlease try again!")

chance=4
pin=7894
while chance!=0:
	print("----------------------------------------------------------------")
	a=int(input("\nenter four digit student id password :"))
	if a!=pin:
		print("---------------------------------------------------------------")
		time.sleep(3)
		print("\nyou have enterd wrong_id password\nplease enter correct id password!\n")
		chance-=1
		time.sleep(2)
		print("----------------------------------------------------------------")
		print(f"you can try only {chance} times only\n")
		print("----------------------------------------------------------------")
	else:
		if x==1:
			time.sleep(2)
			print("----------------------------------------------------------------")
			print("Wlcome to the english classes!")
			print("----------------------------------------------------------------")
			break
		elif x==2:
			time.sleep(3)
			print("Wlcome to the math classes!")
			break
		elif x==3:
			time.sleep(3)
			print("----------------------------------------------------------------")
			print("welcome to science classes")
			print("----------------------------------------------------------------")
			break
		elif x==4:
			time.sleep(3)
			print("----------------------------------------------------------------")
			print("welcome to social studies classes")
			print("----------------------------------------------------------------")
			break
	if chance==0:
		print("Your student id is Blocked for 30 seconds\nPlease wait 30 seconds")
		def countdown(t):
			while t>0:
				print("Countdown is on : ",t,end="\r")
				t-=1
				time.sleep(1)
			#print("times up")
			print("\nThanks for waiting!")
			time.sleep(3)
			chance=4
			while chance!=0:
				print("----------------------------------------------------------------")
				a=int(input("\nenter four digit student id:"))
				if a!=pin:
					time.sleep(2)
					print("----------------------------------------------------------------")
					print("\nyou have enterd wrong_id password\nplease enter correct id password!\n")
					chance-=1
					time.sleep(2)
					print("----------------------------------------------------------------")
					print(f"you can try only {chance} times only\n")
					print("----------------------------------------------------------------")
				else:
					if x==1:
						time.sleep(3)
						print("----------------------------------------------------------------")
						print("Wlcome to the english classes!")
						print("----------------------------------------------------------------")
						break
					elif x==2:
						time.sleep(3)
						print("----------------------------------------------------------------")
						print("Wlcome to the math classes!")
						print("----------------------------------------------------------------")
						break
					elif x==3:
						time.sleep(3)
						print("----------------------------------------------------------------")
						print("welcome to science classes")
						print("----------------------------------------------------------------")
						break
					elif x==4:
						time.sleep(3)
						print("----------------------------------------------------------------")
						print("welcome to social studies classes")
						print("----------------------------------------------------------------")
						break


		#x=int(input("enter in second in integer :"))
		countdown(30)
'''

'''def countdown(t):
	while t>0:
		print(t,end="\r")
		t-=1
		time.sleep(1)
	print("times up")

x=int(input("enter in second in integer :"))
countdown(x)'''

'''import time
def countdown(t):
	while t:
		mins,secs=divmod(t,60)
		timer='{:02d}:{:02d}'.format(mins,secs)
		print(timer,end="\r") 
		time.sleep(1)
		t-=1
	print("Its time to run!")

t=input("enter the time in second: ")
countdown(int(t))'''

#from datetime import datetime
'''x=input("enter in this format hh:mm:ss \n")
hour=x[0:2]
minute=x[3:5]
second=x[6:8]

print(hour,minute,second)
#time1=(hour:minute:second)
while True:
	now=datetime.now()
	h1=now.strftime("%I")
	m1=now.strftime("%M")
	s1=now.strftime("%S")
	if hour==h1:
		if minute==m1:
			if second==s1:
				print("time to wake up")
		
			break
'''
#-----------------------------------------------------------------------------------------------------------
'''
now=datetime.now()
print(now)

x=time.asctime(time.localtime(time.time()))
print(x)

print(datetime.now())

print(dir(math))

print(dir(datetime))

print(now.strftime("%I:%M:%S"))'''

from datetime import datetime
#x=datetime.now()
#print(x.strftime("this watch is made by prince the time is now\n  %I :%M minute %S second %p \nThanks for watching my time !"))

'''
x=input("enter in this format hh:mm:ss\n")
while True:
	y=datetime.now()
	if x==y.strftime("%I:%M:%S"):
		print("its time to wake up")
		break'''

#print(datetime.now())


'''
x={1:{"math":89,"snk":78,"music":45,"hnd":78,"eng":80}}
print(x)
try:
	h=eval(input("enter roll number :"))
			#print("Not result found")
	y=x[h].values()
	print(y)
	z=sum(y)
	if h==1:
		print("Name :-prince kumar")
	elif h==2:
		print("Chhotu sharma")
	print("total marks :",z)
	a=(z/500*100)
	print("Persantage:",a)
except:
	print("Not result found")'''
'''
y=x[h].values()
print(y)
z=sum(y)
if h==1:
	print("Name :-prince kumar")
elif h==2:
	print("Chhotu sharma")
print("total marks :",z)
a=(z/500*100)
print("Persantage:",a)'''





'''import numpy as np
x=np.array([1,2,4,5])
print(np.flip(x))'''



'''import numpy
x=numpy.array([1,2,3,4,5,6,7,8,9])
y=numpy.reshape(x,(3,3))
print(y)'''


import numpy as np
'''
n,m=map(int,input().split())
lista=[list(map(int,input().split())) for i in range(n)]
a=numpy.array(lista)

print(numpy.transpose(a))
print(a.flatten())'''

#x=np.random.rand(10,5)
#print(x) #its show the 10 row and 5 column between 0.1 to 0.99


'''
x=np.arange(1,10)
y=np.reshape(x,(3,3))
print(y)
print(np.trace(y)) #with the help of this method we can find sum of daigonal of metrix
z=np.diag(y)
print(z)
print(z.sum())
print(np.flip(y))
print(np.roll(y,5))
x[0]=11
print(y)
print(np.concatenate(y)) #convert in one array array from matrix
print(y.flatten()) #convert in one array from matrix
print(x[x>10])
print(x[x%2==0])
print(x==2)
print(np.where(x==3))
print(np.where(x%2==0))
x[0:4]=45
x[4:9:2]=50
print(y)
print(np.unique(x)) #drop duplicates with unique method
'''

#x=pd.DataFrame({"Name":["prince","kumar","sharma","chhotu"],
#	"Marks":[45,78,89,56],"per":[45.6,78.5,85.2,52.1] })
#print(x) 
#x.to_csv("cks.csv")


#x=pd.read_csv("cks.csv")
#print(x)

#x=x["per_Rank"]=x["per"].rank(ascending=0)
#x=x.set_index("per_Rank")
#print(x)

'''def x(**y):
	print(y["name"])
	print(y["age"])
x(name="prince kumar",age=21)

def x(*y):
	print(y[1])
	print(y[0])
x("prince kumae","mamta devi")'''
'''
x=["jan","feb","maarch"]
y=["april","may","june","july"]
z=zip(x,y)
print(tuple(z))'''
'''
x="001020300030"
y=x.count("0")
print(y)'''



'''def prince(x):
	y=x.count("0")
	z=x.count("1")
	if y==7 or z==7:
		print("Yes")
	else:
		print("no")
x=input("enter continious number :-")
prince(x)'''
'''
def prince(x):
	y=x.count(0)
	z=x.count(1)
	if y==7 or z==7:
		print("Yes")
	else:
		print("no")
x=int(input("enter continious number :-"))
prince(x)'''




'''
with open("prince.xl","a") as f:
	x=int(input("enter a number:"))
	For i in range(1,11):
		print(x*i)
		f.write(f"{x*i}")'''


import numpy as np
import pandas as pd


'''
class prince:
	def __init__(self):
		x=pd.Series(np.random.randint(20,50,12),index=[1,2,3,4,5,6,7,8,9,10,11,12])
		print(x)
	def first(self):
		x=int(input("enter the number :- "))
		y=0
		while y < 11:
			y+=1
			print(f"{x} x {y} = {x*y}")

class chhotu(prince):
	def __init__(self):
		super().__init__()
		x=np.ones(5)
		print(x)
		print(np.diag(x))

class kk(chhotu):
	def __init__(self):
		super().__init__()
		df=pd.DataFrame({"Month":["January","February","March","April","May","June","'July","August","September","October","November","December"],
			"Weeks":["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","----","----","----","---","---"]})
		print(df)

d=kk()
d.first()'''

'''y={}
x=int(input("enter how much key and value you need  :"))
for i in range(x):
	key=eval(input("enter key :"))
	value=eval(input("enter value :"))
	#y[key]=value
	y.update({key:value})
	
print(y)'''

'''
from datetime import date

def age(birthday):
	today=date.today()
	age=today.year-birthday.year-((today.month,today.day)<(birthday.month,birthday.day))
	print(age)
x=int(input("enter year :"))
y=int(input("enter month :"))
z=int(input("enter day :"))
age(date(x,y,z))'''


'''from datetime import date
def aage(x):
	today=date.today()
	a=today.year-x.year-((today.month,today.day)<(x.month,x.day))
	print(a)
	print("prince your birthday is",x)

x=int(input("enter year :"))
y=int(input("enter month :"))
z=int(input("enter the day :"))
aage(date(x,y,z))'''


'''
import random
def game(you,comp):
	if you==comp:
		return None
	if comp=="s":
		if you=="w":
			return False
		elif you=="g":
			return True

	elif comp=="w":
		if you=="g":
			return False
		elif you=="s":
			return True

	elif comp=="g":
		if you=="s":
			return False
		elif you=="w":
			return True

x=random.randint(1,3)
if x==1:
	comp="s"
elif x==2:
	comp="w"
elif x==3:
	comp="g"

print("computer chhoose for snake (s), Gun (g), Water (w) : ")
you=input("Now your turn please choose one from this sanke(s), water(w),gun(g) :-")
k=(comp,you)

print("Your Turn :",you)
print("Computer Turn :",comp)

if k==None:
	print("Game is Tie !")
elif k==False:
	print("you Lose the Game !")
else:
	print("You won the game !")'''



'''from datetime import date
def age(Birthday):
	today=date.today()
	age=today.year-Birthday.year-((today.month,today.day)<(Birthday.month,Birthday.day))
	#print(age)
	print("Your Date of Birth is :",Birthday)
	print("Your current age is",age)

x=int(input("enter year :\r"))
y=int(input("enter month :\r"))
z=int(input("enter birthday :\r"))
age(date(x,y,z))'''


'''x={"Sunday","monday","Tuesday","wednesday","thursday"}
 y={1,2,3,4,5,6}
 a=x.union(y)
 a.add("prince kumar")
 print(a)
 print(list(a)[2])''' #set slicing

'''x={}
x=set()
print(x)
print(type(x))'''


'''import time
pin=1478
chances=4
while chances!=0:
	x=int(input("enter pasword :"))
	if x!=pin:
		print("Wrong password")
		chances-=1
		print(chances)
	else:
		print("welocome to python Tutorial")
		break

	if chances==0:
		a=10
		while a>0:
			a-=1
			print(a,end="\r")
			time.sleep(1)
		chances=4
		while chances!=0:
			x=int(input("enter pasword :"))
			if x!=pin:
				print("Wrong password")
				chances-=1
				print(chances)
			else:
				print("welocome to python Tutorial")
				break

			if chances==0:
				a=30
				while a>0:
					a-=1
					print(a,end="\r")
					time.sleep(1)'''


'''
import numpy as np
x=np.full((4,5),51,dtype=str)
print(x,end=" ")

(A)
[['5' '5' '5' '5' '5']
 ['5' '5' '5' '5' '5']
 ['5' '5' '5' '5' '5']
 ['5' '5' '5' '5' '5']]

(B)
[['51' '51' '51' '51' '51']
 ['51' '51' '51' '51' '51']
 ['51' '51' '51' '51' '51']
 ['51' '51' '51' '51' '51']]

 (C)
 [[51 51 51 51 51]
 [51 51 51 51 51]
 [51 51 51 51 51]
 [51 51 51 51 51]]

 (D)
 [['51' '51' '51' '51']
  ['51' '51' '51' '51']
  ['51' '51' '51' '51']
  ['51' '51' '51' '51']
  ['51' '51' '51' '51']]

 '''

'''x=np.eye(5,5)
print(x.flatten())'''

'''
class prince:
	def one(self,a,b):
		self.a=a
		self.b=b
		self.cc=a+b
	def two(self,x):
		self.x=x
		for i in range(1,11):
			print(i*x)
	def three(self,c,d):
		self.c=c
		self.d=d
		self.m=c**d

p=prince()
p.one(4,5)
p.two(10)
p.three(5,4)
print(p.cc)
print(p.m)'''

'''
class A:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c1=a**b

	def one(self):
		print("I love you Mom !")
class B:
	def __init__(self,d,e):
		self.d=d
		self.e=e
		self.f=d*e
	def two(self):
		print("And we are five member in my faimly !")

class child(A,B):
	def __init__(self,a,b,d,e,g,h):
		A.__init__(self,a,b)
		B.__init__(self,d,e)
		self.g=g
		self.h=h
		self.i=g//h
	def three(self):
		print("We all are trust at each other !")


x=child(7,8,9,4,5,6)
x.one()
x.two()
x.three()

print("Exponents :",x.c1)
print("Multiplication :",x.f)
print("Floor Divison :",x.i)'''
'''
x=[12,45,78,11,16,18,20]
y=[]
for i in x:
	if i<15:
		div="Third"
	elif i<=20:
		div="Second"
	else:
		div="First"
	print(div)'''

	#print(i)

'''
import time
print("----------------------------------------------------------------")
print("Welcome to the Prince Tutorial!")
print("----------------------------------------------------------------")
time.sleep(2)
print("----------------------------------------------------------------")
print("\nPlease choice which subject do you want to learn\nFor english press == 1\nFor math press == 2\nFor science press == 3\nFor social studies press == 4")
time.sleep(3)
try:
	print("----------------------------------------------------------------")
	x=int(input("\nplease press your choice subject wise :"))
except:
	time.sleep(2)
	print("----------------------------------------------------------------")
	print("\nyou have enterd incorrect input\nPlease try again!")

chance=4
pin=7894
while chance!=0:
	print("----------------------------------------------------------------")
	a=int(input("\nenter four digit student id password :"))
	if a!=pin:
		print("---------------------------------------------------------------")
		time.sleep(3)
		print("\nyou have enterd wrong_id password\nplease enter correct id password!\n")
		chance-=1
		time.sleep(2)
		print("----------------------------------------------------------------")
		print(f"you can try only {chance} times only\n")
		print("----------------------------------------------------------------")
	else:
		if x==1:
			time.sleep(2)
			print("----------------------------------------------------------------")
			print("Wlcome to the english classes!")
			print("----------------------------------------------------------------")
			break
		elif x==2:
			time.sleep(3)
			print("Wlcome to the math classes!")
			break
		elif x==3:
			time.sleep(3)
			print("----------------------------------------------------------------")
			print("welcome to science classes")
			print("----------------------------------------------------------------")
			break
		elif x==4:
			time.sleep(3)
			print("----------------------------------------------------------------")
			print("welcome to social studies classes")
			print("----------------------------------------------------------------")
			break
	if chance==0:
		print("Your student id is Blocked for 30 seconds\nPlease wait 30 seconds")
		def countdown(t):
			while t>0:
				print("Countdown is on : ",t,end="\r")
				t-=1
				time.sleep(1)
			#print("times up")
			print("\nThanks for waiting!")
			time.sleep(3)
			chance=4
			while chance!=0:
				print("----------------------------------------------------------------")
				a=int(input("\nenter four digit student id:"))
				if a!=pin:
					time.sleep(2)
					print("----------------------------------------------------------------")
					print("\nyou have enterd wrong_id password\nplease enter correct id password!\n")
					chance-=1
					time.sleep(2)
					print("----------------------------------------------------------------")
					print(f"you can try only {chance} times only\n")
					print("----------------------------------------------------------------")
				else:
					if x==1:
						time.sleep(3)
						print("----------------------------------------------------------------")
						print("Wlcome to the english classes!")
						print("----------------------------------------------------------------")
						break
					elif x==2:
						time.sleep(3)
						print("----------------------------------------------------------------")
						print("Wlcome to the math classes!")
						print("----------------------------------------------------------------")
						break
					elif x==3:
						time.sleep(3)
						print("----------------------------------------------------------------")
						print("welcome to science classes")
						print("----------------------------------------------------------------")
						break
					elif x==4:
						time.sleep(3)
						print("----------------------------------------------------------------")
						print("welcome to social studies classes")
						print("----------------------------------------------------------------")
						break'''

'''
import numpy as np
x=np.full((4,5),51,dtype=str)
print(x,end=" ")

(A)
[['5' '5' '5' '5' '5']
 ['5' '5' '5' '5' '5']
 ['5' '5' '5' '5' '5']
 ['5' '5' '5' '5' '5']]

(B)
[['51' '51' '51' '51' '51']
 ['51' '51' '51' '51' '51']
 ['51' '51' '51' '51' '51']
 ['51' '51' '51' '51' '51']]

 (C)
 [[51 51 51 51 51]
 [51 51 51 51 51]
 [51 51 51 51 51]
 [51 51 51 51 51]]

 (D)
 [['51' '51' '51' '51']
  ['51' '51' '51' '51']
  ['51' '51' '51' '51']
  ['51' '51' '51' '51']
  ['51' '51' '51' '51']]
'''

'''x=(1.5)
y={"F"}

x=y

print(x is y)'''

x=["a",45,"b","c"]
'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example
The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:
Result =[]
scorelist = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Result+=[[name,score]]
        scorelist+=[score]
    b=sorted(list(set(scorelist)))[1] 

    for a,c in sorted(Result):
        if c==b:
            print(a)
'''

'''
R =[]
s =[]

x=int(input("enter number of sytudent"))
for i in range(x):
    name = input()
    score = float(input())
    R+=[[name,score]]
    s+=[score]
b=sorted(list(set(s)))
k=b[1]

print(k)'''



''' 
for a in sorted(R):
    if a==k:
        print(a)'''
'''
x=["prince","kumar","sharma"]
y=("ankit","kumar","yadav")
#x=y
print(x is y)'''

'''x=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
if "friday" in x:
	print(x)
else:
	print("monday" in x)
	print("january" not in x)'''

#find the greatest number between three number.
'''
x=int(input("enter a first number :"))
y=int(input("enter second number :"))
z=int(input("enter third number: "))

if x>y and x>z:
	print(x)
elif y>x and y>z:
	print(y)
elif z>x and z>y:
	print(z)
elif x==y and x>z:
	print(x,y,"both are equall and greater")
elif x==y and y>z:
	print(x,y,"both are equall and greater then all")
elif z==y and z>x:
	print(z,y,"both are equall and graeter then all")
elif z==x and z>y:
	print(z,x,"Both are equall and grater then all")
else:
	print("All are equall",x,y,z)'''

'''	
import time
#find the finalist between four teams
dc=int(input("Delhi capital  score :"))
rcb=int(input("Royal chalanger bangluru score :"))
#mi=int(input("enter the match score :"))
#kkr=int(input("enter the match score :"))
time.sleep(2)
if dc>rcb:
	s="Delhi capital"
else:
	s="Royal challanger banguluru"

print(s,"Wont the first semi final match by",dc-rcb,"runs")
time.sleep(2)
mi=int(input("Mumbai Indian score :"))
kkr=int(input("Kolkata knight riders score :"))

if mi>kkr:
	s2="Mumbai indian "
else:
	s2="Kolkata knight riders "
time.sleep(2)
print(s2,"Won the second semi final match by",mi-kkr,"runs")
time.sleep(2)
print("\nNow get ready for the final match between",s,"and",s2)
print("\n-------------------------------------------------------------")

x=int(input(s))
y=int(input(s2))
if x>y:
	final=s
else:
	final=s2
time.sleep(2)
print("\nCongratulation team",final,"You won the final match by",x-y,"runs")
'''

'''x=int(input("enter how many even number you want:"))
y=0
z=0
while x>y:
	z+=1
	if z%2==0:
		print(z)
		y+=1'''

'''x=int(input("enter how many even number you want:"))
z=0
c=0
while x>0:
	z+=1
	if z%2!=0:
		print(z)
		x-=1
		c+=x
print(c)'''


'''x=int(input("enter how many even number you want:"))
z=0
for i in range(1,x*2+1):
	if i%2==0:
		print(i)
		z+=i
print("sum of",x,"even number is :",z)'''

#find the factorial of number by user 
'''x=int(input("enter number you want:"))
y=1
for i in range(1,x+1):
	y*=i

print(y)'''
'''
x=int(input("enter how many even number you want:"))
y=1
while x>1:
	y=y*x
	print(y)
	x-=1
print("factorial",y)'''
'''
x=int(input("enter how many even number you want:"))
if x<2:
	print("number is not prime !")
elif x==2:
	print("number is prime!")
else:
	for i in range(2,int(x/2)):
		if x%i==0:
			print("Number is not prime !")
			break
		else:
			print("Number is prime !")
			break'''

'''
while True:
	try:
		x=int(input("enter number :"))
	except:
		print("please enter correct number ")
	if x>100:
		print("hiii")
	else:
		print("byyy")
	j=input("enter the alphabetical k to break the loop :")
	if j=="k":
		break'''


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
'''
x=int(input("enter number :"))
y=2
if x<y:
	print("number is not prime")
elif x==y:
	print("number is prime")
else:
	while x>y:
		if x%y==0:
			print("number is not prime !")
			break
		y+=1
	else:
		print("number is prime")'''

#================================================================================
'''age=int(input("enter age :"))
x="my name is prince ,and i am {} old"
print(x.format(age))'''
'''		
x="prince kumar"
y="bihar"
z="mamta devi"

a="Hii this is {} here i am from {} and my mother name is {} ."
print(a.format(x,y,z))'''

'''x="himachal pradesh"
for i in range(len(x)-1,-1,-1):
	print(x[i],end="")'''

'''x=["january","february","march","april","may","june","july"]
x[0:2]=["hiii","bro"]
print(x)'''

#x=['sunday','monday','tuesday','wednesday','thursday','friday','saturday','monday','monday','friday','saturday']
#x[1:4]=['january']
#x.clear()
#y=x.count("monday")
#print(y)

'''x=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
x.insert(2,"January")
y=["prince","kumar","sharma"]
x.extend(y)
x.insert(0,"hiiii")

print(x)'''

#x=[1,2,['sun','mon',['apple','banana'],'tues'],5,6]
#1.reverse the third list
#x[2][2].reverse()
#x.reverse()
#print(x)

#x=["one","two","three",["prince","kumar",["chhotu","shrama"],"roy"],"four","five"]
#x[3].remove("prince")
#x.remove("one")
#x.pop(3) 	# its delete by index number of value
#del x[2]
#x.extend(["pan"])
#print(x)
#print(x[4:])

'''x=("january","february","march","april","may")
y=("prince","kumar","sharma")
#x+=y
#x=x+y
#print(x+y)
(a,b,c)=y
print(b)
m,n,*o,p=x
print(o)
print(n)'''
'''
x={"apple","mango","banana","lichi","grapes","jackfruits","guava"}
y={"pineapple","plum"}
z=x.union(y)
z.add("prince")
z.add("mohmmad sami")
print(z)'''

'''x={"sunday","monday","tuesday","wednesday","thursday","friday","saturday"}
#y={"sunday","monday","tuesday","january","february","march"}
#z=x.intersection(y)
#print(z)
x.discard("sunday")
x.remove("monday")
y=x.pop()
print(y)
print(x)'''
'''
dic={"name":"prince kumar","age":24,"qualification":"graduate","home":"bihar"}
#print(dic)
dic["village"]="chakkapar"
dic.update({"collage":"rbs college teyai"})
print(dic)
x=input("enter keys :")
print(dic[x])
print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.get("age"))'''

#x=input("write five fruits name :").split()
#y=x.split()
#print(x)
'''
def x(*name):
	print("i love my",name[1])
	print("we all are",name[0])
	print("my name is",name[2])
x("Indian","country","prince kumar")


def g(**a):
	print("my name is",a["name"])
	print("my mothers name is",a["mother"])
	print("my brother name is",a["brother"])
	print("we are",a["member"],"in my faimly")
g(name="prince kumar",mother="mamta devi",member=5,brother="pappu and priyanshu")


def q(*l):
	print("A noun is the name of",l[0])
	print("There are five type of",l[1])
	print("Countable noun is the part of",l[2])
	print("ram is which noun :-",l[3])
q("person","noun","Noun","Proper Noun")


x=lambda a,b:a+b
print(x(10,25))
y=lambda k,r:k**r
print(y(5,5))

x=("prince","kumar","sharma")
y=("name","surname","last_name")
z=zip(x,y)
print(dict(z))'''



'''class a:
	x=45
	y=5
j=a()
print(j.x*j.y)'''
'''
class math:
	def __init__(self):
		x=["himachal", "pradesh"]
		x.reverse()
		print(x)
y=math()'''

'''class x:
	def a(self):
		print("my name is prince kuamr")
f=x()
f.a()
f.a()
f.a()'''


'''class prince:
	def a(self):
		print("good morning dear students")
s=prince()
s.a()'''

'''
class math:
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		self.d=a+b-c
	def one(self,e,f):
		self.e=e
		self.f=f
		self.g=e**f

	def two(self,j,k):
		self.j=j
		self.k=k
		self.m=j*k

ds=math(45,21,78)
ds.one(4,4)
ds.two(15,10)
print(ds.d)
print(ds.g)
print(ds.m)'''

import numpy as np
import pandas as pd


'''class A:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a**b
	def one(self,m):
		self.m=m
		x=np.arange(m)
		print(x)
class B(A):
	def __init__(self,a,b,d,e):
		super().__init__(a,b)
		self.d=d
		self.e=e
		self.f=d*e
	def two(self):
		y=pd.DataFrame({"Date":pd.date_range("20220810",periods=10),
			"name":"prince"})
		print(y)
class C(B):
	def __init__(self,a,b,d,e,g):
		super().__init__(a,b,d,e)
		self.g=g
		j=np.arange(g).reshape(4,4)
		print(j)

	def three(self):
		k=pd.Series(["prince","kumar","sharma","mamta","sharma"],index=[1,2,3,4,5])
		print(k)
	def four(self, )


sd=C(12,10,8,3,16)
sd.one(10)
sd.two()
sd.three()
print("Exponents :",sd.c)
print("Multiplication :",sd.f)'''



'''y=pd.DataFrame({"Date":pd.date_range("20220810",periods=10),"name":"prince"})
print(y)'''

'''class prince:
	def __init__(self,a):
		self.a=a
		while a>0:
			a-=1
			print("Normal Number :",a)
	def first(self):
		print("Failure is the part of sucsses !")
class kumar(prince):
	def __init__(self,a,b):
		super().__init__(b)
		self.b=b
		for i in range(b):
			print(i*b)
	def second(self,c):
		self.c=c
		x=np.arange(c).reshape(5,4)
		print(x)
sd=kumar(15,10)
sd.first()
sd.second(20)'''

'''class grand:
	def __init__(self):
		print("Turning off airplane mode")
class parents:
	def __init__(self):
		print("Turning on mobile data WiFi")
class child(grand,parents):
	def __init__(self):
		grand.__init__(self)
		parents.__init__(self)
		print("Cheaking the signal in your area !")

x=child()'''


'''class parents:
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
x.third()
'''

'''class math:
	def __init__(self):
		print("Failure is the part of sucsses so fight anytime against the failure!")
class eng:
	def onr(self):
		print("someone who likes so much but don't then what he feel")
class hindi(math,eng):
	def __init__(self):
		super().__init__()
		print("After all you will get sucsses !")
x=hindi()
x.onr()'''


'''class prince:
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



'''class st:
	def two(self):
		print("we will beacome a good python teacher !")
class stt:
	def one(self):
		print("this a mangoes!")
class sp(st,stt):
	def __init__(self):
		super(). two()
		super(). one()
		print("I will beacome a good data scientist !")

x=sp()'''


#Polymorphism in inheritance
'''
class parrot:
	def fly(self):
		print("birds can fly better then peacock")
	def run(self):
		print("Milkha singh runs very fast!")
class man:
	def fly(self):
		print("man can not fly like parrot !")
	def run(self):
		print("But man can run like milkha sing")
#def test(self):
#	self.fly()
#	self.run()
x=parrot()
y=man()
#test(x)
#test(y)
for i in (x,y):
	i.fly()
	i.run()'''


'''class Animals:
	def first(self):
		print("Dog is a domestic animals !")
	def second(self):
		print("Cat is being drinking milk daily !")
	def third(self,m,n):
		self.m=m
		self.n=n
		self.o=m**n
class Birds:
	def first(self):
		print("All birds fly in the sky !")
	def second(self):
		print("some birds can not fly because his body is big")
	def third(self,p,q):
		self.p=p
		self.q=q
		self.r=p+q+p+q+q+p+p

a=Animals()
b=Birds()
for i in (a,b):
	i.first()
	i.second()
	i.third(3,4)
print(f"\nExponents : {a.o}")
print(f"Addition : {b.r}")

class prince:
	def first(self):
		print("we are twenty four year old!")
	def second(self):
		print("In this time all human are like")

class kumar:
	def first(self):
		print("this is my personal book!")
	def second(self):
		print("you are my dear friends")
def test(self):
	self.first()
	self.second()
a=prince()
b=kumar()
test(a)
test(b)'''

'''
class main:
	def __init__(self):
		print("Failure is the part of sucsses !")
	def first(self):
		print("tiger saves the forest from diffrent Animals ")
class dual:
	def __init__(self):
		print("We are fire !")
	def second(self):
		print("somthing like best for me !")
class peince(main,dual):
	def __init__(self):
		main.__init__(self)
		dual.__init__(self)
	def third(self):
		print("I want to beacome a good data scientist !")

sd=peince()
sd.first()
sd.second()
sd.third()'''




'''x=[1,4,5,6,2,1,4,4,9,6,1,4,5,8,9,5,7,9,6,5,7,4,5,2,8,6,5,4,8,10]
y={}
for i in x:
	if i not in y:
		y[i]=1
	else:
		y[i]+=1
for i in y:
	if y[i]==1:
		print(i)'''

'''z={}
x=["prince","kumar","sharma","prince","kumar"]
y=len(x)
for i in range(y):
	if x[i] not in z:
		z[x[i]]=1
	else:
		z[x[i]]+=1
for i in z:
	if z[i]==1:
		print(i)'''


'''
number=[4,5,6,7,8,9,4,5,6,1,2,3,1,2,3,4,5,6,7,8,9,12]
counts={}
for i in number:
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] += 1
print(counts)
for i in counts:
    if counts[i] == 1:
        print (i)'''


'''
for i in rooms:
    if not i in seen:
        seen[i] = 1
    else:
        seen[i] += 1

for key, val in seen.items():
    if val != k:
        print(key)'''


'''k = int(input())
rooms = (int(x) for x in input().split(' '))
print(rooms)'''



'''z=[]
x=["kumod",120,"rahul",24,"ankit",25]
y=["name","age"]
for i in range (0,len(x),2):
	m={"name":x[i]}
	y={"age":x[i+1]}
	z.append(m)
	z.append(y)
print(z)'''

'''z=[]
x=["kumod",120,"rahul",24,"ankit",25]
y=["name","age"]
for i in range (0,len(x),2):
	m={y[0]:x[i],y[1]:x[i+1]}
	z.append(m)
print(z)'''

x=["kumod",120,"rahul",24,"ankit",25]
y=["name","age"]
for i in range (0,len(y)):
	for j in range(0,len(x),2):
		z={y[i]:x[j]}
		print(z)


'''
for i in range(1,len(x),2):
	a={"age":x[i]}
	z.update(a)
	print(z)'''
'''
kk={}
p=[]
x=["kumod",120,"ankit",24,"rahul",25]
y=["name","age"]
for i in range (0,len(y),2):
	for j in range(0,len(x),2):
		z={y[i]:x[j]}
		p.append(z)
for k in range(1,len(y)):
	for m in range(1,len(x),2):
		a={y[k]:x[m]}
		print(a)
		p.append(a)
print(p)'''



'''
x=[1,2,3,4,5,6,7,8]
z={}
for i in range (0,len(x),2):
	y={x[i]:x[i+1]}
	z.update(y)
print(z)
print(type(z))'''