

#					Cheptor : File Handling

#*********************************************************************************************************************
#	date 02-08-2022
#*********************************************************************************************************************
'''file Handling

File handling is an important part of any web application
python has several function for creating ,reading,updating and deleting files.

file handling

The key function for working with files in python is the open()function
The open function takes two perameter; filename and mode.
There are four diffrent methods (mode) for opening a file.

"r" - Read - Default value. opens a file for reading ,error if the file does not exists
"a" - append - open a file for appending, creates the file if it does not exists
"w" -write- opens a file for writing,creates the file if it does not exist
"x" - create -creates the specified file return an error

'''
	#syntax
	#	To open a file for rading it is enough to specify 
	#	the name of the file:

'''x=open("pri.py","r")
print(x.read())'''

#y=open("prectice.py","r")
#print(y.read())
'''
file=open("pri.py", "r")
print(file.read(15))'''		# its read the charactor of line

'''x=open("pri.py","r")
print(x.readline())		# its print one line in one time
print(x.readline())
'''

'''x=open("pri.py","a")
x.write("\n\nHonesty is the best policy")
x=open("pri.py","r")
print(x.read())
'''

'''x=open("xyz.py","a")
x.write("\n\nHonesty is the best policy")
x.write("i am prince ")
x=open("xyz.py","r")
print(x.read())'''		# its creat a new file with the text

'''x=open("xyz.py","w")
x.write("failure id the part of sucsses")
x=open("xyz.py","r")
print(x.read())	'''	# its replace the file inter the text 
'''
x=open("wxyz.py","x")
x=open("wxyz.py","w")
x.write("apple is good for health")
x=open("wxyz.py","r")
print(x.read())'''


'''python delete file

To delete a file , you must import the os  module, and run its os . remove() function()
example
remmove the file"xyz.py":'''

#import os
#os.remove("xyz.py")	# if you want to delete permanenet file then use this method 




#x=open("yt.py","r")
#print(x.read())
'''
x=open("wxyz.py","a")
x.write("\nwhat is python ?")
x.write("\npyrhon is a high level interpated oriented language")
x=open("wxyz.py","r")
print(x.read())'''


#***********************************************************************************************************
#	date 	03-08-2022
#******************************************************************************************************************


#import datetime
#x=datetime.datetime.now()
#print(x)

'''delete folder
to delete folder an entire , use the os .rmdir() method:
Example'''
'''import os
os.rmdir("chhotu")
'''
# you can remove only empty folder:


#delete the folder of your your desktop but folder should emepty
#import os
#os.rmdir("killer")
#folder has been deleted from your desktop
'''
import datetime
x=datetime.datetime.now()
print(x)'''

'''some important commands

#cd stand for change directory.
cd.. "come back on c one by one".
cd/.. 'we come back on direct c prompot'
pushd drive_name: "we can change the drive"

pushd D:

popd "we can come back on previous drive"'''

#***********************************************************************************************

#***********************************************************************************************
'''
first print amsg in a file with the help of append "a",msg should be
this is my program.
with the help of try  exceeption method ,find the number is even or
odd.'''
'''x=open("abc.py","a")
#x.write("\nthis is my program")
x.write("\nx=int(input('enter a number'))\ny=0\nwhile x>y:\n\tprint(y)\n\ty+=1")
x=open("abc.py","r")
print(x.read())
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