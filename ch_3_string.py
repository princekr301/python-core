

'''
Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:



Multiline Strings
You can assign a multiline string to a variable by using three quotes:


Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.


Negative Indexing
Use negative indexes to start the slice from the end of the string:


Python - Modify Strings
Python has a set of built-in methods that you can use on strings.

Upper Case
Example
The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())
Lower Case
Example
The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())
Remove Whitespace
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

Example
The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
ADVERTISEMENT

Replace String
Example
The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))
Split String
The split() method returns a list where the text between the specified separator becomes the list items.

Example
The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


string Concatenation
To concatenate, or combine, two strings you can use the + operator.

Example
Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)


String Format
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

Example
age = 36
txt = "My name is John, I am " + age
print(txt)





String Methods
Python has a set of built-in methods that you can use on strings.

Note: All string methods returns new values. They do not change the original string.

Method	Description
capitalize()		Converts the first character to upper case
casefold()		Converts string into lower case
center()		Returns a centered string
count()		Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()		Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

'''
#***************************************************************************************************************************
# exercise of python-string 	STRING SLICING   STRING METHOD





#x="Arunachal pradesh"
#print(len(x))
#print(x[5])
#print(x[-4])


#return second item
#print(x[2])
#return 17th item
#print(x[16])
#return 12 item
#print(x[12])
#return fourth item
#print(x[4])
#return 3rd item
#print(x[3])
#return 15th item
#print(x[15])
#return 1st item
#print(x[1])
#return second item
#print(x[2])
#return ninth item'''
#print(x[9])

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#	Date = 27/06/2022	

#////////////////////////////////////////////////////////////////////////////


'''x="hello delhi"
print(x[0:5])
print(x[-11:-6])
print(x[6])
print(x[-5])'''

'''x="Himachal pradesh"		# 0  1  2  3  4  5  6  7 8 9 10 11 12  13 14 15
print(len(x))				# H  i  m  a  c  h  a  l   p  r  a  d  e  s  h
print(x[3])
print(x[-14])					#
print(x[4])
print(x[-13])
print(x[5])
print(x[-12])
print(x[3:15])
print(x[-14:])
print(x[5:8])
print(x[-12:-8])
print(x[7:8])
print(x[-9:-8])
print(x[-6:-5])
print(x[10:11])
print(x[-16:-2])
print(x[9:16])
print(x[14])
print(x[-16:])
'''
#x= "Himachal pradesh"
#print(x[0::2])
#print(x[2:14:3])
#print(x[-16:-1:2])
#print(x[-16:-1:-2])

'''x="Himachal pradesh"
print(x[0:2])'''


'''x="prince kumar"
y=len(x)
z=0
while y>z:
	print(x[z],end="   ")
	z+=1'''

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////
#	28-06-2022
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#x="Himachal pradesh"
#print(x.upper())		# PRINT WILL ALL IN CAPITAL LETTER
#x="HIMACHAL PRADESH"
#print(x.lower())		#PRINT WILL ALL IN SMALL LETTER

#x=" BIHAR"
#print(x.strip())	# ye start ke backspace ko kam karta hai


'''x=" we all are students"		# its will the old to new word 
print(x.replace("students","indian"))

x="Good morning"
print(x.split())'''		#it will be print in ['good','morning']like this

'''x="one two three four five"
print(x.split())'''



# python-string concatenation
'''x="Good"
y="morning"
z=x+" "+y
print(z)

x="Good"
y="morning"
z=x+y
print(z)

x="good"
y="morning"
z=x,y
print(z)
'''

'''x="Good"
y="morning"
print(x,y)

 Escape sequence : -
	\n ----  for new line
	\t ----  for a tab
	\''----	 for single quote
	\\ ----	 for back slash
'''
# \n its take a new page

'''x="welcome to, \ndata science"
print(x)
'''
# \t its take a one tab
'''x="my name is \tprince kumar sharma"
print(x)
'''

# \b its take a backspace
#x="good    \bmorning"
#print(x)

# python string swapcase = its convert the capital to small and small to capital
#x="hONESTY IS THE BEST policy"
#y=x.swapcase()
#print(x.swapcase())
#print(y)

'''age=23
x="my name is prince ,and i am {} old"
print(x.format(age))
'''
#
'''quantity= 3
item= 45
price= 78.45
x=" i want {} pieces pf item {} for {} price."
print(x.format(quantity,item, price))'''


'''quantity= 3
price= 45
item= 78.45
x=" i want {} pieces pf item {} for {} price."
print(x.format(quantity,item, price))
'''

'''My name is prince i am 23 year old and i passed 12 in 2017,
i purachase 20 oranges and  the price of these oranges are 60.50
'''

'''age=23
passed= 12 
oranges=20
price=60.50
x="My name is prince, i am {} old and i passed {} in 2017 purachase {} oranges and  the price of these oranges are {}"
print(x.format(age,passed,oranges,price))
'''

'''age=input("enter age")
passed=input("date")
graduation=input("gradution date")
x="hii this is prince, when i was {} old then i passed {} 12th exam and completed my graduation {} "
print(x.format(age,passed,graduation))
'''


#**********H.W******HW********HW*********HW***********


#1. reverse the string with the help of for loop
'''x="himachal pradesh"
y=len(x)-1
for a in range(y,0,-1):
	print(x[a],end=" ")'''
#print(x[5:8])  

#2. find the length of this string
#x="Himachal pradesh"
#print(len(x))

#3.return seventh item
#x="Himachal pradesh"
#print(x[6])

#4.return fifth to eeight item
#x="Himachal pradesh"
#print(x[4:8])

#5. take the user input reverse this string with the help of for loop
'''x=str(input("write any name:-\n"))
y=len(x)-1
for z in range(y,-1,-1):
	print(x[z],end=' ')'''

'''x=input("write any name:-\n")
for z in x:
	print(z,end=' ')'''

#6. Take the user input print this string with help of while loop
'''x="Himachal pradesh"
y=len(x)
z=0
while y>z:
	print(x[z],end=" ")
	z+=1'''

#7. print the ** place of a
'''x="Himachal pradesh"
print(x.replace("a","**"))
'''

#8. swapcase the string 
'''x="Himachal PRADESH"
print(x.swapcase())'''

#9. take a user input and split this string
'''x=input("enter anything below\n:-")
print(x.split())
'''