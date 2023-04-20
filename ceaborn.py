
#/---------------------------------------------------------------------------------------------------------------------------------
#				/----------------	21-09-2022	--------------	SeaBorn  --------------/
#/---------------------------------------------------------------------------------------------------------------------------------
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd

#How to start SeaBorn

#pip install SeaBorn



'''x=sns.load_dataset("fmri")
#print(x)
y=x.head()
print(y)
sns.lineplot(x="timepoint",y="signal",data=x,hue="event")
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

'''x=sns.load_dataset("fmri")
y=x.head()
sns.lineplot(x="timepoint",y="signal",data=x,hue="event",style="event",markers=True)
plt.show()'''


import seaborn as sns

'''x=sns.load_dataset("fmri")
print(x)
sns.lineplot(x="timepoint",y="signal",data=x,hue="event",markers=True)
plt.show()'''


import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


'''x=pd.read_csv("pks.csv")
y=x.head(10)
#print(x)
sns.set(style="whitegrid")
sns.barplot(y="MonthlyCharges",x="TotalCharges",data=y,hue="gender")
plt.title("prince kumar")
plt.show()'''


'''x=pd.read_csv("diamonds.csv")
print(x)
y=x.head(10)
sns.set(style="whitegrid")
sns.barplot(x="table",y="price",data=y,hue="color")
plt.show()'''

import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
'''
x=pd.read_csv("fmri.csv")
y=x.head(20)
print(y)
#sns.set(style="whitegrid")
#sns.plot(x="timepoint",y="signal",hue="event",data=y)
#plt.show()
sns.lineplot(x="timepoint",y="signal",hue="event",data=y)
plt.title("prince")
plt.show()
'''
import warnings
warnings.filterwarnings("ignore")

'''x=pd.read_csv("diamonds.csv")
y=x.head(20)
print(y)
sns.set(style="whitegrid")'''
#sns.barplot(x="price",y="depth",hue="cut",data=y,palette="vlag")
#sns.scatterplot(x="price",y="depth",data=y,hue="color",style="color")
#plt.show()
#sns.displot(y["price"],color="g")
#sns.histplot(y["price"],color="g")
#sns.distplot(x["depth"])
#sns.boxplot(x="price",y="depth",data=y)
#sns.pairplot(y,hue="cut")
#plt.show()

import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
'''
x=pd.DataFrame({"name":["prince","ankit","manu","vicky","priya sharma"],
	"marks":[354,259,300,259,254]})
print(x)
#y=x.iloc[0:,0]
y=x["name"]
z=x["marks"]
m=[0.3,0.3,0.3,0.3,0.3]
#z=x.iloc[0:,1]
plt.pie(z,labels=y,explode=m,autopct="%0.1f%%",radius=1)
#sns.barplot(x="name",y="marks",data=x)
plt.title("Performance of students")
#plt.xlabel("names",color="g")
#plt.ylabel("marks")
#plt.grid(True,color="r")
plt.pie([1],colors=["w"],radius=0.4)
plt.show()'''


#x=np.arange(0,10)
#y=x*2
'''
plt.scatter(x,y,marker=True)
plt.title("prince")
plt.grid()
plt.show()'''

#plt.plot(x,y,linestyle="-",marker=True,linewidth=0.5)
#plt.show()
'''
x=np.random.randint(1,10,40)
print(x)
plt.hist(x,color="pink")
plt.grid()
plt.show()'''


'''a=["ram","laxman","sita","ravan","hanuman","kausalya","bharat","bali","prince","chhotu"]
x=np.arange(0,10)
y=x*2
z=np.random.randint(12,20,40)

plt.subplot(1,4,1)
plt.plot(x,y,linestyle="-",linewidth=0.4,marker=True)
plt.title("first grap")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid()

plt.subplot(1,4,2)
plt.bar(a,y,color="red")
plt.title("second graph")
plt.xlabel("name of condidate")
plt.ylabel("number")

plt.subplot(1,4,3)
plt.scatter(x,y,marker="o")
plt.title("third graph")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid()

plt.subplot(1,4,4)
plt.hist(z)
plt.title("fouth graph")
plt.xlabel("Number")
plt.ylabel("repeated Number")
plt.show()'''


'''
x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/Dataset/pks.csv")
print(x.iloc[0:,0:6])
#sns.boxplot(x="Churn",y="tenure",data=x)
#plt.show()

sns.boxplot(x="Partner",y="tenure",data=x,hue="Dependents")
plt.show()'''

#x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/titanic.csv")
#print(x)
import calendar
'''x=2022
y=10
z=calendar.month(x,y)
print(z)'''

'''x=eval(input("enter num ,operator, second num :- "))
print(x)'''
import numpy as np

#w=np.random.randint(1,12,10)
x=np.arange(1,10)
y=x*2
z=x*3
w=x*4


'''n=np.arange(0.0,2.0,0.01)
m=1+np.sin(2*np.pi*n)'''

'''a,((b,c),(d,e),(f,g))=plt.subplots(3,2)
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

x=["Prince","Kumod","Rahul","Ankit","??"]
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
plt.show()