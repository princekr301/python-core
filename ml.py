 


 

'''
 What is machine learning?
 Machine learning is the science (and art) of programming computers so they can learn from data.

 machine learning is the field of study that gives computer the abillity to learn without being explicity programmed.

 A computer program is said to learn from experience E with respect to some task T and some perfornmacne measure  P, if its
 perfornmacne on T, as measured by P,improve with experience E.


 How its work ?
 Machine learning is the science of getting computers to learn and act like human do , and improve
 their learning over time in autonomus fashion, by feeding them data and information in the from of 
 observation and real-world intractions.


 What is the advantage of machine learning ?

 Resolvin complex problems : There are many complex problems, those problems can solve only machine learning 
 Autonoums for everything : Every thing being automatic like metro ,self driving car,chat bot.

 Trends and pattern identification :- for example there is company of amazon ,amazon collect data ,that amazon find the patterns 
 of a customers , that in manner he purchagse things , then he will provide you similar things as per your requirment.


 Wide range of applications : Face detection ,self driving car ,syberfraud detection, Even in face

----------------

 There are many diffrent types of machiine learnings 
 weather are not they are tained with human supervision (supervised ,unsupervised,semi supervised and Reinforcement Learning)



what is supervised Machine Learning ?
Supervise learning is the type of machine learning in which machine are trained using well "labbeled" training data, and on 
basic of data ,machine predict the output.The labbeled data means some input data is already tagged with the correct output .


supervised learning is a process of providing input data as as correct  output  data to the machine learning  model. The aim of a 
supervised learning algorithm is to find a mapping function to map the input variable(x) with the output variable(y)


Whare we use supervised machine learning .
IN the real-world,supervise learning can be uses for risk Assesment,Image classification,Fraud Detection ,spam filtring, etc



HOw supervised learning  Works?
In supervised learning ,models are trained using labelled dataset, where the model learns about each type of data. Oncethe learning
process is tested in the basic of test data and then it predict the output. Suppoose we have a  dataset of different types of shapes
which includes square,rectangle ,tringle ,and polygon .
Now is the first step is that we need  to train the model for each for each shape.

IN given shape has four side s, and all side are equal it will be labbled as a square. If the given shape has three side then it
will be labbeled as triangle . IF the given shape has six sides then it will be labelled as  hexagon.

Now after training we test our model using the test set ,and when it find a new shape ---------------------


Data Acquisition :
Data from Multiple  Sources => You get data from multipule resources like excel  files ,pdf fromat,, csv files, videos ,image etc
,so you get data from different resources.


Data storage => After this you store  this data in a sample storage repository , and you said this storage.

Target data => Now you collect main data from this storage, and you called it target data.

Data Pre processing => NOw you start data pre  processing in this process you work on row data and with the help of data manipulatiion
Techniques Like data cleaning ,data mining you make a tiddy data or meaningful data and then you can applied data visulization on 
'''

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Date  15-11-2022
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
What is train_test_split() method ?
The train_test_split() memthod is used to split our data into training and testing sets. First , we need to 
divide our data into feautures (x) and labels(y). THe dataframe gets divided into x_train,x_test,y_train and y_test
x_train and y_train set are used for training and fitting the model

The train -test is used to estimate the performance of machine learning algorithm that are applicable for predicition-based
Algorithms/applications. This method is a fast easy procedure to perform such that we can compare our own machine learning
model reusults to machine results.
 '''

#--------------------------------------------------------------------------------------
# First of all install sklearn in sublime text 3
# Write in cmd =>	pip install -U scikit-learn
#--------------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
'''
x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/carprices")
#print(x)
#plt.scatter(x["Mileage"],x["Sell Price($)"])
#plt.show()

#plt.scatter(x["Mileage"],x["Age(yrs)"])
#plt.show()

a=x[["Mileage","Age(yrs)"]]	# This independate variable
b=x["Sell Price($)"]		# this in dependent variable

#print(a)
#print(b)
x_train, x_test, y_train, y_test = train_test_split(a, b, test_size=0.3)
#print(y_train)
#print(x_test)
#print(x_train)
#print(y_test)
#print(len(x_train)),print(len(y_train))'''


#------------------------------
# pip install U-scikit-learn  
#------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
'''
x1={"Name":["prince","Kumod","Ankit","raman","anmol","rahul","Manu"],
"Age":[23,22,27,25,24,26,28],
"City":["Begusarai","samastipur","Patna","begusarai","Kanpur","Dwarika","Himachal"],
"Roll_No":[1,2,3,4,5,6,7]}

x=pd.DataFrame(x1)
#print(x)
#print("\n train_test_split")
plt.scatter(x["Name"],x["Age"],marker="*",color="black")
plt.title("Visulizing the data",fontweight="bold")
plt.grid()
#plt.show()

fe=x[["Age","City","Roll_No"]] # feature is a independent variable
le=x["Name"]  # labels is a dependent variable
#print(fe)
#print(le)
#x_train,x_test,y_train,y_test=train_test_split(fe,le,test_size=0.2)
x_train,x_test,y_train,y_test=tts(fe,le,test_size=0.2)
#print(x_train),print(x_test)
#print(y_test),print(y_train)'''

#-------------------------------------------------------------------------------------------------------
# 	Date  18-11-2022
#-------------------------------------------------------------------------------------------------------
import numpy as np
'''
x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/decis_tree.csv")
#print(x)

fe = x.drop("Salary_more_than_100k",axis=1)
#print(fe)
le = x["Salary_more_than_100k"]
#print(le)

#Now converting the categorical data to numerical data
from sklearn.preprocessing import LabelEncoder
le_Company=LabelEncoder()
le_job=LabelEncoder()
le_degree=LabelEncoder()

#This transform method will change this categorical data into numerical data.
#And few column will create

x["Company_n"]=le_Company.fit_transform(x["Company"])
x["Job_n"]=le_job.fit_transform(x["Job"])
x["Degree_n"]=le_degree.fit_transform(x["Degree"])

#print(x)

y=x.drop(["Company","Job","Degree"],axis=1) # inplace=True => its change in original variable
#print(y)
fe1=y[["Company_n","Job_n","Degree_n"]]
le1=y["Salary_more_than_100k"]

from sklearn.model_selection import train_test_split as tts
x_train,x_test,y_train,y_test=tts(fe1,le1,test_size=0.2)

#print(x_train),print(x_test)
#print(y_train),print(y_test)'''

#----------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------
'''
x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/breast-cancer-wisconsin.data.csv")
#print(x)
x.replace('?',-9999,inplace=True)
x.dropna(inplace=True)
#print(x)
x.drop('id',axis=1,inplace=True)
#print(x)
fe=x.drop("class",axis=1)
le=x["class"]
#print(fe)
#print(le)

x_train,x_test,y_train,y_test=tts(fe,le,test_size=0.2)
#print(x_train),print(x_test),print(len(x_train)),print(len(x_test))
#print(y_train),print(y_test),print(len(y_train)),print(len(y_test))

#x1=np.array(x.drop(["class"],1)) # 1 is the axis=1 so don't confuse
#print(x1)


from sklearn.model_selection import train_test_split as tts
x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/decis_tree.csv")
#print(x)
x1=[] 
x2=[]
x3=[]
for i in x["Company"]:
	if i=="Google":
		v=0
	elif i=="Amazone":
		v=1
	elif i=="Facebook":
		v=2
	x1.append(v)
for i in x["Job"]:
	if i=="Sales Executive":
		v1=0
	elif i=="Business Manager":
		v1=1
	elif i=="Computer Programmer":
		v1=2
	x2.append(v1)
for i in x["Degree"]:
	if i=="Bachelors":
		v2=0
	elif i=="Masters":
		v2=1
	x3.append(v2)

x["Company_n"]=x1
x["Job_n"]=x2
x["Degree_n"]=x3
#print(x)
fe=x.iloc[0:,4:]
#print(fe)
le=x.iloc[0:,3]
#print(le)

x_train,x_test,y_train,y_test=tts(fe,le,test_size=0.2)
#print(x_train),print("Length :-",len(x_train))
#print(x_test),print("Length :-",len(x_test))
#print(y_train),print("Length :-",len(y_train))
#print(y_test),print("Length :-",len(y_test))




from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/decis_tree.csv")
y=x.iloc[0:,0:3]

Company_n=LabelEncoder()
Job_n=LabelEncoder()
Degree_n=LabelEncoder()

x["Comapny_num"]=Company_n.fit_transform(x["Company"])
x["Job_num"]=Job_n.fit_transform(x["Job"])
x["Degree_num"]=Degree_n.fit_transform(x["Degree"])
fe=x.iloc[0:,4:]
le=x.iloc[0:,3]
x_train,x_test,y_train,y_test=train_test_split(fe,le)
#print(x_train),print("Length :-",len(x_train)),print("\n"),print(x_test),print("Length :-",len(x_test))
#print("\n")
#print(y_train),print("Length :-",len(y_train)),print("\n"),print(y_test),print("Length :-",len(y_test))

from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import LabelEncoder as le
x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/breast-cancer-wisconsin.data.csv")
#print(x)
x.dropna(inplace=True)
#print(x)
x.replace("?",0.001,inplace=True)
#print(x)
fe=x.iloc[0:,1:9]
le=x.iloc[0:,10]
x_train,x_test,y_train,y_test=tts(fe,le,test_size=0.2)
#print(x_train),print("Length :-",len(x_train)),print("\n"),print(x_test),print("Length :-",len(x_test))
#print("\n")
#print(y_train),print("Length :-",len(y_train)),print("\n"),print(y_test),print("Length :-",len(y_test))

'''
#--------------------------------------------------------------------------------------------------------------------------------------------------
#	Date   21-11-2021
#--------------------------------------------------------------------------------------------------------------------------------------------------

'''
What is k nearest Neighbouur ?
K-Nearesst Neighbouur is one of the simplest machine learning Algorithms based on supervised learning technique.

K-NN Algorithms assumes the similarity between the new case /data and aviable cases and put
the new case into the category that is most similar to the aviable categories

K-NN store all aviable data and classified a new data point based on the similarity. this means when new data appear it can be easily 
classified into a well suite categories by using K-NN Algorithms.

K-NN Algorithms can be used for Regression as well as for classification but mostly it is used for the classification data.
--------------
It is also called lazy leaner Algorithm beacause it does not learn from the training set immediatly insted it stores the datas set.
----------------


What does random state mean ?
Random state is used to set the seed for the random generator so that we can ensure that
the result that we get can be reproduced .Because of the nature of spliting the data in the
train and test is randomised you would get diffreent data assigned to the train and 
test data unless you can control for the random factor.
'''

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split as tts
'''x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/Dataset/Iris.csv")
#print(x)
le_sp=LabelEncoder()
x["Species_n"]=le_sp.fit_transform(x["Species"])
#print(x)
fe=x.iloc[0:,0:5]
#print(fe)
le=x["Species_n"]
#print(le)

x_train,x_test,y_train,y_test=tts(fe,le,test_size=0.2,random_state=42)
#print(x_train),print("Length :-",len(x_train)),print("\n"),print(x_test),print("Length :-",len(x_test))
#print( "\n")
#print(y_train),print("Length :-",len(y_train)),print("\n"),print(y_test),print("Length :-",len(y_test))

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=7)
a=knn.fit(x_train,y_train)
#print(a)'''

#print(a.predict(x_test))
#print(a.score(x_test,y_test)) # caluculate the accuracy of the model

'''
import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import LabelEncoder as le
from sklearn.neighbors import KNeighborsClassifier as kns

x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/Dataset/Iris.csv")
#print(x)
a=le()
x["Species_n"]=a.fit_transform(x["Species"])
#print(x)

x_train,x_test,y_train,y_test=tts(x.iloc[0:,0:5],x.iloc[0:,6],test_size=0.2,random_state=42)
#print(y_train)
from sklearn.neighbors import KNeighborsClassifier as kne
p=kne(n_neighbors=7)
r=p.fit(x_train,y_train)
#print(r)
s=r.score(X_test,y_test)
print(s)'''
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
#x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/Dataset/Iris.csv")
#print(x)


#-----------------------------------------------------------------------------------------------------------------
# 	Date : 22-11-2022
#-------------------------------------------------------------------------------------------------------
#x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/breast-cancer-wisconsin.data.csv")
#x.dropna(inplace=True)
#x.replace("?",999,inplace=True)
#print(x)
#fe=x.iloc[0:,0:10]
#fe=np.array(x.drop("Class"),1)
#print(fe)
#le=x["class"]
#le=x.iloc[0:,10]
#print(len(y_test))

#x_train,x_test,y_train,y_test=train_test_split(fe,le,test_size=0.2)
#print(y_train)
#print(y_test)
#print(len(y_test))
#knn=KNeighborsClassifier()
#a=knn.fit(x_train,y_train)
#print(a)
#b=knn.predict(x_test)
#print(b)
#c=knn.score(x_test,y_test)
#print(c)


from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
a={"Age":[36,42,23,52,43,44,66,35,52,35,24,18,45],
"Experience":[10,12,4,4,21,14,3,14,13,5,3,3,9],
"Rank":[9,4,6,4,8,5,7,9,7,9,5,7,9],
"Nationality":['UK','USA','N','USA','USA','UK','N','UK','N','N','USA','UK','UK'],
"Go":['NO','NO','NO','NO','YES','NO','YES','YES','YES','YES','NO','YES','YES']}

x=pd.DataFrame(a)
#print(x)
p={"UK":1,"USA":2,"N":3}
x["Nationality"]=x["Nationality"].map(p)
r={"YES":1,"NO":0}
x["Go"]=x["Go"].map(r)
#print(x)

fe=x.drop("Go",axis=1)
#print(fe)
le=x["Go"]
#print(le)
x_train,x_test,y_train,y_test=tts(fe,le,test_size=0.3)
#print(y_train)
kn=KNeighborsClassifier(n_neighbors=5)
i=kn.fit(x_train,y_train)
n=kn.predict(x_test)
#print(n)
c=kn.score(x_test,y_test)
#print(c)


#-------------w3school-------------------------------
'''import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

data = list(zip(x, y))
knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(data, classes)

new_x = 8
new_y = 21
new_point = [(new_x, new_y)]

prediction = knn.predict(new_point)
#print(prediction)
plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction[0]])
plt.text(x=new_x-1.7, y=new_y-0.7, s=f"new point, class: {prediction[0]}")
#plt.show()
'''

#-----------------------------------------------------------------------------------------------------------
#  Date 23-11-2022
#-----------------------------------------------------------------------------------------------------------------------
'''What is confusion metrix ?
   Confusion matrix represent counts from predicted and actual values. THe "TN" stand for 
   True Negative which shows the number of negative examples classfied accurately
   similarly, "TP" stand for True Positive which means indicate the number f Positive
   example classfied.
   
   True Positive :-THe model has predicted yes , and the actual is value was also True.(TP)
   True Negative :-The model has predicted No ,and the actual value was No.(TF)
   False Positive :-The model has predicted YEs ,and the actual value was No it is called false positive.
   False Negative :-THe model has predicted No , and tha actual value is yes.It is aslo calles False negative.
'''
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.metrics import confusion_matrix
#x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/breast-cancer-wisconsin.data.csv")
#x.dropna(inplace=True)
#x.replace("?",999,inplace=True)
#print(x)
#fe=x.iloc[0:,0:10]
#fe=np.array(x.drop("Class"),1)
#print(fe)
#le=x["class"]
#le=x.iloc[0:,10]
#print(len(y_test))

#x_train,x_test,y_train,y_test=train_test_split(fe,le,test_size=0.2)
#print(y_train)
#print(y_test)
#print(len(y_test))
#knn=KNeighborsClassifier()
#a=knn.fit(x_train,y_train)
#print(a)
#b=knn.predict(x_test)
#print(b)
#c=knn.score(x_test,y_test)
#print(c)

#cm=confusion_matrix(y_test,b)
#print(cm)

'''import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(6,4))
sns.heatmap(cm,annot=True)
plt.xlabel("Predicted")
plt.ylabel("truth")
#plt.show()'''






#x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/Dataset/Iris.csv")
#print(x)
#le_sp=LabelEncoder()
#x["Species_n"]=le_sp.fit_transform(x["Species"])
#print(x)
#fe=x.iloc[0:,0:5]
#print(fe)
#le=x["Species_n"]
#print(le)

#x_train,x_test,y_train,y_test=tts(fe,le,test_size=0.2,random_state=42)
#print(x_train),print("Length :-",len(x_train)),print("\n"),print(x_test),print("Length :-",len(x_test))
#print("\n")
#print(y_train),print("Length :-",len(y_train)),print("\n"),print(y_test),print("Length :-",len(y_test))

from sklearn.neighbors import KNeighborsClassifier
#knn=KNeighborsClassifier(n_neighbors=7)
#a=knn.fit(x_train,y_train)
#print(a)

#pred=a.predict(x_test)
#print(pred)
#print(a.predict(x_test))
#print(a.score(x_test,y_test)) # caluculate the accuracy of the model
from sklearn.metrics import confusion_matrix
#cm=confusion_matrix(y_test,pred)
#print(cm)
'''plt.figure(figsize=(8,6))
sns.heatmap(cm,annot=True)
plt.xlabel("Truth")
plt.ylabel("Predict")
plt.show()'''

from sklearn.metrics import classification_report
#cr=classification_report(y_test,pred)
#print(cr)
'''plt.figure(figsize=(8,6))
sns.heatmap(cm,annot=True)
plt.xlabel("Truth")
plt.ylabel("Predict")
plt.show()'''

from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns
'''x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/Dataset/Iris.csv")
#print(x.loc[48:80,"Species"])
p={"Iris-setosa":0,"Iris-versicolor":1,"Iris-virginica":2}
x["Species"]=x["Species"].map(p)
#print(x)
fe=x.drop("Species",axis=1)
#print(fe)
le=x["Species"]
#print(le)

x_train,x_test,y_train,y_test=tts(fe,le,test_size=0.2)

kn=KNeighborsClassifier(n_neighbors=5)
fit=kn.fit(x_train,y_train)
#print(fit)
pred=kn.predict(x_test)#.reshape(5,6)
#print(pred)
#print(pred.shape)
accuracy=kn.score(x_test,y_test)
#print(accuracy)
cm=confusion_matrix(y_test,pred)'''
#print(cm)
#plt.figure(figsize=(8,6))
#sns.heatmap(cm,annot=True)
#plt.show()



#----------------------------------------------------------------------------------------------------------------
# Date 24-11-2022
#-----------------------------------------------------------------------------------------------------------------------


'''
What is classification report ?
A classification report is a performance evaluation metric in machine learning .
It is used to show the precision ,recell,F1 Score and support of your traind classification model.

a classification report is used to measure the quaility  of predictions from a classification
Algorithm. How many predictions are True and how are False.
More specically True Positives , False Positive , True Negative and False Negatives
are used to predict the matrix of a classification report
'''
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
#from metrics import classification_report
'''x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/titanic1.csv")
#print(x)
x.dropna(inplace=True)
#print(x)
a={"male":0,"female":1}
x["sex"]=x["sex"].map(a)
#print(x)
fe=x[["pclass","sex","fare"]]
#print(fe)
le=x["survived"]
#print(le)
x_train,x_test,y_train,y_test=train_test_split(fe,le,test_size=0.2)
#print(x_train.shape)
#print(y_train.shape)
#print(x_test.shape)
from sklearn.metrics import classification_report
knn=KNeighborsClassifier(n_neighbors=5)
fit=knn.fit(x_train,y_train)
pred=knn.predict(x_test)
#print(pred.shape)
y=[]
for i in pred:
	if i==0:
		o="Male"
	else:
		o="female"
	y.append(o)
#print(y)

#print(pred)
sc=knn.score(x_test,y_test)
#print(sc)
cm=confusion_matrix(y_test,pred)
#print(cm)
#plt.figure(figsize=(8,6))
#sns.heatmap(cm,annot=True)
#plt.show()
cr=classification_report(y_test,pred)
#print(cr)
'''


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns
'''x=pd.read_csv("breast-cancer-wisconsin.data.csv")
#print(x)
x.dropna(inplace=True)
x.replace("?",999,inplace=True)
le=x["mitoses"]
fe=x.drop("mitoses",axis=1)
#print(fe)
x_train,x_test,y_train,y_test=tts(fe,le,test_size=0.2)
#print(x_train.shape)
#print(y_train)
#print(y_train.shape)
knn=KNeighborsClassifier(n_neighbors=5)
fit=knn.fit(x_train,y_train)
pred=knn.predict(x_test)
xx=pd.value_counts(pred)
#print(xx)
#print(pred)
ac=knn.score(x_test,y_test)
#print(ac)
cm=confusion_matrix(y_test,pred)'''

#print(cm)
#plt.figure(figsize=(10,10))
#sns.heatmap(cm,annot=True)
#plt.show()
#cr=classification_report(y_test,pred)
#print(cr)


#-------------------------------------------------------------------------------------------
#  Date  -28-11-2022
#-------------------------------------------------------------------------------------------
# SimpleImputer in Machine learning
'''
from sklearn.impute import SimpleImputer
x = pd.read_csv('C:/Users/Prince kumar/OneDrive/Desktop/titanic1.csv')
#print(x)
a=x.isnull().sum().sum()
#print(a)
#a = x.loc[0:,('Pclass','Sex','Age','Fare')]
#print(a)
a = x.loc[0:,['pclass','sex','age','fare']]
#print(a)
s = LabelEncoder()
#print(s)

a['s1'] = s.fit_transform(a['sex'])
#print(a)
#a = x.loc[0:,['pclass','s1','age','fare']]
#print(a)

r = a.drop(['sex'], axis=1)
#print(r)

imr = SimpleImputer(missing_values = np.nan, strategy = 'mean')
#print(imr)
imr = imr.fit(r)
i_d = imr.transform(r)'''
#print(i_d)


#z = a.fillna(-000, inpla


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.impute import SimpleImputer

'''
x = pd.read_csv('C:/Users/Prince kumar/OneDrive/Desktop/titanic1.csv')
y=x.loc[0:,["pclass","sex","age","fare"]]
le=x["survived"]
z=LabelEncoder()
y["sex"]=z.fit_transform(y["sex"])
imp=SimpleImputer(missing_values=np.nan,strategy='mean')
imr=imp.fit(y)
id=imr.transform(y)
#print(id)
#print(id.shape)

id_train,id_test,y_train,y_test=tts(id,le,test_size=0.2,random_state=4)
#print(id_train)
#print(id_train.shape)
#print(id_test.shape)
#print(y_train)
knn=KNeighborsClassifier(n_neighbors=5)
fit=knn.fit(id_train,y_train)
pred=knn.predict(id_test)
#print(pred)
ac=knn.score(id_test,y_test)
#print(ac)
cm=confusion_matrix(y_test,pred)
#print(cm)
plt.figure(figsize=(8,6))
sns.heatmap(cm,annot=True)
plt.xlabel("Prediction")
plt.ylabel("Actual")
plt.title("confusion_matrix",fontweight="bold")
plt.show()
cr=classification_report(y_test,pred)
print(cr)'''


#-------------------------------------------------------------------------------------------
# Date -> 01/12/2022
#------------------------------------------------------------------------------------------
'''
What is the support vector machine ?
A support vector machine (SVM) is a type of deep learning algorithm that 
performs supervised learning for classification or Regression of data groups.

There are two types of support vector machine 

1. Linear SVM
2. Non-linear SVM


What is kernel in svm?
Kernel :-> the function used to map a lower dimensional data into a higher dimensional data.
Hyper Plane :-> In SVM this is basically the separation line between the data classes.
Althous in SVR we are going to define it as the line that will help us predict the continuous
value or target value.

what is kernel in support vector machine ?
Kernel Function is a method used to take data as input and tansform it into the required
processing data. "Kernel" is used due to a set of mathmatical function used in Support vector
machine.

providing the window to manipulate the data. So, Kernel Function generally transforms the set.
of data so that a non-linear decision surface is able to transform to a linear equation in higher 
number of dimention spaces. Basically, it returns the linear product between two points in 
feature dimention.

What is Gamma in support vector machine ?
Gamma is a hyperparameter used with  non -linear SVM.One of the most commanly used  Non-linear
kernels is the radial basis function (RBF).Gamma perameter of RBF  controls the distance of
the influence of a single training point.

What is Regularization ?
--------------------

Kernel :-> A kernel is the core components of an operating system. it is also a system program .
It is a part of operating system which converts user commands into machine language.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


'''
x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/Social_Network_Ads.csv")
#print(x)
fe=x.iloc[0:,[2,3]].values
#print(fe)
le=x["Purchased"].values
#print(le)
x_train,x_test,y_train,y_test=train_test_split(fe,le,test_size=0.2,random_state=0)
#print(x_train.shape)
#print(x_test.shape)

# now going to use the standardscaler

sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)
#print(xtest)

#NOw the preprocessing of the data is over .its time to build the model .
# we apply three kernel tricks in this case and try evaluting them
# First model is kernel = "linear"
#---------------------------------------
cl=SVC(kernel='linear',random_state=0)
fits=cl.fit(x_train,y_train)
#print(fit_cl)

pred1=fits.predict(x_test)
#print(pred1)
sc=cl.score(x_test,y_test)
print("Kernel is linear Then accuracy is :-",sc)
cm=confusion_matrix(y_test,pred1)
print(cm)
plt.figure(figsize=(10,8))
sns.heatmap(cm,annot=True)
plt.show()
cr1=classification_report(y_test,pred1)
print(cr1)

#----------------------------------
# Second model is kernel="poly"
cp=SVC(kernel='poly',random_state=0)
fits2=cp.fit(x_train,y_train)
pred2=cp.predict(x_test)
#print(pred2)
sc2=cp.score(x_test,y_test)
cm2=confusion_matrix(y_test,pred2)
print(f"Kernel is poly Then accuracy is :- {sc2}")
print(cm2)
plt.figure(figsize=(10,8))
sns.heatmap(cm2,annot=True)
plt.show()
cr2=classification_report(y_test,pred2)
print(cr2)

#--------------------------------------------------
# Third model when kernel is rbf
crb=SVC(kernel="rbf",random_state=0)
fit3=crb.fit(x_train,y_train)
pred3=crb.predict(x_test)
#print(pred3)
ss=crb.score(x_test,y_test)
cm3=confusion_matrix(y_test,pred3)
print("Kernel is rbf Then accuracy is :-",ss)
print(cm3)
plt.figure(figsize=(10,8))
sns.heatmap(cm3,annot=True)
plt.show()
cr3=classification_report(y_test,pred3)
print(cr3)
'''



#---------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.svm import SVC

#----------------------------------------------------------------------------------
'''
x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/Social_Network_Ads.csv")
#print(x)
fe=x[['Age','EstimatedSalary']].values
le=x['Purchased'].values
#print(le)

x_train,x_test,y_train,y_test=train_test_split(fe,le,test_size=0.2,random_state=0)
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)


cl=SVC(kernel='linear',random_state=0)
fit1=cl.fit(x_train,y_train)
pred1=cl.predict(x_test)
#print(pred1)
ac1=cl.score(x_test,y_test)
print("Accuracy of linear kernel :->",ac1)

cm1=confusion_matrix(y_test,pred1)
print(cm1)
cr1=classification_report(y_test,pred1)
print(cr1,"\n")


cl2=SVC(kernel='poly',random_state=0)
fit2=cl2.fit(x_train,y_train)
pred2=cl2.predict(x_test)
#print(pred2)
ac2=cl2.score(x_test,y_test)
print("\nAccuracy of ploy kernel :->",ac2)

cm2=confusion_matrix(y_test,pred2)
#print(cm2)
cr2=classification_report(y_test,pred2)
print(cr2,"\n")

cl3=SVC(kernel='rbf',random_state=42)
fit3=cl3.fit(x_train,y_train)
pred3=cl3.predict(x_test)
ac3=cl3.score(x_test,y_test)
print("Accuracy of rbf kernel :->",ac3)

cm3=confusion_matrix(y_test,pred3)
#print(cm3)

cr3=classification_report(y_test,pred3)
print(cr3)'''


#--------------------------------------------------------------------------------------
# Date 06-12-2022
#---------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
#------------------------------------------------------------------------------------------------------------------------------------------
# Date - 07-12-2022
#------------------------------------------------------------------------------------------------------------------------------------------
'''
What is Decision Tree ?

Decision tree is supervised machine learning Algorithms based on supervised learning ,that can be used for both
regression and classification problems. The goal is to build up a classifier model that can predict the class value 
of the target variable.

Why we use Decision tree 
It is enable to analyze the possible values of outcomes and the probability of 
accomlishing them


What is entrophy ?
Entrophy is an information theory metric that measures the impurity or uncertenly in a groups
of observations. It determines how a decision tree chooses the split data.

Information Gain
High information gain is a technique to divide the features .it is very important to take decision
which one features you take for training data set.This high information gain 
feature will help you to decide that which one feature you want.

What are the node ?
The main node is referred to as the parent node,
------------------------------------------ 
'''

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
'''x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/decis_tree.csv")
#print(x)
le_com=LabelEncoder()
le_job=LabelEncoder()
le_deg=LabelEncoder()
x['Company']=le_com.fit_transform(x['Company'])
x['Job']=le_job.fit_transform(x['Job'])
x['Degree']=le_deg.fit_transform(x['Degree'])
#print(x)
fe=x.drop("Salary_more_than_100k",axis=1)#.values
#print(fe)
le=x["Salary_more_than_100k"]#.values
#print(le)

x_train,x_test,y_train,y_test=train_test_split(fe,le,test_size=0.2)
#print(x_test.shape)
#print(y_test.shape)


mo=DecisionTreeClassifier()#criterion='entropy',random_state=100,max_depth=3,min_samples_leaf=4)
#print(model)
fits=mo.fit(x_train,y_train)
pred=mo.predict(x_test)
print(pred)
ac=mo.score(x_test,y_test)
print(ac)
tree.plot_tree(fits,feature_names=['Company','Job','Degree'])
plt.show()'''



'''
x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/creditcard.csv")
#print(x)

x = pd.read_csv('C:/Users/Prince kumar/OneDrive/Desktop/titanic1.csv')
x.dropna(inplace=True)
#print(x.isnull().sum())

y=x.loc[0:,["pclass","sex","age","fare"]]
le=x["survived"]
#print(le)
z=LabelEncoder()
y["sex"]=z.fit_transform(y["sex"])
#print(y)
x_train,x_test,y_train,y_test=train_test_split(y,le,test_size=0.2)
dtc=DecisionTreeClassifier(criterion='entropy',random_state=0,max_depth=3,min_samples_leaf=4)
fits=dtc.fit(x_train,y_train)
print(fits)
pred=dtc.predict(x_test)
print(pred)
ac=dtc.score(x_test,y_test)
print(ac)
cm=confusion_matrix(y_test,pred)
print(cm)
cr=classification_report(y_test,pred)
print(cr)
tree.plot_tree(fits,feature_names=["pclass","sex","age","fare"])
plt.show()'''

#------------------------------------------------------------------------------------------------------
'''x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/creditcard.csv")
#print(x)

x = pd.read_csv('C:/Users/Prince kumar/OneDrive/Desktop/titanic1.csv')
x.dropna(inplace=True)
#print(x.isnull().sum())

y=x.loc[0:,["pclass","sex","age","fare"]]
le=x["survived"]
#print(le)
z=LabelEncoder()
y["sex"]=z.fit_transform(y["sex"])
#print(y)
x_train,x_test,y_train,y_test=train_test_split(y,le,test_size=0.2)


print("this is my support vector machine\n\n\n")
svc=SVC(kernel='linear',random_state=50)
fits1=svc.fit(x_train,y_train)
pred1=svc.predict(x_test)
print(pred1)
ac=svc.score(x_test,y_test)
print(ac)
'''


#---------------------------------------------------------------------------------------------------------------------
#		Revision of simple imputer
#------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.impute import SimpleImputer
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

'''
x = pd.read_csv('C:/Users/Prince kumar/OneDrive/Desktop/titanic1.csv')
#print(x.isnull().sum())
y=x.loc[0:,["pclass","sex","age","fare"]]
yy=LabelEncoder()
y['sex']=yy.fit_transform(y['sex'])
#print(y.isnull().sum())
le=x["survived"]
sim=SimpleImputer(missing_values=np.nan,strategy='mean')
#print(sim)
ff=sim.fit(y)
f=sim.transform(y)
#	Or
#f=sim.fit_transform(y)
#print(f)
x_train,x_test,y_train,y_test=tts(f,le,test_size=0.2,random_state=0)
#print(x_train.shape),print(x_test.shape)
knn=KNeighborsClassifier(n_neighbors=7)
fit=knn.fit(x_train,y_train)
pred=knn.predict(x_test)
#print(pd.value_counts(pred))
ac=knn.score(x_test,y_test)
print(ac)'''

#-------------------------------------------------------------------------------------------------------
#	Date 12-12-2022
#------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pylab
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier

'''
In simplest from ,a decision tree is a type of flowchart that show a clear pathway
to a decision.
in term of data anaytics, it is a type of Algorithms that includes conditional 'control'
statements to
classify data. A Decision tree starts at a single point (or,node) which then 
branches (or splits)
in two or more directions.Each branch offers different possible outcomes,
incorporating a varienty of

decision and chance evets untill a final outcome is achived.when shows visually,
their-like tree.. hence the Name
decision trees are extremly usefull for data analytics and machine learning Because
-------------------------------------------------

'''
#"C:\Users\Prince kumar\OneDrive\Desktop\Employee_Attrition.csv"
'''x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/Employee_Attrition.csv")
#print(x.isnull().sum())
#print(x['OverTime'])
a=LabelEncoder()
a1=LabelEncoder()
a2=LabelEncoder()
a3=LabelEncoder()
a4=LabelEncoder()
x['Gender']=a.fit_transform(x['Gender'])
x['MaritalStatus']=a1.fit_transform(x['MaritalStatus'])
x['Attrition']=a2.fit_transform(x['Attrition'])
x['OverTime']=a3.fit_transform(x['OverTime'])
x['JobRole']=a4.fit_transform(x['JobRole'])
le=x['Attrition']
f=['OverTime','Gender','MaritalStatus','JobRole','DistanceFromHome']#,'MonthlyIncome','Age']
fe=x[f]
#print(fe)
x_train,x_test,y_train,y_test=train_test_split(fe,le,test_size=0.2,random_state=25)


dtree=DecisionTreeClassifier(criterion='entropy',max_depth=5,min_samples_leaf=8)
fits=dtree.fit(x_train,y_train)
pred=dtree.predict(x_test)
#print(pred)

ac=dtree.score(x_test,y_test)
print(ac)
tree.plot_tree(fits,feature_names=f)
plt.show()

sv=SVC(kernel='linear',random_state=0)
fits=sv.fit(x_train,y_train)
pred=sv.predict(x_test)
ac=sv.score(x_test,y_test)
print(ac)

knn=KNeighborsClassifier(n_neighbors=5)
fits=knn.fit(x_train,y_train)
pred=knn.predict(x_test)
ac2=knn.score(x_test,y_test)
print(ac2)

from sklearn.ensemble import RandomForestClassifier

rfc=RandomForestClassifier()
fit3=rfc.fit(x_train,y_train)
aaa=rfc.score(x_test,y_test)
print(aaa)'''


#-----------------------------------------------------------------------------------
#		Date - 13-12-20222
#--------------------------------------------------------------------------------------------
#	 Random Forest classifier
#------------------------------------------------------------------------
'''
A random forest classifier.

A random forest is a meta estimator that fits a number of decision tree classifiers on 
various sub-samples of the dataset and uses averaging to improve the predictive accuracy 
and control over-fitting. The sub-sample size is controlled with the max_samples parameter 
if bootstrap=True (default), otherwise the whole dataset is used to build each tree.


Random forest is a popular machine learning algorithm that belongs to the supervised learning
technique. It can be used for both classification and regression problems in ML.it is based on 
ensemble learning , which is a process of combinfing of multipule classifiers to solve a 
complex problem and to improve the performance of the model.

What does random forest Algorithms work ?
There is a training set and test set , in this training set has sample and features, samples are
the rows and features are the columns, training set is the collection of features and sample .
from this training data set I create new data sets , like subsets of training data sets.
may be possible in my two training data set has same data that is called withreplacement

Why we create bootstrap sample?
To create the decision tree we make bootstrap the samples

what is the ensemble classifier ?
when you got the majority -------------------


What is the meaningg of bootstrap ?
Bootstrap means that instead of training on all the observations, each tree of random forest is trained
on a subset of the observations. The chosen subset is called the bags ,and the remaining are
called out bag sample.Multiple trees are trained on different bags, and later the results from all the 
trees are aggregated'''


import seaborn as sns
from sklearn.datasets import load_digits
'''x=load_digits()
#print(dir(x))

le=x.target
#print(le)
fe=x.data
#print(fe)
x_train,x_test,y_train,y_test=train_test_split(fe,le,test_size=0.2,random_state=42)
from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier()#n_estimators=100,criterion='gini')
fits=rfc.fit(x_train,y_train)
pred=rfc.predict(x_test)
ac=rfc.score(x_test,y_test)
print(ac)
cm=confusion_matrix(y_test,pred)
plt.figure(figsize=(8,6))
sns.heatmap(cm,annot=True,cmap='coolwarm',linecolor='grey')
plt.title('RandomForestClassifier')
plt.show()'''


from sklearn.ensemble import RandomForestClassifier

'''x = pd.read_csv('C:/Users/Prince kumar/OneDrive/Desktop/titanic1.csv')
#print(x.isnull().sum())

yy=LabelEncoder()
y1=LabelEncoder()
x['sex']=yy.fit_transform(x['sex'])
x['alive']=y1.fit_transform(x['alive'])

#print(y.isnull().sum())
le=x["survived"]
y=x[['pclass','sex','sibsp','fare','age','alive']]
x_train,x_test,y_train,y_test=train_test_split(y,le,test_size=0.2,random_state=42)
sim=SimpleImputer(missing_values=np.nan,strategy='mean')
x_train=sim.fit_transform(x_train)
x_test=sim.transform(x_test)
rfc=RandomForestClassifier()
fits=rfc.fit(x_train,y_train)
pred=rfc.predict(x_test)
ac=rfc.score(x_test,y_test)
print(ac)'''


'''
x=pd.read_csv("C:/Users/Prince kumar/OneDrive/Desktop/zomato.csv")
x.dropna(inplace=True)
#print("\nin Actual dilevery mode")
#print(x['online_order'].value_counts())
#print(x.isnull().sum())
#print(x['listed_in(type)'])#.isnull().sum())

a=LabelEncoder()
a1=LabelEncoder()
a2=LabelEncoder()
a3=LabelEncoder()
a4=LabelEncoder()
a5=LabelEncoder()

x['online_order']=a.fit_transform(x['online_order'])
x['rest_type']=a1.fit_transform(x['rest_type'])
x['listed_in(type)']=a2.fit_transform(x['listed_in(type)'])
x['location']=a3.fit_transform(x['location'])
x['address']=a4.fit_transform(x['address'])
x['approx_cost(for two people)']=a5.fit_transform(x['approx_cost(for two people)'])


fe=x[['rest_type','listed_in(type)','approx_cost(for two people)','location','address']]
le=x['online_order']

x_train,x_test,y_train,y_test=train_test_split(fe,le,test_size=0.2,random_state=0)
print("\nin Actual dilevery mode")
print(y_test.value_counts())

#sim=SimpleImputer(missing_values=np.nan,strategy='mean')
#x_train=sim.fit_transform(x_train)
#x_test=sim.transform(x_test)

#sc=StandardScaler()
#x_train=sc.fit_transform(x_train)
#x_test=sc.transform(x_test)

rfc=RandomForestClassifier()
fits=rfc.fit(x_train,y_train)
pred=rfc.predict(x_test)
q=[]
for i in pred:
	if i==0:
		d="No"
	else:
		d='Yes'
	q.append(d)
print("\nMachine predicted dilevery mode\n")
print(pd.value_counts(q))
ac=rfc.score(x_test,y_test)
print(ac)
cm=confusion_matrix(y_test,pred)
print(cm)
plt.figure(figsize=(8,6))
sns.heatmap(cm,annot=True)
plt.show()'''


'''
dtree=DecisionTreeClassifier(criterion='entropy',max_depth=5,min_samples_leaf=8)
fits=dtree.fit(x_train,y_train)
pred=dtree.predict(x_test)
#print(pred)

ac=dtree.score(x_test,y_test)
print(ac)
#tree.plot_tree(fits,feature_names=f)
#plt.show()

sv=SVC(kernel='linear',random_state=0)
fits=sv.fit(x_train,y_train)
pred=sv.predict(x_test)
ac=sv.score(x_test,y_test)
print(ac)

knn=KNeighborsClassifier(n_neighbors=5)
fits=knn.fit(x_train,y_train)
pred=knn.predict(x_test)
ac2=knn.score(x_test,y_test)
print(ac2)
'''

#-----------------------------------------------------------------------------------------------------------
#	---------------	Date -  15/12/2022			------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
'''
Underfitting: A statistical model or a machine learning algorithm is said to have underfitting when it cannot 
capture the underlying trend of the data, i.e., it only performs well on training data but performs poorly on 
testing data. (It’s just like trying to fit undersized pants!) Underfitting destroys the accuracy of our 
machine learning model. Its occurrence simply means that our model or the algorithm does not fit the data 
well enough. It usually happens when we have fewer data to build an accurate model and also when we try to
 build a linear model with fewer non-linear data. In such cases, the rules of the machine learning model are
  too easy and flexible to be applied to such minimal data and therefore the model will probably make a lot of
   wrong predictions. Underfitting can be avoided by using more data and also reducing the features
   by feature selection. 

Overfitting: A statistical model is said to be overfitted when the model does not make accurate predictions on 
testing data. When a model gets trained with so much data, it starts learning from the noise and inaccurate data
 entries in our data set. And when testing with test data results in High variance. Then the model does not categorize
  the data correctly, because of too many details and noise. The causes of overfitting are the non-parametric and 
  non-linear methods because these types of machine learning algorithms have more freedom in building the model 
  based on the dataset and therefore they can really build unrealistic models. A solution to avoid overfitting is
   using a linear algorithm if we have linear data or using the parameters like the maximal depth if we are using 
   decision trees. 


What is mean by overfitting ?
Overfitting occurs when the model  cannot generalize and fits too closely to the training dataset
insted . Overfitting happens due to several reasons , such as : The training data size is too small 
and does not contain enough data samples to accurately represent all possible input data values.

In overfitting model on your get high accuracy and low error ,but on testing data set you will get low 
accuracy and high errors, so that is called Overfitting    


What is the mean of underfitting  ?
Underfitting means that your model makes accurate, but initially incorrect predictions. In this case,
 train error is large and val/test error is large too. 


Overfitting :---
 Overfitting means that your model makes not accurate predictions. 
 In this case, train error is very small and val/test error is large.



 Bias:- Assumptions made by a model to make a function easier to learn. 
 It is actually the error rate of the training data. When the error rate
  has a high value, we call it High Bias and when the error rate has a
   low value, we call it low Bias.

   							

Variance:- The difference between the error rate of training data and testing data is
 called variance. If the difference is high then it’s called high variance and when 
 the difference of errors is low then it’s called low variance. Usually, we want to
  make a low variance for generalized our model.


 Reasons for Underfitting:

High bias and low variance 
The size of the training dataset used is not enough.
The model is too simple.
Training data is not cleaned and also contains noise in it.
Techniques to reduce underfitting: 


Increase model complexity
Increase the number of features, performing feature engineering
Remove noise from the data.
Increase the number of epochs or increase the duration of training to get better results.

--------------------------------------------------------------------------------------------

Reasons for Overfitting are as follows:
 High variance and low bias 
The model is too complex
The size of the training data 
Examples:


Techniques to reduce overfitting:

1.Increase training data.
2.Reduce model complexity.
3.Early stopping during the training phase (have an eye over the loss over the training period
   as soon as loss begins to increase stop training).
4.Ridge Regularization and Lasso Regularization
5.Use dropout for neural networks to tackle overfitting.


What is rightfitting ?
Ideally, the case when the model makes the predictions with 0 error , is said to have good fit 
on the data.
'''

import pandas as pd
'''df=pd.read_csv('C:/Users/Prince kumar/OneDrive/Desktop/Loan_will_approve.csv')
#print(x.isnull().sum())
#print(x.nunique())
#print("\n\n")
#df['Property_Area']=a.fit_transform(df['Property_Area']

#df['Loan_Status']=a.fit_transform(df['Loan_Status'])
#print(x.nunique())
#print(x[x['Loan_Status']=='N'])
#print(df.isnull().sum())
a=LabelEncoder()
df['Education']=a.fit_transform(df['Education'])
df['Property_Area']=a.fit_transform(df['Property_Area'])
df['Loan_Status']=a.fit_transform(df['Loan_Status'])


x=df[['Education','Credit_History','Property_Area','LoanAmount','ApplicantIncome']]
y=df['Loan_Status']
si=SimpleImputer(missing_values=np.nan,strategy='mean')
x=si.fit_transform(x)



x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=25)
#print(x_test.shape)

rfc=RandomForestClassifier()
fits=rfc.fit(x_train,y_train)
pred=rfc.predict(x_test)
print(pd.value_counts(pred))
ac=rfc.score(x_test,y_test)
print(ac)'''


from pydataset import data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier

#x=data('DoctorAUS')
#x=x['insurance']
#x1=pd.get_dummies(x,columns=['chcond'],drop_first=True)
#print(x1)

#-------------------------------------------------------------------------------------------------
#		Date 19-12-2022
#------------------------------------------------------------------------------------------------------

'''
Naive Bayes classifier Algorithm

Naive bayes Algorithms is a supervised machine learning Algorithm, which is 
based on bayes theorem and used for solving classification problems.
It is mainly used in text classification that includes a high-dimenstional 
training dataset.
Naive bayes classifiers is one of the simple and most effective classification 
algorithms which helps in building the fast machine learning models that can make
quick predictions .
It is a probability classifier, which means its predict on the basis of the basis of the
probablity of an object.


Why is called naive bayes ?
-------------------- 

Type of Naive bayes model :
there are three type of naive bayes model

1. Gaussian :- The Gaussian model assumes that feauters follow a normal distribution. this means 
if predictions take continous values instead of discrete,Then the model assumes that assumes
that these values are sampled from the Gaussian distribution.

2. Multinomial :-The Multinomial Naive Bayes classifier is used when the data is Multinomial
distributed . it is primerly used for document used for documents classification problems.


3.Bernouli :- The bernauli classifier works similar to Multinomial classifier, but
---------------------------
'''

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pydataset import data
from sklearn.preprocessing import StandardScaler

'''x=pd.read_csv('C:/Users/Prince kumar/OneDrive/Desktop/heart.csv')
#print(x.nunique())
fe=x.drop("output",axis='columns')
le=x['output']

sc=StandardScaler()
fe1=sc.fit_transform(fe)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(fe1,le,test_size=0.2,random_state=40)

from sklearn.naive_bayes import GaussianNB,BernoulliNB
from sklearn.naive_bayes import MultinomialNB

#ss=GaussianNB()
ss=BernoulliNB()
#ss=Multinomial()
fits=ss.fit(x_train,y_train)
pred=ss.predict(x_test)
#print(pred)

ac=ss.score(x_test,y_test)
#print(ac)
from sklearn.metrics import confusion_matrix,classification_report
cm=confusion_matrix(y_test,pred)'''
#print(cm)
#plt.figure(figsize=(8,6))
#sns.heatmap(cm,annot=True)
#plt.show()
#cl=classification_report(y_test,pred)
#print(cl)

#----------------------------------------------------------------------------------------------------------------
#------------------  puja sharma  classes ended ---------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
#			Dipanshu sir by machine learning in Regression started 
#---------------------------------------------------------------------------------------------------------------------

#what is Regression ?
#Regression is a machine learning Techniques which is uused to predict the continous variable
'''there are six type of regression 
1. linear Regression
2. Logical Regression
3. Ridge Regression
4. Lasso Regression
5.Polynomial Regression
6.Bayesian Linear Regression '''


# Linear Regression

'''
Linear Regression in Machine Learning

Linear regression is one of the easiest and most popular Machine Learning algorithms. 
 statistical method that is used for predictive analysis. Linear regression makes predictions
  for continuous/real or numeric variables such as sales, salary, age, product price, etc.

Linear regression algorithm shows a linear relationship between a dependent (y) and one or more 
independent (y) variables, hence called as linear regression. Since linear regression shows the
 linear relationship, which means it finds how the value of the dependent variable is changing
  according to the value of the independent variable.

The linear regression model provides a sloped straight line representing the relationship 
between the variables. Consider the below image:


Linear Regression in Machine Learning
Mathematically, we can represent a linear regression as:


y= a0+a1x+ ε
Here,

Y= Dependent Variable (Target Variable)
X= Independent Variable (predictor Variable)
a0= intercept of the line (Gives an additional degree of freedom)
a1 = Linear regression coefficient (scale factor to each input value).
ε = random error

The values for x and y variables are training datasets for Linear Regression model representation.

Types of Linear Regression
Linear regression can be further divided into two types of the algorithm:

Simple Linear Regression:
If a single independent variable is used to predict the value of a numerical dependent variable, 
then such a Linear Regression algorithm is called Simple Linear Regression.

Multiple Linear regression:
If more than one independent variable is used to predict the value of a numerical dependent variable,
 then such a Linear Regression algorithm is called Multiple Linear Regression.

Linear Regression Line
A linear line showing the relationship between the dependent and independent variables is called 
a regression line. A regression line can show two types of relationship:

Positive Linear Relationship:
If the dependent variable increases on the Y-axis and independent variable increases on X-axis,
 then such a relationship is termed as a Positive linear relationship.

Linear Regression in Machine Learning
Negative Linear Relationship:
If the dependent variable decreases on the Y-axis and independent variable increases on the X-axis,
 then such a relationship is called a negative linear relationship.

Linear Regression in Machine Learning
Finding the best fit line:
When working with linear regression, our main goal is to find the best fit line that means the error
 between predicted values and actual values should be minimized. The best fit line will have the least error.

The different values for weights or the coefficient of lines (a0, a1) gives a different line of regression,
 so we need to calculate the best values for a0 and a1 to find the best fit line, so to calculate this we use 
 cost function.

Cost function-
The different values for weights or coefficient of lines (a0, a1) gives the different line of regression,
 and the cost function is used to estimate the values of the coefficient for the best fit line.
Cost function optimizes the regression coefficients or weights. It measures how a linear regression model 
is performing.

We can use the cost function to find the accuracy of the mapping function, which maps the input variable 
to the output variable. This mapping function is also known as Hypothesis function.
For Linear Regression, we use the Mean Squared Error (MSE) cost function, which is the average of squared
 error occurred between the predicted values and actual values. It can be written as:


For the above linear equation, MSE can be calculated as:

Linear Regression in Machine Learning
Where,

N=Total number of observation
Yi = Actual value
(a1xi+a0)= Predicted value.

Residuals: The distance between the actual value and predicted values is called residual.
 If the observed points are far from the regression line, then the residual will be high, 
 and so cost function will high. If the scatter points are close to the regression line,
  then the residual will be small and hence the cost function.

Gradient Descent:
Gradient descent is used to minimize the MSE by calculating the gradient of the cost function.
A regression model uses gradient descent to update the coefficients of the line by reducing the
 cost function.

It is done by a random selection of values of coefficient and then iteratively update the values 
to reach the minimum cost function.
Model Performance:
The Goodness of fit determines how the line of regression fits the set of observations. The process 
of finding the best model out of various models is called optimization. It can be achieved by below method:


1. R-squared method:

R-squared is a statistical method that determines the goodness of fit.
It measures the strength of the relationship between the dependent and independent variables on a scale of 0-100%.
The high value of R-square determines the less difference between the predicted values and actual values and hence
 represents a good model.

It is also called a coefficient of determination, or coefficient of multiple determination for multiple regression.
It can be calculated from the below formula:
Linear Regression in Machine Learning


Assumptions of Linear Regression
+*/-+*/-/*+/*-*+*/+-/*+*/*-*/+*/-*+*/-*+*/-+*/-*+*/*-*+*/-*+*/-/*+*/-*+/-/+*/-*+*/-*+*/-/+/*/-/*+*/-+*/+/--+*/-+*/+-*+-*+/-*+*-*+*/*/

Below are some important assumptions of Linear Regression. These are some formal checks while building a Linear 
Regression model, which ensures to get the best possible result from the given dataset.

Linear relationship between the features and target:
Linear regression assumes the linear relationship between the dependent and independent variables.

Small or no multicollinearity between the features:
Multicollinearity means high-correlation between the independent variables. Due to multicollinearity, 
it may difficult to find the true relationship between the predictors and target variables. Or we can
 say, it is difficult to determine which predictor variable is affecting the target variable and which 
 is not. So, the model assumes either little or no multicollinearity between the features or independent
 variables.

Homoscedasticity Assumption:
Homoscedasticity is a situation when the error term is the same for all the values of independent variables. 
With homoscedasticity, there should be no clear pattern distribution of data in the scatter plot.

Normal distribution of error terms:
Linear regression assumes that the error term should follow the normal distribution pattern. If error terms 
are not normally distributed, then confidence intervals will become either too wide or too narrow, which may 
cause difficulties in finding coefficients.

It can be checked using the q-q plot. If the plot shows a straight line without any deviation, 
which means the error is normally distributed.

No autocorrelations:
The linear regression model assumes no autocorrelation in error terms. If there will be any correlation 
in the error term, then it will drastically reduce the accuracy of the model. Autocorrelation usually occurs 
if there is a dependency between residual errors.
'''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pylab
from scipy import stats as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

'''x=pd.read_csv('C:/Users/prince kumar/Downloads/Copy of placement (4).csv')
#print(x)
print(x.isna().sum())
print("Finding the co-relation between both columns\n",x.corr())
#a=1
#for i in x:
#	plt.subplot(1,2,a)
#	st.probplot(x[i],dist="norm",plot=pylab);
#	plt.xlabel(i)
#	a+=1
#pylab.show()

plt.scatter(x['cgpa'],x['package'],marker='*',color='red')
#plt.show()

x1=x[['cgpa']]
y=x[['package']]

x_train,x_test,y_train,y_test=train_test_split(x1,y,test_size=0.2,random_state=42)
print(x_train.shape)

lr=LinearRegression()
fits=lr.fit(x_train,y_train)
#print(fits)
pred=lr.predict(x_test)
#print(pred)

ac=lr.score(x_test,y_test)
print(ac)

m=lr.coef_
print("Coefficient :-",m)
c=lr.intercept_
print("intercept",c)

plt.scatter(x['cgpa'],x['package'],color='green',marker='*')
#plt.plot(x_train,lr.predict(x_train),color='red')
plt.plot(x_test,lr.predict(x_test),color="pink")
pylab.show()

y=m*6.89+c # Y=MX+C methods
print("Prdicted values in the data set :-",y)
'''

#--------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
# 	Date 21-12-2022
#---------------------------------------------------------------------------------------------------------------
import warnings
warnings.filterwarnings("ignore")

#Multipule Linear Regression
#when we have more than 2  continous featrues then it is called Multiple regression
'''
x=pd.read_csv('C:/Users/prince kumar/Downloads/Admission_Prediction (2).csv')
#print(x)
#print(x.isna().sum())
x.fillna(x['GRE Score'].mean(),inplace=True)
x.fillna(x['TOEFL Score'].mean(),inplace=True)
x.fillna(x['University Rating'].mean(),inplace=True)
#print(x.isna().sum())

x.drop(columns=['Serial No.'],inplace=True)
#print(x)
corr=x.corr()
sns.heatmap(corr,annot=True)
plt.title('Co-relation of this dataset',fontweight='bold')
#plt.show()

fe=x.drop(columns=['Chance of Admit'])
#print(fe)
leb=x[['Chance of Admit']]
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
fea=scaler.fit_transform(fe)
#print(fea)
x_train,x_test,y_train,y_test=train_test_split(fea,leb,test_size=0.2,random_state=42)
#print(x_test.shape)
lr=LinearRegression()
fits=lr.fit(x_train,y_train)
#print(fits)
ac=lr.score(x_test,y_test)
print("Accuracy of LinearRegression testing data : -",ac)
ac1=lr.score(x_train,y_train)
print("Accuracy of LinearRegression Training data :- ",ac1)
pred=lr.predict(x_test)
#print(pred)
m=lr.coef_
#print("\nSlope or Coefficient :-\n",m)
c=lr.intercept_
#print('\nC or Intercept :-',c)
from sklearn.linear_model import LassoCV,Lasso

#lassocv=LassoCV(alphas=None,cv=10,max_iter=100000,normalize=True)
lcv=LassoCV(alphas=None,cv=10,max_iter=100000,normalize=True)
#print(lcv)

fitcv=lcv.fit(x_train,y_train)
#print(fitcv)
alpha=lcv.alpha_ # It will show best alpha value
#print("Value of alpha :-",alpha)
acc=lcv.score(x_test,y_test)
print('Accuracy of LassoCV model in testing data:-',acc)
acc1=lcv.score(x_train,y_train)
print('Accuracy of LassoCV model in training data:-',acc1)
pred2=lcv.predict(x_test)
#print(pred2)

#Applying the new model Lasso regression
lso=Lasso(alpha)
fits3=lso.fit(x_train,y_train)
#print(fits3)
ac3=lso.score(x_test,y_test)
print("Accuracy of Lasso model in testing data :-",ac3)
ac4=lso.score(x_train,y_train)
print("Accuracy of Lasso model in training dataset :-",ac4)
pred3=lso.predict(x_test)
#print(pred3)

from sklearn.linear_model import RidgeCV,Ridge

alphas = np.random.uniform(low=0, high=10, size=(50,))


ridgecv = RidgeCV(alphas =alphas,cv=10,normalize = True)
fits4=ridgecv.fit(x_train, y_train)
alpha1=ridgecv.alpha_  # Ridge model in use this alpha value
ac5=ridgecv.score(x_test,y_test)
print("Accuracy of the RidgeCV model in testing data :-",ac5)
ac7=ridgecv.score(x_train,y_train)
print("Accuracy of the RidgeCV model in training data :-",ac7)


ridge_model = Ridge(alpha=alpha1)
fits5=ridge_model.fit(x_train, y_train)
ac6=ridge_model.score(x_test,y_test)
print("Accuracy of the Ridge model in testing data :-",ac6)
ac8=ridge_model.score(x_train,y_train)
print("Accuracy of the Ridge model in training data :-",ac8)'''


#------------------------------------------------------------------------------------------------
#		Date - 22-12-2022
#------------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
'''x=pd.read_csv("C:/Users/Prince kumar/Downloads/Linear Regression - Sheet1.csv")
print(x)
fe=x[['X']]
#print(fe)
le=x[['Y']]
#print(le)
from sklearn.preprocessing import MinMaxScaler
from scipy import stats as st
import matplotlib.pyplot as plt
import seaborn as sns
mns=MinMaxScaler()
fe1=mns.fit_transform(fe)'''
#print(fe1)

#plt.scatter(fe1,le,color='red')
#plt.show()

from sklearn.preprocessing import PolynomialFeatures
#pf=PolynomialFeatures(2)
#fe2=pf.fit_transform(fe1)
#print(fe2)
'''
from sklearn.model_selection import train_test_split as tts
x_train,x_test,y_train,y_test=tts(fe1,le,test_size=0.2,random_state=0)
#print(x_train.shape)
#print(x_test.shape)
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
fits=lr.fit(x_train,y_train)
ac=lr.score(x_test,y_test)
#print(ac)
pred=lr.predict(x_test)
#print(pred)
m=lr.coef_
#print("Cofficient :-",m)
c=lr.intercept_
#print("Intercept :-",c)
from sklearn.metrics import r2_score,mean_squared_error
r2=r2_score(y_test,pred)
print("R2_Score : -",r2)
mse=mean_squared_error(y_test,pred)
print("mean_squared_error :-",mse)

plt.scatter(x_test,pred,label="prediction",c='red')
plt.scatter(x_test,y_test,label="Actual",c='green')
plt.legend()
plt.grid()
plt.show()'''

#----------------------------------------------------------------------------------------------------------------------------------------------
#----------------------- date 27-12-2022------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------Logistic Regression ---------------------------------------------

'''
Logistic Regression in Machine Learning

Logistic regression is one of the most popular Machine Learning algorithms, which comes
under the Supervised Learning technique. It is used for predicting the categorical 
dependent variable using a given set of independent variables.

Logistic regression predicts the output of a categorical dependent variable. Therefore
 the outcome must be a categorical or discrete value. It can be either Yes or No, 0 or 1,
  true or False, etc. but instead of giving the exact value as 0 and 1, it gives the 
  probabilistic values which lie between 0 and 1.

Logistic Regression is much similar to the Linear Regression except that how they are used.
 Linear Regression is used for solving Regression problems, whereas Logistic regression is
  used for solving the classification problems.

In Logistic regression, instead of fitting a regression line, we fit an "S" shaped logistic 
function, which predicts two maximum values (0 or 1).

The curve from the logistic function indicates the likelihood of something such as whether 
the cells are cancerous or not, a mouse is obese or not based on its weight, etc.

Logistic Regression is a significant machine learning algorithm because it has the ability 
to provide probabilities and classify new data using continuous and discrete datasets.


Logistic Regression can be used to classify the observations using different types of data and 
can easily determine the most effective variables used for the classification. The below image
 is showing the logistic function:

Logistic Regression in Machine Learning

Note: Logistic regression uses the concept of predictive modeling as regression; therefore,
 it is called logistic regression, but is used to classify samples; Therefore, it falls under
 the classification algorithm.

Logistic Function (Sigmoid Function):
The sigmoid function is a mathematical function used to map the predicted values to probabilities.
It maps any real value into another value within a range of 0 and 1.

The value of the logistic regression must be between 0 and 1, which cannot go beyond this limit, 
so it forms a curve like the "S" form. The S-form curve is called the Sigmoid function or the 
logistic function.

In logistic regression, we use the concept of the threshold value, which defines the probability 
of either 0 or 1. Such as values above the threshold value tends to 1, and a value below the 
threshold values tends to 0.

Assumptions for Logistic Regression:

The dependent variable must be categorical in nature.
The independent variable should not have multi-collinearity.

Logistic Regression Equation:
The Logistic regression equation can be obtained from the Linear Regression equation. The mathematical
steps to get Logistic Regression equations are given below:

We know the equation of the straight line can be written as:


Logistic Regression in Machine Learning
In Logistic Regression y can be between 0 and 1 only, so for this let's divide the above equation by (1-y):


Logistic Regression in Machine Learning
But we need range between -[infinity] to +[infinity], then take logarithm of the equation it will become:


Logistic Regression in Machine Learning
The above equation is the final equation for Logistic Regression.


Type of Logistic Regression:
On the basis of the categories, Logistic Regression can be classified into three types:


Binomial: In binomial Logistic regression, there can be only two possible types of the dependent variables, 
such as 0 or 1, Pass or Fail, etc.


Multinomial: In multinomial Logistic regression, there can be 3 or more possible unordered types of the 
dependent variable, such as "cat", "dogs", or "sheep"


Ordinal: In ordinal Logistic regression, there can be 3 or more possible ordered types of dependent 
variables, such as "low", "Medium", or "High".

'''
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pylab
from scipy import stats as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import r2_score,rand_score

'''
df=pd.read_csv("C:/Users/Prince kumar/Downloads/data (1).csv")

df.drop(columns=['id','Unnamed: 32'],inplace=True)
#print(df.isnull().sum())
a=LabelEncoder()
sc=StandardScaler()
df['diagnosis']=a.fit_transform(df['diagnosis'])
x=df.drop('diagnosis',axis=1)
#print(x)
y=df[['diagnosis']]
#print(y)
x=sc.fit_transform(x)
#print(x)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=125)
#print(x_train.shape)
#print(x_test.shape)
#print(y_train.shape)
#print(y_test.shape)
log=LogisticRegression()
log.fit(x_train,y_train)
pred=log.predict(x_test)
#print(pred)
ac=log.score(x_test,y_test)
#print(ac)
acc=log.score(x_train,y_train)
#print(acc)
mse=mean_squared_error(y_test,pred)
#print(mse)
m=log.coef_
#print(m)
c=log.intercept_
#print(c)
mae=mean_absolute_error(y_test,pred)
#print(mae)
mape=mean_absolute_percentage_error(y_test,pred)
#print(mape)
r2s=r2_score(y_test,pred)
#print(r2s)'''

#x=pd.read_excel("C:/Users/Prince kumar/OneDrive/Desktop/mldataset/Dummy Data.xlsx")
#print(x)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------  Date 29-12-2022  --------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                 Decision Tree Classifier/Regression
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
Decision Tree Classification Algorithm
Decision Tree is a Supervised learning technique that can be used for both classification and Regression 
problems, but mostly it is preferred for solving Classification problems. It is a tree-structured classifier,
 where internal nodes represent the features of a dataset, branches represent the decision rules and each
  leaf node represents the outcome.

In a Decision tree, there are two nodes, which are the Decision Node and Leaf Node. Decision nodes are used 
to make any decision and have multiple branches, whereas Leaf nodes are the output of those decisions and do 
not contain any further branches.

The decisions or the test are performed on the basis of features of the given dataset.

It is a graphical representation for getting all the possible solutions to a problem/decisionbased on given conditions.
It is called a decision tree because, similar to a tree, it starts with the root node, which expands on further branches 
and constructs a tree-like structure.


In order to build a tree, we use the CART algorithm, which stands for Classification and Regression Tree algorithm.
A decision tree simply asks a question, and based on the answer (Yes/No), it further split the tree into subtrees.

Below diagram explains the general structure of a decision tree:

Note: A decision tree can contain categorical data (YES/NO) as well as numeric data.


Decision Tree Classification Algorithm


Why use Decision Trees?
There are various algorithms in Machine learning, so choosing the best algorithm for the given dataset and problem
 is the main point to remember while creating a machine learning model. 
 Below are the two reasons for using the Decision tree:

1. Decision Trees usually mimic human thinking ability while making a decision, so it is easy to understand.
2. The logic behind the decision tree can be easily understood because it shows a tree-like structure.
	Decision Tree Terminologies

Root Node: Root node is from where the decision tree starts. It represents the entire dataset, which further
 gets divided into two or more homogeneous sets.

Leaf Node: Leaf nodes are the final output node, and the tree cannot be segregated further after getting a leaf node.

Splitting: Splitting is the process of dividing the decision node/root node into sub-nodes according to the given conditions.

Branch/Sub Tree: A tree formed by splitting the tree.

Pruning: Pruning is the process of removing the unwanted branches from the tree.

Parent/Child node: The root node of the tree is called the parent node, and other nodes are called the child nodes.



How does the Decision Tree algorithm Work?

In a decision tree, for predicting the class of the given dataset, the algorithm starts from the root node of the tree. 
This algorithm compares the values of root attribute with the record (real dataset) attribute and, based on the comparison, 
follows the branch and jumps to the next node.

For the next node, the algorithm again compares the attribute value with the other sub-nodes and move further. 
It continues the process until it reaches the leaf node of the tree. The complete process can be better understood
using the below algorithm:


Step-1: Begin the tree with the root node, says S, which contains the complete dataset.
Step-2: Find the best attribute in the dataset using Attribute Selection Measure (ASM).
Step-3: Divide the S into subsets that contains possible values for the best attributes.
Step-4: Generate the decision tree node, which contains the best attribute.
Step-5: Recursively make new decision trees using the subsets of the dataset created in step -3. 
Continue this process until a stage is reached where you cannot further classify the nodes and called the final
 node as a leaf node.

Decision Tree Classification Algorithm
Attribute Selection Measures
While implementing a Decision tree, the main issue arises that how to select the best attribute for the root node and for 
sub-nodes. So, to solve such problems there is a technique which is called as Attribute selection measure or ASM. By this
 measurement, we can easily select the best attribute for the nodes of the tree. There are two popular techniques
 for ASM, which are:


Information Gain

Gini Index
1. Information Gain:
Information gain is the measurement of changes in entropy after the segmentation of a dataset based on an attribute.
It calculates how much information a feature provides us about a class.

According to the value of information gain, we split the node and build the decision tree.

A decision tree algorithm always tries to maximize the value of information gain, and a node/attribute having the highest
 information gain is split first. It can be calculated using the below formula:
Information Gain= Entropy(S)- [(Weighted Avg) *Entropy(each feature)  


Entropy:-
Entropy is a metric to measure the impurity in a given attribute. It specifies randomness in data. Entropy 
can be calculated as:

Entropy(s)= -P(yes)log2 P(yes)- P(no) log2 P(no)

													Where,
													S= Total number of samples
													P(yes)= probability of yes
													P(no)= probability of no



2. Gini Index:
Gini index is a measure of impurity or purity used while creating a decision tree in the CART(Classification and Regression Tree) algorithm.
An attribute with the low Gini index should be preferred as compared to the high Gini index.
It only creates binary splits, and the CART algorithm uses the Gini index to create binary splits.

Gini index can be calculated using the below formula:

		Gini Index= 1- ∑jPj2



Pruning: Getting an Optimal Decision tree
Pruning is a process of deleting the unnecessary nodes from a tree in order to get the optimal decision tree.

A too-large tree increases the risk of overfitting, and a small tree may not capture all the important features 
of the dataset. Therefore, a technique that decreases the size of the learning tree without reducing accuracy is known 
as Pruning. There are mainly two types of tree pruning technology used:
Cost Complexity Pruning Reduced Error Pruning.


Advantages of the Decision Tree

It is simple to understand as it follows the same process which a human follow while making any decision in real-life.
It can be very useful for solving decision-related problems.
It helps to think about all the possible outcomes for a problem.
There is less requirement of data cleaning compared to other algorithms.


Disadvantages of the Decision Tree

The decision tree contains lots of layers, which makes it complex.
It may have an overfitting issue, which can be resolved using the Random Forest algorithm.
For more class labels, the computational complexity of the decision tree may increase.
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Decision Tree Classifier / Regression
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats as st
import pylab
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.metrics import confusion_matrix,classification_report
from IPython.display import Image
import graphviz
from sklearn import tree
import warnings
warnings.filterwarnings('ignore')


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
x = sns.load_dataset('iris')
#print(x.isnull().sum())
a=LabelEncoder()
x['species']=a.fit_transform(x['species'])
#print(x)

fe=x.drop("species",axis=1)
le=x[['species']]

sc=StandardScaler()
fe=sc.fit_transform(fe)
#print(fe)
x_train,x_test,y_train,y_test=train_test_split(fe,le,test_size=0.2,random_state=120)
#print(y_test.shape)
dt=DecisionTreeClassifier()
fts=dt.fit(x_train,y_train)
#print(fts)
ac=dt.score(x_train,y_train)
ac1=dt.score(x_test,y_test)
#print("Accuracy of training data :- ",ac)
#print("Accuracy of teesting data :- ",ac1)

pred=dt.predict(x_test)
#print("Predicte values:-",pred)
p=np.array(y_test)
#print("Actual values :-",p.T)


#plt.figure(figsize=(15,10))
#tree.plot_tree(fts,filled=True)
#plt.show()

#----------------------------------------------------------------------------------------------------------------

gp={'criterion':['gini','entropy'],
'max_depth':range(2,32,1),
'min_samples_leaf':range(1,10,1),
'min_samples_split':range(1,10,1),
'splitter':['best','random']}
#print(gp)

gs=GridSearchCV(estimator=fts,param_grid=gp,cv=5,n_jobs=-1)
#print(gs)
fits=gs.fit(x_train,y_train)
#print(fits)

#print(gs.best_score_)
#print(gs.best_params_)

#---------------------------------------------------------------------------------------------------------------------------------

dtc=DecisionTreeClassifier(criterion='gini',max_depth=11,min_samples_leaf=4,min_samples_split=5,splitter='random')
ftss=dtc.fit(x_train,y_train)
#print(ftss)
ac2=dtc.score(x_test,y_test)
#print(ac2)
ac3=dtc.score(x_train,y_train)
#print(ac3)
pred1=dtc.predict(x_test)
cm=confusion_matrix(y_test,pred1)
print(cm)
clr=classification_report(y_test,pred1)
print(clr)

plt.figure(figsize=(10,8))
sns.heatmap(cm,annot=True)
plt.show()

#plt.figure(figsize=(12,10))
#tree.plot_tree(ftss,filled=True)
#plt.show()
'''

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Date 03-01-2023
#---------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Random Forest Classifier and Regression

A random forest regressor.

A random forest is a meta estimator that fits a number of classifying decision trees 
on various sub-samples of the dataset and uses averaging to improve the predictive 
accuracy and control over-fitting. The sub-sample size is controlled with the 
max_samples parameter if bootstrap=True (default), otherwise the whole dataset is 
used to build each tree.



Random Forest is a popular machine learning algorithm that belongs to the supervised
 learning technique. It can be used for both Classification and Regression problems 
 in ML. It is based on the concept of ensemble learning, which is a process of 
 combining multiple classifiers to solve a complex problem and to improve the 
 performance of the model.


As the name suggests, Random Forest is a classifier that contains a number of decision 
rees on various subsets of the given dataset and takes the average to improve the 
predictive accuracy of that dataset. Instead of relying on one decision tree,

the random forest takes the prediction from each tree and based on the majority votes of 
edictions, and it predicts the final output.

The greater number of trees in the forest leads to higher accuracy and prevents the 
problem of overfitting.


The below diagram explains the working of the Random Forest algorithm


Random Forest Algorithm
Note: To better understand the Random Forest Algorithm, you should have knowledge
 of the Decision Tree Algorithm.


Assumptions for Random Forest
Since the random forest combines multiple trees to predict the class of the dataset,
 it is possible that some decision trees may predict the correct output, while others 
 may not. But together, all the trees predict the correct output. Therefore, below are
  two assumptions for a better Random forest classifier:

There should be some actual values in the feature variable of the dataset so that the classifier can predict accurate results rather than a guessed result.
The predictions from each tree must have very low correlations.
Why use Random Forest?
Below are some points that explain why we should use the Random Forest algorithm:

It takes less training time as compared to other algorithms.
It predicts output with high accuracy, even for the large dataset it runs efficiently.
It can also maintain accuracy when a large proportion of data is missing.
How does Random Forest algorithm work?
Random Forest works in two-phase first is to create the random forest by combining N decision tree, and second is to make predictions for each tree created in the first phase.

The Working process can be explained in the below steps and diagram:

Step-1: Select random K data points from the training set.

Step-2: Build the decision trees associated with the selected data points (Subsets).

Step-3: Choose the number N for decision trees that you want to build.

Step-4: Repeat Step 1 & 2.


Step-5: For new data points, find the predictions of each decision tree, and assign the new data points to the category that wins the majority votes.

The working of the algorithm can be better understood by the below example:

Example: Suppose there is a dataset that contains multiple fruit images. So, this dataset is given to the Random forest classifier. The dataset is divided into subsets and given to each decision tree. During the training phase, each decision tree produces a prediction result, and when a new data point occurs, then based on the majority of results, the Random Forest classifier predicts the final decision. Consider the below image:

Random Forest Algorithm
Applications of Random Forest
There are mainly four sectors where Random forest mostly used:

Banking: Banking sector mostly uses this algorithm for the identification of loan risk.
Medicine: With the help of this algorithm, disease trends and risks of the disease can be identified.
Land Use: We can identify the areas of similar land use by this algorithm.
Marketing: Marketing trends can be identified using this algorithm.
Advantages of Random Forest
Random Forest is capable of performing both Classification and Regression tasks.
It is capable of handling large datasets with high dimensionality.
It enhances the accuracy of the model and prevents the overfitting issue.
Disadvantages of Random Forest
Although random forest can be used for both classification and regression tasks, it is not more suitable for Regression tasks.
'''
#*********************************************************************************************************************************************
#**********************************************************************************************************************************************

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor
from sklearn.metrics import confusion_matrix,classification_report,mean_squared_error,mean_absolute_error,mean_absolute_percentage_error,r2_score
'''
x=pd.read_csv("C:/Users/Prince kumar/Downloads/train (5).csv")
#print(x.head())
#print(x.isna().sum())
x.drop(columns=["Alley","PoolQC","Fence","MiscFeature"],inplace=True)
#print(x.isna().sum())
#print(x.info())
#print(x.isna().any())


for i in x:
	if x[i].isna().any()==True:
		if x[i].dtype=="float":
			if x[i].mean()-x[i].median()>10:
				x[i].fillna(x[i].median(),inplace=True)
			else:
				x[i].fillna(x[i].mean(),inplace=True)
		elif x[i].dtype=="object":
			x[i].fillna(x[i].mode()[0],inplace=True)


#for i in x:
#    if x[i].isnull().any():
#        if x[i].dtype==float:
#            if x[i].mean()-x[i].median()<10:
#                x[i].fillna(x[i].mean(),inplace=True)
#            else:
#                x[i].fillna(x[i].median(),inplace=True)
#       elif x[i].dtype=='object':
#            x[i].fillna(x[i].mode()[0],inplace=True)

#print(x.isna().sum())
#print(x.info())

ln=LabelEncoder()
for i in x:
	if x[i].dtype=='object':
		x[i]=ln.fit_transform(x[i])

#print(x.head())

fe=x.drop('SalePrice',axis=1)
#print(fe)
le=x[['SalePrice']]
#print(le)

sc=StandardScaler()
fe=sc.fit_transform(fe)
#print(fe)

x_train,x_test,y_train,y_test=train_test_split(fe,le,test_size=0.2,random_state=0)
#print(x_train.shape,y_train.shape)

#********************************************************************************
# Random forest regression model - 1
#------------------------------------
rf=RandomForestRegressor()
fits=rf.fit(x_train,y_train)
#print(fits)
pred=rf.predict(x_test)
pred1=rf.predict(x_train)
#print(pred)
ac=rf.score(x_train,y_train)
ac1=rf.score(x_test,y_test)
#print("Accuracy of the Training Data :-",ac)
#print("Accuracy of the Testing Data ;-",ac1)

print("\n\nRandom_Forest_regressor Model_1\n")
print("Accuracy of training data with the r2_score :-",r2_score(y_train,pred1))
print("Accuracy of the testin data with the r2_score ;-",r2_score(y_test,pred))
print("mean_squared_error",mean_squared_error(y_test,pred))

#*********************************************************************************


#***********************************************************************************
# Adaboost regression model - 2
#------------------------------------------
ada=AdaBoostRegressor()
fits1=ada.fit(x_train,y_train)
preds=ada.predict(x_test)
preds1=ada.predict(x_train)
#print(preds)
acc=ada.score(x_train,y_train)
acc1=ada.score(x_test,y_test)
#print("Accuracy of the Training Data :-",acc)
#print("Accuracy of the Testing Data ;-",acc1)

print("\nAda_boost_regressor Model_2")
print("Accuracy of training data with the r2_score :-",r2_score(y_train,preds1))
print("Accuracy of the testin data with the r2_score ;-",r2_score(y_test,preds))
print("mean_squared_error",mean_squared_error(y_test,pred))

#*******************************************************************************************

#*****************************************************************************************************
# Gradient Boosting REgression model - 3
#-------------------------------------------------------------------
grd=GradientBoostingRegressor()
fits2=grd.fit(x_train,y_train)
pred3=grd.predict(x_test)
pred4=grd.predict(x_train)
ac3=grd.score(x_train,y_train)
ac4=grd.score(x_test,y_test)

#print("Accuracy of the Training Data :-",ac3)
#print("Accuracy of the Testing Data ;-",ac4)
print("\nGradient_Boosting_regressor Model_3")
print("Accuracy of training data with the r2_score :-",r2_score(y_train,pred4))
print("Accuracy of the testin data with the r2_score ;-",r2_score(y_test,pred3))
print("mean_squared_error",mean_squared_error(y_test,pred3))

#***********************************************************************************************
# Decision Tree regressor
#-----------------------------------------------------------------
from sklearn.tree import DecisionTreeRegressor
dt=DecisionTreeRegressor()
fi=dt.fit(x_train,y_train)
pr=dt.predict(x_test)
pr1=dt.predict(x_train)
print("\nDecision Tree Regression model_4")
print("Accuracy of Training data :-",r2_score(y_train,pr1))
print("Accuracy of Testing data :-",r2_score(y_test,pr))

'''

#----------------------------------------------------------------------------------------------------------------------------
#  Date 05-01-2023
#----------------------------------------------------------------------------------------------------------------------------
# xgboost Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pylab
from scipy import stats as st
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,StandardScaler
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import confusion_matrix,classification_report,r2_score,mean_squared_error
from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB,MultinomialNB
from sklearn.svm import SVC
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor,AdaBoostClassifier
from sklearn.ensemble import GradientBoostingRegressor,GradientBoostingClassifier
from xgboost import XGBClassifier,XGBRegressor
from catboost import CatBoostRegressor,CatBoostClassifier
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Ridge,Lasso,RidgeCV,LassoCV
from sklearn.linear_model import LogisticRegressionCV

'''a="C:/Users/Prince kumar/OneDrive/Desktop/mldataset/home/test.csv"
b="C:/Users/Prince kumar/OneDrive/Desktop/mldataset/home/train.csv"
tr=pd.read_csv(b)
te=pd.read_csv(a)
#print(tr.shape)
#print(te.shape)
#print(tr.isna().sum())
#print(te.isna().sum())

df=pd.concat([tr,te])
#print(df.shape)
a=df.isna().sum()
b=df.isna().sum()/df.shape[0]

df.drop(columns=["MiscFeature","Fence","PoolQC","Alley","FireplaceQu"],inplace=True)
#print(df.shape)
#print(df.describe())
cor=df.corr()
#rint(cor)
#print(df.columns)
#print(cor.index)
#print(df.info())
#print(df.isna().sum())

for i in df:
	if df[i].isna().any():
		if df[i].dtype==float:
			if df[i].median()-df[i].mean()>10:
				df[i].fillna(df[i].median(),inplace=True)
			elif i=="SalePrice":
				continue
			else:
				df[i].fillna(df[i].mean(),inplace=True)
		elif df[i].dtype==object:
			df[i].fillna(df[i].mode()[0],inplace=True)
#print(df.isna().sum())
#print(df.isna().sum().sum())
#print(df.info())
ln=LabelEncoder()
for i in df:
	if df[i].dtype==object:
		df[i]=ln.fit_transform(df[i])

#print(df.info())
df.drop(columns=["Id"],inplace=True)
#print(df.columns)
#print(df.nunique())

df_test=df[df["SalePrice"].isna()]
df_train=df[df["SalePrice"].isna()==False]
df_test.drop(["SalePrice"],axis=1,inplace=True)
#print(df_test)
#print(df_train)

#print("\nTesting data\n\n",df_test.isna().sum())
#print("\n\nTraining Data\n\n",df_train.isna().sum())

x=df_train.drop(columns=["SalePrice"])
#print(x.info())
y=df_train[["SalePrice"]]
#print(y)

sc=StandardScaler()
x1=sc.fit_transform(x)
#print(x1.shape)
x_train,x_test,y_train,y_test=train_test_split(x1,y,test_size=0.2,random_state=45)
#print(x_train.shape)
knn=KNeighborsRegressor(n_neighbors=7)
knn.fit(x_train,y_train)
ac=knn.score(x_train,y_train)
ac2=knn.score(x_test,y_test)
#print(ac2)
pred=knn.predict(df_test)#.reset_index()
df_test["SalePrice"]=pred
#print(df_test)
#print(r2_score(y_test,pred))
#print(knn.score(x_test,y_test))


#11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
nb=GaussianNB()
nb.fit(x_train,y_train)
ac3=nb.score(x_train,y_train)
ac4=nb.score(x_test,y_test)
p=r2_score(y_test,nb.predict(x_test))
#print(ac3)
#print(ac4)
#print(p)


#111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
sv=SVC(kernel="rbf")
sv.fit(x_train,y_train)

ac5=sv.score(x_train,y_train)
ac6=sv.score(x_test,y_test)
print(ac5)
print(ac6)
'''

#Hyperperameter tuning IN svc algorithms























































































'''
alphas = np.random.uniform(low=0, high=10, size=(50,))
ridgecv = RidgeCV(alphas =alphas,cv=10,normalize = True)
ridgecv.fit(x_train, y_train)
ridgecv.alpha_
ridge_model = Ridge(alpha=ridgecv.alpha_)
ridge_model.fit(x_train, y_train)'''



























