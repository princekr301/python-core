 
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

#import module as mod
#print(mod.per1)		#this module will use in another file



'''class gradent:
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
'''
#print(x.d)
'''

#this module will use in another file

import module as m
m.x.second()
m.x.first()
print("Addition :",m.x.d)
print("exponent :",m.x.g)
'''


#***********************************************************************************
# some functions 
'''abs() function
The abs() function return the absolute the values ot the specified number '''
'''x=-987
print(abs(x))#return the absolute value of the 

x=6+56j
print(abs(x))'''

#pow() this module is used to do exponent of two number
# when it's in three number then first two number do exponent and third number 
#do work of modules 
#pow()function

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

#import os			# this module is used to delete the file
#os.remove("pri.py")
