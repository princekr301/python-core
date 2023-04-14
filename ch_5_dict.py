


# set in python

#  set in python : -
#  set : - set is collection of non repitative elements


# properties of set 

# 1. set are unorderd => elements order does not matter .
# 2. set are unindexed => can't acses elements by index .
#3. there is no way to change items in set.
#4. set can't contain dublicate values.

'''
Set Methods
Python has a set of built-in methods that you can use on sets.

Method	Description

add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
'''

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



#*************************************************************
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# chepter  :- python in dictionary and set 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Define : - Dictionary is a high collection of keys values pairs.

# Properties of python dictionary

#it is ordered 
#it is mute
#it is indexed
#can not contain dublicate keys


'''
Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

Method			Description
clear()			Removes all the elements from the dictionary
copy()			Returns a copy of the dictionary
fromkeys()		Returns a dictionary with the specified keys and value
get()			Returns the value of the specified key
items()			Returns a list containing a tuple for each key value pair
keys()			Returns a list containing the dictionary's keys
pop()			Removes the element with the specified key
popitem()		Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()		Updates the dictionary with the specified key-value pairs
values()		Returns a list of all the values in the dictionary
'''

 #				new cheptor in python 
#				 python dictionaries


# Dictionary are written with curly brackets, and have keys and values
#dictionay are odered , changable  and does not allow duplicate keys
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

'''

# Make a program so that when enter a state by user ,
# its capital will be shown

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
print("the capital of",x,"is",state_capital[x])
'''






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
# This value return a keys list of  all keys in the dict
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

del myDict["man"]
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

#create a dictionary with the help of dict method


'''myDict={
"name": "xyz",
"company": "abcd",
"state" :"delhi",
"post": "manager",
"salary": 40000
}
x=dict(myDict)
print(x)'''






 # create dictionary with user input  while loop
'''
# it  is an empty dictionary
myDict={}

x=int(input("enter the number:-"))
y=0
while x>y:
 	key=str(input("write key:-"))
 	value=eval(input("write value:-"))		# note:-take str in "keys" in form
 	myDict[key]=value
 	y+=1
print(myDict)'''


#it is my output of while loop in dictionary by user
'''
enter the number:-3
write key:-hii
write value:-"rohan"
write key:-mina
write value:-456
write key:-ram
write value:-"fidh"
{'hii': 'rohan', 'mina': 456, 'ram': 'fidh'}
'''






#print dictionary by user input with the help of for loop
'''
myDict={}
x=int(input("enter how much need dict:-"))
for y in range(0,x):
	key=str(input("write key:-"))
	value=eval(input("write value;-"))
	myDict[key]=value
print("eng to hnd dict",myDict)
'''






#***********************************************************************
# 12-07-2022
#**************************************************************

#Nested loop
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
y={}
x=int(input("enter how much key and value you need  :"))
for i in range(x):
	key=eval(input("enter key :"))
	value=eval(input("enter value :"))
	y[key]=value
print(y)












