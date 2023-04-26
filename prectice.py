#print("hello world")



# string.copy() its work is do copy the strings

'''x=["one","two","three","four","five"]
y=x.copy()
print(y)
'''


# string.reverse() this function print reverse  string

'''x=["sun","mon","tue","wed","thu"]
x.reverse()
print(x)'''



# string.sort()this function arrange the integer in serial number.

'''x=[5,4,7,2,1,6,9,3,8]
x.sort()		# this function arrange in serial number
print(x)
'''

# string.sort(reverse=True)
#this function arrange the number in dessending order

'''x=[34,56,21,23,87,89]
x.sort(reverse=True)
print(x)'''

'''x=["B","A","D","C","F","E"]
x.sort(reverse=True)
print(x)'''

# string.sort() print in assending order

'''x=[145,102,254,100,524,987,321]
x.sort()
print(x)

x=["B","A","D","C","F","E"]
x.sort()
print(x)'''

# string.index("name") this function show that how many number is on index
'''x=["sun","mon","tue","wed","thu"]
y=x.index("wed")
print(y)'''				# cmd will print 3 number index

'''x=['one','two','three','four','five']
y=x.index('three')
print(y)	'''			# cmd will print  2 number index


'''x=["january","february","march","april","may","june","july","august"]
x.clear()
print(x)
x=[1,4,5,2,3,4]
y=x.index(5)
print(y)'''				# cmd will print 3 number index


# string.clear() this function clear the list.

'''x=["january","february","march","april","may","june","july","august"]
x.clear()
print(x)'''


'''x=[1,5,4,9,8,7,9]
x.clear()
print(x)'''



# input in the list by index

'''x=["sunday","monday","tuesday","wednesday"]
x[2]="prince"
print(x)'''			# it replace no of index by user


'''x=["ass","ant","arm","air","apple","arrow"]
x[0:2]="prince","kumar"
print(x)'''		#cmd print ['prince', 'kumar', 'arm', 'air', 'apple', 'arrow']


'''x=[10,15,48,78,23,56,89,74]
x[2:5]=1,2,3
print(x)'''




# string.count(number or name that reapet)  
# this function count the that number is reapeted more time

'''x=[12,4,5,78,12,36,12,56,12]
y=x.count(12)
print(y)'''			# 12 came in this list 4times




#string.append("str or int") 
#this function add the str or int last off list in index

'''x=["sun","mon","tue","wed"]
x.append("thu")
print(x)'''

'''x=[23,4,54,25,87]
x.append(100)
print(x)'''


# string.insert(index,"str")
#  this function add the str or int  at index number by the user

'''x=["jan","feb","mar","apr","may","jun"]
x.insert(2,"prince")
print(x)'''


'''x=["music","song","photo","list"]
x.insert(1,'video')
print(x)'''




# string.extend(new list) 
#this function is used to add a new list in first list.

'''x=["apple","ball","cat","dog"]
y=["egg","fish","girl","hen"]
x.extend(y)
print(x)

x=["jan","feb","mar","apr","may"]
y=[1,2,3,4]
x.extend(y)
print(x)'''


# string.remove("str") 
# this function is used to remove the index word in list.

'''x=["sunday","monday","tuesday","wednesday","thursday"]
x.remove("monday")
print(x)'''


'''x=[1,2,5,4,8,9,3]
x.remove(3)
print(x)'''

#string.pop(index no. )
#this function is used to remove the index of word.

'''x=['cat','dog','fox','ox','ant']
x.pop(3)
print(x)

x=[12,45,78,23,56,89,89,12]
x.pop(0)
print(x)'''

#del x[] 
#sthis function is used to same as x.pop of work

'''x=["sun","mon","tue","wed","thu"]
del x[2]
print(x)'''			# list in 2nd index tue is removed



'''x=[12,45,78,23,56,89]
del x[3]
print(x)	'''		# list in 3rd index removed 23



#/*/*/*/*/*/*/*/*/*/**/*/*/*/*/*/*/*/*/*/*/***/*/*/*/*///*/*/*/*/*/*/*/*/*/*//**//*//*/*/*/*/*/*/

#29-06-2022

#/*/*/**//**/*/*/*/*/*/*/**/*/*/*/*//*//*///*/*/**/*/*/*/*/*/*/*/**/*/*


#prectice question
# print a list with the help of while and for loop
'''x=["one","two","three","four","five"]
y=len(x)
z=0
while y>z:
	#print(x[z])
	print(x[z],end="   ")
	z+=1'''


#for loop

'''x=["sun","mon","tue","wed","thu","fri","sat"]
for z in x:
	print(z,end=" ")'''


# print a revrse list with the help of for loop and while loop

#for loop reverse print
'''x=["jan","feb","mar","apr","may","jun","jul","aug"]
y=len(x)-1
for v in range(y,-1,-1):
	#print(x[v])
	print(x[v],end="  ")
'''

# while loop reverse print
'''x=["mummy","pappu","priya","prince","priyanshu"]
y=len(x)-1
while y>=0:
	#print(x[y])
	print(x[y],end=" ")
	y-=1'''


#print a list with the help of for loop and wwhile loop by user input
 
									# for loop



'''x=input("write anything\n")
y=x.split()
for v in y:
	print(v)
	#print(v,end=" ")
'''


									#while loop


'''x=input("write anything\n")
y=x.split()
z=len(y)
w=0
while z>w:
	#print(y[w])
	print(y[w],end=" ")
	w+=1'''

# /*/**/*/*/*****************////////////////////***********////////////**********////

#	30-06-2022 prectice in home

#/*/*/*/*/*/*/*/*/*/*/*/*/**************//////////////*//**/*/**************/


'''# cheak if item exists

x=["sunday","monday","tuesday","wednesday"]
print("monday" in x)	# cmd will print "true"
print("saturday" in x)			# cmd will print "false"
print("friday" not in x)		# cmd will print "true"
print("monday" not in x)		# cmd will print "false"

'''
'''x=["one","two","three","four","five"]
if "one" in x:
	print("this is true")
	if "two" in x:
		print("this is true")
'''


'''x=["anr","fish","egg","lion"]
x.reverse()
print(x)'''

	#assending and dessending order program	
	#with the help of x.sort and x.sort(reverse=True)


'''x=[5,4,8,9,3,1,7]
x.sort(reverse=True)
print(x)


x=[5,4,8,9,3,1,7]
x.sort()
print(x)'''


'''x=["jan","feb","mar","apr","may","june"]
y=x.index("mar")
print(y)    # print the si no of index [2]'''


'''x=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
x[1:4]=['january']
print(x)'''




'''x=[[1,2,3],[4,5,6],[7,8,9]]
x.clear()
print(x)'''



'''x=["sunday","monday","tuesday","wednesday"]
#x[2]="prince"
#print(x)
print(len(x))
'''



'''x=34
y=23
if x>y:
	print("this is true")
if y<x:
	print("this is true")'''



'''txt="hello world"
x=txt.strip()
print(txt)'''


'''print(bool("abc"))
print(bool(0))
'''

# write five fruits name in a list by user

'''f1=input("enter fruits name")
f2=input("enter fruits name")
f3=input("enter fruits name")
f4=input("enter fruits name")
f5=input("enter fruits name")
fruits=[f1,f2,f3,f4,f5]
print(fruits)'''

#			(or)

'''fruits = input("write fruits name\n:-")
#fruits.split()
print(fruits.split())
#print(fruits)'''


# write a program to acsept marks of 6 students an display then in shorted manner.

'''m1=int(input("enter marks of student : - "))
m2=int(input("enter marks of student : - "))
m3=int(input("enter marks of student : - "))
m4=int(input("enter marks of student : - "))
m5=int(input("enter marks of student : - "))
m6=int(input("enter marks of student : - "))
my_list=[m1, m2, m3, m4, m5, m6]
my_list.sort()
print(my_list)'''


#write a program to enter the marks of six student with name by user.

'''m1=(input("enter marks of student : - "))
m2=(input("enter marks of student : - "))
m3=(input("enter marks of student : - "))
m4=(input("enter marks of student : - "))
m5=(input("enter marks of student : - "))
m6=(input("enter marks of student : - "))
my_list=[m1, m2, m3, m4, m5, m6]
my_list.sort()cd 
print(my_list)'''

# cheak a tupple that can not be chaged in item.
'''x=(1,5,4,7,8,9)
x[2]=120
print(x)'''

#write a program to sum of 4 number in list

'''x=[12,45,23,56]
#print(sum(x))
print(x[0]+x[1]+x[2]+x[3])
#we have both option'''


# write a program to count the number of zores in the follwing tuple.
'''a=(7,0,8,0,0,9)
b=a.count(0)
print(b)'''

'''x=(input("write any thing"))
y=x.split()
z=len(y)
a=0
while z>a:
	print((y[a]))
	a+=1'''



'''x=(input("write any thing"))
y=x.split()
print(list(y))'''

#///////////////////////////////////////////////////////////////

#04-07-2022 prectice work in list

# x=['apple','banana',['grapes','cherry'],'pineapple','lichi']
# x.insert(2,'prince')
# print(x)
# x[2].insert(3,'orange')	#adding the second list in orange of index 3
# print(x)
# print(x[2])		# it print index 2 only

# x[2].append("prince")
# print(x)			# adding the last of second list
# x.append("maumma")
# print(x)			# adding the last of first list 

# x[2].clear()		# celar the second list
# print(x)
# x[2].append([1,2,3,4])
# print(x)			# adding the 4 int in second list

#x.remove("pineapple")
#print(x)			# removing the 'pineapple'from the list

# x.pop(3)			# removing the str of index 3rd 'pineapple'
# print(x)


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

#*****************/////////////////*****************
# nested list

'''x=['apple','banana',['charry','orange','kiwi'],'melon','mango']
#print(x)
x[2].insert(0,"papaya")
print(x)
'''
'''x=("one","two","three")
y=("sharma",)
x+=y
print(xs)'''


'''x=("one","two","three","four","five","six")
(jan, *feb, march)=x
print(feb)'''


'''x=("one","two","three","four","five")
a=len(x)-1
for y in range(a,-1,-1):
	print(x[y],end=" ")			# reverse print with for loop
'''


'''x=("one","two","three","four","five")
y=len(x)
z=0
while y>z:
	print(x[z],end=" ")
	z+=1'''


'''x=("one","two","three","four","five")
y=len(x)-1
while y>=0:
	print(x[y],end=" ")
	y-=1'''





'''num1=int(input("enter first number\n: -"))
num2=int(input("enter second number\n: -"))
num3=int(input("enter third number\n: -"))
num4=int(input("enter forth number\n: -"))
num5=int(input("enter fifth number\n: -"))
num6=int(input("enter sixth number\n: -"))
num7=int(input("enter seventh number\n: -"))
num8=int(input("enter eighth number\n: -"))
x=[num1, num2, num3, num4, num5, num6, num7, num8]
print(x)
print(type(x))
'''

#  nested list loop

'''x=["one","two",[1,2,3],"three"]
#y=["pk","ch"]
x.insert(0,"prince")
x.insert(1,"kumar")
print(x)

'''

# reverse print by indexing

'''x=["one","two","three","four","five"]
print(x[3:0:-1])
'''




# create a tuple with eight values 
# typecasting

'''x=("jan","feb","mar","apr","may","jun","jul","aug")
y=list(x)
y[1:4]=("prince",)
z=tuple(y)
print(z)'''


'''x=(1,2,3,4,5)
y=("a","b","c","d")
print(x+y)'''



# multiply tuples

'''x=(1,2,3,4,5)
y=x*2
print(y)


x=("a","v","c")
y=x*4
print(y)'''


# intuple remove one item and add two item in the set
'''x=(1,2,3,4,5,6,7,8)
y=list(x)
y[2:3]=(45,84)
x=tuple(y)
print(x)'''




'''x={'prince',"kumar","sharma"}
x.remove('prince')
x.remove("kumar")
x.add("chhotu")
x.discard()
print(x)

'''

#*****************************************************************************************
# join tuple
'''x=(1,2,3,4,5,5)
y=('k','l','i')
print(x+y)
'''
'''x=("prince",1,2)
y=x*3
print(y)'''

'''x=(1,2,4,5,2,1,1,1,11,8,9,8,7,1,)
y=x.count(1)
print(y)
'''

'''x=(1,2,3,4,5,6,7,8,9)
y=x.index(5)
print(y)
x=("a","b","c","d","e","f")
y=x.index("c")
print(y)'''


'''x=('one','two','three','four','five')
y=list(x)
y[2:3]=('prince','kumar')
x=tuple(y)
print(x)'''

'''x=('one','two','three','four','five')
y=list(x)
y.insert(2,'prince kumar')
x=tuple(y)
print(x)




x=('one','two','three','four','five')
y=list(x)
y.append('prince')
x=tuple(y)
print(x)'''



'''x=('one','two','three','four','five')
y=list(x)
y.remove("five")
#y.pop()
x=tuple(y)
print(x)
'''
'''x=('one','two','three','four','five')
a,b,c,d,e=x
print(c)
print(e)'''

'''x=("one","two","three","four","five","six","seven","eight")
y=list(x)
y.insert(3,"prince")
x=tuple(y)
print(x)'''



'''x=("one","two","three","four","five","six","seven","eight")
y=list(x)
y=y[-1::-1]
#y.reverse()
x=tuple(y)
print(x)'''


#set
'''set={"mark","one","prince","sahrma","kumar","prince"}
print(set)'''



'''set={"mark","one","prince","sahrma","kumar","prince",123,321,45.45,89.45,true}
print(set)
'''

'''x=set()
x.add(5)
x.add("prince")
print(x)'''


'''x=set(("prince","kumar",85,98.2,"prince"))
print(x)
'''

'''x={"sunday","monday","tuesday"}
for y in x:
	print("this is true")
'''
'''x={'sunday','monday','tuesday'}
y=[1,2,3,1.2,1]
x.update(y)
print(x)'''


'''a=set()
x={'sunday','monday','tuesday'}
y=[1,2,3,1.2,1]
a.update(y,x)
print(a)'''


'''x={'wednesday','sunday','saturday',34}
x.remove("sunday")
print(x)'''


'''x={'sunday','monday','tuesday'}
#y=[1,2,3,1.2,1]
x.add("prince")
print(x)'''


'''x={'sunday','monday','tuesday'}
#x.clear()
del x
print(x)'''




'''x={"sunday","monday","tuesday","wednesday","thursday","friday","saturday"}
y={"sunday","monday","tuesday","january","february","march"}
h=x.intersection(y)
print(h)'''






'''x={"one","two","three","four"}
y={1,2,3}
x.update(y)
print(x)'''


'''x=set()
x.add("prince")
x.add("kumar")
x.add(100)
print(x)

'''

'''x={"ant","aple","axe","arrow"}
y={1,2,3,"hello"}
x.update(y)
a={"prince","kumar"}
z=x.union(a)
print(z)'''



'''x={"ant","aple","axe","arrow","prince","kumar"}
x.remove("ant")
x.discard("aple")
y=x.pop()
print(y)
print(x)'''



'''students={"name": "prince kumar","home": "bihar","age": 23}
print(students)
print(type(students))
print(len(students))'''



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
"odisha":"bhubaneswar"
}
x=input("enter state name :-\n")
print("the capital of",x,"is",state_capital[x])
#print(state_capital.keys())
#print(state_capital.values())
'''

# In a list, the fruit has been named in which "a" is available
# print  in a new list


'''fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)'''

#In a list, the animals has been named in which "o" is available
# print  in a new list




'''animals=["dog","fox","lion","tiger","camel","cat","wolf","zebra"]
o_animals=[]
for x in animals:
	if "o" in x:
		o_animals.append(x)
print(o_animals)
'''


'''myDict={
"ram": "sita",
"shiv": "parvati",
"ramayana": "mahabharat",
}
myDict["princes"]="princeeeee"
#myDict.update({"prince": "kumar"})
#if "ram" in myDict:
#	print("yes ram in myDict")
print(myDict.keys())'''


'''Dict={
"fire":"water", "water": "fire","up":"down","come": "go",
"hii": "byy"
}

Dict.update({"hii":"bihar"})
print(Dict.keys())
print(Dict.items())'''

# remove the string fromm dict


'''dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict.pop("model")
dict.popitem()
del dict["brand"]
print(dict)'''


'''myDict={
"flower": "rose",
"fruits": "apple",
"orange": "fruits",
"name": "prince kumar",
"home": "bihar",
"dog": "animal"
}
del myDict["dog"]
myDict.popitem()
myDict.




print(list(myDict.items()))'''


# if, elif and else
'''age=int(input("enter a number:-\n"))
if (age>30) and (age<50):
	print("you can work in my company in",age,"year")
elif (age>18 or age==18):
	print("you can learn in my company in",age,"year,")
else:
	print("you can't work in my company in",age,"year")

'''



'''a=None
if (a is None):
	print("yes")
else:
	print("no")




x=[12,45,78,89,56,23]
print(45 not in x)
print(23 in x)
for y in x:
	print(y)'''




'''x= eval("enter a number")
print(x)
'''

'''a=[1,2,3]
b=a
print(a is b, a==b)		# true true
'''

#write a program to find greatest of four number entered by user.

'''num1=int(input("enter first number:-"))
num2=int(input("enter second number:-"))
num3=int(input("enter third number:-"))
num4=int(input("enter forth number:-"))
if num1>num4:
	x=num1
else:
	x=num4

if num2>num3:
	y=num2
else:
	y=num3
	
if x>y:
	print("greatest number is",x)
else:
	print("greatest number is",y)'''


# write a program to find weather a given  username contains less than 10 charactor or not.
'''x=str(input("enter any charactor:-\n"))
y=len(x)==10
print(y)'''



# write a program which find out wweather a given name is present in a list or not.
'''x=["prince","ankit","kumod","ram","yanshu"]
if "prince" in x:
	print("yes")
else:
	print("no")
'''



# create a live triangle with 3D shape

'''import turtle
n=10
pen=turtle.Turtle()
for i in range(n*3):
	pen.forward(i*10)
	pen.right(120)
turtle.done()'''

# create a live square with 3D shape

'''import turtle
n=10
pen=turtle.Turtle()
for i in range(n*3):
	pen.forward(i*10)
	pen.right(90)
turtle.done()'''





'''import turtle
n=10
x=turtle.Turtle()
for i in range(n*3):
	x.forward(i*10)
	x.right(170)
turtle.done()'''


'''
import turtle
n=20
x=turtle.Turtle()
for i in range(n*3):
	x.forward(i*10)
	x.right(170)
turtle.done()'''


#  like star 

'''import turtle
n=20
x=turtle.Turtle()
for i in range(n*3):
	x.forward(i*10)
	x.right(160)
turtle.done()'''


'''myDict={"name": "prince","age": 32,"home":"bihar","work": "student"}

print(myDict["name"])'''

'''
faimly={
	"mother name": "mamta devi",
	"brother name": ["pappuu kumar","pryanshu kumar"],
	"sister": "priya sharma"
}

#print(faimly.keys())
#print(faimly.values())
#print(faimly.items())
print(faimly.get("mother name"))
'''



'''z={}
x = int(input("Enter any number: "))
y = 0
while y<x:
	keys=str(input("Enter any key: "))
	values = eval(input("Enter any value: "))
	z[keys]=values
	y+=1
print(z)
'''

'''z={}
x= int(input("enter any number:-"))
y=0
while x>y:
	keys=str(input("enter any key:-"))
	values=input("enter any value:-")
	z[keys]=values
	y+=1
print(z)'''

#print dic with the help of for loop

'''z={}
x=int(input("enter any number: -"))
for i in range(0,x):
	keys=str(input("enter any name:-"))
	values=input("enter any value:-")
	z[keys]=values
print(z)'''

#print the dicctionary with the help of whwile loop
'''
z={}
x=int(input("enter any number: -"))
y=0
while x>y:
	keys=str(input("enter any key:-"))
	values=eval(input("enter any values: -"))
	z[keys]=values
	y+=1
print(z)'''



# to print aet eith the help of while loop
'''z=set()
x=int(input("enter any number: -"))
y=0
while x>y:
	set=eval(input("enter any set:-"))
	z.add(set)
	y+=1
print(z)
'''

 # create a prime number with the help of for loop by user.

'''num=int(input("enter any number:- "))
prime = True
for i in range(2,num):
	if (num%i==0):
		prime=False
		break
if prime:
	print("this number is prime")
else:
	print("this number is not prime")
'''

'''# create a factorail program with the help of for loop

num=int(input("enter any number: -"))
factorial=1
for i in range(1,num+1):
	factorial=factorial*i
print("the factorail of",num,"is",factorial)'''




# pattern program

'''x=int(input("enter any number: -"))
for y in range(0,x+1):
	for z in range (y):
		print("*",end=" ")
	print()


'''
'''x=4
for i in range(x):
	print("*"*(i+1))
print( )
'''
#  	  *
#    ***
#   *****
#  *******
# *********


'''x=5
for i in range(5):
	print(" "*(x-i-1),end=" ")
	print("*"*(2*i+1),end=" ")
	print(" "*(x-i-1))'''



'''def add(a,b):
	print(a+b)

def sub(a,b):
	print(a-b)

def mul(a,b):
	print(a*b)

mul(5,6)
add(5,15)
sub(14,10)'''


#make functions with two and three arguments and apply all airthmetic operations on it

'''def add(a,b):
	print(a+b)

def sub(c,d):
	print(c-d)

def mul(e,t):
	print(e*t)

mul(5,6)
add(5,15)
sub(14,10)'''


'''def prince(a,b,c,d,e):
	print(a+b*c/d-e)

def avg(a,b,c,d,e):
	print((a+b+c+d+e)/5)

prince(2,4,10,5,6)
avg(12,10,8,6,4)
'''
# make functions with two and three arguments and apply all airthmetic operations on it

'''def prince(a,b,c,d,e):
	print(a+b*c/d-e)

def avg(a,b,c,d,e):
	x=(a+b+c+d+e)/5
	print(x)

def simp(a,b,c,d,e):
	print((a*b*c)/d-e)

prince(2,4,10,5,6)
avg(12,10,8,6,14)
simp(2,4,10,5,6)'''




'''t=turtle.Turtle()
s=turtle.screen().bgcolor('black')
t.speed(0)
n=70
h=0
for i in range(360):
	c=colorsys.hsv_to_rgb(h, 1, 0.8)
	h+=1/n
	t.color(c)
	t.left(1)
	t.fd(1)
	for j in range(2):
		t.left(2)
		t.circle(100)'''


# create a function with the help of user input.

'''def d():
	a=int(input("enter any number: -"))
	b=int(input("enter any number:-"))
	print(a*b*a*b)
d()
d()'''

# create a function with the help of user input.

'''def p():
	x=int(input("x = "))
	y=int(input("y = "))
	z=int(input(" z = "))
	print("the multiplication of x*y*z is :-",x*y*z)
	print("the sum of x+y+z is : -",x+y+z)
	print("the sub of x-y-z is",x-y-z)
p()'''



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




# print by even number in function by user input
'''
def even(x):
	y=0
	z=0
	while x>y:
		z+=1
		if z%2==0:
			print(x,"even number is:-", z)
			y+=1

even(int(input("enter number:-")))
'''
'''

from turtle import *


speed(0)
bgvoolor("black")
color("white")
hideturtle()

n=1
p=True

while True:
	circle(n)
	if p:
		n=n-1
	else:
		n=n+1

	if n==0 or n==60:
		p=not p

	left(1)

done()
'''
# default perameter
'''def satia(a,b):
	pass
def x(city="delhi"):
	print("I live in",city)

x("madrash")
x("london")
x()
x()
x("begusarai")


def os(vaya="teghra"):
	print("i live in",vaya)

os("pidhsuli")
os("begusarai")
os()
os()


#default perameter

def  x(name="prince"):
	print("My name is",name)

x()
x("chhotu kumar")
x("priya sharma")
x()
x("pappu kumar")



def c(fun="power"):
	print("this is the fundamental program",fun)

c("victory")
c()
c()
c("i love you")


def x(company="prince pvt ltd"):
	print("the name of my company is",company)

x()
x()
x("prince software service tech")
x("chhotu pvt ltd")
x("mamta industry pvt ltd")'''



# return values


'''
def y(x):
	return x*5
print(y(4))


def cv(t,r):
	return 3*t,4*r
print(cv(4,2))


def pk(x,y,z):
	return 4*x,3*y,8*z
print(pk(2,5,8))


def c(delhi="scientist"):
	print("i am",delhi)

c()
c("prince")
c("cooder")
c()
c("web devlolper")


def x(a,b,c):
	return 7*a, 5*b, 6*c
print(x(3,4,5))


def v(z,x,c):
	return 7*z, 8*x, 5*c
print(v(4,56,8))




x= lambda a,b,c:a+b+c
print(x(4,5,6))

prince= lambda a,s,d,f:a*s-d/f*d+a+s+d+f
print(prince(12,45,78,13))

def x(a,b):
	return 4*a,8*a,7*b
print(x(4,5))


x=[]
num=int(input("enter any number:-"))
y=0
while num>y:
	value=eval(input("write the value of list:-"))
	#value="prince","kumar","sharma",456
	x.append(value)
	y+=1
print(x)


c=[]
x=int(input("enter any number:-"))
for i in range(x):
	value=eval(input("write any value:-"))
	c.append(value)
print(c)


a={}
x=int(input("enter a number:-"))
for i in range(x):
	key=str(input("enter key:-"))
	value=eval(input("enter value:-"))
	a.update({key:value})
print(a)


def odd(x):
	y=0
	for i in range(1,x*2,2):
		print("odd number",i)

		y=y+i
	print(y)

odd(int(input("enter odd number:-")))

'''


'''
y=lambda a,b,d,r:a+b-d*r
print(y(5,4,6,3))


def x(name="prince"):
	print("my name is",name)

x()
x("sharmaji")
x("sirji")

g= lambda a: a
print(g("ram"))'''



# python zip function

'''x=("ram","mohan","sita")
y=("sita","mira","baap")
z=zip(x,y)'''
#print(list(z))
#print(dict(z))
#print(set(z))
#print(tuple(z))



#prime number
#from math import sqrt
'''def isprime(n):
	if n<=1:
		return False

	for i in range(2,n+1):
		if n%i==0:
			return False

		return True

if isprime(int(input("enter a number:-"))):
	print("prime number")
else:
	print("not a prime number")'''

'''x={
"name": "prince",
"job": "tech",
"home":"bihar"
}	
x.popitem()
print(x)'''

'''x={"prince","kumar","sharma","moj","tikk","tokk"}
y=x.pop()
x.discard("prince",)
x.remove("sharma")
#print(x)
print(y)'''




'''def x(t):
	for i in range(1,11):
		print(i,"x",t,"=",i*t)

x(int(input("enter any table:")))


def x(t):
	if t<=1:
		return=False
	elif t'''


'''n = int(input())
if n % 2:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")'''


# leap year finding program  which year is leap year
'''def leap(year):
	if (year%400==0) or (year%100!=0 and year%4==0):
		print("leap year")
	else:
		print("not leap year")
    
    # Write your logic here

leap(year = int(input("write")))'''



# find a program from 1900 to 2020 how many leap year
'''
x=0
for i in range(1900,2021):
	if (i%400==0) or (i%4==0 and i%100!=0):
		print("leap year :",i)
		x=x+1
print("from 1900 to 2020 in",x,"leap year")'''

'''def is_leap(year):
    return (year%4==0) or (year%400==0 and year%100!=0)

year = int(input())
print(is_leap(year))'''



'''def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)'''



#**************************************************************************
#	chepter 	 oops  class in python
#*******************************************************************************



'''class x:
	def y(self):
		print("hello world")
z=x()
z.y()'''
'''

class prince:
	a=4
	b=5
	c=a+b
d=prince()
print(d.c)

class pk:
	p=12
	q=13
	r=14
	s=15
	t=p+q+r+s
u=pk()
print(u.t)


class math:
	a=456
	b=789
	c=213
	d=a+b-c
e=math()
print(e.d)



class simp:
	a=23
	b=23
	c=23
	d=a+b+c
e=simp()
print(e.d)'''



'''
class m:
	def x(self,a,b):
		self.a=a
		self.b=b
		self.c=a+b
d=m()
d.x(5,8)
print(d.c)'''


'''
class x:
	def y(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		self.d=a+b+c
p=x()
p.y(4,6,8)
print(p.d)

class th:
	def sub(self,a,b,c,d):
		self.a=a
		self.b=b
		self.c=c
		self.d=d
		self.e=b+a/c*d-a-d
		self.f=(a+b+c+d)/4

g=th()
g.sub(15,10,12,4)
w=g.e
x=g.f
print("simplification :",w)
print("average :",x)'''

'''
class mint:
	def x(self,name,home,state):
		self.name=name
		self.home=home
		self.state=state
p=mint()
p.x("prince kumar","begusarai","bihar")
print("my name is :",p.name)
print("i live in :",p.home)
print("my state name is :",p.state)

class m:
	def n(self,a,b):
		self.a=a
		self.b=b
		self.c=a+b
o=m()
o.n("prince ","kumar")
print(o.c)

class t:
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c

#ts=t("ram","kam","ass")
ts=t(12,10,5)
print(ts.a+ts.b+ts.c)


class x:
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		self.d=b**c
	def p(self):
		print("my name is :",self.a)
y=x("prince",12,3)
y.p()
print(y.d)


class l:
	def pk(self,name,num1,num2):
		self.name=name
		self.num1=num1
		self.num2=num2
		self.mix=(name,num1+num2)
	def pr(self,num3,num4):
		self.num3=num3
		self.num4=num4
		self.mod=num3%num4


	def pi(self,num5,num6):
		self.num5=num5
		self.num6=num6
		self.floor=num5//num6

	def pn(self,num7,num8):
		self.num7=num7
		self.num8=num8
		self.add=num7+num8+num7+num8

x=l()
x.pk("prince",12,8)
print("mixing :",x.mix)
x.pr(127,15)
print("module :",x.mod)
x.pi(159,16)
print("floor divison :",x.floor)
x.pn(12,10)
print("adding :",x.add)


class m:
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		self.d=a*b*c
		self.e=a+b+c
t=m(24.6,20.4,12)
print(t.d)
print(t.e)


class x:
	def pk(self,name,mother):
		self.name=name
		self.mother=mother
cs=x()
cs.pk("prince kumar","mamta devi")
print("hi this is :",cs.name)
print("my mother name is :",cs.mother)



class person:
	def x(self,a,b,c,d):
		self.a=a
		self.b=b
		self.c=c
		self.d=d
		self.simp=a*d+c/b-a

pas=person()
pas.x(12,10,60,5)
print("simplification :",pas.simp)


class v:
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		self.d=a+b+c
	def y(self):
		print("second function :",self.b)

x=v("hello \ni am ","prince kumar ","\nfrom bihar ")
x.y()
print(x.d)
#x.y()
'''

'''class math:
	def x(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		self.d=(a+b)/c
		self.e=(a+b+c)/3
pk=math()
pk.x(9,6,3)
print(pk.d)
print(pk.e)'''





# modify objects properties
'''
class math :
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def x(self):
		print("My name is",self.name)

y=math("chhotu",120)
y.x()
print("i am",y.age,"year old")



# using the del meyhod to delete the class in arguments

class srt:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		#self.c=a+b
	def x(self):
		print("hii i am",self.a)

	def z(self):
		print("i like coading :",self.b)


y=srt("chhotu sharma"," python")
y.x()
y.z()
#del self
print(y.a+" "+y.b)


creat a class and make three method in this class in first method do exponents
in second method print any statement and in third method find the modules. take diffrent arguments for 
all method , and __init__function in this use


class math:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a+b*a-b

	def x(self,d,e):
		self.d=d
		self.e=e
		self.f=d**e

	def y(self,g,h):
		self.g=g
		self.h=h
		self.i=g/h+g/h

z=math(15,10)
print("simplify :",z.c)

z.x(3,4)
print("exponents :",z.f)

z.y(10,5)
print("princify :",z.i)


class math:
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		self.d=a%b*c

	def x(self,e,f,g):
		self.e=e
		self.f=f
		self.g=g
		self.h=e+f-g+e+f+f

	def y(self,i,j,k):
		self.i=i
		self.j=j
		self.k=k
		self.l=(i*j*k)/j+k
	def z(self,m,n,o):
		self.m=m
		self.n=n
		self.o=o
		self.p=m%n+o-m*n

ans=math(87,9,5)
print("frist method :",ans.d)

ans.x(12,45,56)
print("second method :",ans.h)

ans.y(12,10,4)
print("third methods :",ans.l)

ans.z(79,12,14)
print("forth methods :",ans.p)


creat a class and make three method in this class in first method do exponents
in second method print any statement and in third method find the modules. take diffrent arguments for 
all method , and __init__function in this use


class math:
	def __init__(self,a):
		self.a=a
		b=1
		while b<11:
			print(a,"x",b,"=",b*a)
			b+=1



	def x(self,p,q):
		self.p=p
		self.q=q
		self.r=q**p

prince=math(int(input("enter table :")))

prince.x(4,5)
print("\nexponents :",prince.r)


# print table and multipule in class __init__ def function by user input

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



# example of single level inheritance


class parents():
	def first(self):
		print("\nwelcome to this world")
class child(parents):
	def second(self):
		print("i am so lucy \nbecause god gifted me like \nkind mother")

x=child()
x.first()
x.second()


class prince():
	def first(self):
		print("\nwelcome to this world my dear")

class chhotu(prince):
	def second(self):
		print("\nand love with nature not with dust")

x=chhotu()
x.first()
x.second()
'''

'''class prince():
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		self.d=a+b+c

class chhotu(prince):
	def x(self,p,q,r):
		self.p=p
		self.q=q
		self.r=r
		self.s=q+p*r

al=chhotu(12,4,6)
print(al.d)

al.x(4,5,6)
print(al.s)'''



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
class parents():
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		self.d=a+b+c

class child(parents):
	def x(self,p,q,r):
		self.p=p
		self.q=q
		self.r=r
		self.s=q*p*r

y=child(12,4,23)
print("addition :",y.d)

y.x(4,6,45)
print("multiply :",y.s)'''

'''
class m():
	def __init__(self,a,b,c,d):
		self.a=a
		self.b=b
		self.c=c
		self.d=d
		self.e=a+b+c+d
		self.g=a*b+c/d-a/c*d
		self.f=(a+b+c+d)/4

class n(m):
	def x(self):
		print("addition x function :",w.e)

	def y(self):
		print("The simplification x function :",w.g)

class o(n):
	def z(self,p,r,q):
		self.p=p
		self.r=r
		self.q=q
		self.v=p%q*r

w=o(12,10,14,20)
w.x()
w.y()
print("The average of function x :",w.f)

w.z(47,12,4)
print("the module of function z :",w.v)
'''
'''class m():
	def __init__(self,a,b,c,d):
		self.a=a
		self.b=b
		self.c=c
		self.d=d
		self.e=a+b*c*d

	def x(self):
		print("Hello welcome to this world")
class n(m):
	def y(self,p,q,r,s):
		self.p=p
		self.q=q
		self.r=r
		self.s=s
		self.t=q/p*r-s

	def z(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
		self.d=a*b-c

pk=n(12,9,8,10)
print("this is simplification :",pk.e)
pk.x()
pk.x()
pk.y(12,144,10,20)
print("this math solution :",pk.t)

pk.z(12,8,25)
print("math x and- function :",pk.d)



def x():
	a=int(input("enter a number :"))
	b=int(input("enter a number :"))
	print(a+b)
	print(a*b)
	print(a/b)
	print(a-b)

x()'''


# print by user input
'''class x:
	def __init__(self):
		a=int(input("enter a number :"))
		b=int(input("enter a number :"))
		c=int(input("enter a number :"))
		self.a=a
		self.b=b
		self.c=c
		self.c=a+b+c
		self.d=a*b*c
	def q(self):
		print("module :",y.a%y.b)

y=x()
print(y.c)
print(y.d)
y.q()'''




'''
class Person:

	def __init__(self, fname, lname):
    	self.firstname = fname
    	self.lastname = lname
​
  	def printname(self):
    	print(self.firstname, self.lastname)
​
class Student(Person):
  pass
​
x = Student("Mike", "Olsen")
x.printname()
​


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age)'''


#print("hello world")
'''from abc import ABC
class prince(ABC):
	def first1(self):
		pass

class per(prince):
	def first(self,a,b):
		self.a=a
		self.b=b
		self.c=a+b
	def second(self):
		r="pRINCE KUMAR"
		#rk=r.swapcase()
		#print(rk)
		#or
		print(r.swapcase())

x=per()
x.first(4,5)
print(x.c)
x.second()'''

'''
class math:
	def f1(self):
		print(f"Now created this program to solve area and perimeter of circle")
	def circle(self):
		a=22/7
		r=int(input("radius is :-"))
		self.area=a*r*r
class math1(math):
	def circle1(self):
		a=22/7
		r=int(input("radius is :-"))
		self.perimeter=2*a*r

pk=math1()
pk.f1()
pk.circle()
print(f"The area of circle is {pk.area}")
pk.circle1()
print(f"the perimeter of circle is {pk.perimeter}")'''



#create a program to find the curved surface area and volume of cylinder
'''from abc import ABC
class math(ABC):
	def asd(self):
		pass

class cylinder(math):
	def c_area(self):
		py=22/7
		r=int(input("if radius is :-"))
		h=int(input("and height is :-"))
		self.area=2*py*r*h

	def vol(self):
		py=22/7
		r=int(input("radius is :-"))
		h=int(input("radius is :-"))
		self.volume=py*r*r*h

x=cylinder()
x.c_area()
print(f"The curved surface area of cylinder is: {x.area}")
x.vol()
print(f"The volume of cylinder is: {x.volume}")
'''


'''
from math import pi
r=int(input("input the radius :"))
area=pi*r**2
#print("the are of circle with radius"+str(r)+ "is: " +str(pi * r**2))
print("the area of circle with radius is",area)'''




#'%.2f%s'%(1.81425,818)


#perimeter is 44 find raadius

'''pera=float(input("if the circle of perameter is :-"))
pi=22/7
radius=pera/(pi*2)
print(f"the circle which perameter is {pera} of radius is {radius}")'''


'''
import math
x=float(input("enter square number"))
y=math.sqrt(x)
print(y)'''


# watch the number is prime or not prime
'''
import math
def check(n):
	if n==1:
		return False
	for x in range(2,(int)(math.sqrt(n))+1):
		if n%x==0:
			return False
	return True

n=int(input("enter number ="))
if check(n):
	print("prime")
else:
	print("not prime")'''


'''
n=int(input("enter the number"))
prime=False
for i in range(2,n):
	if n%i==0:
		prime=True
		break
if prime:
	print("the number is prime")
else:
	print("not prime")
'''

'''
n=int(input("enter a number"))
if n>1:
	for i in range(2,int(n/2)+1):
		if n%i==0:
			print(f"{n} is not prime")
			break
	else:
		print(f"{n} is prime")
else:
	print(f"{n} is not prime")'''


 # create two class and make in first class in first method cheak the prime number 
#and second class in factorial 

'''class math:
	def __init__(self):
		n=int(input("enter the number: "))
		if n>1:
			for i in range(2,int(n/2)+1):
				if n%i==0:
					print(f"{n} is not prime number")
					break
			else:
				print(f"{n} is prime number")

		else:
			print(f"{n} is not prime number")

class math1(math):
	def __init__(self):
		super().__init__()
		x=int(input("enter any number"))
		fact=1
		for i in range(1,x+1):
			fact=fact*i
		print(f"{x} of factorial is :{fact}")

class math2(math1):
	def __init__(self):
		super().__init__()
		t=int(input("enter table :"))
		r=1
		while r<11:
			print(f"{r} x {t} = {r*t}")
			r+=1


y=math2()'''

'''n=int(input("enter a number :- "))
a=2
while a<int(n/2):
	if n%a==0:
		a+=1
		print(f"{n} is not a prime")
		break
else:
	print(f"{n} is prime")'''
'''
print("hello world")
x=int(input("enter a number : "))
y=2
while int(x/2)>y:
	y+=1
	if x%y==0:

		print("not prime number")
		break
else:
	print("prime number")
'''


'''
x=int(input("enter number"))
pi=22/7
area=pi*x**2
print(int(area))'''

#find the program of factorial number while loop
'''
x=int(input("enter a number"))
y=1
fact=1
while y<=x:
	fact=fact*y
	y+=1
print(f"{x} of factorial is :{fact}")

#find the factorial by for loop
x=int(input("enter a number"))
fact=1
for i in range(1,x+1):
	fact=fact*i
print(f"{x} of factorial is {fact}")
'''

#prime number by while loop
'''x=int(input("enter any number"))
y=2
while y<=int(x/2):
	y+=1
	if x%y==0:
		print("number is not prime")
		break
else:
	print("number is prime")'''
'''
def is_leap(year):
    if (year%400==0) or (year%100!=0 and year%4==0):
        #print("is_leap")
        return True
    else:
    	#print("False")
    	return False
#is_leap(int(input()))
year=int(input("year"))
#print(is_leap(year))
print(is_leap(year))
'''
'''x=int(input("enter a number"))
y=int(input("enter a number"))
z=int(input("enter a number"))
n=int(input("enter a number"))
prince=[]
for i in range(x+1):
	for j in range(y+1):
		for k in range(z+1):
			if i+j+k!=n:
				prince.append([i,j,k])
print(prince)'''
'''
X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

X += 1
Y += 1
Z += 1

tmp_list = [[x, y, z] for x in range(X) for y in range(Y) for z in range(Z) if x + y + z != N]
print(tmp_list)

'''

'''
x=int(input())
y=int(input())
z=int(input())
N=int(input())
ans=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k!=N:
                ans.append([i,j,k])
print(ans)'''



#Given the participants score sheet for your University Sports Day,
 #you are required to find the runner-up score. You are given  scores. 
# Store them in a list and find the score of the runner-up.

#x=int(input("enter a number"))
'''y=map(int,input("enter anumber").split())
lst=list(y)
scores=list()
for score in lst:
	if score not in scores:
		scores.append(score)
	else:
		continue
print(scores)
scores.sort(reverse=True)
print("runner up of the univesity :",scores[1])
#order=sorted(scores,reverse=True)
#print(order[1])'''




'''
n=input("hiiii")
list1=n.split(' ')
for i in list1:
    print(i.capitalize(),end=' ')
'''
#print('1'+'2')

#inheritance in polymorphism
'''
class Bird:
	def intro(self):
		print("There are many types of birds.")
	
	def flight(self):
		print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
	def flight(self):
		print("Sparrows can fly.")
	
class ostrich(Bird):
	def flight(self):
		print("Ostriches cannot fly.")
def test(self):
  self.intro()
  self.flight()
  
#obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

#test(obj_bird)
test(obj_spr)
test(obj_ost)'''
'''
x=map(int,input("enter scores :").split())
y=list(x)
y.sort(reverse=True)
print(y)
print(f"runner-up in this university {y[1]}")'''

#polymorphism in opps
'''class math:
	def first(self):
		print("in this subject we solve math question")
	def second(self):
		print("and calculating the integer and float number")
class hindi:
	def first(self):
		print("this subject is for read the story")
	def second(self):
		print("And learn to speak in hindi and solveing the word problem")
class science:
	def first(self):
		print("this subject is for precticallly learn about elements")
	def second(self):
		print("And with the help of this subject do invetion of any machine")
m=math()
h=hindi()
s=science()
for i in (m,h,s):
	i.first()
	i.second()'''
	
#data abstraction method
'''from abc import ABC
class prince(ABC):
	def first(self):
		pass

class math(prince):
	def first(self):
		print("math is main subject for me i have done honors in math")
class hindi(prince):
	def first(self):
		print("hindi is my mother tongue language in our country")
class english(prince):
	def first(self):
		print("English is globel language and we should learn this language")
class sst(prince):
	def first(self):
		print("Social studies we learn historical accsedent of by king")

m=math()
#m.first()
h=hindi()
#h.second()
e=english()
#e.first()
s=sst()
#s.first()
for i in (m,h,e,s):
	i.first()'''
'''
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

print("You owe",tax,"Rupees in tax!")'''

'''
from abc import ABC
class main(ABC):
	def good(self):
		pass
class animal(ABC):
	def dog(self):
		print("dog is braking")
class animal1(ABC):
	def cat(self):
		print("cat is mewing")

class animal2(ABC):
	def lion(self):
		print("lion is roaring")

a=animal()
a1=animal1()
a2=animal2()
a.dog()
a1.cat()
a2.lion()'''

'''class main:
	def __init__(self):
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
		super().__init__()
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
ob=main_1()
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
	print("weldone prince")
'''
'''
import matplotlib.pyplot as pyplot
x_values=list(range(11))
squares=[x**2 for x in x_values]
cubes=[x**3 for x in x_values]

fig,axs=plt.subplots(2,1, sharex=True)

axs[0].scatter(x_values,squares)
'''

# this method is used to read the file of your pc or leptop
'''x=open("pri.py","rt")
print(x.read())'''

#this method is used to read the charactor by input in file of your
#leptop
'''
file=open("pri.py","r")
print(file.read(50))'''


#this method is used to read the one line by one print option 
'''x = open("pri.py","r")
print(x.readline())
print(x.readline())
print(x.readline())'''


#this method is used to append or add the text in the file 
#and we create a new file not in my system
'''
x=open("pri2.py","a")
x.write("\ni want to become a ideal person in my life")
x.write("\n file handling is an an important chepter for web application")
x=open("pri2.py","r")
print(x.read())
x.close()'''


#this method is used to replace the of all  the data in new data by me that 
#give in method like(x.write("failure is the paart of sucsess")) this

'''x=open("pri2.py","w")
x.write("prince kumar\t\tsharma")
x=open("pri2.py","r")
print(x.read())'''


#this method is used to create a new file and add text 
'''
x=open("pri3.py","x")
x=open("pri3.py","w")
x.write("\n\n\nmilk gives us cow")
x.close()
x=open("pri3.py","r")
print(x.read())'''



'''python delete file

To delete a file , you must import the os  module, and run its os . remove() function()
example
remmove the file"xyz.py":'''

#import os
#os.remove("xyz.py")'''



#import os
#os.remove("pri2.py")
#os.remove("pri1.py")
#os.remove("pri3.py")

'''
import math
x=float(input("enter square number"))
y=math.sqrt(x)
print(y)'''


#import datetime
#x = datetime.datetime.now()
#print(x)
'''
import datetime
print(datetime.datetime.now())

y=[]
x=int(input("enter number"))
for i in range(x):
	name=input("write name :")
	score=int(input("enter score:"))
	y+=[[name,score]]
y.sort()
print(y)




result=[]
scorelist=[]
x=int(input())
for i in range(x):
    y=input()
    z=float(input())
    result+=[[y,z]]
    scorelist+=[z]
b=sorted(list(set(scorelist)))[1]
for a,c in sorted(result):
    if c==b:
        print(a)'''


#*************************************************************************************
# you tube
#********************************************************************************
'''x=[56,78,89,45,76]
avg=(sum(x)/5)
print(f"Average of {x} this number is {avg}")'''

'''
marks=[78,86,72,70,90]
persent=((sum(marks)/500)*100)
print(f"persantage of this marks {persent}%")
'''
'''x=[]
m=int(input("enter the subject :"))
for i in range(m):
	mark=int(input("enter marks :"))
	x.append(mark)
per=((sum(x)/500)*100)
print(f"persantage of the marks is {per}%")'''


#in dictionary print the sub name with number and find average of marks.
'''
x={}
m=int(input("enter the subject :"))
for i in range(m):
	sub=input("enter subject :")
	mark=int(input("enter marks :"))
	x.update({sub:mark})
#per=((sum(x)/500)*100)
#print(f"persantage of the marks is {per}%")
print(sum(x.values())/m)'''


#find the average of this list and find.
'''x=[56,45,23,68]
y=((x[0]+x[1]+x[2]+x[3])/4)
print(y)'''

'''
def avg(x):
	#marks=((x[0]+x[1]+x[2]+x[3])/4)
	marks=(sum(x)/4)
	return marks

n=[]	
for i in range(3):
	m=int(input("enter marks :"))
	n.append(m)
# calling the function with the help of loop
y=avg(n)
print(y)
'''
'''def greet(name):
	f="good morning" + name
	return f
v=greet("prince")
print(v)


def x(name):
	print("good morning"+ "",name)

x("prince")'''


# by default argument
'''def frist(name="prince"):
	print(f"good morning {name}")

frist()
frist("chhotu")'''

#factorial program in function
'''def fact(x):
	p=1
	for i in range(1,x+1):
		p=p*i
	print(p)
fact(5)'''

#	or with the formulae
'''
def fact(x):
	if x==1 or x==0:
		return 1
	else:
		return x*fact(x-1)
f=fact(5)
print(f)
'''
# print list with the help of user input
'''
list1=[]
while True:
	n=eval(input("enter the number :"))
	list1.append(n)
	choice=input("if you want to stop the list press yes  :")
	if choice=="yes":
		break
print(list1)'''

'''x=input("write elemetns with space :")
y=x.split()
print(y)'''
'''
x=input("enter a number :")
y=input ("enter a number :")
sum=int(x)+int(y)
print("The sum of two number is:"+str(sum))
'''
'''x="prince kumar"
print(x.upper())
print(x.lower())
print(x.find('k'))
print(x.find('kumar'))
print(x.replace('kumar','sharma'))
y=x.replace('prince','chhotu')
print(x)
print(y)
print("k" in x)
print("o" in x)
print(not 5>10)
print(12<10)'''

# mini caluculator program

'''first=input("enter number :")
operator=input("enter operator(+,-,*,/,**,//,%) :")
second=input("enter second number :")
first=float(first)
second=float(second)

if operator=="+":
	print(first+second)
elif operator=="-":
	print(first-second)
elif operator=="*":
	print(first*second)
elif operator=="/":
	print(first/second)
elif operator=="%":
	print(first%second)
elif operator=="//":
	print(first//second)
elif operator=="**":
	print(first**second)
else:
	print("invalid number")'''
'''
num=(range(5))
print(num)'''
'''
x=10
while x>=0:
	print(" ",end="")
	print("*"*x)
	x-=1
x=10
y=0
while x>=y:
	print(y*"#",end="")
	print(""*y,end="% ")
	print(y*"*")
	print(" "*y,end="%")
	print("@"*y,end=" %")
	y+=1
'''

'''
marks={"hindi":78, "english":88, "math":98, "snk":72}
marks["sc"]=90
marks["sc"]=80
print("Name : - Prince kumar\nClass  : - 10th\nRoll number :1500223\nTotal Marks=500")
#print(marks)
#print(marks["math"])
total_marks=sum(marks.values())
#x=sum(marks.values())
#print(sum(marks.values()))
#print(x)
print("marks obtained :",total_marks)
persentage=(sum(marks.values())/500)*100
print("Persatntage :",persentage,"%")'''
'''
result={"prince kumar":{"hnd":78,"math":80,"eng":66,"sc":84,"sst":72},
"Ankit kumar":{"hnd":88,"math":60,"eng":96,"sc":94,"sst":92},
"manu singh":{"hnd":79,"math":81,"eng":66,"sc":64,"sst":78}
}
#result["prince kumar"]["hnd"]=30
#result["Ankit kumar"].update({"hnd":50})

result.pop("manu singh")
#name=input("Name of student :")
#ob_marks=sum(result[name].values())
#per=(sum(result[name].values())/500)*100
print(result)
#print(result.keys())
#print(result.values())
#print(result["prince"].values())
#print("Obtained marks :",ob_marks)
#print(f"percentage of marks :{per}%")
'''
#*************************************************************

'''try:	
	result={"prince kumar":{"hnd":78,"math":80,"eng":66,"sc":84,"sst":72},
	"ankit kumar":{"hnd":88,"math":60,"eng":96,"sc":94,"sst":92},
	"manu singh":{"hnd":79,"math":81,"eng":66,"sc":64,"sst":78}
	}
	name=input("Name of student :")
	ob_marks=sum(result[name].values())
	per=(sum(result[name].values())/500)*100
#print(result)
#print(result.keys())
#print(result.values())
#print(result["prince"].values())
	print("Obtained marks :",ob_marks)
	print(f"percentage of marks :{per}%")
except:
	print("please enter student correctly !")
else:
	print("congratulation Dear student")
finally:
	print("\t\t\t\t\t\t\tmade By Prince")
'''
'''
try:
	result={"prince kumar":{"hnd":78,"math":80,"eng":66,"sc":84,"sst":72},
	"ankit kumar":{"hnd":88,"math":60,"eng":96,"sc":94,"sst":92},
	"manu singh":{"hnd":79,"math":81,"eng":66,"sc":64,"sst":78},
	"kumod kumar":{"hnd":89,"math":91,"eng":56,"sc":54,"sst":68},
	"anmol asha":{"hnd":70,"math":85,"eng":63,"sc":54,"sst":70},
	"chhotu kumar":{"hnd":40,"math":55,"eng":53,"sc":54,"sst":68}
	}
	name=input("Name of student:")
	ob_marks=sum(result[name].values())
	per=(sum(result[name].values())/500)*100	
#print(result["prince"].values())
	print(f"Full marks     : 500")
	print("Obtained marks :",ob_marks)
	print(f"percentage     : {per}%")
	if ob_marks>300:
		div="First Divison"
	elif ob_marks>225:
		div="Second Divison"
	elif ob_marks>200:
		div="Third Divison"
	else:
		div="Fail"
	print(f"Divison        : {div}")
except:
	print("please enter student correctly !")
else:
	print("★彡[ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴ ᴅᴇᴀʀ ꜱᴛᴜᴅᴇɴᴛ!]彡★")
finally:
	print("★彡[ᴛʜɪꜱ ᴘʀᴏᴊᴇᴄᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ ᴘʀɪɴᴄᴇ ꜱʜᴀʀᴍᴀ]彡★")
'''






'''file Handling

File handling is an important part of any web application
python has several function for creating ,reading,updating and deleting files.

file handling

The key function for working with files in python is the open()function
The open function takes two perameter; filename and mode.
There are four diffrent methods (mode) for opening a file.

"r" - Read - Default value. opens a file for reading ,error if the file does not exists
"a" - append - open a file for appending, creates the file if it does not exists
"w" -write
"x" - create Honesty is the best policyHonesty is the best policyHonesty is the best policy

Honesty is the best policy
i want to become a ideal person in my life
i want to become a ideal person in my life
i want to become a ideal person in my life
 file handling is an an important chepter for web application'''


#***************************************************************************************
#	date  04-08-2022
#*******************************************************************************************

#modules command in this file and program in pk.py file
#and will run here

'''import pk
pk.a("prince")

print(pk.x)
print(pk.x[3])

print(pk.y)


import pk
pk.x=A()
pk.x.first()
print(x.c)

import pk
pk.x.first()
#print(pk.x.first())
pk.x.second(12,10,8)
print("addition :",pk.x.d)

import pk
print(pk.per1)
print(pk.per1["age"])
print(pk.per1.items())

import pk
pk.x.second()
pk.x.first()
print("Addition :",pk.x.d)
print("exponent :",pk.x.g)
'''

'''
def x(name="prince"):
	print(f"Good morning {name}!")

list1=["prince","kumar",234,456.12]'''
#print(list1)
'''
n=int(input("enter table"))
for i in range(1,11):
	print(i*n)'''
'''
class main:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a**b
	def first(self):
		print(f"this is an module program that is taken from prectice file")
class prince(main):
	def __init__(self,a,b,d,e):
		super().__init__(a,b)
		self.d=d
		self.e=e
		self.f=d%e
	def second(self):
		print("Nothing is impossible")
ob=prince(12,3,89,9)'''
'''
x=20
y=0
while y<10:
	y+=1
	print(y*x)

x1=int(input("enter number :"))
for i in range(x1*2+1):
	if i%2==0:
		print("even :",i)
'''
'''
x=["prince","kumar","shsarma"]
x.insert(2,"chhotu")
x[1]="python"
x.pop(0)
x.extend(["mohan"])
print(x)'''
#print(x[2])
#print(x[:5])
#print(x.replace("i","")

#cheak="y"
'''while cheak=="y":

	try:
		print("\nıllıllı⭐🌟 R͙e͙s͙u͙l͙t͙ 🌟⭐ıllıllı")
		result={
		"prince kumar":{"hnd":98,"math":90,"eng":86,"sc":94,"sst":82},
		"ankit kumar": {"hnd":88,"math":60,"eng":96,"sc":94,"sst":92},
		"manu singh":  {"hnd":79,"math":81,"eng":66,"sc":64,"sst":78},
		"kumod kumar": {"hnd":89,"math":91,"eng":56,"sc":54,"sst":68},
		"anmol asha":  {"hnd":70,"math":85,"eng":63,"sc":54,"sst":70},
		"priya sharma":{"hnd":40,"math":55,"eng":53,"sc":54,"sst":68},
		"chhotu kumar":{"hnd":20,"math":35,"eng":53,"sc":24,"sst":18},
		"priyanshu kumar":{"hnd":30,"math":35,"eng":35,"sc":46,"sst":59}
		}
		#if you want to update the marks of student then use this method
		#result["prince kumar"]["hnd"]=30
		#result["Ankit kumar"].update({"hnd":50})


		name=input("Name of student:")
		ob_marks=sum(result[name].values())
		per=(sum(result[name].values())/500)*100	
	#print(result["prince"].values())
		print(f"Full marks     : 500")
		print("Obtained marks :",ob_marks)
		print(f"percentage     :{per}%")
		if ob_marks>300:
			div="First Divison"
		elif ob_marks>225:
			div="Second Divison"
		elif ob_marks>200:
			div="Third Divison"
		else:
			div="Fail"
		print(f"Divison        : {div}")
	except:
		print("\nplease enter student name correctly !")
		print("There is no student by this name\n")
	else:
		print("\n★彡[ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴ ᴅᴇᴀʀ ꜱᴛᴜᴅᴇɴᴛ!]彡★")
	finally:
		print("★彡[ᴛʜɪꜱ ᴘʀᴏᴊᴇᴄᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ ★ᴘʀɪɴᴄᴇ ᴋᴜᴍᴀʀ★]彡★")
	cheak=input("\nif you want cheak another student of number than press y else n :")
'''

'''x=[10,20,30,40,10]
y=[75,65,35,75,30]
if x[0]==x[-1]:
	print("Result is True")
else:
	pint("result is false")
if y[0]==y[-1]:
	print("Result is True")
else:
	print("Result is false")'''
'''
x={"sharma":5478,"music":78}
while True:
	key=input("etner the key :")
	value=eval(input("enter the value :"))
	x.update({key:value})
	y=input("if you want to stop then press y :")
	if y=="y":
		break'''
#print(x)
'''
name="prince kumar"
age=23
home="bihar"
if name=="prince kumar":
	if age==23:
		print(home)'''

'''n=int(input("etner a number :"))
for i in range(n):
	for j in range(i+1):
		print(i+1,end=" ")
	print()'''
'''
list1=[]
score=[]
x=int(input())
for i in range(x):
    y=input("enter ")
    z=float(input("enter"))
    list1+=[[y,z]]
    score+=[z]
b=sorted(list(set(score)))[1]
for a,c in sorted(list1):
    if c==b:
        print(a)'''

'''scorelist=[]
x= int(input("enter the number of student :"))
for i in range(x):
	n=int(input("enter score of student :"))
	scorelist.append(n)
result=sorted(scorelist,reverse=True)
print("runner-up :",result[1])
#print(scorelist)'''

'''
x=int(input("enter number of student :"))
y=map(int,input("put the score of student :").split())
lst=list(y)
scores=list()
for score in lst:
    if score not in scores:
        scores.append(score)
    else:
        continue
order=sorted(scores,reverse=True)
print(order[1])'''

'''y=map(int,input("put the score of student :").split())
#lst=list(y)
print(y)'''
'''
x=int(input("enter a number :"))
while x>0:
	print(x)
	x-=1

x=int(input("enter odd nnumber :"))
y=0
z=0
while x>y:
	z+=1
	if z%2!=0:
		print(z)
		y+=1
x=int(input("enter a number :"))
for i in range(1,x*2+1,2):
	print("even number :",i,end=" ")

	'''

'''
x=["sun","mon","tue","wed","thu","fri","sat"]
y=len(x)-1
#for i in range(y,-1,-1):
#	print(x[i])
while y>=0:
	print(x[y].split(),end="\n")
	y-=1
x=["sun","mon","tue","wed","thu","fri","sat"]
y=len(x)
z=0
while y>z:
	print(x[z])
	z+=1
x=("sun","mon","tue","wed","thu","fri","sat")
y=len(x)-1
for i in range(y,-1,-1):
	print("\n",x[i])
x="january","february","march","april","may"
#for i in range(len(x)-1,-1,-1):
#	print(x[i])
y=len(x)-1
while y>=0:

	print(x[y].split())
	y-=1'''
'''choice="k"
while choice!="p":

	n=int(input("write and cheak the number :- "))
	if n>=1:
		for i in range(2,int(n/2)+1):
			if n%i==0:
				print(n,"not prime :")
				break
			else:
				print(n,"prime")
				break
	else:
		print("prime number")
	choice=input("\n\nif you want to break the program then press p :")'''

'''x=int(input("enter number :"))
if x>=1:
	for i in range(2,int(x/2)+1):
		if x%i==0:
			#print(i)
			print("not prime",x)
			break
		else:
			#print(i)
			print("prime number",x)
			break
else:
	print("none")
'''
'''
x=["ram","mohan","sohan","sita","gita"]
#y=x.index("sohan")
#print(y)
#x.pop(3)
#x.remove("ram")
x.insert(0,"prince")
x[0]="chhotu"
print(x)
print(x[0::2])
print(x[-1::-2])

class math:
	def __init__(self):
		print("honesty is the best policy")
class st:
	def first(self):
		print("i am a student")
class prince(math,st):
	def __init__(self):
		math.__init__(self)
		st.first(self)
		print("god is best")
ob=prince()'''

'''y=[]
x=int(input("enter number of list :"))
for i in range(x):
	list1=eval(input("enter number or name :"))
	y.append(list1)
print(y)'''

'''y={}
x=int(input("enter number of dict :"))
for i in range(x):
	key=str(input("enter the key :"))
	value=eval(input("enter the values :"))
	y[key]=value
print(y)'''

'''m=int(input("enter the table :"))
n=0
while n<10:
	n+=1
	print(f"{m} x {n} = {m*n}")

string=str(input("enter a string :"))
print(string[-1::-1])'''
'''
class first:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		self.c=a+b
	def statement1(self):
		y=[]
		x=int(input("How many index you want in a list :"))
		for i in range(x):
			list1=eval(input("enter number or name :"))
			y.append(list1)
		print(y)
class second:
	def __init__(self):
		y={}
		x=int(input("enter number of dict :"))
		for i in range(x):
			key=str(input("enter the key :"))
			value=eval(input("enter the values :"))
			y[key]=value
		print(y)
	def statement2(self):
		print("\nToday is my python test")
class third:
	def __init__(self):
		m=int(input("enter the table :"))
		n=0
		while n<10:
			n+=1
			print(f"{m} x {n} = {m*n}")
	def statement3(self):
		print("Python test was taken by puja mem")

class forth(first,second,third):
	def __init__(self,a,b):
		first.__init__(self,a,b)
		second.__init__(self)
		third.__init__(self)
		string=str(input("enter a string :"))
		print(string[-1::-1])

	def statement4(self):
		print("Thank you for your support")
ob=forth(45,40)
print(f"\nAddition : {ob.c} \n")
ob.statement1()
ob.statement2()
ob.statement3()
ob.statement4()'''

'''x=["sun","mon","tue","wed","thu","fri","sat"]
y=len(x)
z=0
while y>z:
	print(x[z])
	z+=1

x=["sun","mon","tue","wed","thu","fri","sat"]
y=len(x)
for i in x:
	print(i)'''
'''
x="honesty is the best policy"
print(x.replace(" ","**"))'''
'''
try:
	x=int(input("enter a number :"))
	for i in range(1,x+1):
		x=x+1
		print(x*i)
except:
	print("something is went wrong")
else:
	print("program is working good")
finally:
	print("welcomr to the home"'''

'''a=lambda x,y,z:x+y*z
print(a(12,4,10))'''



'''def math():
	x=lambda a,b,c:a+b/c
	print(x(12,40,10))
math()'''
'''
class ab:
	x=lambda a,b,c:a+b-c
ab()
print(ab.x(12,4,2))



class a:
	def math(self,a,b):
		self.c=a+b
		#print(a+b)
ab=a()
ab.math(12,32)
print(ab.c)

x={"mon","tue","wed","thu"}
y={"mon","tue","wed","fri"}
z={"mon","tue","sun","sat"}
x.symmetric_update(y,z)
print(x)'''

'''
x=["mon","tue","wed","thu"]
y=["mon","tue","wed","fri"]
z=["mon","tue","sun","sat"]
a=zip(x,y,z)
print(list(a))


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



'''def x(name, Age, Class):
	print("My name is ",name)
	print("I am",Class,"with math honors")
	print("I am",Age,"year old")

x(name="prince kumar", Age=22, Class="graduate")'''



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



def a(**x):
	print(x["name"])
	print(x["age"])
	print(x["state"])
	print(x["country"])

a(name="prince", age="23", state="bihar",country="India")'''


# a file named "geek", will be opened with the reading mode.
#file = open('test.py', 'r')
# This will print every line one by one in the file
#for each in file:
#	print (each)





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
}'''
'''
x="pynative"
for i in range(0,len(x),2):
	print(x[i])

x="pynative"
print(x[0::2])'''

'''import re
#regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\[A-Z|a-z]{2,}\b'
def cheak(email):
	if (re.fullname)'''


'''
x=[10,20,30,40,10]
y=[75,65,35,75,30]
if x[0]==x[-1]:
	print("Result is True")
else:
	pint("result is false")
	
if y[0]==y[-1]:
	print("Result is True")
else:
	print("Result is false")'''





'''def cheak(x):
	if x[0]==x[-1]:
		return True
	else:
		return False

list1=[10,20,30,40,10]
list2=[75,65,35,75,30]

first=cheak(list1)
print(first)

second=cheak(list2)
print(second)

'''
# Q1. if First and last index is equall then print "Result is true"
#     else print "Result is False"

'''
list1=[]
list2=[]
x=int(input("How may index want in a list :"))
for i in range(x):
	y=eval(input("enter a number in list1 :"))
	list1.append(y)
print(" ")
for i in range(x):
	z=eval(input("enter a number in list2 :"))
	list2.append(z)

print(list1)
print(list2)
if list1[0]==list1[-1]:
	print("Reult is True!")
else:
	print("Result is false!")

if list2[0]==list2[-1]:
	print("Result is True!")
else:
	print("Result is False!")'''


'''
m={}

m[4]=20
m[2]=45
m[3]=15
m[6]=58
m[1]=26

print(m)
print(sorted(m.items()))'''
'''
def squrt(n):
	square_root=n**0.5
	print(square_root)
squrt(int(input("enter the square number :")))'''

#find the term of number 
#number is 23 of sum
'''ap=5,10,15,20,25
a=5
n=23

d=ap[1]-ap[0]
c=ap[2]-ap[1]
if d==c:
	an=a+(n-1)*d
	print("23rd number is :",an)
else:
	print("it is not ap")

for i in range(5,500,5):
	if i==23*5:
		print(i)
		break'''





#AP 17,23,29,35..... Find the 23rd term of .
#print(6*23)
#print(17+(23-1)*6)
'''for i in range(17,500,6):
	if i==(23*6):
		print(i)'''
		
#find the HCF of 225 and 330
'''key_value={}
key_value['ravi'] = '10'       
key_value['rajnish'] = '9'
key_value['sanjeev'] = '15'
key_value['yash'] = '2'
key_value['suraj'] = '32'

print(sorted(key_value.items()))'''

'''
input

key_value = {}
# Initialize value
key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323


print("Task 2:-\nkey and value are sorted in alphabetical order by the key")
#print(sorted(key_value.items()))
for i in (sorted(key_value)):
	print((i,key_value[i]),end=" ")
	#print(sorted(key_value.items()))
	#break'''

'''OUTPUT
key_value {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
Task 2:-
Keys and Values sorted in alphabetical order by the key  
(1, 2) (2, 56) (3, 323) (4, 24) (5, 12) (6, 18) '''



'''print("\nıllıllı⭐🌟 R͙e͙s͙u͙l͙t͙ 🌟⭐ıllıllı,⭐🌟 R͙e͙s͙u͙l͙t͙ 🌟⭐ıllıllı\n")
x={1:{"hnd":45,"eng":56,"math":89,"sc":56,"sst":63},
2:{"hnd":65,"eng":59,"math":59,"sc":55,"sst":78},
3:{"hnd":58,"eng":72,"math":80,"sc":40,"sst":36},
4:{"hnd":33,"eng":66,"math":66,"sc":78,"sst":47},
5:{"hnd":64,"eng":36,"math":44,"sc":64,"sst":90},
6:{"hnd":33,"eng":86,"math":70,"sc":30,"sst":44}}
#print(x)
y=int(input("Roll Number   :- "))
mark_ob=sum(x[y].values())
per=mark_ob/500*100
if y==1:
	print("\nStudent Name  :- Prince kumar")
elif y==2:
	print("\nStudent Name  :- Kumod kumar")
elif y==3:
	print("\nStudent Name  :- Ankit kumar")
elif y==4:
	print("\nStudent Name  :- Rahul kumar")
elif y==5:
	print("\nStudent Name  :- Manu singh")
elif y==6:
	print("\nStudent Name  :- Anmol asha")
else:
	print("Not Record found")

print(f"Obtained Marks :- {mark_ob}")
print(f"Persantage     :- {per}")
if mark_ob>=300:
	print("Divison  :- First divison")
elif mark_ob>=225:
	print("Divison 	:- Second divison")
elif mark_ob>=200:
	print("Divison  :- Third divison")
else:
	print("fail")'''


'''
def hcf(x,y):
	if x>y:
		smaller=y
	else:
		smaller=x
	for i in range(1,smaller+1):
		if ((x%i==0) and (y%i==0)):
			hcf=i
	print(f" H.C.F OF {x} AND {y} IS {hcf}")
			

x=int(input("enter first number :"))
y=int(input("enter second number :"))
hcf(x,y)'''


#Function to find HCF the using Euclian algorithm

'''def hcf(x,y):
	while(y):
		x,y=y,x%y
	print(x)
hcf(54,24)'''

# Python code demonstrate the working of
# sorted() with lambda

# Initializing list of dictionaries
'''lis = [{"name": "Nandini", "age": 20},
	{"name": "Manjeet", "age": 20},
	{"name": "Nikhil", "age": 19}]

# using sorted and lambda to print list sorted
# by age
#print("The list printed sorting by age: ")
#print(sorted(lis, key=lambda i: i['age']))
print(sorted(lis))
print("\r")'''

# using sorted and lambda to print list sorted
# by both age and name. Notice that "Manjeet"
# now comes before "Nandini"
#print("The list printed sorting by age and name: ")
#print(sorted(lis, key=lambda i: (i['age'], i['name'])))

#print("\r")

# using sorted and lambda to print list sorted
# by age in descending order
#print("The list printed sorting by age in descending order: ")
#print(sorted(lis, key=lambda i: i['age'], reverse=True))

'''
x={"name":23,"prince":56}
x.update({"mother":89,"brother":23})
print(x)'''
'''
import random
min=1
max=6
cheak="yes"
while cheak=="yes" or cheak=="y":

	x=int(input("enter min number :"))
	y=int(input("enter max number :"))
	print("dice is rolling............")
	print("output is ..........")
	a=random.randint(min,max)
	b=random.randint(min,max)
	print("Computer choice is .. :",a)
	print("Computer choice is .. :",b)
	if a and b == x and y:
		print("you won the game.!")
	else:
		print("You lose the game !")
	cheak=input("if you want to leave the game then press y else press enter:")
'''
'''
from datetime import date

def xy(x):
	today=date.today()
	age=today.year-x.year-((today.month,today.day)<(x.month,x.day))
	print(age)
a=int(input("year :"))
b=int(input("month :"))
c=int(input("birthday :"))
xy(date(a,b,c))'''


'''x=545665
b=str(x)
print(b[-1::-1])'''
#for i in range(len(b)-1,-1,-1):
#	print(b[i],end=" ")
'''
from datetime import date
def age(x):
	today=date.today()
	age=today.year-x.year-((today.month,today.day)<(x.month,x.day))
	print(f"Your age is :{age} ")

a=int(input("Year :"))
b=int(input("month :"))
c=int(input("birthday :"))
age(date(a,b,c))'''
'''
import random
min=1
max=3
while True:
	a=int(input("enter your first number :"))
	b=int(input("enter your second number :"))
	print("Dice is rolling .......")
	print("result is on your desktop....")
	c=random.randint(min,max)
	d=random.randint(min,max)
	print(c)
	print(d)
	if c and d == a and b:
		print("You won the game!")
	else:
		print("You lose the game!")
	cheak =input("if you want to break then press yes or y :")
	if cheak=="y":

		print("thank you!")
		break'''
'''
x="greek grook is the best"
y=x.replace("g","t").replace("k","x")
print(y)'''
'''
x={}
x[1]=41,78,86,56,32
x[2]=42,56,78,96,36
x[3]=25,78,56,23,59
x[4]=14,96,85,56,65
x[5]=22,58,74,98,69
x[6]=85,78,56,98,45
y=int(input("enter keys :"))
z=sum(x[y])
print(z)'''
'''
import random
def game(comp,you):
	if comp==you:
		return None
	if comp=="s":
		if you=="w":
			return False
		elif you=="g":
			return True
	if comp=="w":
		if you=="s":
			return True
		elif you=="g":
			return False
	if comp=="g":
		if you=="w":
			return True
		elif you=="s":
			return False

print("Comp Turn: snake(s), Gun(g), Water(w) ?")
randno=random.randint(1,3)
if randno==1:
	comp=="s"
elif randno==2:
	comp="g"
elif randno==3:
	comp="w"

you=input("your turn: snake(s), water(w), gun(g) ? ")
a=game(comp,you)

print(f"You choose {you}")
print(f"Computer choose {comp}")

if a==None:
	print("Game is Tie!")
elif a==True:
	print("You won the game!")
else:
	print("You lose the game!")'''

#print("abc.DEF".capitalize())

'''
a= "prince KUMAR"
print(a.capitalize())
x="hii this PRINCE KUMAR sharMA from bihar cuRRENTly i ilve in chakkapar SO   YOU dont MAINd"
print(x)
print(x.capitalize())

class math :
	def __init__(self):
		x=int(input("enter table :"))
		for i in range(1,11):
			print(f"{x} x {i} = {x*i}")
	def one(self):
		y="MOHan is A MORAL PErson"
		print(y.capitalize())

class eng:
	def __init__(self):
		print("A noun is the name of person place or things or\n All naming word are called noun")

	def two(self):
		z="a b c d e f g h i j k l m n o p q r s t u v w x y z"
		for i in range(len(z)-1,-1,-1):
			print(z[i],end="")

class main(math,eng):
	def __init__(self):
		math.__init__(self)
		eng.__init__(self)
		a=int(input("enter number :"))
		fact=1
		for i in range(1,a+1):
			fact=fact*i
		print(f"The number {a} of factorial is : {fact}")

p=main()
p.one()
p.two()'''

'''import random
def game(comp,you):
	if comp==you:
		return None
	if comp=="s":
		if you=="w":
			return False
		elif you=="g":
			return True
	if comp=="w":
		if you=="s":
			return True
		elif you=="g":
			return False
	if comp=="g":
		if you=="w":
			return True
		elif you=="s":
			return False
print("computer chhose sanke (s) water(w) gun(g) :")
co=random.randint(1,3)
if co==1:
	comp="s"
elif co==2:
	comp="w"
elif co==3:
	comp="g"

you=input("enter youy choice snake gun aor water :")

a=game(comp,you)
print("computer chice is :",comp)
print("your choice is :",you)
if a == None:
	print("Game is tie!")
elif a:
	print("you won the game!")
else:
	print("You lose the game !")'''


'''from datetime import date
def age1(x):
	today=date.today()
	age=today.year-x.year-((today.month,today.day)<(x.month,x.day))
	print("your age is ",int(age))

a=int(input("Year :"))
b=int(input("Month :"))
c=int(input("birthday :"))
age1(date(a,b,c))'''

'''x=input("Enter your user id :- ")
if x=="Prince301":
	y=input("enter password :- ")
	if y=="mamta123@":
		print("sucsesfuly logged in")
	else:
		print("wrong password!")
else:
	print("wrong user id!")'''




#user id   password create a new account and log in 

'''print("Create a new account")
a=input("Enter you name :-")
b=input("Mother's name :-")
c=input("D.O.B  :-")

y=input("enter user id  :")
p=input("enter password :")
r=input("enter password again :")
print("\nThank you accoount created sucsesfuly!\n welcome to this app!")
print("\nLog in your acount now\n")
user=input("enter your user id :")
if user==y:
	d=input("enter again user id :")
	if d==y:
		m=input("enter password !")
		if m==p:
			print("thankyou")
			print("Your account created sucsesfuly")
		else:
			e=input("enter password again :")
			if e==p:
				print("welcome to prince home!")
			else:
				print("Try again after sometime!")
else:
	print("wrong user id ")
	f=input("enter user id again :")
	if f==y:
		g=input("password :")
		if g==p:
			print("You are sucsesfuly logged in !")
	else:
		print("try diffrent password!")'''

'''x=int(input("enter a number :"))
y=1
z=1
while x>=y:
	z=z*y
	y+=1
print("factorial :",z)

n=int(input("enter a number :"))
if n>1:
	for i in range(2,int(n/2)+1):
		if n%i==0:
			print("not prime")
			break
		else:
			print("prime number!")
			break
else:
	print("not prime!")'''

'''
def hcf(x,y):
	if x>y:
		smaller=y
	else:
		smaller=x
	for i in range(1,smaller+1):
		if ((x%i==0) and (y%i==0)):
			hcf=i
	print(f" H.C.F OF {x} AND {y} IS {hcf}")
			

x=int(input("enter first number :"))
y=int(input("enter second number :"))
hcf(x,y)'''


#Function to find HCF the using Euclian algorithm

'''def hcf(x,y):
	while(y):
		x,y=y,x%y
	print(x)
hcf(54,24)'''

'''def hcf(a,b):
	if a<b:
		smaller=a
	else:
		smaller=b
	for i in range(1,smaller+1):
		if ((a%i==0) and (b%i==0)):
			h=i
	print(h)
c=int(input("enter first number :"))
d=int(input("enter second number :"))
hcf(c,d)

x=int(input("enter a number :"))
y=int(input("enter a number :"))
while (y):
	x,y=y,x%y
print(x)

def hcf(a,b):
	while (b):
		a,b=b,a%b
	print("hcf :",a)
hcf(45,120)'''

'''def hcf(x,y):
	if x<y:
		s=x
	else:
		s=y
	for i in range(1,s+1):
		if ((x%i==0) and (y%i==0)):
			h=i
	print(h)
hcf(45,120)


a=45
b=120
while (b):
	a,b=b,a%b
print(a)'''

'''
for i in range(4):
	x=input("user id :- ")
	if x=="prince301":
		for k in range(4):
			y=input("password :")
			if y=="12345":
				print("you are logged in!")
				break
'''
			#else:
			#	print("password blocked")
			#	break
	#else:
	#	print("blocked")
		#break

'''
import random
def game(comp,me):
	if comp==me:
		return None
	elif comp=="s":
		if me=="w":
			return False
		elif me=="g":
			return True
	elif comp=="w":
		if me=="g":
			return False
		elif me=="s":
			return True
	elif comp=="g":
		if me=="s":
			return False
		elif me=="w":
			return True

c=random.randint(1,3)
if c==1:
	comp="s"
elif c==2:
	comp="g"
elif c==3:
	comp="w"

print("computer choose snake s water w and gun g :")
me=input("your turn choose snake s , water w  gun g :")
a=game(comp,me)

print("your chice is : ",me)
print("computer choice is : ",comp)
if a==None:
	print("Game is tie!")
elif a:
	print("you won the game !")
else:
	print("You lose the game!")'''

'''import random
def game(comp,you):
	if comp==you:
		return None
	elif comp=="s":
		if you=="w":
			return False
		elif you=="g":
			return True
	elif comp=="g":
		if you=="w":
			return True
		elif you=="s":
			return False

	elif comp=="w":
		if you=="g":
			return False
		elif you=="s":
			return True
			
c=random.randint(1,3)

if c==1:
	comp="s"
elif c==2:
	comp="w"
elif c==3:
	comp="g"
you=input("enter your choice snake(s) gun(g) water(w)  :- ")
a=game(comp,you)
print("computer choice :",comp)
print("your choice  : ",you)

if a==None:
	print("Game is Tie!")
elif a==True:
	print("You Won the game!")
else:
	print("You lose the game!")


#princekr301@gmail.com
#normal email cheaker program
def cheak(email):
	x="princek*****@gmail.com"
	if email[-10:]==x[-10:]:
		print("Vailid Email!")
		
	else:
		print("InVailid Email!")
#x=princekr301@gmail.com
email=input("write an email id :- ")
cheak(email)'''


'''x="princekr301@gmail.com"
y="satyanarayansharma1234@gmailcom"
print(y[-10:])
print(x[-10:])
if x[-10:]==y[-10:]:
	email="vailid Email Account!"
else:
	email="Invailid Email Account!"

print(email)'''

'''x=["prince","kumar","sharma","mohan"]
y=["mamta","devi"]
x.insert(1,"mom")
x.extend(y)
print(x)'''
'''
def hcf(x,y):
	if x>y:
		smaller=x
	else:
		smaller=y
	for i in range(1,smaller+1):
		if (x%i==0) and (y%i==0):
			t=i
	print(t)
x=int(input("first number :"))
y=int(input("second number :"))
hcf(x,y)'''

'''tables=[lambda x=x: x*10 for x in range(1, 11)]
for table in tables:
	print(table())'''



'''x=[lambda y=y:y*10 for y in range(1,11)]
for i in x:
	print(i())'''


'''x=[1,2,3,4,8,9,10]
y=[]
for i in range(1,len(x)+1):
	if i not in x:
		y.append(i)
print(y)'''

'''x=["prince","kumar","sharma","mayank","kumar","prince"]
y=[]
for i in range(len(x)):
	n=i+1
	for j in range(n,len(x)):
		if x[i]==x[j] and x[i] not in y:
			y.append(x[i])
print(y)'''


'''x=["a","b","c","d","e","c","e","e"]
y=[]
for i in range(len(x)):
	n=i+1
	for j in range(n,len(x)):
		#print(x[j],end=" ")
		if x[i]==x[j]:
			print(x[i])'''
#print(n)



#The person whose name has appeared twice ,take out that name and issue a new list.
#List given below.!  ????????????
'''x=['prince','kumod','rahul','ankit','mohan','prince','manu','rahul','kumod']
y=[]
for i in range(len(x)):
	n=i+1
	for j in range(n,len(x)):
		if x[i]==x[j]:
			y.append(x[j])
print(y)'''

'''
from datetime import datetime
import winsound
#from playsound import playsound
alarm_time=input("enter the time of alarm to be set :HH:MM:SS \n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_second=alarm_time[6:]
#alarm_period=alarm_time[9:11].upper()
print("setting up alarm")
print(alarm_hour)
print(alarm_minute)
print(alarm_second)
#print(alarm_period)
while True:
	now=datetime.now()
	current_hour=now.strftime("%I")
	current_minute=now.strftime("%M")
	current_second=now.strftime("%S")
	#current_period=now.strftime("%p")
	#if (alarm_period==current_period):
	if (alarm_hour==current_hour):
		if (alarm_minute==current_minute):
			if (alarm_second==current_second):
				print("wake up !")
				winsound.playsound("sound.wav",winsound.SND_ASYNC)
				break'''


# generate pi to nth digit
# Chudnovsky algorihtm to find pi to n-th digit
# from https://en.wikipedia.org/wiki/Chudnovsky_algorithm
# https://github.com/microice333/Python-projects/blob/master/n_digit_pi.py
'''
import decimal
def compute_pi(n):
    decimal.getcontext().prec = n + 1
    C = 426880 * decimal.Decimal(10005).sqrt()
    K = 6.
    M = 1.
    X = 1
    L = 13591409
    S = L
    for i in range(1, n):
        M = M * (K ** 3 - 16 * K) / ((i + 1) ** 3)
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X
    pi = C / S
    return pi


while True:
    n = int(input("Please type number between 0-1000: "))
    if n >= 0 and n <= 1000:
        break
print(compute_pi(n))'''
'''
password=1234
balance=5000
print("enter your four digit pin")
while True:

	pin=int(input("enter your digit pin:- "))
	if password!=pin:
		print("try again")
	if password==pin:
	
		print("""choice your option
			1==balance inquairy
			2==withdrawl_balance
			3==credit balance
			4==exit""")'''



'''
import time
print("=========================.............")
print("Welcome to prince ATM!")
time.sleep(5)
print("----------------------------------------")
print("please insert your card!")
time.sleep(5)
password=1234
balance=5000
chance=4
print("/////////////////////////////////////////////////////////")

print("""choice your option
	1==balance inquairy
	2==withdrawl_balance
	3==credit balance
	4==exit
----------------------------------------------------------""")
	

time.sleep(2)
option=int(input("selcet option :"))

while True:
	if option==1:
		time.sleep(3)
		while chance!=0:
			print("---------------------------------------------------")
			pin=int(input("enter your four digit pin:- "))
			if password!=pin:
				chance-=1
				print("Your pin is incorrect please try again!")
				print("------------------------------------------------")
			else:
			# password==pin:
				print("-------------------------------------------------")
				#print("--_-_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_---\n")
				print("please wait cheaking your account!")
				time.sleep(3)
				print(f"Your balnce is {balance}")
				time.sleep(3)
				print("\nthank you for visiting prince ATM!")
				break
		
	elif option==2:
		withdrawl_amount=int(input("enter your ammount:"))
		time.sleep(3)
		while chance!=0:
			print("---------------------------------------------------")
			pin=int(input("enter your four digit pin:- "))
			if password!=pin:
				chance-=1
				print("Your pin is incorrect please try again!")
				print("------------------------------------------------")
			else:

			# password==pin:
				print("-------------------------------------------------")
		
				print("please wait transaction is being processing!")
				time.sleep(4)
				print("please collect your ammount!")
				time.sleep(2)
				balance=balance-withdrawl_amount
				print("--_-_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_---")
				print(f"Your left balance is {balance}")
				time.sleep(3)
				print("Thank you for visiting prince ATM!")
				break

	elif option==3:
		credit=int(input("Enter your credit amount :"))
		time.sleep(2)
		while chance!=0:

			print("---------------------------------------------------------------------------------")
			pin=int(input("enter your four digit pin:- "))
			if password!=pin:
				chance-=1
				print("Your pin is incorrect please try again!")
				print("-------------------------------------------------------------------------------")
			else:

			# password==pin:
				print("--------------------------------------------------------------------------------")
		
				print("Put your ammount in the ATM slot")
				time.sleep(2)
				print("please wait your amount is adding !")
				time.sleep(3)
				balance=balance+credit
				print("--_-_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--__---_-----____------___")
				print(f"Your updated amount is {balance}")
				time.sleep(2)
				print("Thank you for using prince ATM!")
				break
	elif option==4:
		print("Thank you for your support")
	user_exit=input("Would you like to exit? Yes/No  :")
	if user_exit=="Yes":
		#print("///////////////////////////////////////////////////////////////////")
		print("Thank you for using prince bank !!")
		break
	else:
		continue'''




'''
import time
print("Welcome to prince Bank!")
time.sleep(3)
print("please insert your Dabit card!")
pin=1234
chances=4
balance=20000
while chances!=0:
	p=int(input("enter your four digit code :"))
	if pin!=p:
		time.sleep(3)
		chances-=1
		print("you entered wrong pin! ")
		time.sleep(2)
		print(f"your chances is now {chances}")
		time.sleep(2)

	else:
		print("enter what tou want!")'''



'''import random

x="abcdefghijklmnopqrstuvwxyz"
y="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
z="!@#$%^&*/"
a="1234567890"
mix=x+y+z+a
lenth=8

password="".join(random.sample(mix,lenth))
#password=random.randint(mix,lenth)
print(f"Your new password is :=> {password}")'''
'''from ite
x=[1,2,3,4]
y=["a","b","c","d"]
for i in chain(x,y):
	print(i)'''

'''num = int(input("enter a number :"))
if num > 1:
	for i in range(2, num//2):
		if (num % i) == 0:
			print(num, "is not a prime number")
			break
		else:
			print(num, "is a prime number")
			break
else:
	print(num, "is not a prime number")'''


'''x=int(input("enter year :"))
if x%400==0 or (x%4==0 and x%100!=0):
	print("leap year")
else:
	print("not leap year")'''
'''
import time
print("*********************************************************************************")
print("**********************************************************************************")
time.sleep(2)
print("welcome to prince bank!")
time.sleep(3)
print("\nInsert your dabit card !")
time.sleep(3)
print("please wait computer is reading your card!")
time.sleep(3)
balance=10000
chance=4
password=2810
print("Good\nplease choose an option below!")
time.sleep(2)
print(		\n1==Balaance inquairy
#2==Withdaraw balance
#3==Credit amount
		 )
time.sleep(3)
option=int(int(input(" Choice your option  :- ")))

if option==1:

	while chance!=0:
		x=int(input("enter your pin :"))
		if password!=x:
			time.sleep(2)
			print("you have enterd incorrect pin")
			time.sleep(2)
			print("please try again !")
			chance-=1
			time.sleep(2)
			print("you have now",chance,"chances left!")
		else:
			time.sleep(3)

			print("please wait fatching your balance!\n")
			time.sleep(3)
			print("Your Balance is ",balance)
			break
if option==2:
	y=int(input("how much money do you want to withdrawl :- "))
	while chance!=0:
		x=int(input("enter your pin :"))
		if password!=x:
			time.sleep(2)
			print("you have enterd incorrect pin")
			time.sleep(2)
			print("please try again !")
			chance-=1
			time.sleep(2)
			print("you have now",chance,"chances left!")
		else:
			time.sleep(3)
			print("please wait transaction is being processing")
			time.sleep(2)
			print("take your Amount!")
			time.sleep(2)
			balance=balance-y
			print("your left balance is ",balance)
			time.sleep(2)
			print("Thank you for using prince bank!")
			break
if option==3:
	y=int(input("how much money do you want to credit :- "))
	while chance!=0:
		x=int(input("enter your pin :"))
		if password!=x:
			time.sleep(2)
			print("you have enterd incorrect pin")
			time.sleep(2)
			print("please try again !")
			chance-=1
			time.sleep(2)
			print("you have now",chance,"chances left!")
		else:
			time.sleep(3)
			print("please wait your Amount is being Adding in your Bank! ")
			time.sleep(3)
			print("deposites your Amount!")
			time.sleep(3)
			balance=balance+y
			print("your updated balance is ",balance)
			time.sleep(2)
			print("Thank you for using prince bank!")
			break'''




import time

print("hello!")
time.sleep(5)
print("hiii")











