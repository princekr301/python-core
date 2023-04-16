
'''
what is numpy?
Numpy stand for numerical python. Numpy is python library used for working with array.
1.NumPy is a Python library.
2.NumPy is used for working with arrays.
3.NumPy is short for "Numerical Python".
'''
#create array with the help of arange function

#import numpy as np
'''x=np.arange(15)
print(x)		# its print 0 to 14 in single row not in column
print(x.dtype)  
x=np.arange(2,10)
print(x)
print(x.dtype)'''
'''x=np.arange(1,20,3)
print(x)
print(x.dtype)
print(type(x))'''


#how to create basic array
#we create basic array with the help of zeros() funnction and ones() function.
#example :

import numpy as p
'''x=p.zeros(5)
print(x)		#its print zero in decimal form in raw not in column like this[0.0.0.0.0.]
print(x.dtype)	#it return a float data types

y=p.ones(4)
print(y)	# its return [1.1.1.1.] this thing in decimal form in single row.
print(y.dtype)'''
'''
x=p.ones(5)
print(x)
print(type(x))'''


#how can we concatenate arrays
'''
x=p.array([1,2,3,4,5])
y=p.array([6,7,8,9,10])
z=p.concatenate((x,y))
print(z)
print(z.dtype)'''


#we convert data of list and tuple
#and pair does not matter
'''
a=p.array(((1,2,3)))
b=p.array(((4,5,6,45,78,)))
c=p.array(((7,8,9,23)))
d=p.concatenate((a,b,c))
print(d)'''

#if i am putting arange(),zeros(),ones()then output come in single raw in decimal form
#example :-
'''m=p.arange(4.5)
n=p.zeros(3)
o=p.ones(4)
r=p.concatenate((m,n,o))
print(r)'''

#how can be sort arrays.
#x=p.array([12,45,23,48,15,10,52,78])
#y=p.sort(x)	# its return data in accending oreder
#print(y)
#	(OR)
#print(p.sort(x))

'''upcasting
python automatically converts one data type to another data type .
This process does not need any user invoirment pythin prompotes of lower data type,
for example,
1st powerfull data "string"
2nd powerfull data "complex"
3rd powerfull data "float"
4th at last data  "integer"'''

'''x=p.array([12,45,45.1,21j,"prince"])
print(x)
print(type(x))
print(x.dtype)'''

'''x=p.array([12,45,45.1,21j,])
print(x)
print(type(x))
print(x.dtype)'''

'''x=p.array([12,45,45.1])
print(x)
print(type(x))
print(x.dtype)'''

'''
x=p.array([12,45,45])
print(x)
print(type(x))
print(x.dtype)'''


'''x=p.array([12,45,45,21,])
print(x)
print(type(x))
print(x.dtype)'''

#how can be insert  in dimentions in array
#its like a arguments  ndmin=5 then print 5dimention(square bracket)
#example:-
'''x=p.array([12,45,78,26],ndmin=5)
print(x)	#its return 5 square bracket in array
print(x.ndim)'''

#y=p.array({(12,45,78)},ndmin=6)
#print(y)	#we can apply list tupple set as your wish

# How can we count dimention in array
#we can count dimention with the help of {x.ndim} method
#example:-
#x=p.array([[[[[[[[[[[12,45,78,6]]]]]]]]]]])
#print(x)
#print(x.ndim) #its return number of dimention


#what is shape method in array
#example :-
#x=p.array([[[[12,45,78,15,48]]]])
#print(x)
#print(x.shape)

#x=p.array([[[[[12,23,45],[15,59,48]]]]])
#print(x)
#print(x.shape)	#(1, 1, 1, 2, 3)like this shape

#use of transpose method 
#this method is used to inter change the raw and column
#example:-
#x=p.array([[12,45,78,56],[25,14,36,58]])
#print(x.transpose())

#x=p.array([[45,78,52,41],[1,2,12,45]])
#print(x.transpose())
#   (OR)
#print(x.T)
#we can apply x.transpose()  or x.T both gives same output

#x=p.array([[45,78,56,78,56],[78,45,89,56,12],[58,36,14,69,28]])
#print(x)
#print(x.transpose())
#print(x.T)

#use of eye() method in array
#x=p.eye(5)
#print(x) # its return 5x5 of matrix

#x=p.eye(4,5) #first number is for column and second number is for raw
#print(x)

#x=p.eye(2,3) #first peramter for column and second perameter for  raw
#print(x)

#use of diagonal method
#its gives us diagonal 0f eye method

'''x=p.eye(5,3)
print(x)
y=p.diag(x) #its return diagonal of metrix in single raw
print(y)
print(y+5)''' #now we 5 added to in the diagonal


'''x=p.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(x)
y=p.diag(x)
print(y)'''

'''x=p.array([[12,45,78],p.arange(1,4),p.ones(3)])
print(x)
a=p.diag(x)
print(a)'''

#use of diagflat method()
#this diagflat() shift the elements in the matrix as diagonal sequence
'''x=p.diagflat([[1,2,4,9,3],[5,4,7,6,7]])
print(x)
y=p.diag(x)
print(y)'''

'''x=p.diagflat([[1,2,3],[7,8,9]])
print(x)
a=p.diag(x)
print(a)'''

'''x=p.arange(16)
#print(x)
y=p.diag(x)
#print(y)
z=p.diag(y)
print(z)
'''


'''x=p.arange(1,12)
y=p.diagflat(x)
print(y)
z=p.diag(y)
print(z)'''
#print(z+10)
'''
x=p.arange(1,17).reshape(4,4)
print(x)
a=p.diag(x)
print(a)
'''
'''x=p.diagflat([1,2,3,4,5,6])
print(x)
x=p.arange(1,7).reshape(2,3)
print(x)'''

#*****************************************************************************
#  Rivison
#****************************************************************************************
'''x=p.array([[1,2,3],p.arange(3),p.zeros(3),p.ones(3)])
#print(x)
a=p.sort(x)
print(a)'''


'''a=p.arange(5)
b=p.zeros(5)
c=p.ones(5)
d=p.array([2,8,4,6,10])
x=p.concatenate((a,b,c,d))
print(x)
y=p.sort(x)
print(y)'''

'''x=p.array([[12,45,78,89],[58,36,14,25],[78,89,23,56,]],ndmin=5)
print(x)
print(x.ndim)'''

'''x=p.array([[12,45,78,23],[89,56,23,15]])
y=p.transpose(x)
#print(y)
#or 
print(x.T)



x=p.array([[12,45,78,23],[89,56,23,15],[34,45,56,78]])
y=p.transpose(x)
#print(y)
#or
print(x.T)'''



'''x=p.eye(5)
print(x)

y=p.eye(8,10)
print(y)
z=p.diag(y)
print(z)'''

'''x=p.diagflat([34,45,6,8,56,34,34,23])
print(x)
y=p.diag(x)
print(y)
print(y+10)'''

'''x=p.diag((12,45,78))
print(x)'''


#*******************************************************************************************************************************************
#	17-08-2022
#************************************************************************************************************************

import numpy as np
'''x=np.arange(20)
y=x.reshape(4,5)
print(y)
print(np.argmin(y))
print(np.argmax(y))
print(np.argsort(y))'''



#x=np.array([25,47,36,14])
#a=np.array([36,142,55,12])
#b=np.array([58,47,69,35])
#y=np.sum((x,a,b))
#print(y)
#z=np.sum((x,a,b),axis=0)	 #its return sum of column in a list
#print(z)
#z=np.sum((x,a,b),axis=1)	#its return sum of row in aa list
#print(z)
#p=(x+a+b)
#print(p)



#matrix math caluculation

'''x=np.array([[5,4,7,2],[10,8,6,4],[2,6,4,0]])
y=np.array([[10,8,4,5],[12,14,18,16],[4,3,2,1]])
print(x+y)
z=(x+y)
print(np.sort(z))
print(np.argmin(z)) #its return the smallest number of index number in matrix.
print(np.argmax(z)) # its return the biggest number of index number in matrix.
print(np.max(z))	#its return the biggest number from this matrix.
print(np.min(z))	#its return the smallest number from this matrix.
'''

#use of full() method
#x=np.full((4,3),5)
#print(x)
#print(np.diag(x))
#x=np.full((5,5),5),"hii",np.full((6,6),6)
#print(x)

'''x=np.eye(5,5)
print(x)	#its print diagonal in metrix left side to right side
y=np.fliplr(x)	#its print diadonal in metrix right to left side
print(y)'''
'''
x=np.array([[1,2,3,4,5],[6,7,8,9,10]])
y=np.diagflat(x)	#its return a matrix of 9 x 9 .
print(y)
z=np.fliplr(y)
print(z)
print(np.diag(y))	#its return diagonal
print(np.diag(z))
print(x.transpose())'''


#x=np.full((25,20),'prince')
#print(x)

#x=np.array([12,45,78,56,89])
#y=np.mean(x)
#print("mean of this number is :",y)
#z=np.median(x)
#print(z)

'''x=np.arange(4,29,5)
print(x)
print(np.median(x))


x=np.array([4,6,2,1,10])
print(np.median(x))'''

'''x=np.arange(16)
x=x.reshape(4,2,2)
print(x)
print(np.median(x))'''


'''x=np.random.randint(100,200,10)
print(x)
print("Mean :",np.mean(x))'''

'''x=np.random.randint((15,20,10))
print(np.diag(x))'''


'''x=np.arange(40,100,4).reshape(5,3)
print(x)
print("Total number of sum :",np.sum(x))
print(np.sum(x),axis=1)'''





# apply standard deviation
'''x=np.array([2,4,6,8,10])
print(np.std(x))'''



'''x=np.full((4,3,2),8) #4 metrix 3x2 value 4
print(x)

x=np.full((4,5),10)
print(x)'''

'''x=np.array([1,2,3,4,5,6])
 x[0]=258
 x[3]=123
 x[4]=121
 print(x)
 print(x.argmax()) # maximum number of index
 print(x.argmin())''' # minimum number of index

'''
x=np.array([5,2,4,8,6,9,7])
print(x>=5)
print(np.nonzero(x>5))'''

'''x=np.random.randint(12,40,20).reshape(4,5)
print(x)
print(x>35)
print(np.nonzero(x==35))
print(x.T)'''

'''a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a>=10)
print(a[a%2!=0])
print(a[a%2==0])
print((a > 5) | (a == 5))
'''

'''data = np.array([[1, 2], [5, 3], [4, 6]])
print(data)
print(data.min(axis=1))
print(data.max(axis=0))'''




'''data = np.array([[1, 2], [3, 4], [5, 6]])
ones_row = np.array([[1, 1]])
print(data + ones_row)'''


#how to reverse array with the help of flip() method

'''x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(x)
print(np.flip(x))'''


'''x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(x)
print(np.flip(x))'''


#Use of linspace method => its provide a aarray with two number in how many 
#number that you need  its never throw error

'''x=np.linspace(10,50,num=5,retstep=True)
print(x)
print(np.diag(x))'''


#full()method => this method is used to print matrix by your command
#in this you can give four peramter np.full((2matrix,3row,4column),5value)

'''x=np.full((2,4,5),10,dtype=int)
print(x)

y=np.full((10,10),5)
print(y)'''

#random.randint()function => this method is used to print any random number 
#between two number by your command
#ex :-np.random.randint(from20, to40, number15)
'''x=np.random.randint(120,200,40).reshape(10,4)
print(x)
'''

'''def matrix(f):
	x=np.arange(3,38,3).reshape(4,3)
	print(x)
	print(np.diag(x))
matrix()
matrix()'''

#x=np.eye(4,5)
#print(x)

'''x=np.linspace(12,20,num=30,dtype=int).reshape(6,5)
print(x)'''

#**********************************************************************************************************
#	Date 22-08-2022
#****************************************************************************************************
'''import numpy as np
x=np.full((2,4,5),10)
print(x)'''


#numpy iteratting with the help of for loop
#2D one dimention

'''x=np.array([[12,45,78,998,32,45,14]])
for i in x:
	print(i)
	for j in i:
		print(j)'''


#if more then 2 or 3 dimention then use nditer() method 
#np.nditer()

'''x=np.array([[[[[[[[12,478,45,98,56,65,58,8]]]]]]]])
for i in np.nditer(x):
	print(i)'''

#copy() method
#this method is used to do copy the array and become a new data in copy method
'''x=np.array([12,45,78,98,56,23,14])
y=x.copy()
x[0:3]=400
y[0:3]=500
print(x)
print(y)'''

# view() method
'''x=np.array([45,78,98,62,145,89,5])
y=x.view()
y[0]=500
print(x)
print(y)'''

'''x=np.arange(5,50,3)
y=x.view()
print(y)
x[0]=25863
#print(y)
print(x)
#print(x.view())'''

#searching array
#np.where(x) method => with the help of this method we can find the index number of the array
#value 
#x=np.array([[12,45,78,98,23]])
#print(np.where(x==45))

'''x=np.array([12,45,78,89,56,23,26])
#z=np.where(x=23)
y=np.where(x==12)
print(z)
print(y)'''


'''x=np.array([12,45,78,89,56,23,26])
print(np.where(x==78))
print(np.where(x==12))'''


#distribution 
#x=np.random.randint(10,100,size=100)
#print(x)

'''x=np.random.randint(10,100,size=(10,20))
print(x)'''

#commulative sum
'''x=np.array([1, 2, 3])
y=np.cumsum(x)
print(y)'''

'''x=np.arange(1,20)
y=np.cumsum(x)
print(y)'''
'''x=np.arange(5)
y=np.cumsum(x)
print(y)'''

'''numpy product method
with the help of this method we can find the product
its work is do multiplicaion particularlty'''

'''x=np.array([1, 2, 3, 4])
y=np.array([5, 6, 7, 8])
z=np.prod([x,y])

print(z)'''
#output=(1*2*3*4*5*6*7*8)

#np.lcm(num1,num2)
#with the help of this method we can find the lcm of any numbers.
'''x=45
y=40
z=np.lcm(x,y)
print(z)'''

'''a=12
b=20
c=40	#we can find maximum 2 number in one time
d=50
x=np.lcm(a,b)
print(x)'''

'''a=4
b=20
print(np.lcm(a,b))'''


#np.lcm.reduce()
#with the help of this function wee can find 3 or more 

'''arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)'''

'''x=np.array([12,45,78,20])
y=np.lcm.reduce(x)
print(y)'''

'''x=np.array([20,40,60,80])
print(np.lcm.reduce(x))'''
 




#find the HCF WITH THE HELP OF np.gcd() method

'''Finding GCD (Greatest Common Denominator)
The GCD (Greatest Common Denominator), also known as HCF (Highest Common Factor) 
is the biggest number that is a common factor of both of the numbers.'''

'''num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)'''

'''x=500
y=450
z=np.gcd(x,y)
print(z)'''

'''x=45
y=100
z=np.gcd(x,y)
print(z)'''


#np.gcd.reduce()
#with the help of this method we can find hcf more then 2 number.
'''x=np.array([12,40,80,100,15])
y=np.gcd.reduce(x)
print(y)'''

'''x=np.array([45,400,25])
print(np.gcd.reduce(x))'''


#************************************************************************************************************
#using of comperision operator
#x=np.array([12,45,10,15,16,8])
#print(x[x>20])	#its return the value of array greater then then 20

'''x=np.array([1,2,3,4,5,6,7,8,9,10])
y=x[(x>2) & (x<10)]
print(y)'''

#x=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
#y=[(x>4)&(x<10)]
#print(y)
#z=(x>1)|(x>10)
#print(z)

'''x=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
y=np.cumsum(x,axis=1)
print(y)

x=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
y=np.cumsum(x,axis=0)
print(y)'''

#factorial program in numpy
'''n=int(input("enter number which you want factorial :"))
x=np.arange(1,n+1)
print(np.prod(x))'''


#Brodcasting in numpy python

'''x=np.array([1,2,3,4])
y=np.array([5,6,7,8])
print((x*y))'''


'''x = np.sin(np.pi)
print(x)
print(np.pi)'''

#Finding Union
#To find the unique values of two arrays, use the union1d() method.
#np.union1d(x,y)
#Example
#Find union of the following two set arrays:

import numpy as np

'''arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
print(newarr)'''


'''x=np.array([1,1,4,5,4,8,5,4,7])
z=np.array([1,5,9,6,3,8,5,2,7])
a=np.unique(x) #return the single value duplicate value not allowd
y=np.union1d(x,z)  #when two array then it is use don't accsept duplicate value
print(y) #its remove the duplicate values in array like set don't accsept duplicate value.
print(a)'''




#*****************************************************************************************************************************************
#	24-08-2022 		prectice before test
#**************************************************************************************************************************

'''x=np.arange(3,50,3).reshape(4,4)
print(x)'''

'''x=np.zeros((2,10,5),dtype=int)
print(x)

x=np.ones((3,8,5),dtype=int)
print(x)'''

'''x=np.array([[1,2,3,4,5]])
y=np.array([[6,7,8,9,10]])
z=np.concatenate((x,y))
print(z)'''

'''x=np.array([[12,45,78,56,14,24,15,40],[12,45,78,99,25,32,36,48]])
y=np.array([[1,4,5,2,7,3,9,6]])
z=np.concatenate((x,y))
#print(np.sort(z))
#print(np.flip(z))
print(z.transpose())'''

'''x=np.eye(10,10,dtype=int)
print(x)
#print(np.diag(x))

x=np.eye(12,10)
print(np.diag(x))'''

'''x=np.array([[1,4,5,7,2],[9,6,5,8,10]])
y=np.diagflat(x)
print(y)
print(np.diag(y))'''

'''x=np.array([[12,45,78,41],np.arange(4),np.zeros(4)])
print(x)'''

'''x=np.array([10,5,12])
y=np.array([20,25,30])
z=np.sum((x,y),axis=0) # it return sum of all number 
print(z)'''

'''x=np.full((3,4,5),10,dtype=float)
print(x-5)
y=np.full((10,12),25)
print(y)'''

'''x=np.eye(5,5)
print(x)
y=np.fliplr(x)
print(y)'''

'''x=np.arange(16).reshape(4,4)
print(np.fliplr(x))'''

'''x=np.array([[12,45,78,56]])
print(x)
print(np.fliplr(x))
print(np.flip(x))
print(np.sort(x))'''

'''x=np.linspace(12,20,num=10,retstep=True)
print(x)
y=np.linspace(20,40,num=21,dtype=int).reshape(3,7).reshape(7,3).reshape(3,7).reshape(7,3)
print(y)'''

'''x=np.linspace(10,20,40,retstep=True)#.reshape(8,5)
print(x)'''


'''x=np.empty((10,8),dtype=int)
print(x)
x=np.empty((5,4,5),dtype=int)
print(x)'''

'''x=np.random.randint(20,40,50).reshape(10,5)
print(x)'''

'''x=np.array([12,45,78,56,48,15,26,48,59,110,105])
print(x)
print(x.argmax())
print(x.argmin())
print(x.argsort())
print(x.min())
print(x.max())
print(np.max(x))'''


'''x=np.array([[23,45,23,76,12],[54,14,65,33,87]])
print(x.flatten())'''


'''x=np.array([[23,45,23,76,12],[54,14,65,33,87]])
y=np.array([[112,26,59,23,69]])
z=np.concatenate((x,y))
print(z)
print(z.flatten())'''


'''x=np.array([[2,5,8],[9,6,3]])
y=np.array([[7,4,1],[9,5,1]])
z=np.concatenate((x,y))
a=np.concatenate((x,y),axis=0)
b=np.concatenate((x,y),axis=1)
#print(z)
print(a)
print("adding raw wise :\n",b)'''


'''x=np.array([1,2,3])
y=np.array([7,8,9])
z=np.vstack((x,y))
#z=np.stack((x,y))
print(z)

x=np.array([12,45,78,89,56,23,45,48,25])
y=np.array_split(x,5)
print("spliting matrix :\n",y)
'''

'''x=np.array([[[12,45,78,23,56,89,15]]])
for i in np.nditer(x):
	print(i)

x=np.array([[12,23,45,14],[7,8,9,4]])
y=np.array([1,2,3,4])
print(x*y)'''


'''x=np.array([12,45,788,9,235,788,6])
print(np.where(x==788))
print(x[x==788])
print(x[x<50])
print(x[x%2==0])
print(x%2==0)

print(x[x>15])'''

'''x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])
print(np.cumsum((x,y)))'''


'''x=np.array([5,6,7,8])
y=np.array([1,2,3,4])
print(np.subtract((x,y)))'''

'''
x=np.eye(6,5)
print(x)
a=np.full((6,5),10)
print(a)


x=np.array([5,4,6,2,1])
print(np.cumsum(x))

x=np.array([48,56,60,80])
print(np.lcm.reduce(x))

x=np.array([125,225])
print(np.gcd.reduce(x))

x=np.array([15,10,8])
print(np.prod(x))

a=12
b=5
print(np.hypot(a,b))

x=np.array([12,45,78,45,6,15,12,8,78,36,59])
y=np.array([12,45,78,89,56,3,23,14,59,26,15,5])
print(np.unique(x))		# ignore the duplicate value
print(np.union1d(x,y)) #  its show the single value like set dont acsept duplicate value

import pandas as pd
x=pd.Series([12,45,78,89,56,1,5,"prnice"])
print(x)'''

'''np.sqrt()
with the help of this method we can get the sqrt root of the any number'''

'''x=np.array([[256,25,49,64],[81,100,121,144]])
y=(x%2==0)
print(x[x%2==0])
print(np.extract(y,x))
print(y)'''


'''x=np.ones((5,6),dtype=int)
print(x)
print(np.array_split(x,5))
print(x*4)'''
#using of comperision operator
#x=np.array([12,45,10,15,16,8])
#print(x[x>20])	#its return the value of array greater then then 20

'''x=np.array([1,2,3,4,5,6,7,8,9,10])
y=x[(x>2) & (x<10)]
print(y)'''

#x=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
#y=[(x>4)&(x<10)]
#print(y)
#z=(x>1)|(x>10)
#print(z)

a=np.array([2,6,1,9,10,3,27])
#b=a[a>5]
b=a[(a>5)&(a<11)] #its return between 5 to 11 of all number with this method

#b=a[a<11]
print(b)

