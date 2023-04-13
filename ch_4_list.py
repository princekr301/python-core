
'''
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.






List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

Example
Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)
List Items
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

Note: There are some list methods that will change the order, but in general: the order of the items will not change.

Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

Allow Duplicates
Since lists are indexed, lists can have items with the same value:



List Methods
Python has a set of built-in methods that you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	return in assending order the list
sort(reverse=True) print in desending order



List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:

Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)



#///////////////////////////////////////////////////////////////////
#	29-06-2022
#////////////////////////////////////////////////////////////

#	List
# string type data
Days=["sun","mon","tues","wed"]
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
	print(y)'''
	#print(y,end=" ")


'''x=["one","two","three","four","five"]
y=len(x)
z=0
while y>z:
	print(x[z])
	z+=1 '''

'''x=["one","two","three","four","five"]
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
	print(y,end=" ")
'''

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
print(y)
'''



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
x.pop(2)
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
#x[2].extend(y)	# list

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

'''
Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

Example
Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)
Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow Duplicates
Since tuples are indexed, they can have items with the same value:

Example
Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

Example
Packing a tuple:

fruits = ("apple", "banana", "cherry")
But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

Example
Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

ADVERTISEMENT

Using Asterisk*
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

Example
Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)



Tuple Methods
Python has two built-in methods that you can use on tuples.

Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''





# tuple : - a tuple is collection which is odered and allow duplicate.



'''x=("sunnday","monday","tuesday","wednesday","thursday","sunday")

print(x)
print(len(x))
print(type(x))
'''


'''x=("prince")
print(type(x))
'''



'''x=tuple("prince")
print(type(x))
print(x)			# return <class tuple>

x=("prince",)
print(type(x))		# return <class tuple>
print(x)'''


# creat a tuple in eight item 

'''x=("jan","feb","mar","apr","may","jun","jul","aug")

# reeturn 3rd item
print(x[2])
print(x[-6])


#return 4th item
print(x[3])
print([-5])


#return fift to seventh item
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

# all program done with the help ofnegative and positive indexing



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
(jan, feb, *march)=x'''
#print(jan)
#print(march)

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
	#print(y)
'''

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

'''x=(1,2,3,4,5)
y=("a","b","c","d")
print(x+y)


# multiply tuples

x=(1,2,3,4,5)
y=x*2
print(y)


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

'''x=(1,2,3,4,5,6,7,8,9)
y=x.index(5)
print(y)


x=("a","b","c","d","e","f")
y=x.index("c")
print(y)
'''




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





