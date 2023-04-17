
'''
what is pandas?
pandas instruction
pandas is a python library used for working with data sets.
it has fuctions for analyzing, cleaning,cleaning exploring,and manuplating data.

the name pandas has a reference to both "panel data", and "python data analysis"
and it was created by wes Mckinney in 2008.

why use pandas?
pandas allow us to anayze big data and make conclusion based on statistical theoies.

pandas series?
what is a series?
A pandas series like a column in a table.
it is a one -dimentional array holding off any type .

series is  a one dimentional labled array capable of holding anyy data type
'''

import pandas as pd
'''x=pd.Series([12,45,78,9,56,23])
print(x)
print(type(x))
print(len(x))'''

'''x=pd.Series(["a","b","c","d","e","f"])
print(x)
print(len(x))'''

'''x=pd.Series(["Prince","kumar","Sharma"])
print(x)'''


'''x=pd.Series([12,45,12.1,15.4,"prince","kumar",21j,True,False])
print(x)
print(type(x))
print(len(x))
print(x.size)
print(x.shape)
print(x.ndim)'''


import numpy as np
import pandas as pd

'''x=pd.Series(["a","b","c","d","e","f"])
print(x[3])
'''
#how can be create labels
#with the index argument, you can name your own labels.
'''x=pd.Series([1,2,3,4,5,6], index=["a","b","c","d","e","f"])
print(x)'''

'''x=pd.Series(["prince","kumar",23,45],index=["A","B","C","D"])
print(x)'''


'''print(x["b":"d"])
print(x[1:4])
print(x[-6])
print(x[0])'''

'''x=pd.Series([12,45,78,89,56,23])
print(x[0:3])

x=pd.Series(np.random.randint(5),index=["a","b","c","d","e"])
print(x)'''

#x=pd.Series(np.random.randint(100,1000,5),index=["a","b","c","d","e"])
#print(x)


'''x=pd.Series({"prince":25,"ankit":56,"anshu":58})
print(x)
print(x.index)
print(x.values)'''


'''x=pd.Series({"Name":"prince","Roll no":45,"class":"10th"})
print(x)
print(x.index)
print(x.values)

x=pd.Series((12,56,89,47,58,10),index=("a","b","c","d","e","f"))
print(x)'''

#Basic airthmetic operation


'''x=pd.Series([12,56,89,47,58,10])
y=pd.Series([12,56,89,47,58,10])
print("Addition")
print(x+y)
print("subtract")
print(x-y)
print("multiplication")
print(x*y)
print("Divide")
print(x/y)
print("Floor divison")
print(x//y)'''


'''x=pd.Series([12,56,89,47,58,10])
print("Addition")
print(x+5)
print("subtract")
print(x-10)
print("multiplication")
print(x*2)
print("Divide")
print(x/2)
print("Floor divison")
print(x//5)
print("exponent\n",x**2)




print(20**32)
print(30**78)'''

'''Pandas DataFrame
A data frame is a 2 dimentional labled data structure, like a 2 dimentional array,
or pandas with row and columns.'''

'''x=pd.DataFrame({"name":["prince","ankit","mannu","kumod"],"marks":[45,78,56,58]})
print(x)
print(type(x))
print(x.index)
print(len(x))'''

'''
x=pd.DataFrame({"Name":["prince","ankit","mohan","raju"],"marks":[48,15,26,48]},index=["a","b","c","d"])
print(x)



x=pd.DataFrame({"Name":["prince","ankit","mohan","raju"],"marks":[48,15,26,48]},index=["a","b","c","d"])
print(x)'''


'''fruits=pd.DataFrame({"Fruits":["Apple","Banana","Mango"],"price":[45,56,62],
	"Quality":["good","better","best"]},index=[1,2,3])
print(fruits)'''
#how can change sequence of column

'''fruits=pd.DataFrame({"Fruits":["Apple","Banana","Mango"],"price":[45,56,62],
	"Quality":["good","better","best"]},index=[1,2,3],columns=["price","Quality","Fruits"])
print(fruits)'''

#three column and 8 rows

'''x=pd.DataFrame({"num":[1,2,3,4,5,6,7,8],"roman":["i","ii","iii","iv","v","vi","vii","viii"],
	"in_eng":["one","two","three","four","five","six","seven","eight"]},index=["a","b","c","d","e","f","g","h"])
print(x)'''

'''x={"fruits":["Apple","Banana","orange"],
"animals":["Dog","horse","cow"],
"birds":["crow","parrot","peacock"]}

y=pd.DataFrame(x,index=["A","B","C"],columns=["birds","fruits","animals"])
print(y)'''

#**********************************************************************************************************************************************************
#	Date 31-08-2022
#**********************************************************************************************************************************************************
import pandas as pd
import numpy as np
#cncate 
#append
'''
x=pd.DataFrame({"Name":["kajal","ritu","priya"],"Marks":[78,56,92]},index=[1,2,3])
y=pd.DataFrame({"Name":["ankit","mohan","priyanshu"],"Marks":[98,86,52]},index=[1,2,3])
z=(x,y)
w=pd.concat(z)
print(w)'''

'''
x=pd.DataFrame({"Name_1":["kajal","ritu","priya"],"Marks":[78,56,92]},index=[1,2,3])
y=pd.DataFrame({"Name":["ankit","mohan","priyanshu"],"Marks":[98,86,52]},index=[1,2,3])
z=x.append(y)
print(z)'''

#inner merge
'''
x=pd.DataFrame({"Name_1":["Ashish","Arvind","Sahil","Deepak","Nikhil","Abhishek","rahul","nikkhil"],"math":[99,98,87,97,67,95,25,48]})
y=pd.DataFrame({"Name_2":["Ashish","tejaswi","omkar","nikhil","Abhishek","rahul","ranjeet"],"Marks":[78,45,59,26,18,89,59]})
z=pd.merge(left=x, right=y, how="inner",left_on="Name_1",right_on="Name_2",indicator=True)
print(z)'''


#outer merge
'''x=pd.DataFrame({"Name_1":["Ashish","Arvind","Sahil","Deepak","Nikhil","Abhishek","rahul","nikkhil"],"math":[99,98,87,97,67,95,25,48]})
y=pd.DataFrame({"Name_2":["Ashish","tejaswi","omkar","nikhil","Abhishek","rahul","ranjeet"],"Marks":[78,45,59,26,18,89,59]})
z=pd.merge(left=x,right=y,how="outer",left_on="Name_1",right_on="Name_2",indicator=True)
print(z)'''

#left merge
'''x=pd.DataFrame({"Name_1":["Ashish","Arvind","Sahil","Deepak","Nikhil","Abhishek","rahul","nikkhil"],"math":[99,98,87,97,67,95,25,48]})
y=pd.DataFrame({"Name_2":["Ashish","tejaswi","omkar","nikhil","Abhishek","rahul","ranjeet"],"Marks":[78,45,59,26,18,89,59]})
z=pd.merge(left=x,right=y,how="left",left_on="Name_1",right_on="Name_2",indicator=True)
print(z)'''

#right merge
'''x=pd.DataFrame({"Name_1":["Ashish","Arvind","Sahil","Deepak","Nikhil","Abhishek","rahul","nikkhil"],"math":[99,98,87,97,67,95,25,48]})
y=pd.DataFrame({"Name_2":["Ashish","tejaswi","omkar","nikhil","Abhishek","rahul","ranjeet"],"Marks":[78,45,59,26,18,89,59]})
z=pd.merge(left=x,right=y,how="outer",left_on="Name_1",right_on="Name_2",indicator=True)
print(z)'''


#string method method in pandas
#convert string in the series \index to lower case.


#use str.lower() method =>
# this method is used to do small letter of all words.
'''
x=pd.Series(["Ashish","prince","kumod","ankit","avishek"])
#print(x)
print(x.str.lower())''' 



#use str.upper() method => 
#this method is used to do capital letter letter of all words.

'''x=pd.Series(["prince","kumar","saharma","ankit","kumod"])
print(x.str.upper())'''



#use of str.title() method => 
#with the hwlp of these method we can do first word of letter do dcapital like (proper name) 

'''x=pd.Series(["prince","kumar","saharma","ankit","kumod"])
print(x.str.title())'''


#use of str.len() method =>
# with the help of these method we can find the lenth of every name of in series.

'''x=pd.Series(["prince","kumar","saharma","ankit","kumod"])
print(x.str.len())'''



#use of str.split() method => 
#with the help of these method we can do seperate in a list per name charactor

'''x=pd.Series(["prince","kumar","saharma","ankit","kumod"])
print(x.str.split())'''


#use of cat(sep="pattern") => 
#with the help of these method we can print in horizontally with place of comma in replace (**) like this .

'''x=pd.Series(["prince","kumar","saharma","ankit","kumod"])
print(x.str.cat(sep="**"))'''


#use of contain method=>
# with the help of these method we can print boolen value 
#the value we find in method that value present in name then it will show true else print false.

'''x=pd.Series(["prince","kumar","saharma","ankit","kumod","priya","priyanshu"])
print(x.str.contains('ri'))'''

'''x=pd.Series(["prince","kumar","shrama","kumod","ankit"])
print(x.str.contains("ku"))'''


#use of replace method =>
# with the help of these method we can replacce the value by me as you want before the place of new value

'''x=pd.Series(["prince","kumar","saharma","ankit","kumod"])
print(x.str.replace("p","**"))'''


#use of reapet method method =>
#with the help of these method we can repeat the all name many time by me 
'''x=pd.Series(["Avishek ","Annu ","arnnav "])
print(x.str.repeat(3))
'''
#***********************************************************************************************************************
#	Date 01-09-2022		1st september 2022
#***********************************************************************************************************************

#count() it use the count the specified strings by user.

'''x=pd.Series(["prince","kumar","shrama"])
print(x.str.count("a"))

x=pd.Series(["annu","anmol","asha","anju"])
print(x.str.count("a"))'''

#startswith() method
'''
x=pd.Series(["prince","kumar","sahrma","priya","priyanshu"])
print(x.str.startswith("p"))
print(x.str.startswith("k"))'''

'''x=pd.Series(["prince","kumar","sahrma","priya","priyanshu"])
print(x.str.endswith("e"))'''

#find() method
'''x=pd.Series(["Annu","aramAn","prince","kumar"])
print(x.str.find("A"))'''

#x=pd.Series(["Annu","aramAn","prince","kumar"])
#print(x.str.swapcase())

#x=pd.Series(["pRINCE","kUMAR","sHARMA"])
#print(x.str.swapcase())

#Drop Duplicate
#drop_duplicate()
#x=pd.DataFrame({"Fruits":["apple","mango","apple","banana","lichi"],"cost":[45,85,45,96,82]})
#print(x.drop_duplicates())

'''x=pd.DataFrame({"Fruits":["apple","mango","apple","banana","lichi"],"cost":[45,85,45,96,82]})
 y=pd.DataFrame()
 #print(y)
 print(y.drop_duplicates())''' 



 #Group and aggrigate mathod
#x.groupby("company")
'''x=pd.DataFrame({"company":["google","google","yahoo","yahoo","Amazon","Amazon"],"person":["prince","ankit","rishu","aman","ankita","suraj"],"Sales_in_india":[456,123,200,258,400,600]})
y=x.groupby("company")

#Now using aggrigate method
print(y.sum())
print(y.std())
print(y.mean())
print(y.count())
print(y.describe())
print(y.describe().transpose()) 	# it will change the position of data frame row to column and column to row
print(y.describe(),["Amazon"])		# 
'''

'''create a data DadtaFrame first column should be product and group this data frame according to product,
second column should be company name and third column should be cost apply all methods on this data frame.
s um,mean,min,count,describe,change the postion of row and column.
'''
'''x=pd.DataFrame({"product":["leptop","leptop","mobile","mobile","cpu","cpu"],"company":["dlf","mri","agi","ghf","jkl","ekj"],
	"price":[200,500,320,400,250,257]})
#print(x)
y=x.groupby("product")

#now adding aggrigate
print("sum")
print(y.sum())


print("mean")
print(y.mean())


print("min")
print(y.min())


print(y.count())
print(y.describe())


print("\n  Transpose of dataframe")
print(y.describe().T)

print(y.describe().T["leptop"])'''

#************************************************************************************************************
# ****************************  		     date 06-09-2022		    *************************************
#************************************************************************************************************
import pandas as pd
#merge
'''
x=pd.DataFrame({"name":["prince","kumar","sharma","priya"],"roll":[1,2,3,4]})
y=pd.DataFrame({"name2":["priyanshu","kumar","sharma","pappu"],"roll":[5,2,3,6]})


z=pd.merge(left=x,right=y,how="inner",left_on="name",right_on="name2",indicator=True)
print(z)'''
   
#*************Data set********************
#x=pd.read_csv("iris.csv")
#print(x)
#rint(x.shape)
#print(x.head()) # its return starting of 5 row and column
#print(x.tail())	#its return bottum of 5 row and column
#print(x.head(15))#its return starting of 15 row and column
#print(x.tail(20))#its return last of 20 row and column



#use of x.iloc[row range,column range] method
#with the help of these method we can print specified row and column by user

#print(x.iloc[1:15,0:6])


#use of x.loc[row range,column name] method

#with the help of these method we can print specified row by giving range
#and column by column name

#print(x.loc[1:10,("SepalWidthCm","Species")])

#Apply some aggrigaate function

'''x=pd.read_csv("iris.csv")
print(x)

#now applying aggrigate method
print(x.sum())
print(x.min())
print(x.max())
print(x.mean())
print(x.describe())
print(x.count())
print(x.std())'''


#use of to_csv("enter file name") method 
#with the help of these method we can save data in specified excel file by user

'''x=pd.DataFrame({"name":["prince","kumar","sharma","priya"],"roll":[1,2,3,4]})
x.to_csv("pppp.csv")'''

'''
x=pd.read_csv("chhotu.csv")
print(x)'''

#*******************************************************************************************
#	07-09-2022
#************************************************************************************


'''x=pd.DataFrame({"Name":["prince","Anmol","rahul","mayank"],"Marks":[45,78,89,56]})
x.to_csv("prince.csv")'''


#x=pd.read_csv("dataone.csv")
#print(x)
#x.dropna(inplace=True)
#print(x)
#y=x.dropna() its remove the null values
#print(y)

#x.fillna("prince",inplace=True) #its replace in original file

#y=x.fillna("prince")	# its replace in duplicate file
#print(y) 	#replaace the place of non vallue

#x["Calories"].fillna(123567,inplace=True)	#its replace in calories column in nun cells in original dataset.
#print(x)

#y=x["Calories"].fillna(123456) 	#it will replace in clories column at the place of null cells
#print(y)

#y=x["Date"].fillna(456789)
#print(y)

#if i want to print two column only then yse loc method 
#z=x.loc[0:,("Date","Calories")]
#print(z.fillna(4567899))

#print(x)
#z=x.dropna()
#z=x.fillna(1)


#clean the date formating date with the help of to.datetime() methods.

#z["Date"]=pd.to_datetime(z["Date"])
#print(z)

#when you want to change only one cell then use this loc method.
#z=x
#z.loc[7,"Duration"]=980
#print(z)

#******************************************************************************************************************************************************
#	08-09-2022
#**************************************************************************************************************************************************************

import pandas as pd
'''x=pd.DataFrame({"foo":["one","one","one","two","two","two"],
	"bar":["A","B","C","A","B","C"],
	"baz":[1,2,3,4,5,6],
	"zoo":["x","y","z","q","w","t"]})
#print(x)

y=x.pivot(index="foo",columns="bar",values="baz")
print(y)'''

'''
x=pd.DataFrame({"foo":["one","one","one","two","two","two"],
	"bar":["A","B","C","A","B","C"],
	"baz":[1,2,3,4,5,6],
	"zoo":["x","y","z","q","w","t"]})
#print(x)

y=x.pivot(index="foo",columns="bar",values="baz")
print(y)

print("\n2nd pivot\n")
z=x.pivot(index="foo",columns="bar")["baz"]
print(z)

print("\n3rd pivot\n")
m=x.pivot(index="foo",columns="bar",values=["baz","zoo"])
print(m)
'''
'''
a={'emp':["prince","prince","chhotu","chhotu"],"month":["Jan","Feb","Jan","Feb"],"profit":[456,123,789,159],"loss":[120,100,500,250]}
x=pd.DataFrame(a)
y=x.pivot(index="emp",columns="month",values=["profit","loss"])
print(y)'''

'''
a={'emp':["prince","prince","chhotu","chhotu"],"month":["Jan","Feb","Jan","Feb"],"profit":[4560,1230,789,159],"loss":[1201,1001,500,250]}
x=pd.DataFrame(a)
y=x.pivot(index="emp",columns="month",values=["profit","loss"])'''
#print(y)

#print(y.sum())
#print(y.describe())


#for output in excel
#   g=y.describe()
#g.to_csv("pk.csv")


#for pivot in excel in excel
#y.to_csv("pk.csv")





'''
import time
for i in range(30,-1,-1):
	print(i,end="\r")
	time.sleep(1)'''
	
'''
s={"company":["google","google","google","HCL","HCL","HCL","ACC","ACC","ACC"],
"Month":["January","February","March","January","February","March","January","February","March",],
"Employee":["prince","prince","prince","Ankit","Ankit","Ankit","anuj","anuj","anuj"],
"Salary":[12000,12000,12000,12000,12000,12000,8000,56400,45600],
"Bonus":[800,400,600,2000,400,500,456,789,800]}
x=pd.DataFrame(s)
#print(x)
y=x.pivot(index=["company"],columns=["Month","Employee"],values=["Salary","Bonus"])
print(y)
y.to_csv("pk.csv")
print("Done")'''


#***************************************************************************************************************************
#	Date 12-09-2022
#************************************************************************************************************************************

'''x=pd.DataFrame({"Fruits":["apple","mango","banana","lichi"],"Animals":["Tiger","lion","Dog","camel"]})
#print(x)
x.to_excel("hii.xlsx")
print("Done")'''


#-------------------------------------------------------------------------------------------------
#		Note :- pip install openpyxl 
#-------------------------------------------------------------------------------------------------


#a=pd.read_excel("hii.xlsx")
#print(a)
'''
with pd.ExcelWriter("hii.xlsx") as f:
	x=pd.DataFrame({"student":["prince","ankit","anshu","aman"],"marks":[45,89,45,56]})
	x.to_excel(f,sheet_name="prince")
	y=pd.DataFrame({"Fruits":["apple","mango","banana","lichi"],"Animals":["Tiger","lion","Dog","camel"]})
	y.to_excel(f,sheet_name="chhotu")
	z=pd.DataFrame({"company":["google","linux","hcl","ixcenture"],"staff":[78,45,89,56]})
	z.to_excel(f,sheet_name="company")
	print("Done")'''
	
	



#x=pd.DataFrame({"student":["prince","ankit","anshu","aman"],"marks":[45,89,45,56]})
#x.to_excel("css.xlsx",index=False)
#y=pd.read_excel("css.xlsx")
#print(y)


#x=pd.read("")
#y=x.drop()

#*************************************************************************************
x=pd.read_csv("dataone.csv")
#print(x)

#print first 5 rows
#print(x.head())

#print last 0f 5 rows
#print(x.tail())

#y=x.iloc[20:30,0:]
#print(y)

#z=x.drop(["Date","Calories"],axis=1)
#print(z)

#find one columns and 14 rows 
#a=x.iloc[0:14,0]
#print(a)

#delete the row 12,34,20 row of this data set
#j=x.dropna()
'''print(j)
print(j.shape)
b=j.drop([5,2],axis=0)
print(b)
print(b.shape)'''

#find the min max mean count caluculate all value
'''print(j.min())
print(j.max())
print(j.mean())
print(j.count())
print(j.describe())'''

'''
with pd.ExcelWriter("prince.xlsx") as f:
	k=j.min()
	k.to_excel(f,sheet_name="min")
	l=j.max()
	l.to_excel(f,sheet_name="max")
	m=j.describe()
	m.to_excel(f,sheet_name="describe")
	n=j.sort_values(by="Pulse")
	n.to_excel(f,sheet_name="short")
	print("Done")'''


'''
Create aa program to amake aa dataframe for student performance, 4 school should be there and  take student as per yourrequirment.
and present the performance of the school. Do groupby this DataFrame according to school and make some sheet on xecel and perform 
all aggrigate function.'''
'''
a={"School":["kjp school","kjp school","kjp school","kjp school","Cambridge English academy","Cambridge English academy","Cambridge English academy","Cambridge English academy","St paul public school","St paul public school","St paul public school","St paul public school","Rainbow school","Rainbow school","Rainbow school","Rainbow school"],
"Student_Name":["Ankit kumar","Aman kumar","Anmol kumar","rani shrama","bhavya sharma","ajit kumar","ram kumar","stuti kumari","rahul sharma","suraj kumar","vandna kumari","Sunaina sharma","Prince kumar","saurav kumar","Raunak raj","Amrit raj"],
"Marks":[78,75,71,76,75,85,95,84,93,51,62,58,47,69,94,77]}
x=pd.DataFrame(a)
#print(x)
y=x.groupby("School")
#print(y.count())
#print(y.min())
with pd.ExcelWriter("school_data.xlsx") as f:
	j=y.min()
	j.to_excel(f,sheet_name="minimum_value")

	k=y.max()
	k.to_excel(f,sheet_name="maximum_value")

	l=y.count()
	l.to_excel(f,sheet_name="count_st")

	m=y.mean()
	m.to_excel(f,sheet_name="average_marks")

	n=y.describe()
	n.to_excel(f,sheet_name="all_details")

	o=y.describe().T["kjp school"]
	o.to_excel(f,sheet_name="kjp")

	print("Done")
'''


 #Apply group by on this data set and do groupby by with "season" columns, and apply aggrigate function
 #and make some sheets on excel and show all performance on each sheet.extract the numrical value.
'''
x=pd.read_csv("matches.csv")
#print(x)
a=x.loc[0:,("Season","id","win_by_runs","win_by_wickets")]
#print(a)
y=a.groupby("Season")
print(y.count())
print(y.min())
print(y.max())
print(y.mean())
print(y.sum())
print(y.describe())'''




'''
df=pd.DataFrame({"Name":["Avery","Jas","John","hunter","Jonas","Amir","Mickey","Kelly","Terry","marcus"],
	"Age":[25,25,27,22,29,29,21,25,22,22],"Height":[6.2,6.6,6.5,6.5,6.10,6.9,6.8,7.0,6.2,6.4],
	"Weight":[180,235,205,185,231,240,235,238,190,220]})
#print(df)

x=df.sort_values(by="Weight",ascending=0)  		#show in descending order if put 1 then it will show in ascending order
print("\n#.5 Rows which have largest weight !\n")
print(x.head())


y=df.sort_values(by="Name",ascending=1)
print("\n#2. 3 name which are elder in the data frame by the Alphabetical range !\n ")
print(y.iloc[0:3,0:])'''


#t=df.nlargest(5,["Weight"])
#print(t)

'''
x=pd.DataFrame({"Name":["prince","kumar","Sharma"],"Marks":[78,89,56,]})

y=DataFrame(x)
y.insert(0,"school":["hii","byy","gui"])

print(y)'''


#create three sheets on the excel and extract first to  15 rows  from this data set and show on first sheet extract 20 row 
#from mid and show in the second sheet extract two collumn and 30 row and show it.
'''
x=pd.read_csv("titanic.csv")
print(x)

with pd.ExcelWriter("titanic1.xlsx") as f:
	a=x.head(15)
	a.to_excel(f,sheet_name="15_pasanger")

	b=x.iloc[15:31,0:]
	b.to_excel(f,sheet_name="mid_30_passenger")

	c=x.iloc[1:31,2:4]
	c.to_excel(f,sheet_name="2column")

	print("Done")'''
'''
x=pd.DataFrame({"saving":np.random.randint(100,200,10),"Current":np.random.randint(150,300,10)})
#print(x)
deposit=[100,2000,3000,4000,50000,60000,7000,8000,9000,12000]
#print(pd.concat((x,y)))
#z=pd.merge(left=x,right=y,left_on="saving",right_on="Deposit")
x["Deposit"]=deposit
print(x)'''

'''
x=pd.DataFrame({"Name_1":["Ashish","Arvind","Sahil","Deepak","Nikhil","Abhishek","rahul","nikkhil"],"math":[99,98,87,97,67,95,25,48]})
y=pd.DataFrame({"Name_2":["Ashish","tejaswi","omkar","nikhil","Abhishek","rahul","ranjeet"],"Marks":[78,45,59,26,18,89,59]})
z=pd.merge(left=x,right=y,how="outer",left_on="Name_1",right_on="Name_2",indicator=True)
print(z)'''

#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

'''x=pd.date_range("20220825",periods=10)
print(x)

x=np.random.randn(10,4)
print(x)

#x=pd.DataFrame(np.random.randn(10,4),index=[1,2,3,4,5,6,7,8,9,10],columns=["A","B","C","D"])
#print(x)
 
x=pd.DataFrame({"A":[1,2,3,4],
	"B":pd.Timestamp("20220510"),
	"C":pd.Series(1,index=list(range(4)),dtype=int),
	"D":np.array([5]*4,dtype=int),
	"E":"prince"})
'''
#print(x)
#y=x.to_numpy()
#print(y) 	# its convert the dataframe into numpy matrix

#y=x[0:4]
#print(y)

#x=pd.DataFrame(np.random.randint(20,100,50).reshape(10,5),columns=["First","Second","Third","Forth","Fifth"])
#print(x)

#print("\nGreater then 50 number of data frame\n")

#y=x[x["First"]<40]  # find the value less then 40
#print(y)

#z=x.loc[x["Second"]<50]	#find the value less then 50 
#print(z)

#z=x[(x>50)&(x<60)]  #we can find the between value in table
#print(z)


'''x=pd.DataFrame({"Date":pd.date_range("20220810",periods=10),
	"Deposit":np.random.randint(8000,15000,10),
	"Credit":np.random.randint(10000,20000,10),
	"Name":"prince"},index=["A","B","C","D","E","F","G","H","I","J"],columns=["Date","Name","Credit","Deposit"])
#x.index=[1,2,3,4,5,6,7,8,9,10]
print(x)
print("\nAfter Putting Few Statement \n")'''

#y=x[x["Deposit"]>10000] #show the value less then 
#print(y)

#y=x.loc[x["Credit"]<15000]		 # Show the value less then with loc method.
#print(y)

#y=x.iloc[0:,2:]<15000 			 #it will show boolen value in true or false.
#print(y)

#y=x.loc[(x["Credit"]>12000)&(x["Credit"]<15000)] 		#It will show between of the value with the help of loc method 
#print(y)

#y=x.loc[(x["Deposit"]>10000)&(x["Deposit"]<12000)]
#print(y)

#y=x[(x["Deposit"]>12000) & (x["Deposit"]<15000)]		#it show between value without methods.
#print(y)






'''
x=pd.DataFrame({"Date":pd.date_range("20220810",periods=10),
	"Withdrawl":np.random.randint(8000,15000,10),
	"Credit":np.random.randint(10000,20000,10),
	"Name":"prince"},index=["A","B","C","D","E","F","G","H","I","J"],
	columns=["Date","Name","Credit","Withdrawl"])
#x.index=[1,2,3,4,5,6,7,8,9,10]
print(x)

print("\nAfter Putting Few Statement \n")

z=x["Credit"]-x["Withdrawl"]
x["Saving"]=z
print(x)'''


'''
d=[]

marksheet=pd.DataFrame({"Result_Date":pd.Timestamp("2022-08-25"),
	"Students_Name":["Prince kumar","Amit kumar","Suraj kumar","Raman kumar","Ankit kumar"],
	"Roll_No":[4,3,5,1,2],"Marks":[380,330,255,290,401]})
#print(marksheet)

per=marksheet["Marks"]/500*100
#marksheet["Persantage"]=per
#			OR
marksheet.insert(4,"Persentage",per)
#print(marksheet)
m=marksheet["Persentage"]
for i in m:
	if i<50:
		div="Third Div"
	elif i<60:
		div="Second Div"
	else:
		div="First Div"
	#print(div)
	d.append(div)
#print(d)
marksheet["Divison"]=d
#print(marksheet)

y=marksheet.sort_values(by="Roll_No",ignore_index=True)
#			OR
#y=marksheet.nlargest(5,["Roll_No"])
print(y) '''


'''x=pd.DataFrame({"A":[5,6,8,5,10],"B":[9,4,6,10,7],"C":[24,16,20,18,9]})
print(x)
print("numpy")
y=x.to_numpy()
print(y)'''