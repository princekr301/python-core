

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#									Matplotlib
#----------------------------------------------------------------------------------------------------------------------------------
#									19-09-2022
#--------------------------------------------------------------------------------------------------------------------------------------------

#		pip install Matplotlib
#-----------------------------------------------------------------------------------------------------------------------------------
import matplotlib 
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

#How can be create a line plot
 
'''x=np.arange(1,11)
y=x*2
plt.plot(x,y)
#plt.show()

#How can be add title on label
plt.title("simpleline plot")
plt.xlabel("data on axis-x")
plt.ylabel("data on axis-y")
#plt.show()

# How can be change the color of graph
plt.plot(x,y,color="y",linestyle="*",linewidth=10)
plt.show()'''


'''x=np.arange(1,11)
y=x*2
z=x*3
plt.plot(x,y,color="g",linestyle=":",linewidth=5)
plt.plot(x,z,color="y",linestyle=":",linewidth=5)
plt.title("Data nisulization")
plt.xlabel("axis-x, range")
plt.ylabel("axis-y, range")
plt.grid(True)
plt.show()'''

'''
x=np.arange(1,11)
y=x*2
z=x*3

plt.subplot(1,2,1)	# first 1 for perameter  row , second 2 for columns and last 1 perameter for subplot
plt.plot(x,y,color="green",linestyle=":",linewidth=5)
plt.subplot(1,2,2)
plt.plot(x,z,color="brown",linestyle=":",linewidth=5)
plt.show()'''



# i want to stack both plot columns wise

'''
x=np.arange(1,11)
y=2*x
z=3*x
plt.subplot(2,1,1)
#plt.subplot(2,1,2)
plt.plot(x,y,color="black",linestyle=":",linewidth=5)
plt.subplot(2,1,2)
plt.plot(x,z,color="red",linestyle=":",linewidth=5)
plt.show()'''

#--------------------------------------------------------------------------------------------------------------------------
#										Date = 20-09-2022
#--------------------------------------------------------------------------------------------------------------------------
 
#Now we create bar plot.

#we apply bar plot on the catogorical and we apply histogram for numerical values.
'''
Student={"Prince":89,"Ankit":78,"Priya":85,"Suraj":66}
x=list(Student.keys())
y=list(Student.values())
print(x)
print(y)
plt.bar(x,y)
plt.xticks(rotation="vertical")
plt.show()'''


#Vertical bat plot


'''vegitable_basket={"Brinjal":100,"Potato":145,"Tomato":123}
veg_name=list(vegitable_basket.keys())
veg_cost=list(vegitable_basket.values())

plt.bar(veg_name,veg_cost)
plt.title('bar plot')
plt.xlabel("Vagitables name")
plt.ylabel("vegitable cost")
plt.grid()
plt.show()'''


#Horizontal plot

'''
vegitable_basket={"Brinjal":100,"Potato":145,"Tomato":123}
veg_name=list(vegitable_basket.keys())
veg_cost=list(vegitable_basket.values())

plt.barh(veg_name,veg_cost,color="red",)
plt.title('bar plot')
plt.xlabel("Vagitables name")
plt.ylabel("vegitable cost")
plt.grid()
plt.show()'''

#Scatter plot
'''x=[10,20,30,40,50,60,70,80,90]
y=[8,1,7,2,0,3,7,3,2]

plt.scatter(x,y)
plt.show()'''


'''x=[4,5,1,6,2,3,7,8]
y=[80,20,30,40,50,60,80,90]
plt.scatter(x,y,color="red")
plt.title("prince")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()

plt.show()'''


#if i want to change the size of perameter, and cahnge the mark

'''x=[4,5,1,6,2,3,7,8]
y=[80,20,30,40,50,60,80,90]
plt.scatter(x,y,color="red",marker="*",s=200)
plt.title("prince")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()

plt.show()'''


'''x=[4,5,1,6,2,3,7,8]
y=[80,20,30,40,50,60,80,90]
z=[12,15,16,25,10,2,7,9]
plt.scatter(x,y,color="red",marker="*",s=200)
plt.scatter(x,z,marker="o",color="g",s=200)
plt.title("prince")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()

plt.show()'''

#Create  scatter sub plot row wise and column wise
#column wise

'''x=[4,5,1,6,2,3,7,8]
y=[80,20,30,40,50,60,80,90]
z=[12,15,16,25,10,2,7,9]
plt.subplot(1,2,1)
plt.scatter(x,y,color="blue",marker="*",s=200)
plt.title("prince")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.subplot(1,2,2)
plt.scatter(x,z,color="green",marker="o",s=100)
plt.title("prince")
plt.xlabel("x-axis")
plt.ylabel("z-axis")
#plt.grid()

plt.show()'''

#Row wise
'''
x=[4,5,1,6,2,3,7,8]
y=[80,20,30,40,50,60,80,90]
z=[12,15,16,25,10,2,7,9]
plt.subplot(2,1,1)
plt.scatter(x,y,color="blue",marker="*",s=200)
plt.title("prince")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.subplot(2,1,2)
plt.scatter(x,z,color="green",marker="o",s=100)
plt.title("prince")
plt.xlabel("x-axis")
plt.ylabel("z-axis")
plt.grid()
#plt.subplots_adjust(left=0,bottom=0.1,right=0.9,top=0.9,wshape=0.5,hshape=0.5)

plt.show()'''


#histogram plot =>histogram show the how many times all number or name are reapeted by the graph
'''
x=[5,4,5,4,7,5,4,7,8,5,4]
plt.hist(x,color="g")
plt.show()'''

'''
x=[1,2,3,4,5,6,1,2,3,4,5,3,1,2,5,4,5,10,9,8,10]
plt.hist(x,color="pink",bins=5)
plt.show()'''	# its show how many time all name are reapeted


'''x=pd.read_csv(("iris.csv"))
y=x.head()
plt.bar(y)
plt.show()'''


#------------------------------------------------------------------------------------------------------------------------------
#					Date  21-09-2022
#------------------------------------------------------------------------------------------------------------------------------

#pie chart => A pie chart is a graph that repersent the data in the circular graph.
#the slice of pie 
#show the relative size of the data


#Why we ue this pie chart

'''vegitable=["Potato","brinjal","onion","chilly"]
cost=[85,74,40,96]
plt.pie(cost,labels=vegitable)
plt.show()
'''


'''vegitable=["Potato","brinjal","onion","chilly"]
cost=[85,74,40,96]
#plt.pie(cost,labels=vegitable,autopct="%0.2f%%",colors=["yellow","grey","green","red"])
plt.pie(cost,labels=vegitable,autopct="%0.2f%%",colors=["yellow","grey","green","red"])
plt.show()'''



#Use of doughnut chart

''' 
vegitable=["Potato","brinjal","onion","chilly"]
cost=[85,74,40,96]
plt.pie(cost,labels=vegitable,radius=1)
#plt.pie(cost,labels=vegitable,autopct="%0.2f%%",colors=["yellow","grey","green","red"])
#plt.pie(cost,labels=vegitable,autopct="%0.2f%%",colors=["yellow","grey","green","red"])
plt.pie([1],colors=['w'],radius=0.4)
plt.show()'''


'''vegitable=["Potato","brinjal","onion","chilly"]
cost=[85,74,40,96]
plt.pie(cost,labels=vegitable,radius=7)
#plt.pie(cost,labels=vegitable,autopct="%0.2f%%",colors=["yellow","grey","green","red"])
plt.pie(cost,labels=vegitable,autopct="%0.2f%%",colors=["yellow","grey","green","red"])
plt.pie([1],colors=['w'],radius=2)
plt.show()'''

# Explode the pie chart


'''y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()
'''
'''
name=["prince","priya","pappu","vicky","mom"]
age=[24,25,28,18,45]
crack=[0.2,0,0,0,0.1]
plt.pie(age,labels=name,explode=crack,autopct="%0.2f%%")
plt.title("faimly_age_Diffrence")
plt.show()'''


#/---------------------------------------------------------------------------------------------------------------------------------
#				/----------------	21-09-2022	--------------	SeaBorn  --------------/
#/---------------------------------------------------------------------------------------------------------------------------------
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd

#How to start SeaBorn

#First off all install seaborn from cmd in write given below ->
#pip install SeaBorn



'''x=sns.load_dataset("fmri")
#print(x)
y=x.head()
print(y)
sns.lineplot(x="timepoint",y="signal",data=x)
plt.show()'''

'''
x=sns.load_dataset("fmri")
#print(x)
#y=x.head()
print(x)
sns.lineplot(x="timepoint",y="signal",data=x,hue="event")
plt.show()'''


'''
a={"Team":["india","pakistan","india","pakistan","india","pakistan","india","pakistan"],
"score":[12,10,8,15,2,6,8,9],
"over":[1,1,2,2,3,3,4,4]}

x=pd.DataFrame(a)
print(x)
sns.lineplot(x="over",y="score",data=x,hue="Team",style="Team",marker="o")
plt.show()'''


'''
x=sns.load_dataset("fmri")
y=x.head()
sns.lineplot(x="timepoint",y="signal",data=x,hue="event",style="event")
plt.show()
'''

#------------------------------------------------------------------------------------------------------------
#		Data 	26-09-2022
#------------------------------------------------------------------------------------------------------------
'''x=sns.load_dataset("fmri")
y=x.head()
sns.lineplot(x="timepoint",y="signal",data=x,hue="event",style="event",markers=True)
plt.show()'''
import pandas as pd
import seaborn as sns
'''x=pd.read_csv("pks.csv")
y=x.head()
print(y)'''

'''
pks=sb.load_dataset("fmri")

#y=pks.head()
print(pks)
sns.lineplot(x="timepoint",y="signal",data=pks,hue="event",style="event",markers=True)
plt.show()'''

'''
a=pd.read_csv("fmri.csv")
#print(a)
sns.set(style="whitegrid")
sns.barplot(x="timepoint",y="signal",data=a)
plt.show()'''

'''
x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/Excel/Pokemon(1).csv")
print(x)
sns.set(style="whitegrid")
sns.barplot(x="Legendary",y="Speed",data=x,hue="Generation",palette="vlag")
plt.show()


sns.barplot(x="Legendary",y="Speed",data=x,hue="Generation",color="orange")
plt.show()'''


'''
x=pd.read_csv("Iris.csv")
y=x.head()
sns.scatterplot(x="SepalLengthCm",y="PetalLengthCm",data=x,hue="Species",style="Species")
plt.show()'''


'''x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/Excel/Iris.csv")
print(x)
'''

#***********************************************************************************************************
#		Date 	26-09-2022
#*************************************************************************************************************

'''x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/dataset/diamonds.csv")
print(x)
y=x.head()
#sns.histplot(x["price"])
#sns.displot(x["price"])
sns.distplot(x["price"])
plt.show()'''

'''
x=pd.read_csv("diamonds.csv")
print(x)
y=x.head()
#sns.histplot(x["price"])		#histplot
#sns.displot(x["price"])		#displot
sns.distplot(x["price"],rug=True)		#distplot
plt.show()'''


import warnings
warnings.filterwarnings('ignore')

'''x=pd.read_csv("diamonds.csv")
sns.distplot(x["price"],kde=False,color="pink")
plt.ylabel()
plt.show()''' 
'''
x=pd.read_csv("diamonds.csv")
sns.distplot(x["price"],color="b",hist=False)
plt.show()'''

'''x=pd.read_csv("pks.csv")
print(x)
sns.boxplot(x="Churn",y="tenure",data=x)
plt.show()'''


#cheak the realation between Monthlycharges and internateservice

'''x=pd.read_csv("pks.csv")
sns.boxplot(x="InternetService",y="MonthlyCharges",data=x)
plt.show()'''

#How can we change the order of boxplot

'''x=pd.read_csv("pks.csv")
sns.boxplot(x="Contract",y="tenure",data=x,linewidth=2,order=["One year","Month-to-month","Two year"])
plt.show()'''

#
'''x=pd.read_csv("pks.csv")
sns.boxplot(x="Contract",y="tenure",data=x,hue="PaymentMethod")
plt.show()'''

'''x=sns.load_dataset("iris")
sns.pairplot(x,hue="species")
plt.show()'''

#******************************************************************************************************
#				Date 	28-09-2022
#******************************************************************************************************
#x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/Excel/Supermarket Sales.csv")
#print(x)
#x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/Dataset/iris.csv")
#y=x.iloc[0:,2]
#print(y)
#sns.boxplot(y)
#plt.show()

#sns.bioplot(x)
#plt.

#sns.histplot(x["SepalLengthCm"])
#plt.show()

#Create a data set of student name and show the subjects and students % of marks with the
#help of any plot, visualization looks, meaningful and understandable.


'''x=pd.read_excel("student.xlsx")
print(x)

sns.barplot(x="Name",y="marks",data=x)
plt.show()'''

#plt.pie(x,marks,labels=Name,autopct="%0.1f%%")
#plt.show()

#Choose any data set and show the visualization with the help of bar graph.
'''x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/Excel/Supermarket Sales.csv")
y=x.head(20)
print(y)
sns.barplot(x="City",y="gross income",data=y)
plt.show()'''


#Choose any data set and show the visualization with the help of scatter plot, and line plot.
'''x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/dataset/pokemon.csv")
y=x.head(20)
print(y)'''
#sns.set(style="whitegrid")
#sns.scatterplot(x="attack")


'''name=["prince","priya","pappu","vicky","mom"]
age=[24,25,28,18,45]
crack=[0.2,0,0,0.5,0.1]
plt.pie(age,labels=name,explode=crack,autopct="%0.2f%%")
plt.title("faimly_age_Diffrence")
plt.show()'''

'''x=pd.read_csv("titanic.csv")
print(x)'''

'''x=["prince",'ram',"mohan","nagin","ankit"]
u=[22,78,56,23,45]
z=[0,0.2,0,0,0]
plt.pie(u,labels=x,autopct="%0.2f%%",radius=1,explode=z)
plt.title("counter")
plt.pie([1],colors=["w"],radius=0.4)
plt.show()

plt.bar(x,u)
plt.xticks(rotation="vertical")
plt.show()'''