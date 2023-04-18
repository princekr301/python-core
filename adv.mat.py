

# Question 
# with the help of pandas filter few condition and find the data that we need


'''x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/titanic.csv")
y=x[(x["Sex"]=="male")&(x["Age"]<10)]
y=x[(x["Age"]<18) & (x["Fare"]<18)]
z=y[(y["Sex"]=="female") & (y["Embarked"]=="S")]
print(z)'''

#with the help of this method we can delete the column that we want.😉
#z.drop("Parch",axis=1)
#z.pop("Parch")

#It should be replace "pk" at the place of 1 and 0 by multipule replacement
#z.replace([1,0],"pk")

# If you want to add a new column according to index then use insert method❤
#z.insert(0,'Date',pd.Timestamp("25-08-2022"))
#z["Date"]=pd.date_range("20220825",periods=8)

#How can we add new rows in dataset
#z.loc[len(z.index)]=[225,10,5,"prince kumar","Male",23,1,1,2366564,100,"F4","S"]
#pk=pd.DataFrame({"PassengerId":[123],"Survived":[2],"Pclass":[10],"Name":["prince kumar sharma"],"Sex":["Male"],"Age":[24],"SibSp":[12],"Parch":[10],"Ticket":["GMTPK5261E"],"Fare":[123.45],"Cabin":["S6"],"Embarked":["PKL"]})
#z.append(pk)
#p=pd.concat((z,pk)) 
#print(p)



# Question
# with the help of pandas clean the data  of date and nan value of the palace of add something
'''
x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/titanic.csv")
#print(x)
x["Date"]=pd.to_datetime(x["Date"])
#print(x)
#y=x.loc[(x["Sex"]=="Male") & (x["Age"]>10)]
y=x.iloc[0:,4:]
#print(y)
z=y[(y["Age"]==18)&(y["Sex"]=="Male")]
#z=y.loc[(y["Age"]==18)&(y["Sex"]=="Male")]
print(z)'''

'''
import calendar
x=2022
y=9
z=calendar.month(x,y)
print(z)'''

#---------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#		Date 	03-10-2022 
#---------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------

'''
drop any four rows the data set
return 3 rows from the data bottom
return 6 rows from the head.
return any 15 rows from the mid
find the mean ,count,min,max,from this data set


Count the value of any two columns.
take some data as you want and make a bar graph on this data.
find the mean of specified column.

drop any two columns.
find the column of six row from mid.

show the number of rows and columns in dataset

gatting the frequency  of most of the match awwards.
Getting the top 10 '''

import matplotlib.pyplot as plt
import seaborn as sns

1.
'''
x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/titanic.csv")
#print(x)
y=x.drop("Name",axis=1)
print(y)

2.
a=x.iloc[0:3,0:]
print(a)

3.
print(x.head(6))

4.
print(x.iloc[50:70,0:])

5.
b=x["Age"]
print("Minimum age of this columns\n")
print(b.min())

print("maximum age of this collumns\n")
print(b.max())

print("count the number of person\n")
print(b.count())

print("Average of the students of  Age")
print(b.mean())'''

6.
'''x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/titanic.csv")
print("conting how many times 18 reapeted\n")
c=x.value_counts("Age")
print(c)

sns.displot(x["Age"],color="red")
plt.title("cheaking the age repeatation")
plt.show()'''


7.
'''x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/titanic.csv")
x=x.iloc[0:,2:]
y=x.iloc[200:225,0:]
print(y)'''

8.
'''x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/titanic.csv")
print(x.shape)'''


9.
#Getting the frequency of most of the match rewards
#x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/dataset/matches.csv")
#print(x)
#y=x.value_counts("player_of_match")
#print(y.head(30))


#-----------------------------------------------------------------------
'''																	#---
a=x.loc[0:,"player_of_match"]										#---
b={}																#---
#print(a)															#---
for i in a:															#---
	if i not in b:													#---
		b[i]=1														#---	
	else:															#---
		b[i]+=1														#---
																	#---
m=sorted(b.items(),key=lambda x:x[1],reverse=True)					#---
n=dict(m)															#---
for i in n:															#---
	if n[i]==20:													#---
		print(i)'''													#---
#-----------------------------------------------------------------------

10.
#top 10 player of the match
'''x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/dataset/matches.csv")
y=x.value_counts("player_of_match")

print("Top 10 player of the match")
print(y.head(10))'''

import matplotlib.pyplot as plt
import seaborn as sns
11.
#Finding out the number of toss wins wrt each team.
'''
x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/dataset/matches.csv")
y=x.value_counts("toss_winner")
print(y)'''


12.
#top five player of the match awards.

'''x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/dataset/matches.csv")
y=x.value_counts("player_of_match").head()
z=dict(y)
a=z.keys()
b=z.values()
c=[0.2,0,0,0,0]

plt.subplot(1,2,1)
plt.bar(a,b,color="orange")
plt.title("Top Five Player performance",color="blue",fontweight="bold")
plt.xlabel("Team Name")
plt.ylabel("Man of the match")
#plt.xticks(rotation="vertical")
#plt.grid()
plt.subplot(1,2,2)
plt.pie(b,labels=a,autopct="%0.2f%%",explode=c)
plt.title("Top Man of the match Awards",color="blue",fontweight="bold")
plt.show()'''



13.
'''import numpy as np
i=np.arange(0.0,2.0,0.01)
j=1+np.sin(2*np.pi*i)'''

'''
x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/dataset/matches.csv")
y=x[x["toss_decision"]=="field"]
z=y.value_counts("winner").head()
a=dict(z)
m=a.keys()
n=a.values()
o=[0.2,0,0,0,0]

a,((b,c),(d,e))=plt.subplots(2,2)
b.pie(n,labels=m,autopct="%0.2f%%",explode=o,radius=1)
#plt.title("Top 5 Winner After Batting")
b.pie([1],colors=["w"],radius=0.4)
c.plot(i,j,linestyle=":",linewidth=5,marker="o")
#plt.xticks(rotation="vertical")
d.bar(m,n,color="orange")
d.set_xlabel("X-axis")
d.set_ylabel("Y-axis")
d.tick_params(axis="y")
e.pie(n,labels=m)
plt.suptitle("Top five winner after batting",fontweight="bold")
plt.show()'''



14.
#Looking at the number of matches played each season.
'''
x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/dataset/matches.csv")
y=x.value_counts("Season")
print(y)
sns.histplot(x["Season"])
plt.show()'''

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
'''x=[10,11,12,13,14,15]
x.sort(reverse=True)
print(x)'''


#extract the string that repeated four times
'''x=["a","b","c","a","a","n","a","m","q","b","b","b"]
y={}
for i in x:
	if i not in y:
		y[i]=1
	else:
		y[i]+=1
for i in y:
	if y[i]==4:
		print(i)'''
 
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/exams.csv")
y=x[(x["gender"]=="female") &(x["parental level of education"]=="high school")]
z=y.nlargest(10,["math score"]).head(10)
z
#m,((a),(b))=plt.subplots(1,2)
#a.lineplot(x="Name",y="math score",data=z)
#b.barplot(x="Name",y="math score",data=z)
#plt.show()
plt.subplot(2,2,1)
sns.lineplot(x="Name",y="math score",data=z)
plt.title("Top 5 Student",fontweight="bold")
plt.xticks(rotation="vertical")
plt.subplot(2,2,2)
sns.barplot(x="Name",y="math score",data=z)
plt.title("Top 5 Student",fontweight="bold")
plt.xticks(rotation="vertical")
plt.show()'''


import numpy as np
import matplotlib.pyplot as plt
'''
i=np.arange(0.0,2.0,0.01)
j=1+np.sin(2*np.pi*i)

x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/dataset/matches.csv")
y=x[x["toss_decision"]=="field"]
z=y.value_counts("winner").head()
a=dict(z)
m=a.keys()
n=a.values()
o=[0.2,0,0,0,0]

a,((b,c),(d,e))=plt.subplots(2,2)
b.pie(n,labels=m,autopct="%0.2f%%",explode=o,radius=1)
#plt.title("Top 5 Winner After Batting")
b.pie([1],colors=["w"],radius=0.4)
c.plot(i,j,linestyle=":",linewidth=5,marker="o")
#plt.xticks(rotation="vertical")
d.bar(m,n)
d.set_xlabel("X-axis")
d.set_ylabel("Y-axis")
#d.xticks(rotation="vertical")
e.pie(n,labels=m)
plt.suptitle("Top five winner after batting",fontweight="bold")
plt.show()'''


'''x=np.arange(1,10)
y=x*2
z=x*3
w=x*4

n=np.arange(0.0,2.0,0.01)
m=1+np.sin(2*np.pi*n)

a,((b,c),(d,e),(f,g))=plt.subplots(3,2)
b.plot(x,y)
plt.title("hello")
c.plot(x,z)
plt.title("zero")
d.plot(w,x)
plt.title("byyy")
e.plot(y,w)
plt.title("game")
f.plot(z,w)
plt.title("asfds")
g.plot(n,m)
plt.title("best")
#plt.subtitle("hiii")
plt.show()'''


'''plt.plot(n,m,color="red")
plt.title("prince")
plt.show()'''

'''x=["Prince","Kumod","Rahul","Ankit","??"]
y=[90,85,75,65,25]
z=[45,78,89,56,23]
k=[0.2,0,0,0,0]
n=np.arange(0.0,2.0,0.01)
m=1+np.sin(2*np.pi*n)


a,((b,c),(d,e),(f,g))=plt.subplots(3,2)
b.pie(y,labels=x,autopct="%0.1f%%",radius=1)
b.pie([1],colors=["w"],radius=0.4)
#b.title("First Pie")
c.plot(n,m)
#c.title("Bar chart")
d.bar(x,y)
e.pie(y,labels=x,autopct="%0.1f%%",explode=k)
f.bar(y,z)
g.pie(y,labels=x)
plt.suptitle("Five students of performance!",fontweight="bold")
plt.show()'''


'''x=np.arange(1,10)
y=x*2
z=x*3
w=x*4

n=np.arange(0.0,2.0,0.01)
m=1+np.sin(2*np.pi*n)

plt.subplot(2,3,2)
plt.plot(n,m)

plt.subplot(2,3,3)
plt.plot(x,y,marker="o",linestyle="-")

plt.subplot(2,3,4)
plt.plot(y,z)

plt.subplot(2,3,5)
plt.plot(x,y)

plt.subplot(2,3,6)
plt.bar(x,y)
 
plt.subplot(2,3,1)
plt.bar(x,w)
plt.show()'''

import pandas as pd
import matplotlib.pyplot as plt

'''x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/exams.csv")
y=x.groupby("parental level of education")
print(y.count())

sk=x.value_counts("parental level of education")
school=dict(sk)
name=school.keys()
number=school.values()
ex=[0,0,0,0,0,0.1]
 

a,((b,c),(d,e))=plt.subplots(2,2)
b.pie(number,labels=name,autopct="%0.2f%%",explode=ex)
b.set_title("Number of schools!",color="orange",fontweight="bold")

c.bar(name,number)
c.set_title("Bar Graph",color="orange",fontweight="bold")
c.set_xlabel("Name of Schools",color="orange",fontweight="bold")
c.set_ylabel("Number of school")

d.scatter(name,number,marker="o")
d.set_title("scatter Graph",color="orange",fontweight="bold")
d.set_xlabel("Name of Schools",color="orange",fontweight="bold")
d.set_ylabel("Number of school",color="orange",fontweight="bold")

e.plot(name,number,linestyle="-",linewidth=8,marker="*",color="green")
e.set_title("plot Graph")
e.set_xlabel("Name of Schools")
e.set_ylabel("Number of school")

plt.suptitle("Schools of Visualization by prince!",fontweight="bold",color="red")
plt.show()'''


x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/exams.csv")
#y=x.groupby("race/ethnicity")
#print(y.count())
y=x.value_counts("race/ethnicity")



