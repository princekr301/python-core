



'''print('welcome to Prince Bank ! machine')
restrat=("y")
chances=3
balance=1000
while chances >= 0:
password=int(input('please enter four digit pin'))
if password==(1234):
	print("you entered your pin correctly")
	while restart not in ('n','NO','no','N'):
		print("please press 1 for your balance\n")
		print("please press 2 for your withdrawl\n")
		print("please press 3 for your pay in\n")
		print("please press 4 for your return card\n")
		option = int(input("what would you like to choose?"))
		if option ==1:
			print('your balance is inr',balance,'\n')
			restart =input("would you like to go back?")
			if restart in ('n','NO','no','N'):
				print('thank you for banking with Prince Bank ! machine')
				break
		elif option == 2
			option2 = ('y')
			withdrawl = int(input('how much would you like to withdraw?'))
			if withdrawl in [10,20,40,60,80,100]:
				balance = balance - withdrawl
				print('your baalance is now inr',balance)
				restart = input('what would you like to do?')
				if restart in ('n','NO','no','N'):
					print('thank you for banking with Prince Bank ! machine')
					break'''




'''
import time
print("=========================.............")
print("Welcome to Prince Bank !!")
time.sleep(5)
print("----------------------------------------")
print("please insert your card!")
time.sleep(5)
password=1234
balance=5000
print("/////////////////////////////////////////////////////////")

print("enter your four digit pin")
while True:
	print("---------------------------------------------------")
	pin=int(input("enter your digit pin:- "))
	if password!=pin:
		print("Your pin is incorrect please try again!")
		print("------------------------------------------------")
	if password==pin:
		print("-------------------------------------------------")

		print("""choice your option
			1==balance inquairy
			2==withdrawl_balance
			3==credit balance
			4==exit
			----------------------------------------------------------""")
	

		time.sleep(4)
		option=int(input("selcet option :"))
		if option==1:
			time.sleep(5)
			print("--_-_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_---")
			print(f"Your balnce is {balance}")
			time.sleep(3)
			print("\nthank you for Using Prince Bank !!")
			break
		elif option==2:
			withdrawl_amount=int(input("enter your ammount:"))
		
			print("please wait transaction is being processing!")
			time.sleep(4)
			print("please collect your ammount!")
			time.sleep(2)
			balance=balance-withdrawl_amount
			print("--_-_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_---")
			print(f"Your left balance is {balance}")
			time.sleep(3)
			print("Thank you for Using Prince Bank !!")
			break
		elif option==3:
			credit=int(input("Enter your credit amount :"))
			time.sleep(2)
			print("Put your ammount in the Bank ! slot")
			time.sleep(2)
			print("please wait your amount is adding !")
			time.sleep(3)
			balance=balance+credit
			print("--_-_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_---")
			print(f"Your updated amount is {balance}")
			print("Thank you for using Prince Bank !!")
			break
		elif option==4:
			break'''



'''
import time
print("=========================.......................................................................................................................................................................................")
print("Welcome to Prince Bank !!")
time.sleep(5)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("please insert your card!")
time.sleep(5)
password=1234
balance=5000
print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")

#print("enter your four digit pin")
#while True:
#	print("---------------------------------------------------")
#	pin=int(input("enter your digit pin:- "))
#	if password!=pin:
#		print("Your pin is incorrect please try again!")
#		print("------------------------------------------------")
#	if password==pin:
#		print("-------------------------------------------------")

print("""choice your option
	1==balance inquairy
	2==withdrawl_balance
	3==credit balance
	4==exit
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")
	

time.sleep(2)
option=int(input("selcet option :"))

if option==1:
	time.sleep(3)
	while True:
		print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
		pin=int(input("enter your four digit pin:- "))
		if password!=pin:
			print("***************************************************************************************************************************************************************************************************")
			print("You  entered incorrect pin please try again!")
			print("----------------------------------------------------------------------------------------------------------------")
		if password==pin:
			print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
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
	while True:
		print("---------------------------------------------------")
		pin=int(input("enter your four digit pin:- "))
		if password!=pin:
			print("Your pin is incorrect please try again!")
			print("------------------------------------------------")
		elif password==pin:
			print("-------------------------------------------------")
	
			print("please wait transaction is being processing!")
			time.sleep(4)
			print("please collect your ammount!")
			time.sleep(2)
			balance=balance-withdrawl_amount
			print("--_-_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_---")
			print(f"Your left balance is {balance}")
			time.sleep(3)
			print("Thank you for Using Prince Bank !!")
			break

elif option==3:
	credit=int(input("Enter your credit amount :"))
	time.sleep(2)
	while True:
		print("---------------------------------------------------")
		pin=int(input("enter your four digit pin:- "))
		if password!=pin:
			print("Your pin is incorrect please try again!")
			print("------------------------------------------------")
		elif password==pin:
			print("-------------------------------------------------")
	
			print("Put your ammount in the Bank ! slot")
			time.sleep(2)
			print("please wait your amount is adding !")
			time.sleep(3)
			balance=balance+credit
			print("--_-_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_---")
			print(f"Your updated amount is {balance}")
			time.sleep(2)
			print("Thank you for using Prince Bank !!")
			break
elif option==4:
	print("Thank you for your support")
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
		try:
			withdrawl_amount=int(input("enter your ammount:"))
		except:
			print("plese amount in integer only")
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
	user_exit=input("\nWould you like to exit? Yes/No  :")
	if user_exit=="Yes":
		print("\n///////////////////////////////////////////////////////////////////")
		print("\nThank you for using Prince bank !!")
		break
	else:
		continue