

'''
what is numpy?
Numpy stand for numerical python. Numpy is python library used for working with array.
1.NumPy is a Python library.
2.NumPy is used for working with arrays.
3.NumPy is short for "Numerical Python".'''

#how can create an array

''''import numpy
x=numpy.array ([1,2,3,4,5])
print(x)
print(type(x))
print(x.size)
print(len(x)) 	# But ye kaam nhi kerega aage chal ke numpy me


import numpy
y=numpy.array (["prince","kumar","sharma"])
print(y) 
print(type(x))'''

import numpy as np

'''x=np.array([1,2,3,4,5,6])
print(x),
print(type(x))

print(np.__version__)'''

#x=np.array([1,2j,8.9,"prince"])
#print(x)

#What is diffrence between numpy array and nd array.
#ndarray() is a class, while numpy.array() is function/function to create ndarray.


#single dimention array:
#1d

'''x=np.array([1,2,3,4,5])
print(x)
print(x.ndim) #it return the lenght of the array.mean square bracket
print(x.size)'''


#2D	it means second dimenstion array

'''x=np.array([[1,2,3,4,5]])
print(x)
print(x.ndim)
print(x.size)


#3D it means third dimention array
x=np.array([[[1,2,3,4,5]]])
print(x)
print(x.ndim)
print(x.size)

#4D  it means dimention array

x=np.array([[[[1,2,3,4,5]]]])
print(x)
print(x.ndim)
print(x.size)'''


'''x=np.array([[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]]])
print(x)
print(x.ndim)
print(x.size)
print(x[])'''

'''
x=np.array([[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]]])
print(x[0][0][2][0])
#print(x[0][0][0:2])
print(x[0,0,0][4]+x[0,0,2][0])'''





#extraxt this value
#return 7,12,18,1,20,3
#return 7 to 10
#return 12 to 13
#revesse thihs array [16,17,18,19,20]
#return 6 to 10
#return 2 to 3
#print each array seperatly
'''
x=np.array([[[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]]]])
print(x[0][0][0][1][1])

print(x[0][0][0][2][1])
print(x[0][0][0][3][2])
print(x[0][0][0][0][0])
print(x[0][0][0][3][4])
print(x[0][0][0][0][2])

print(x[0][0][0][1][1:])	#return 7 to 10
print(x[0][0][0][2][1:3])	#return 12 to 13
print(x[0][0][0][3][-1::-1])#revesse thihs array [16,17,18,19,20]
print(x[0][0][0][1][1:])	#return 6 to 10
print(x[0][0][0][0][1:3])	#return 2 to 3
'''


'''
x=np.array([[[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]]]])
print(x.shape)
print(x.size)
print(x.ndim)'''


#x=np.array([1,2,3,4,5])
#print(x.shape)
#x=np.array([[4,5,6]])
#print(x.shape)

'''x=np.array({1,2,3,4})
print(x)
print(x.shape)'''

#x=np.array([12,10,14,14,])
#print(x)

#import numpy as prince
'''x=prince.array([[[["prnice","kumar","sharma","bihar"]]]])
print(x)
print(x.size)
print(x.ndim)
print(x.shape)'''

#x=prince.array([[[12,45,7,8],[12,45,8,6],[25,36,45,2]]])
#print(x)
#print(x.size)
#print(x.ndim)
#print(x.shape)
#print(x[0][0][0])
#print(x[0][0][0:5])
#print(x[0][1][0:])
#print(x[0][2][0:])
#print(x[0][2][:2])
'''
import numpy as s
x=s.array(["prince",213,14.1,21j])
for i in x:
	print(i)'''

#import numpy as a
#x=a.array([[[1,2,3],[10,10,10]]])
#x=a.array([[582,258,741,963],[456,789,123,159],[1,2,3,4]])
#print(x)	# print the  value of x  
#print(x.shape)	# return list of number and list in number in tuple
#print(x.size)	# return the size of length array
#print(x.ndim)	# return the list of number
#print("how many list in array :",x.ndim)

'''import numpy as chhotu
x=chhotu.array([[[1,4,7],[2,5,8]]])
#print(x)
print(x[0][1][0:1])'''


#import numpy as p

#x=p.array([[12,23,45,56],[12,45,78,56]])
##print(x)
#rint(type(x))
#print(x.size)
#print(x.shape)
#print(x.ndim)
'''x=p.array({"mohan":56,"ram":56,"shyam":78})
print(x)
print(type(x))
print(x.size)
print(x.ndim)
print(x.shape)'''
'''
y=p.array(((12,25,40)))
print(y)
print(y.shape)
print(y.size)
print(y.ndim)'''

'''x=p.array([[1,2,3,5]])
print(x)
print(x.size)
print(x.ndim)
'''
'''y=p.array([[[[12,45,78,89],[1,2,5,1]]]])
print(y)
print(y.size)
print(y.ndim)
print(y.shape)
print(y[0][0][0][0])'''

#import numpy as f
#x=f.array([[[[12,45,78],[77,44,11],[88,55,22],[99,66,33]]]])
#print(x[0][0][0][0])
#print(x[0][0][0])
#print(x[0][0][1])
#print(x[0][0][2])
#print(x[0][0][1][0:])
#print(x[0][0][1][0:3])
#print(x[0][0][2])
#print(x[0][0][1][0:2])


#import numpy as f
'''x=f.array(((((((12,45,78,89,56,23)))))))
print(x)
print(x.ndim)
print(x.shape)'''

'''x=f.array({12:45,45:58,78:41,89:25,"56":5})
print(x)
print(x.ndim)
print(x.shape)'''

#x=f.array([[[12,45,78,25],[78,89,56,45],[25,36,69,47]]])
#print(x[0][0:2])
#print(x[0][1][0:3])
#print(x[0][2][3])
#print(x[0][0][2])
'''print(x[0][0][0:2])
print(x[0][1][0:2])
print(x[0][2][0:2])
print(x[0][2][2:])
print(x[0][0][0:])'''


'''import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)'''

'''import numpy as p
x=p.array([12,45,78,89,56],ndmin=8)
print(x)
print(x.ndim)'''


'''import numpy as f
x= f.array([[[[[23,45,78,85],[47,14,25,58],[96,85,77,65]]]]])
#print(x[0,0,0,0,1:])
#print(x[0,0,0,2,0:3])		# output return [96 85 77]
#print(x[0,0,0,1,2:4])
#print(x[0,0,0,0,1+2])
#print("Add of two number is :",x[0,0,0,0,0]+x[0,0,0,1,2])
print(x[0,0,0,0:3,1:3])'''



#*********************************************************************************************************************
#										16-08-2022
#*********************************************************************************************************************
#create array with the help of arange() function
import numpy as p
'''x=p.arange(6)
print(x)


x=p.arange(2,10)
print(x)


x=p.arange(1,10,2)
print(x)'''


#how to create basic array
#numpy.zeros()method
'''x=p.zeros(6)
print(x)
print(type(x))

y=p.ones(7)
print(y)
print(type(y))

z=p.ones(4)
print(y)
'''

#How can be concadinate arrays.
'''x=p.array([1,2,3,4,5])
y=p.array([6,7,8,9,10])
z=p.concatenate((x,y))
print(z)

a=p.array([4,5,6])
b=p.array([7,8,9])
c=
'''

#how can be sort array
'''x=p.array([12,45,56,10,15])
y=p.sort(x)
print(y)'''
#print(p.sort(x))


#UPCASTING
'''x=p.array([12,450,12.1,])
print(x)
print(x.dtype)
print(type(x))

y=p.array([5,4,5.2,"ram",10])
print(y)
print(y.dtype)

z=p.array([45,56,21j,5.4])
print(z)
print(z.dtype)

a=p.array([12,45,78,56])
print(a.dtype)

x=p.array([12,45,89],ndmin=5)
print(x)'''
'''
x=p.array([12,45,23,56],ndmin=5)
print(x)
print(type(x))
print(x.ndim)
print(x.size)
print(x.shape)'''

#use of transpose()  or T
#it interchange the position of raws and columns:

#x=p.array([[12,45,78,89],[1,2,3,4]])
#print(x)
#print(x.transpose())
#or
#print(x.T)

#y=p.array([[1,2,3,4],[45,78,89,23]])
#print(y.T)  #or print(y.transpose()) output should be same in both case

#eye()  methods

#x=p.eye(2)
#print(x)

#x=p.eye(5)
#print(x)

#x=p.eye(5,5)
#print(x)

#x=p.eye(5,5)	# first perameter for row and second peramter for column
#print(x)
#a=p.diag(x)		# it is factching the diagonal elements
#print(a)
#print(a+5)

#this diagflat() method 
'''x=p.diagflat([[1,2,3,4],[5,6,7,8]])
print(x)
a=p.diag(x)
print(a+5)'''
'''
x=p.arange(16)
#print(x)
a=p.diagflat(x)
b=p.diag(a)
print(a)
print(b)
print(b+3)
#print(a+3)'''

#x=p.arange(16).reshape(4,4)
#print(x)
#a=p.diag(x)
#print(a)
#print(a+5)
#print(p.diagflat(a+5))


#import numpy as np
#x=np.array([[1,2,3,4],[2,6,7,2]])
#a=np.diagflat(x)
#print(a)
#b=np.diag(a)
#print(b)


'''
x=np.arange(10)
print(x)
a=np.daig(x)
print(a)'''

#*********************************************************************************************************************************************************
#	Date : 17-08-2022
#*********************************************************************************************************************************************************

import numpy as n
'''x=n.array([[12,45,78,41],n.arange(4),n.zeros(4)])
print(x)'''

'''x=n.diagflat([[12,45,78,5]])
print(x)'''

'''x=n.array([[12,45,78,23],[78,89,256,23]])
y=n.diagflat(x)
print(y)
z=n.diag(y)
print(z)'''


'''
a=n.array([[45,78,99,56]])
b=n.array([[14,25,36,58]])
c=n.concatenate((a,b))
print(c.transpose())'''

# use of rshape method
#1 diaamention

#x=n.array([12,45,78,89,56,23,15,59,36,58,14,25])
#print(x.reshape(4,3))
#print(x.reshape(2,6))
#print(x.reshape(12,1))
#print(x.reshape(1,3,4))
#print(x.reshape(2,3,2))

'''x=n.arange(20)
print(x.reshape(4,5))
print(x.reshape(2,2,5))'''


'''x=n.arange(16)
#print(x.reshape(4,4))
print(x.reshape(2,2,4))'''


#numpy caluculation
#create two array
import numpy as fj
#sum of total row and collumn
'''x=fj.array([10,5,12])
y=fj.array([20,25,30])
z=fj.sum([x,y]) # it return sum of all number 
print(z)'''



'''x=fj.array([10,5,12])
y=fj.array([20,25,30])
print(fj.sum((x,y)))
z=fj.sum((x,y),axis=1)  #axis=0 add both element in respect to column
print(z)'''

'''
x=fj.array([10,5,12])
y=fj.array([20,25,30])
z=fj.sum([x,y],axis=1)	#axis=1 add these elements with respect to row
print(z)'''

'''x=fj.array([[12,45,78,56],fj.arange(1,5),fj.arange(15,19)])
print(fj.sum(x))'''


'''x=fj.array([10,5,12,23,54])
y=x+5
print(y)



x=fj.array([10,5,12,23,54])
y=x-5
print(y)

x=fj.array([10,5,12,23,54])
y=x/2
print(y)



x=fj.array([10,5,12,23,54])
y=x*2
print(y)


x=fj.array([10,5,12,23,54])
y=x**2
print(y)


x=fj.array([10,5,12,23,54])
y=x+5
print(y)'''


#Numpy math function
#Mean : the avearage value
#to caluculate the mean ,find the sum of all values, and divided by sum number of value.

'''x=fj.array([12,45,78,56,14])
y=fj.mean(x)
print(y)'''
'''x=fj.array([[2,4,5,1,5],[12,13,14,15,6]])
y=fj.array([[12,45,78,56,2],[10,56,74,20,22]])
print(fj.mean((x,y)))'''

# the median value in the value in the middle, after you have sorted all the values.

'''x=fj.array([12,45,78,56,14,100])
y=fj.median(x)
print(y)

x=fj.array([1,2,3,4,5,6])
print(fj.median(x))'''

'''x=fj.array([[4,3,5],[7,9,2]])
y=fj.array([[8,4,2],[3,2,1]])
print(fj.median((x,y)))'''

# apply standard deviation
'''x=fj.array([12,45,78,56,14])
y=fj.std(x)
print(y)

x=fj.array([2,5,7,8,48])
print(fj.std(x))'''

'''x=fj.zeros((5,6))
x=x+2
print(x)
y=x*3
print(y)
'''
#use of full() method
#frist peramter for row ,second perameter for column and third perameter value in metrix

'''x=fj.full((4,6),5)
print(x)
print(x+3)'''


'''x=fj.arange(10,50,5)
print(x)
x=x*2
print(x)'''

#x=fj.arange(100,500,5)
#print(x)


#x=fj.full((5,5),100)
#print(x)


#Inatailizing numpy array with random numbers:
#first perameter for specified for number and secon also specified
#the number and third parameter tell how much number you want

#x=fj.random.randint(1,50,5)
#print(x)

'''x=fj.random.randint(6,50,10)
print(x)'''



'''x=fj.random.randint(100,500,5,)
print(x*5)'''


#three peramter are here frist(4)is for matrix,second(3) is for row
#and third(2)is for column  last(8)vlaue in matrix
'''x=fj.full((4,3,2),8)
print(x)
'''

#use of fliplr() method
'''x=fj.eye(5,5)
print(x)
y=fj.fliplr(x)
print(y)'''

#create a matrix with the zeros and add 2 in this metrix,
#dimentions should be five and row and column should be 5 and 6
#multiply this matrix with 8

'''x=fj.zeros((5,6))
print(x+2)
print(x*8)'''

#create two arrays and apply sum of raw wise
'''x=fj.array([12,45,78,89])
y=fj.array([47,58,69,14])
z=fj.sum((x,y),axis=1)
print(z)'''

#create two arrays and apply sum column wise
'''x=fj.array([12,45,78,89])
y=fj.array([47,58,69,14])
z=fj.sum((x,y),axis=0)
print(z)'''

#*******************************************************************************************************
#	18-08-2022
#********************************************************************************************************
import numpy as np
#x=np.eye(5,6)
#print(x)

#use of linspace methods
#z=np.linspace(4,8,num=4)
#print(z)

'''x=np.linspace(2,7,num=7)
print(x)
x=np.linspace(4,8,num=6)
print(x)'''

#x=np.linspace(2,8,num=4)
#print(x)

#x=np.linspace(3,10,num=5)
#print(x)


#retstep tell us what will be the space between the elements
#x=np.linspace(3,10,num=5,retstep=True)
#print(x)
'''x=np.linspace(2,8,num=4)#retstep=False)
print(x)'''

#x=np.linspace(2.0,3.0,num=5,retstep=True)
#print(x)

#skip the last value of array
#x=np.linspace(3,10,num=5,endpoint=False)
#print(x)
'''x=np.linspace(3,10,num=6,endpoint=False)
print(x)'''


#use of empty() method in numpy array
#x=np.empty([4,5],dtype=int)
#print(x)

'''x=np.empty([10,4,5],dtype=int)
print(x)'''

#x=np.empty([8,10])
#print(x)

#use of argmin() and argmax() method and argsort()
# flip()

'''x=np.array([12,45,78,15,24,10,20])
print(x.argmax())
print(x.argmin())
print(x.argsort())
print(np.sort(x))
print(np.flip(x))	#reverse print the array
print(np.min(x))'''


#x.flatten() method 
#x=np.array([[23,45,23,76,12],[54,14,65,33,87]])
#print(x.flatten())	# its return in one array all value 


'''Numpy join array
joining means putting contents of two or more arrays in a single array.

join 2D arrays'''

'''x=np.array([1,2,3])
y=np.array([7,8,9])
z=np.concatenate((x,y))
print(z)'''

#2d arrays
'''x=np.array([[2,5,8],[9,6,3]])
y=np.array([[7,4,1],[9,5,1]])
z=np.concatenate((x,y))
a=np.concatenate((x,y),axis=0)
b=np.concatenate((x,y),axis=1)
print(z)
print(a)
print("adding raw wise :\n",b)'''

#stack function 
#joining arrays with help of stack function

'''x=np.array([1,2,3])
y=np.array([7,8,9])
#z=np.stack((x,y))
z=np.stack((x,y))
print(z)'''


#joining 
'''x=np.array([[1,2,3]])
y=np.array([[7,8,9]])
#z=np.stack((x,y))
z=np.vstack((x,y))
print(z)'''

#split into arrays
#the return value of the array array_split () method in an erray conatining each of the

'''x=np.array([12,45,78,89,56,23,45,48,25])
y=np.array_split(x,8)
print(y)'''
#print(np.array_split(x,10)) #it not return error any condition list value


#splitting 2D arrays
#x=np.array([[12,45,78],[2,5,8],[9,6,3],[7,4,1],[15,59,58]])
#print(np.array_split(x,5))

#create an empty array raw and column as u want and add 200 with this matrix
'''x=np.empty((5,4),dtype=int)
print(x+200)'''


'''x=np.linspace(12,20,num=4,endpoint=True).reshape(2,2)
print(x)'''

'''x=np.eye(5,8)
print(x)
y=np.diag(x)
print(y+6*7)'''


'''x=np.eye(4,5,dtype=int)
print(x)
y=np.linspace(21,50,num=30).reshape(6,5)
print(y)'''

#x=np.array([[12,45,78,89],[23,12,15,48]])
'''y=np.arange(10).reshape(2,5)
print(np.vstack(y))
print(y.T)'''

#x=np.arange(2,10,3)
#print(x)

'''x=np.zeros((5,4),dtype=int)
print(x)'''
'''
x=np.array([[1,2,3,4],[10,11,12,13]])
y=np.array([[5,6,7,8],[14,15,16,17]])
print(np.concatenate((x,y)))'''
#x=np.array([[12,45,78],[12,36,69]],ndmin=5)
#print(x)

#x=np.eye(3,4,dtype=int)
#print(x)

'''x=np.arange(24).reshape(2,3,4)
print(x)'''
#************************************************************************************************************************
#	22-08-2022
#************************************************************************************************************************
import numpy as np
'''x=np.array([12,45,78,89,56,23,45,78,15])
print(np.array_split(x,4))'''

#Numpy array iterating
#itrating array
#we deal with multidimentinal array in numpy ,we can do this basic for  loop of python

'''x=np.array([1,4,5,7,8,9,6,5,20])
for i in x:
	print(i)'''

'''x=np.array([[1,4,8,9,5],[3,2,5,4,7]])
for i in x:
	for j in i:
		print(j)'''

'''x=np.array([[[12,78,45,9,6],[36,25,59,44,23,56,87],[59,6,32,14,54]]])
for i in x:
	for j in i:
		for k in j:
			print(k)'''



#if more then 5 array then we apply the method np.nditer()
'''x=np.array([[[[[[12,45,78,89,23],[49,15,26,30,46]]]]]])
for i in np.nditer(x):
	#print(i)
	print(i,end=" ")'''

'''x=np.arange(((10)))
for i in np.nditer(x):
	print(i)'''


'''x=np.eye(4,5)
for i in x:
	for j in i:
		print(j)'''

'''copy() method    
this method is used to do copy origininal array and then i will changing the original array then copy array in 
show no change
if copy array in i am changing then original array in show no change ,

main diffrence between copy and view of an array is that copy is a new array ,and the view is just original array


View() method 
view method is used to only view the data.'''


'''x=np.array([12,45,78,89,56,20])
	y=x.copy()
	x[0]=100
	
	print(x)
	print(y)
	
	
	x=np.array([12,45,78,23])
	y=x.view()
	x[2]=780
	print(x)
	print(y)'''	

#searching arrays
#with the help of the is method show the index no of the array number by search.

'''x=np.array([12,45,78,89,56,23])
y=np.where(x==89)
print(y)'''

'''x=np.array([12,45,78,56,23,56,10])
y=np.where(x%2==0)
print(y)'''

'''x=np.array([12,78,45,59,23,51])
print(np.where(x%2!=0))
'''
#x=np.array([45,78,56,89,23,15])
#print(x%2==0)
#print(x>50)
'''x=np.arange(16).reshape(4,4)
print(x>10)'''

'''x=np.array([12,45,78,89,56])
print(x>60)'''


#create a matrix with the help of eye function and add two in this matrix after do exponent with this matrix.
'''x=np.eye(5,5)
y=(x+2)
z=(y**2)
print(z)'''

#create a array with the help of arange function (16) and reshape and multiply with two
#after the multiply find the diagonal of this matrix and substract 1with this diogonal.
'''x=np.arange(16).reshape(4,4)
y=x*2
print(y)
z=np.diag(y)
print(z)
print(z-1)'''


#**********************************************************************************************************
#	23-08-2022
#**********************************************************************************************************
#  use a comperision operator in numpy
#with the help of this comperision show the value of array.

'''x=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(x[x<5])
print(x[x>12])
print(x[x>5])'''

'''x=np.array([[12,78,56,21],[74,51,62,59]])
print(x[x%2==0])

x=np.array([[14,58,69,47,52,34],[47,59,35,14,31,101]])
print(x[x%2!=0])'''


#logical caluculation in numpy
#its show the boolen value.

'''x=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
y=x[(x>2)&(x<10)]
print(y)'''

''' 
z=(x>1)&(x<10)
print(z)'''


#use of comunity sum in numpy 	np.cumsum()
#with the help of this method we add number in array in particullarly

'''x=np.array([[1,2,3,4],[5,6,7,8]])
y=np.cumsum(x)
print(y)
z=np.cumsum(x,axis=0) 	#its adding numbe in verically
print(z)
a=np.cumsum(x,axis=1)	#its adding number in horizontally
print(a)'''

#Brodcaasting in numpy
#in this caluculation we can apply only number of element shoould bw same then 
#it it will run else throw error

'''x=np.array([1,2,3,4])
y=np.array([5,6,7,8])
print(x*y)'''

'''x=np.array([[4,5,6,3],[7,8,9,2]])
y=2
print(x*y)'''


'''x=np.array([[[7,5,3],[9,5,1]]])
y=np.array([8,5,2])
print(x*y)'''

#***************************************************************************************************************************
#	24-08-2022
#*********************************************************************************************************************
'''x=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
y=x.reshape(1,4,5)
print(y)
b=np.concatenate(y)
print(b)
z=y.T
print(z)'''

'''a=[]
x=int(input("enter number :"))
for i in range(x):
	y=int(input("enter value:"))
	a.append(y)
#print(a)
d=int(input("enter dimention :"))
arr=np.array([a],ndmin=d)
print(arr)'''


#***********************************************************************************************************
#*  ddate 05-09-2022
#***********************************************************************************

#create 2D and convert 6 dimention
import numpy as np
'''x=np.array([[12,45,78,56]],ndmin=6)
print(x)'''

#create four dimention and return elements of the array
'''x=np.array([[[[121,78,45,89,56,23]]]])
print(x[0:2])'''

# create 4 array and put 4d and return 2 array
'''x=np.array([[[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]]])
print(x[0,0,0:2])

x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y=x.reshape(6,2)
z=x.reshape(3,4)
print(y)
print(z)'''

'''x= np.array([12,45,78,89])
y=np.array([14,25,366,47])
print(np.stack((x,y),axis=0))
print(np.stack((x,y),axis=1))'''

x=np.ones((5,6),dtype=int)
print(np.array_split(x,5))













