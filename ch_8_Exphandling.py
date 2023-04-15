 


#			Chepter : Exception Handling
#***************************************************************************************
'''
Exception Handling

When an error occurs, or exception as we call it ,python will normally stop
and generate an error
message. these exceptions can be handled using the try statement:
the try block lets you test a block of code for errors.
the except block lets you handle the error.
the else block lets you execute code when there is no error.
the finally block lets  you execute code , regardless of the result of the 
try -and except block.
'''


#print(x) 	#ts give error because x is no variable

'''
If we make program in exception handling then never my program will crash
if we enter input wrong output throw in exception block it will print a message
your input is wrong.'''

'''
try:
	print(x)
except:
	print("x should be defined")'''
'''
x=3
y=0
z=x/y
print(z)'''
'''
try:
	x=3
	y=0
	z=x/y
	print(z)
except ZeroDivisionError:
	print("zero should not be required")
finally:
	print("have a nice day")'''


'''try:
	x=12
	y=4
	z=x/y
	print(z)
except:
	print("okay")
else:
	print("prince")
finally:
	print("good")'''
'''
x=3
y="hello"
z=x+y
print(z)'''

'''
try:
	x=3
	y="hello"
	z=x+y
	print(z)
except:
	print("put intger here")
finally:
	print("have a nice day")'''

#Else block: you can use the else keyword to define  a block of code to be 
#executed if no errors were raised:
'''
try:
	print("honesty is the best policy")
except:
	print("every thing is good")
else:
	print("nothing is wrong")'''

'''Finally block:
the finally block , if specified, will be executed regardless if the try block
raises an erroror not'''

'''try:
	print("good morning mom")
except:
	print("everything is good")
else:
	print("nothing is wrong")
finally:
	print("good luck")'''

#take a user input .
#create a program in try block, find the voter is eligible or not.
'''
try:
	age=int(input("enter age:"))
	if age>=18:
		print("voter is eligible for vote")
	else:
		print("voter is not eligible for vote")
except:
	print("please enter correct age in integer")
else:
	print("nothing is wrong")
finally:
	print("create by prince")'''


#take user input
#create a program in try block ,find the odd and even number
'''
try:
	x=int(input("enter a number"))
	if x%2==0:
		print("even number")
	else:
		print("odd number")
except:
	print("enter number correctly in integer ")
else:
	print("nothing is wrong")
finally:
	print("good")'''


'''Raise an exception
As a python you can choose to throw an exception if a condition occurs.
to throw (or raise) an exception, use the raise keyword.
example : Raise an error an and stop the program if x is lower than 0:'''

'''x=-1
if x<0:
	raise Exception("sorry no numbers executed below zero")'''


'''the raise keyword is used to raise an exception .
you can define what kind of error to raise , and the text to print the user.
example
raise a typeerror if x is not an integer:'''


'''a=5
if a%2 !=0:
	raise Exception("the number should't be an odd integer")'''



'''take user input and print any random number of even number or any random number
or any random number of odd number
and show the sum of these even numbers and odd numbers'''
'''
try:
	x=int(input("enter a number"))
	y=0
	z=0
	a=0
	while x>y:
		z+=1
		if z%2==0:
			print(f"even : {z}")
			y+=1
			a+=z
	print(f"sum of {x} even number is: {a}")
except:
	#raise Exception
	print("the number should be in integer")
else:
	print("nothing is wrong")
finally:
	print("good")'''
'''
try:
	x=int(input("enter a number :"))
	y=0
	for i in range(2,(x*2)+1,2):
		print(f"even number :{i}")
		y+=i
	print(f"sum of {x} even number is {y}")
except:
	print("please enter number in integer")
else:
	print(f"everything is okay")
finally:
	print(f"good")'''


'''x=(False,-2,-5)
y=(x,2,7)
print(y)'''
#print("\U0001F917")
#print("\U0001F62A")
'''
try:
	x=int(input("enter a number :"))
	y=x+8-4
	print(y)
except:
	print(f"write number in integer there is something went wrong :")
else:
	print(f"good")
finally:
	print(f"best of luck")'''


#x="123prince"
#raise Exception(f"there is some mistake please care this")
 

'''try:
	income=int(input("please enter annual income :"))
	if income <=1000:
		tax=(income*10)/100
		print(f"{income} of 10% is {int(tax)}Rupees")
	elif income>1000 and income<2000:
		tax=(income*25)/100
		print(f"{income} of 25% is {int(tax)}Rupees")
	else:
		print("no tax")
except:
	print("enter number is in integer form")
else:
	print("thank you for paying tax")
finally:
	print("best of luck")
'''

#create program to caluculate of income tax by our anual package
'''
try:
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
except:
	print("please enter amoount correctly in integer !")
else:
	print("Thank you for paying the tax on time !")
finally:
	print("best of luck for you progress !")
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
	print("weldone prince")'''


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
	print("★彡[ᴛʜɪꜱ ᴘʀᴏᴊᴇᴄᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ ᴘʀɪɴᴄᴇ ꜱʜᴀʀᴍᴀ]彡★")'''


