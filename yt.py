'''a=input("enter yoour name")
a=int(a)		#convert to a integer as possible then str can,t take
print(type(a))'''


#add the sum of two number

'''A=23
B=26
print("sum of all :-",A+B)'''

#Write a python program to find reminder when a number is divided by z.

'''x=35
y=12
print("the reminder when x is divided by y is : -",x%y)'''

#write a python program to find average of two
# numbers enterd by the user 

'''a=34
b=12
c=62
Avg=(a+b+c)/2
print("the average of three number is :-",Avg)'''



#Write a python program to caluculate square of a number
#enterd by the user.

'''x=int(input("enter a number: -"))
print("the square of your number is : -",x*x)'''


#string in python 
# string is a data type in python .string is 
#sequence of a charactor  encodes.


# there are three type of strings
'''1 single code string 
2.dual code string
3. triple code string'''

#example:-

#		x='prince'		#single code string
#		x= "prince"		# dual code string
#		x='''prince'''	# trple code string

'''a="prince"
b=34
print(a,b)
print(type(a))
print(type(b))
'''
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#					 chepter string slicing
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''string slicing in python 
A string slicing in python can be sliced for getting a part of  string.
 Example : -
 	   -6  -5  -4  -3  -2  -1=Reverse count
 Name = P 	R 	I 	N 	C 	E
 		0 	1	2	3 	4 	5= counting start

The index in a string start from 0 to length-1
in python'''

#Example : -

#x="Prince"
#print(x[5])	  	# 5 index is same the -1
#print(x[-1])
#print(x[2:4])
#print(x[0:5:2])
#print(len(x))
#print(type(x))


#Name = '''India is my country and all indian are my brother and sister 
#and i love my country thank you '''
#print(Name)
#  print(len(Name))
#print(Name[0:50:3])


'''string function 
some of the mostly uesd function to perform 
operations on or manipulate string are

1. len() function =nthe function retturn the length of the string.
	example : -'''
'''x= "prince kumar sharma"
print(len(x))'''


'''2. string.endswith(" any line ") = this function tells weather
 the variable string end with the string " any line " or not if string 
 is " " it is true 

 		Example : -'''
'''x= "i play cricket with friends"
print(x.endswith("friends"))	# print true
print(x.endswith("play"))		# print false
'''

'''3. string count(" ") = count the total number of  accurate 
of any characctor
	Example:-'''
'''x= "my mother is my life"
print(x.count("m")) 	# he count how much 'm'
'''

'''4. string.capitalize() = this function capitalize
the first charactor of a given string.
example: -'''

'''x= "i love my mother"
print(x.capitalize())		# frist word done capital lettter 
'''

'''5. string.find(word) : = This function find word returns
 the index  of first accurance of that word in string 
 	Example : -'''
'''x="we all are indian right"
	print(x.find("are"))'''	
#cmd print accurance of number 7 index


'''6. string.replace("old word",new word) =  This function replace the old word with new word 
in the index. 
Example : -'''
#print(x.replace('father', 'mother'))
# cmd replace the the old name to new name

'''7. Escape sequence : -
	\n ----  for new line
	\t ----  for a tab
	\''----	 for single quote
	\\ ----	 for back slash

'''

#cheptor function python -prectice set 

'''1. write a python program to display a user input name 
followed by good after noon using input.
'''
'''x=input("wrtie any name\n")
y= 'Good afternoon'
print(y,x)'''

'''2.Write a program to fill in a letter template given
below with name and date.

Letter = Dear </name/>
		Greeting from prince company.i am happy to tell you about your selection
		you are selected in my company
		have a great day ahead
		thanks for regards
		by prince
		you are selected!
		</date/>'''

#Letter = '''		\n\n\tDear  </name/>
#		Greeting from prince pvt Ltd.\n\ti am happy to tell you about your selection
#		you are selected in my company
#		\thave a great day ahead
#		\tthanks for regards
#			\t\t\tby prince
#	</date/>'''
#name=input("please enter the name:-\n")
#date=input("enter a date")
#Letter=Letter.replace("</name/>", name)
#Letter=Letter.replace("</date/>", date)
#print(Letter)




#					date  03-06-2022

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# chepter  :- python in dictionary and set 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Define : - Dictionary is a high collection of ray values pairs.

# Properties of python dictionary

#it is ordered 
#it is mute
#it is indexed
#can not contain dublicate keys
#
#

#Some methods use in python dictionary

#list(myDict.keys or values()) : - return a list in kays or values.

# (myDict.keys()):-  it is used to print all key in  single line.

#(myDict.values()) :- it is used to print all values.

#  myDict.items() :- it is useed to print a list of (key,value) tuple.

# myDict.update({"key": "value"}) :- it is used to updates the dict
#									 with supplised key value pairs.


#myDict.get("key"):- return the value of the supplied key  and values is returned.



# syntax:-		
#keys		value
'''x={
"prince": "a student",
"marks": 120,
"list": [2,5,8]
}
print(x["marks"])
print(x["list"])
print(x["prince"])
'''

'''myDict={
"love": "it mean like,you desire",
"hate": "it he don't like you, you are not desire",
"mother": "maa,symbol of love"
}
print(myDict["love"])
print(myDict["hate"])
print(myDict["mother"])'''






# example of dictionary in metods

'''Mydict={
"weeks": "sunday,monday, tuesday, wedneday",
"months": ("january", "febraury", "march", "april"),
"numbers": [12,32,45,56,78],
"alphabet": ("a","b","c","d")
}
print(Mydict["months"])
print(Mydict["numbers"])
print(Mydict["alphabet"])
print(list(Mydict))
print(list(Mydict.keys()))
print(list(Mydict.values()))
print(list(Mydict.items()))
Mydict.update({
"name": "prince kumar sharma",
"power": "electronic"
})
Mydict.update({"mobile": "i play game"})
print(Mydict.keys())
print(list(Mydict))
print(Mydict.values())
print(Mydict.items())'''



# write a program with key values of animals fruits birds and colour name


'''myDict={
"animals": ("cow","cat","rat","tiger","lion","dog"),
"birds": "parrot,peacock,vulter, cuckoo,crow,saprrow",
"fruits": "apple,mango,banana,lichi,pomigrenet,guava,",
"colours": "red,black,white,orange,yellow,pink,blue,green"
}
a=input("write any name :-")
#print(myDict[a])
#print(myDict["a"])
#print(myDict.keys())
#print(myDict.values())
print(list(myDict.get(a)))'''

#***************************set in python***********************************

#  set in python : -
#  set : - set is collection of non repitative elements


# properties of set 
# 1. set are unorderd => elements order does not matter .
# 2. set are unindexed => can't acses elements by index .
#3. there is no way to change items in set.
#4. set can't contain dublicate values.




#  example : -
# x={"ram":"mohan"}		# this is <class dict>
'''x={1,2,3,4,5}		# set is non repitative element 
print(x)
print(type(x))'''


'''x={}
print(type(x))	'''	# empty < class dict >


'''x=set()
print(type(x))'''		# empty < class set >



# add some value in empty set
'''x=set()
x.add(1)
x.add(4)
#x.add("prince")
print(x)
'''

# remove () method use in set
'''x={4,5,7,8,9}
x.remove(5)		# remove 5 from set x
x.remove(9)
print(x)'''		# then 5 will be removed in this set


'''x={4,5,7,8,9}
x.clear()		# clear number from set x
print(x)'''

#*******************//////////////////////////*****************************




#prectice set in python dictionary

# 1. write a program to create a dictonary of hindi word with values as their endlish translation
# provide user with an option to look it up
'''myDict={
"kitab": ["book" ,"that we read in school"],
"kalam": ["pen" ,"pencil" ,"that we write in school"],
"khus": ["happay","joyful"]
}
print("The meaning of word is: -"myDict["kitab"])
print(myDict["kalam"])
print(myDict["khus"])
print(myDict.keys())
print(myDict.values())
print(list(myDict.items()))
'''

# 2.write a program to input eight nummbers from the user 
#  and display all the unique numbers once
'''num1=int(input("enter first number\n: -"))
num2=int(input("enter second number\n: -"))
num3=int(input("enter third number\n: -"))
num4=int(input("enter forth number\n: -"))
num5=int(input("enter fifth number\n: -"))
num6=int(input("enter sixth number\n: -"))
num7=int(input("enter seventh number\n: -"))
num8=int(input("enter eighth number\n: -"))
x={num1, num2, num3, num4, num5, num6, num7, num8}
print(x)
print(type(x))
print(len(x))
'''

# 3.can be have a set with 18(int) and 18(str)as a values in it
# x={18,"18"}
# print(x)	# print both because one is int and one is str


# 4.what will be the length of the following
'''x=set()
x.add(20)
x.add(20.0)
x.add("20")
print(x)			# print {20, '20'}
print(len(x))		# length is 2 answer
print(type(x))		# <class set>
'''
# 5. x={ } what is the type of 
# x={}
# print(type(x))		# < class dict >


# 6. create an empty dict . allow 4 friends to enter their favorate 
# language  as values and use  keys  as their  assume that the names 
# are unique

'''favlang={}
a=input("enter your favorate language prince\n")
b=input("enter your favorate language kumod\n")
c=input("enter your favorate language ankit\n")
d=input("enter your favorate language priyanshu\n")
favlang["prince"]=a
favlang["kumod"]=b
favlang["ankit"]=c
favlang["priyanshu"]=d
#print(favlang.keys())
#print(favlang)
print(favlang.items())'''




# 7. if name of two friends are same what will 
#  happen to the program in question number 6 ?
'''favlang={} 
a=input("enter your favorate language prince\n")
b=input("enter your favorate language kumod\n")
c=input("enter your favorate language ankit\n")
d=input("enter your favorate language priyanshu\n")
favlang["prince"]=a
favlang["kumod"]=b
favlang["ankit"]=c
favlang["prince"]=d	
print(favlang)'''
# recently putted value will show in this condition
# same name ke last me jo value denge wahi show karega 
# aur jo pahle put kiye the wo remove ho jayega





## 8. if  languages of two friends are same what will happen
# in the program in question number 6? 
'''favlang={}
a=input("enter your favorate language prince\n")
b=input("enter your favorate language kumod\n")
c=input("enter your favorate language ankit\n")
d=input("enter your favorate language priyanshu\n")
favlang["prince"]=a
favlang["kumod"]=b
favlang["ankit"]=c
favlang["priyanshu"]=d
print(favlang)	'''		#if language is same then show all 

# agar language same hogi to value me koi problem nhi hogi
# wahi print krega jiska jo language hai


# 9. can you change the values inside a list which is 
#  contend in set x.
# x={8,7,12,"prince",[1,2]}
# print(x)		##  print :unhashable type: 'list'

# we can't add a list in set  so this is wrong question



# Lesson name : - dictionary and set in python is completed
#********************++chepter end++ *********************************

#*****************++New cheptor start++*******************************
#Lesson name : - Function in python
'''
A function is group of statement performing a specified task.

When a program gets bigger in size and its complementy grow  it diffrent
for a programer  to keep track on  which piece of code is doing what

A function can be reeuse by the programer any number of times.

Example and syntax of a function 
The syntax of a function looks as follows:'''

'''def function():
	print("hello world!")
function()'''

'''
This function can be run any number of times any where in the program

function call 
Werever we want to call a function .we put the name of the function followed by 
the perameter as follows '''

#function() #=> This is called function

'''
Function Definition => The part of cointaing the exact set the instruction which
are executed during the function call.

How many types of function => There are two types of function
1. user defined function 
2. built in function

1.User defined function'''

'''def greet(name):
	print("Good Morning "+name)

greet("prince kumar")
greet("pappu kumar and priyanshu kuamr")
greet("mumma")'''

#2.Example of built in function => len(),print(),range(), etc


#1.use of return method

'''def x(a,b):
	return a+b
def y(c,d):
	return c**d

ob=x(12,8)
print("sum of two number :",ob)
oc=y(5,3)
print("Eexponents :",oc)'''


#2.Default argument of example

'''def x(name="prince kumar"):
	print("Good Morning "+name)

x()
x("priyanshu kumar")
x("mummy")'''

'''
Default Perameter value => We can have a value default argument in a function 
if we specify name = "sir" in the line of the containing def this value is used when 
no argument is passed.'''


#Q1.Factorial program in function
'''def fact(x):
	product=1
	for i in range(1,x+1):
		product=product*i
	print("factorial :",product)
fact(int(input("etner the number which factorial do you want :")))'''

'''		or
Recursion => Recursion is a function which call itself it is used to directly
use a mathematical formula as a function 
for example : -		'''
'''def fact(x):
	if (x==0) or (x==1):
		return 1
	else:
		return x*fact(x-1)		# <==> look calling itself it is callrd recursion 
f=fact(int(input("etner the number :")))
print("factorial :",f)'''


# Here we called the second function
#x("Python")
#x()


#************************Prectice set of function***************************************






