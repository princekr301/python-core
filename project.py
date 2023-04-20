#project 1.
#	In this project we see the reult of all student by the input of 
#	name.
#	you will display the full marks, obtained marks,persantage,and
#	student greeting for this work.


'''
cheak="y"
while cheak=="y":
	try:
		print("ıllıllı⭐🌟 R͙e͙s͙u͙l͙t͙ 🌟⭐ıllıllı")
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
		#result.pop("chhotu kumar") # to delete the marksheet


		name=input("Name of student:")
		ob_marks=sum(result[name].values())
		#per=(sum(result[name].values())/500)*100
		per=ob_marks/5	
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
		print("please enter student name correctly !")
		print("There is no student by this name!")
	else:
		print("★彡[ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴ ᴅᴇᴀʀ ꜱᴛᴜᴅᴇɴᴛ!]彡★")
	finally:
		print("★彡[ᴛʜɪꜱ ᴘʀᴏᴊᴇᴄᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ ★ᴘʀɪɴᴄᴇ ᴋᴜᴍᴀʀ★]彡★")
	cheak=input("If you want to cheak another student of result then press y  else n :")
'''








try:
	print("\nıllıllı⭐🌟 R͙e͙s͙u͙l͙t͙ 🌟⭐ıllıllı,⭐🌟 R͙e͙s͙u͙l͙t͙ 🌟⭐ıllıllı\n")
	x={1:{"hnd":64,"eng":56,"math":89,"sc":64,"sst":63},
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
		print("fail")
except:
	print("Result not found!")
	print("Please enter correct roll number!")
else:
	print("★彡[ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴ ᴅᴇᴀʀ ꜱᴛᴜᴅᴇɴᴛ!]彡★")


	




	
'''
#Project 2.
#		Mini caluculator 
#	this project coluculate any two number.
try:
# mini caluculator program
	first=input("enter first number :")
	operator=input("enter operator(+ - * / ** % // ) : ")
	second=input("enter second number :")
	first=float(first)
	second=float(second)

	if operator=="+":
		output=(first+second)
	elif operator=="-":
		output=(first-second)
	elif operator=="*":
		output=(first*second)
	elif operator=="/":
		output=(first/second)
	elif operator=="%":
		output=(first%second)
	elif operator=="//":
		output=(first//second)
	elif operator=="**":
		output=(first**second)
	#else:
	#	output=("invalid number")
	print(f"Output :{output}")
except:
	print("please enter number correctly!")
	print("please enter operator correctly!")
else:
	print("Caluculate Again!")
finally:
	print("!")'''



#x=eval(input("enter num operator 2nd :-"))
#print(x)





#3.dice roll generator

'''
import random
min_value=1
max_value=6
roll_again="yes"
while roll_again=="yes" or roll_again=="y":
	x=input("you guess min_value :")
	y=input("you guess max_value :")
	print("dice is rolling....")
	print("the value are :")
	a=random.randint(min_value,max_value)
	b=random.randint(min_value,max_value)
	print(a)
	print(b)
	if x and y == a and b:
		print("you won the game")
	else:
		print("\nyou lost the game\n")
	roll_again=input("Roll the dice again :")
'''






'''while True:
	try:
	# Make a program so that when enter a state by user ,
	# its capital will be shown
		state_capital={
		"bihar": 	"patna",
		"assam":  		"dispur",
		"uttar pradesh":	 "lucknow",
		"rajsthan": 			 "jaipur",
		"goa": 						"panji",
		"kerala":						"Thiruvananthapuram",
		"manipur": 							"imphal",
		"gujarat": 								"gandhinagar",
		"jharkhand":						 		"ranchi",
		"madhya pradesh":						 		"bhopal",
		"punjab": 											"chandigarh",
		"tamil nadu":										 "chennai",
		"west bengal":											 "kolkata",
		"uttarakhand":												 "dehradun",
		"odisha":														"bhubaneswar",
		"Arunachal pradesh":										 "itanagar",
		"chhatisgarh": 												"raipur",
		"haryana": 												"chcandigarh",
		"himachal pradesh":									 "shimla",
		"karnatka": 										"bengaluru",
		"meghalaya": 									"shillong",
		"mizoram": 									"aizawl",
		"nagaland":								 "kohima",
		"sikkim":							 "gangtok",
		"telangana": 						"Hyderabad",
		"tripura": 						"Agartala",
		"channai" :					"Tamilnadu",
		"maharstra":			"Mumbai",
		"jammu and kashmir" :"Srinagar"
		}

		x=input("\nenter the name of state :-")
		print("the capital of",x,"is",state_capital[x])
	except:
		print("\nplease enter the state name correctly :")
	else:
		print("that's great!")
	#finally:
		#print("good luck")
	x=input("\nif you wnat to break this program then press b  else press enter :")
	if x=="b":
		print("thank you!")
		break'''






'''
while True:
	try:
		state_capital={
		"Andhra Pradesh":	"Amaravati",
		"Arunachal Pradesh":"Itanagar",
		"Assam":"Dispur",
		"Bihar":"Patna",
		"Chhattisgarh":	"Naya Raipur",
		"Goa":	"Panaji",
		"Gujarat":	"Gandhinagar",
		"Haryana":	"Chandigarh",
		"Himachal Pradesh":	"Shimla",
		"Jharkhand":	"Ranchi",
		"Karnataka":"Bengaluru (formerly Bangalore)",
		"Kerala":	"Thiruvananthapuram",
		"Madhya Pradesh":	"Bhopal",
		"Maharashtra":	"Mumbai",
		"Manipur":	"Imphal",
		"Meghalaya":	"Shillong",
		"Mizoram":	"Aizawl",
		"Nagaland":	"Kohima",
		"Odisha":	"Bhubaneswar",
		"Punjab":	"Chandigarh",
		"Rajasthan":	"Jaipur",
		"Sikkim":	"Gangtok",
		"Tamil Nadu":	"Chennai",
		"Telangana":	"Hyderabad",
		"Tripura":	"Agartala",
		"Uttar Pradesh":"Lucknow",
		"Uttarakhand":	"Dehradun, Gairsain (Summer)",
		"West Bengal":	"Kolkata"}
		y=input("\nenter the name of state :")
		yy=state_capital[y]
		print(f"The capital of {y} is :{yy}!")

	except:
		print("please enter First letter in capital letter of state :")
	else:
		print("That's Great!\n")
	x=input("if you want to break this program then press  p  else press enter :")
	if x=="p":
		print("Thanks for you suport!")
		break'''







#Age caluculator program => with the help of this program you can find the age of any person with the help of D.O.B


'''from datetime import date
while True:
	try:
		def agecaluculator(birthday):
			today=date.today()
			age=today.year-birthday.year-((today.month,today.day)<(birthday.month,birthday.day))
			print(f"\nYour Age is :{age}")
		agecaluculator(date(int(input("\nenter date of year :")),int(input("enter date of month :")),int(input("enter birthday :"))))
	except:
		print("enter the date of birth correctly!")
	else:
		print("\nThank you for intrested in Age caluculator!\n ")
	number=input("if you want cheak other person of age then press enter else press  no :")
	if number =="no":
		print("Thank you!\n")
		break'''

#snake water and gun game

'''
import random
while True:
	try:

		def game(comp,you):
			if comp==you:
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

		print("computer choose sanke (s) gun (g)  water (w) :-")
		co = random.randint(1,3)
		if co==1:
			comp="s"
		elif co==2:
			comp="g"
		elif co==3:
			comp="w"
		you=input("Your choice :sanke (s) gun (g)  water (w) :- ")
		a=game(comp,you)

		print("You choice :",you)
		print("comp choice :",comp)

		if a==None:
			print("The game is tie !")
		elif a==True:
			print("You won the game !")
		else:
			print("You lose the game !")
	except:
		print("enter name correctly!")
	else:
		print("good job!")
	a=input("if you want to break the game press y")
	if a=="y":
		print("thanks")
		break'''





#user id nad password create a new account and log in 

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







#countdown project or alarm setup
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
				print(" Its time to wake up !")
				break'''





'''
#random password generator
import random

x="abcdefghijklmnopqrstuvwxyz"
y="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
z="!@#$%^&*/"
a="1234567890"
mix=x+y+z+a
lenth=8

password="".join(random.sample(mix,lenth))
#password=random.randint(mix,lenth)
print(f"Your new password is :=> {password}")'''





#mini atm machine project

'''
import time
print("=========================.......---------------.............................................................................")
print("Welcome to Prince Bank !!")
time.sleep(4)
print("----------------------------------------------------------------------------------------------------------------------------")
print("please insert your card!")
time.sleep(5)
password=1234
balance=14500
chance=4
#print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
print("**************************************************************************************************************")
print("""choice your option
	1==balance inquairy
	2==withdrawl_balance
	3==credit balance
	4==exit
---------------------------------------------------------------------------------------------------------------------------------""")
time.sleep(2)
option=int(input("selcet option :"))

while True:
	if option==1:
		time.sleep(3)
		while chance!=0:
			print("---------------------------------------------------------------------------------------------------------------")
			pin=int(input("enter your four digit pin:- "))
			if password!=pin:
				chance-=1
				print("Your pin is incorrect please try again!")
				print("------------------------------------------------------------------------------------------------------------")
			else:
			# password==pin:
				print("-----------------------------------------------------------------------------------------------------------")
				#print("--_-_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_---\n")
				print("please wait cheaking your account!")
				time.sleep(3)
				print(f"Your balnce is {balance}")
				time.sleep(3)
				print("\nthank you for Using Prince Bank !!")
				break
		
	elif option==2:
		withdrawl_amount=int(input("enter your ammount:"))
		time.sleep(3)
		while chance!=0:
			print("-----------------------------------------------------------------------------------------------------------------")
			pin=int(input("enter your four digit pin:- "))
			if password!=pin:
				chance-=1
				print("Your pin is incorrect please try again!")
				print("-----------------------------------------------------------------------------------------------------------")
			else:

			# password==pin:
				print("----------------------------------------------------------------------------------------------------------")
		
				print("please wait transaction is being processing!")
				time.sleep(4)
				print("please collect your ammount!")
				time.sleep(2)
				balance=balance-withdrawl_amount
				print("--_-_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_---")
				print(f"Your left balance is {balance}")
				time.sleep(3)
				print("\nThank you for Using Prince Bank !!")
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
		
				print("Put your ammount in the ATM ! slot")
				time.sleep(2)
				print("please wait your amount is adding !")
				time.sleep(3)
				balance=balance+credit
				print("--_-_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--__---_-----____------___")
				print(f"Your updated amount is {balance}")
				time.sleep(2)
				print("\nThank you for using Prince Bank !!")
				break
	elif option==4:
		print("Thank you for your support")
	user_exit=input("\nWould you like to use again?  press Yes/No  :")
	if user_exit=="Yes":
		print("\n///////////////////////////////////////////////////////////////////")
		print("\nThank you for using Prince bank !!")
		continue
	else:
		break'''
 

 #countdown project
'''import time
def countdown(t):
	while t:
		mins,secs=divmod(t,60)
		timer='{:02d}:{:02d}'.format(mins,secs)
		print(timer,end="\r")
		time.sleep(1)
		t-=1
	print("fire i the whole!")

t=input("enter the time in second: ")
countdown(int(t))'''




#Students of class room id password


import time
'''
print("----------------------------------------------------------------")
print("Welcome to the Prince Tutorial!")
print("----------------------------------------------------------------")
time.sleep(2)
print("----------------------------------------------------------------")
print("\nPlease choice which subject do you want to learn\nFor english press == 1\nFor math press == 2\nFor science press == 3\nFor social studies press == 4")
time.sleep(3)
try:
	print("----------------------------------------------------------------")
	x=int(input("\nplease selcet Which subject do want to learn  :"))
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
		time.sleep(1)
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




#Print calendar of any months with the cooding

import calendar


'''
year=2022
month=10
x=calendar.month(year,month)
print(x)'''



# select * from emp;

insert into emp(employee_id,employee_name,Age,salary,Department)

values(201,"bhanu Patel",32,100000,"ceo"),
(202,"Ankit gill",40,50000,"manager"),
(203,"Manu singh",32,20000,"Data Analytics"),
(204,"vivek gulliya",35,10000,"Watchman"),
(205,"rohit sharma",40,25000,"MIS"),
(206,"majnu bhai",22,250000,"Boss"),
(207,"uday settie",25,150000,"Boss"),
(208,"Dr Ghunghru",48,45000,"Actor"),
(209,"Rajeev",34,78000,"Hero"),
(210,"Sanjana",30,45000,"Heroine"),
(211,"princess",20,250000,"wife"),
(212,"priya sharma",457800,"data scientist"),
(213,"mamta sharma",45,78000,"machine learning eng");
(214,"kritika senan",29,7800,"sales"),
(215,"deepika patukor",30,8400,"Data Scietist"),
(216,"suraj kumar",29,78000,"Data engineer"),
(217,"Bhavya singh",23,8000,"teacher"),
(218,"Arya sharma",19,7500,"teacher"),
(219,"komal kumari",20,4500,"sales"),
(220,"kajal singh",26,12000,"HR"),
(221,"Rishu kumari",18,15000,"Teacher"),
(222,"Archana kumari",17,6000,"Student"),
(223,"Guriya devi",40,15000,"sales"),emp
(224,"Anshu singh",16,45000,"sales"),
(225,"Mayuri sharma",31,25000,"Data Analytics"),
(226,"Mayra sharma",25,48000,"DS"),
(227,"Manya sharma",26,58000,"DA"),
(228,"Priya sharma",28,45000,"Sales"),
(229,"Rajeev sharma",35,78000,"Managerr"),
(230,"barkha sharma",23,40000,"data analytics"),
(231,"Megha sharma",21,31000,"Data Engineer"),
(232,"Muskan sharma",19,45000,"ML engineer"),
(233,"Anshuman sharma",22,32000,"Software engineer"),
(234,"MAdhu sharma",26,54000,"Media Analytics"),
(235,"Anshu singh",21,15000,"MIS"),
(236,"Dr.Babita sharma",85000,"Proffesor"),
(237,"Ashmita sharma",18,25000,"Teacher"),
(238,"Tulshi sharma",20,15000,"Teacher"),
(239,"Manash sharma",18,45000,"Superviser"),
(240,"Amrendra sharma",45,80000,"Owner"),
(241,"Manish sharma",48,78000,"Buisness Man"),
(242,"Deepa sharma",29,29000,"Hotel Managmet"),
(243,"Jyoti sharrma",25,35000,"Air hostage"),
(244,"Saurav sharma",21,28000,"army"),
(245,"Sonu shrama",20,18000,"Teacher"),
(246,"Deepak sharma",30,25000,"Assistant"),
(247,"Rupak sharma",27,20000,"Teacher"),
(248,"Renu sharma",28,45000,"stenographer"),
(249,"Sakuntala sharma",42,29000,"sales"),
(250,"Mukesh singh",46,35000,"principal");

