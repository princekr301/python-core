
import numpy as np
import pandas as pd

'''x=pd.Series([12,45,78,"prince"],index=["A","B","C","D"])
print(x)'''


'''x=pd.DataFrame((np.random.randint(10,20,15)))#index=["a","b","c","d","e"])
print(x)'''

'''x=pd.DataFrame({"Animals":[1,2,3,4,5],"Wild Animals":["Lion","Tiger","Elephant","fox","Bear"],"Domestic Animals":["Cow","Bufellow","Goat","Dog","Cat"]
	,"Insects":["bee","Butterfly","Honey bee","Mosquito","--"],"V.small Animals":["snake","lizard","rat","ant","--"]},index=['A','B','C','D','E'])
print(x)'''
'''
m={"Animals":["monkey","lapord","chimpanjee","deer","kangaroo","vultchure","fox","muel","----","----","-----","Lion",],
"Birds" :["parrot","cuckoo","crow","pigen","swan","bulbul","duck","eggle","Hen","peacock","cock","Sparrow"],
"Insects":["bee","Butterfly","Mosquito","Dragonfly","tellow jacket","Ant","spider","Lady bug","snail","----","---","fish"],
"Fruits":["Appple","Banana","Orange","Mango","Plum","Cherry","Lichi","Coconut","Gauva","Lemon","Pine Appple","Pomegranet"]
}

x=pd.DataFrame(m,columns=("Fruits","Birds","Insects","Animals"))
print(x)
print(type(x))'''



import pandas as pd

'''calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)'''

'''x={"color":["Red","Orange","Purple","Megenta","green"],
"rang":["Lal","pila","nila","hara","nika"],
"action":["low","high","normal","level","good"]}

a=pd.DataFrame(x,index=["i","ii","iii","iv","v"],columns=["action","color","rang"])
print(a)'''

'''
marksheet={"prince":{"hnd":45,"math":89,"eng":58,"sst":86,"sc":63},
"ankit":{"hnd":35,"math":69,"eng":98,"sst":44,"sc":52},
"rani":{"hnd":45,"math":89,"eng":58,"sst":86,"sc":56},
"priyanshu":{"hnd":78,"math":78,"eng":88,"sst":98,"sc":83},
"priya":{"hnd":78,"math":78,"eng":88,"sst":98,"sc":83},}

x=pd.DataFrame(marksheet)
print(x)'''

'''x={"fruits":45,"mango":78,"agras":58}
y=pd.Series(x)
print(y)'''

'''x=pd.Series(np.random.randint(10,20,15))
print(x)'''
'''
x=pd.DataFrame([12,56,89,47,58,10])
y=pd.DataFrame([12,56,89,47,58,10])
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
#***********************************************************************************************************************************************
#	Data 	31-08-2022
#***********************************************************************************************************************************************
import pandas as pd
import numpy as np

#use of concat((x,y)) methods =>
#with the help of this method we can join the two pandas series.
'''x=pd.DataFrame({"Name":["prince","Ankit","Manu"],"Marks":[78,79,77]},index=["A","B","C"])
y=pd.DataFrame({"Name":["Anmol","Priya","Bhanu","Mohan","prince"],"Marks":[49,48,74,84,99]},index=["D","E","F","G","H"])
#z=(x,y)
#print(pd.concat(z))
print(pd.concat((x,y)))'''

'''x=pd.DataFrame({"Name":["prince","Ankit","Manu"],"Marks":[78,79,77]})#,index=["A","B","C"])
y=pd.DataFrame({"Name":["Anmol","Priya","Bhanu","Mohan","prince"],"Marks":[49,48,74,84,99]})#,index=["D","E","F","G","H"])
z=pd.DataFrame({"Name":["Mamta","Gunjan","Bhavna"],"Marks":[93,82,71]})#,index=["I","J","K"])
a=(x,y,z)
print(pd.concat(a))'''

'''x=pd.DataFrame({"name":["prince","kumar"],"marks":[89,78]},index=[1,2])
y=pd.DataFrame({"name1":["anshu","jyoti","deepa"],"marks1":[78,63,64]},index=[3,4,5])
z=(x,y)
print(pd.concat(z))'''


#use x.append(y) methods => with the help of this method wee can add new DataFrame at the last of index
'''x=pd.DataFrame({"Name":["prince","Ankit","Manu"],"Marks":[78,79,77]},index=["A","B","C"])
y=pd.DataFrame({"Name":["Anmol","Priya","Bhanu"],"Marks":[49,48,74]},index=["D","E","F"])
a=x.append(y)
print(y)'''

'''x=pd.DataFrame({"Name_1":["prince","Ankit","Manu","Priya"],"Marks":[78,79,77,58]},index=["A","B","C","D"])
y=pd.DataFrame({"Name_2":["Anmol","Priya","Bhanu","prince","Manu"],"Marks":[49,48,74,82,93]},index=["E","F","G","H","I"])
z=pd.merge(left=x,right=y,how="inner",left_on="Name_1",right_on="Name_2",indicator=True)
print(z)'''

'''x=pd.DataFrame({"Name_1":["prince","Ankit","manu"],"Marks":[46,96,64]})
y=pd.DataFrame({"Name_2":["prince","manu","Ram","annu"],"Marks":[96,49,55,68]})
z=pd.merge(left=x,right=y,how="right",left_on="Name_1",right_on="Name_2",indicator=True)
print(z)'''



'''x=pd.DataFrame({"Name_1":["Ashish","Arvind","Sahil","Deepak","Nikhil","Abhishek","rahul","nikkhil"],"math":[99,98,87,97,67,95,25,48]})
y=pd.DataFrame({"Name_2":["Ashish","tejaswi","omkar","nikhil","Abhishek","rahul","ranjeet"],"Marks":[78,45,59,26,18,89,59]})
z=pd.merge(left=x, right=y, how="outer",left_on="Name_1",right_on="Name_2",indicator=True)
print(z)'''

'''x=pd.DataFrame({"Name_1":["prince","Ankit","Manu","Priya"],"Marks":[78,79,77,58]},index=["A","B","C","D"])
y=pd.DataFrame({"Name_2":["Anmol","Priya","Bhanu","prince","Manu"],"Marks":[49,48,74,82,93]},index=["E","F","G","H","I"])
z=pd.merge(left=x,right=y,how="outer",left_on="Name_1",right_on="Name_2",indicator=True)
print(z)'''

'''x=pd.DataFrame({"Name_1":["prince","Ankit","Manu","Priya"],"Marks":[78,79,77,58]},index=["A","B","C","D"])
y=pd.DataFrame({"Name_2":["Anmol","Priya","Bhanu","prince","Manu"],"Marks":[49,48,74,82,93]},index=["E","F","G","H","I"])
z=pd.merge(left=x,right=y,how="left",left_on="Name_1",right_on="Name_2",indicator=True)
print(z)'''

'''x=pd.DataFrame({"Name_1":["prince","Ankit","Manu","Priya"],"Marks":[78,79,77,58]},index=["A","B","C","D"])
y=pd.DataFrame({"Name_2":["Anmol","Priya","Bhanu","prince","Manu"],"Marks":[49,48,74,82,93]},index=["E","F","G","H","I"])
z=pd.merge(left=x,right=y,how="right",left_on="Name_1",right_on="Name_2",indicator=True)
print(z)'''


'''x=pd.DataFrame({"Name_1":["prince","Ankit","Manu","Priya"],"Marks":[78,79,77,58]})
y=pd.DataFrame({"Name_2":["Anmol","Priya","Bhanu","prince","Manu"],"Marks":[49,48,74,82,93]})
#z=pd.merge(left=x,right=y,how="left",left_on="Name_1",right_on="Name_2",indicator=True)
y=pd.merge(left=x,right=y,how="right",left_on="Name_1",right_on="Name_2",indicator=True)
print(y)'''


#x.str.upper()
#x.str.lower()
#x.str.title()
'''x=pd.Series(["prince","kumar","sahrma"])
print(x.str.title())
print(x.str.upper())
print(x.str.lower())'''

#x.str.len() => with the help of these method we can find the length of each name.
#x.str.split() => with the help of these method we do all name in list bracket.

'''x=pd.Series(["prince ","kumar ","sahrma "])
print(x.str.len())
print(x.str.split())
print(x.str.cat(sep="**"))
print(x.str.repeat(3))'''


#x.str.contains("pr")
#x=pd.Series(["prince","kumar","sahrma"])
#print(x.str.contains("ku"))

#x.str.replace()
#x=pd.Series(["prince","manu","priya","pappu"])
#print(x.str.replace("p","A"))

'''x=pd.Series(["prince","kumar","sharma"])
print(x.str.cat(sep="@@"))'''

#****************************************************************************************************************************

'''x=pd.Series(["prince","kumar","sharma"])
print(x.str.startswith("p")) #if startswith with user value then show true else false
print("\n endswith")
print(x.str.endswith("a")) #if endswith with user number then return boolen value
print("\ncounts")
print(x.str.count("m")) #count the the value that we give argument each data
print("\nfind")
print(x.str.find("r")) #show the index number of value that we find
print("\n swapcase")
print(x.str.swapcase()) #its exchange from lower to upper and upper to lower
print("\n title")
print(x.str.title())'''


#x=pd.DataFrame({"Names":["prince","kumar","ankit","Manu","prince","Manu"],"marks":[100,80,90,70,100,70]})
#print(x.drop_duplicates())#with the help of these method dropping the the duplicate value and print only single value

'''
a={"Company":["HCL","HCL","HCL","LG","LG","MI","MI"],
"employer":["prince","anshu","Priya","annu","ankit","mayur","mahi"],
"Profit":[1000,800,600,500,400,1200,200]}
x=pd.DataFrame(a)
#print(x)
y=x.groupby("Company")
print(y)

#Now aggrigating the gruop
print("\nsum method with total profit of Company")
print(y.sum())

print("\n minimum profit of company ")
print(y.min())

print("\n mean of company profit")
print(y.mean())

print("\nfind the maximum profit of this company")
print(y.max())

print("\n show how many employer and number of profit")
print(y.count())

print("\n describe the detalis of company")
print(y.describe())

print("\n Describe the company details in row to column mode! ")
print(y.describe().transpose())

print("\n describe about company LG Only")
print(y.describe().T["LG"])'''

'''
x=pd.DataFrame({"company":["google","google","linux","linux","intel","intel"],"employee":["prince","raja","amrit","anand","kriti","mona"],"profit":[1200,800,900,700,1000,500]})
y=x.groupby("company")
'''
#print(y.describe())

'''profit
         count    mean         std    min    25%     50%     75%     max
company
google     2.0  1000.0  282.842712  800.0  900.0  1000.0  1100.0  1200.0
intel      2.0   750.0  353.553391  500.0  625.0   750.0   875.0  1000.0
linux      2.0   800.0  141.421356  700.0  750.0   800.0   850.0   900.0 '''

#print(y.describe().T["google"])
#print(y.describe().T)

'''a={"name":["prince","kumar","sharma","chhotu","raj","mohit"],"age":[12,45,78,23,46,78]}
b={"name2":["prince","sharma","ram","ravan","raj","Mohan"],"age":[12,78,55,89,46,25]}
x=pd.DataFrame(a)
y=pd.DataFrame(b)'''
'''z=pd.merge(left=x,right=y,how="inner",left_on="name",right_on="name2",indicator=True)
print(z)
m=pd.merge(left=x,right=y,how="outer",left_on="name",right_on="name2",indicator=True)
print(m)
n=pd.merge(left=x,right=y,how="left",left_on="name",right_on="name2",indicator=True)
print(n)
o=pd.merge(left=x,right=y,how="right",left_on="name",right_on="name2",indicator=True)
print(o)'''

#m=pd.concat((x,y))
#print(m)

#x=pd.Series(["prinrce","kumar","sharma","mohan","chhotu","anklit"],index=["a","b","c","d","e","f"])
#print(x.str.cat(sep="**"))

#print(x.str.contains("h")) 
#print(x.str.count("r"))
#print(x.str.find("r"))
#print(x.str.findall("i"))
#print(x.str.findall("r"))
#print(x["a":"f"])
#print(x[0:5])
#print(x[1],x[2])

import pandas as pd
#x=pd.read_csv("iris.csv")
#print(x)
#print(x.sum())
#print(x.min())
#print(x.count())
#print(x.describe())


#use of iloc[row range ,column range]
#print(x.iloc[5:10,1:5])
#print(x.iloc[0:11,0:])
#print(x.loc[0:11,("Id","SepalLengthCm")])	# loc method in both range are excluded

'''x=pd.DataFrame({"Name":["prince","Anmol","rahul","mayank"],"Marks":[45,78,89,56]})
x.to_csv("prince.csv")
print("Done")'''

'''x=pd.read_csv("prince.csv ")
print(x)
print(x.min())
print(x.describe())
print(x.iloc[5:25,0:5])'''



#x=pd.Series(["prince","kumar","sahrma"])
#print(x.str.findall("r "))
'''fruits=pd.DataFrame({"Fruits":["Apple","Banana","Mango"],"price":[45,56,62],
	"Quality":["good","better","best"]},index=[1,2,3],columns=["price","Quality","Fruits"])
print(fruits)
print(fruits.iloc[0:2,1])
'''

import pandas as pd
#x=pd.read_csv("dataone.csv")
#print(x)

#if you want to clear all empty set in original file then apply x.dropna(inspace=True)
#x.dropna(inspace=True)
#print(x)

#if you want to delete empty cell in duplicates sheet then us this methood
#y=x.dropna()
#print(y)

#if you want to replace the blanks cell in any number or string then use this method.
#print(x.fillna(120,inspace=True)) 	#replace in original file 

#y=x.fillna("prince")
#print(y)	# repplace in duplicates file


'''for i in range(1,21):
	print("\n",end="")
	for j in range(1,11):
		print(i*j,end="  ")'''
'''x=pd.Series(p)
x.to_csv("table.csv")
print("done")'''
import numpy as np
'''a=pd.Series(np.random.randint(100,200,25))
print(a)
a.to_csv("random.csv")'''


#x=pd.read_csv("dataone.csv")
#y=x.iloc[5:15,2:4]
#print(y)
#z=x.loc[1:20,("Date","Pulse","Duration")]
#print(z)
'''print(x.shape)
print(len(x))
print(x.head())
print(x.tail())
print(x.head(12))'''

#y=x["Date"].fillna("chhotu")
#print(y)	# it will show only column of date only and add chhotu at balanks cells.


#x=pd.read_csv("dataone1.csv")
#print(x)
#x["Date"]=pd.to_datetime(x["Date"])
#x.to_csv("dataone1.csv")
#print("done")
#y=x.dropna()
#y["Date"]=pd.to_datetime(y["Date"])
#y["Date"]=pd.to_datetime(y["Date"])
#print(y)


#x.fillna(120,inplace=True)
#print(x)


'''with open("aks.csv","a") as f:

	x.loc[0:10,"Duration"]=1111
	x.loc[11:20,"Duration"]=9999
	f.write(f"{x}")
	print("done")'''



'''x=pd.read_csv("dataone1.csv")
#print(x)

x["Date"]=pd.to_datetime(x["Date"])
#print(x)

y=x.loc[0:5,("Duration","Date","Pulse")]
print(y)'''
'''

x={"student":["prince","prince","prince","ankit","ankit","ankit","manu","manu","manu"],
"subject":["Math","English","Hindi","Math","English","Hindi","Math","English","Hindi"],
"Marks":[45,89,78,56,89,78,81,96,82]}
a=pd.DataFrame(x)
#print(a)
y=a.pivot(index="student",columns="subject",values="Marks")
print(y)

print(y.sum())
print(y.min())'''

'''
x=pd.DataFrame({"Name":["prince","karan","arjun","prince","arjun"],"marks":[12,45,78,12,78]})
y=pd.DataFrame({"Name_1":["arjun","rohan","anuj","prince","amrit"],"marks":[78,89,71,12,52]})

#print(x.drop_duplicates())
#print(x.loc[0:2,("marks")])
#z=pd.concat((x,y))
#print(z)
y=pd.merge(left=x,right=y,how="outer",left_on="Name",right_on="Name_1",indicator=True)
print(y)'''

#x=pd.Series(["prince",45],["ankit",40])
#print(x)
'''x=pd.DataFrame({"Name":["prince","ankit","aman"],"num":[12,45,78]},index=(1,2,3),columns=("num","Name"))
#print(x)
print(x.size)
print(x.shape)
print(type(x))
print(x.index)
print(x.values)'''
'''
a={"Sub":["Hnd","Hnd","Hnd","Hnd","Eng","Eng","Eng","Eng","Math","Math","Math","Math"],
"Students":["Prince","Muskan","SUnaina","Deepa","Prince","Muskan","SUnaina","Deepa","Prince","Muskan","SUnaina","Deepa"],
"Marks":[98,87,54,65,99,87,84,85,88,78,79,69]}
x=pd.DataFrame(a)
#print(x)
y=x.pivot(columns="Sub",index="Students",values="Marks")
print(y)'''


'''x=pd.DataFrame({"Name":["prince","kumar","sharma","chhotu"],
	"Marks":[45,78,89,56],"per":[45.6,78.5,85.2,52.1] })
#print(x) 
#x.to_csv("cks.csv")


#x=pd.read_csv("cks.csv")
#print(x)

x=x["per_Rank"]=x["per"].rank(ascending=0)
x=x.set_index("per_Rank")
print(x)

'''
'''
x=pd.DataFrame({"Name":["prince","kumar","sharma","chhotu"],
	"Marks":[45,78,89,56],"per":[45.6,78.5,85.2,52.1] })
#print(x) 
#x.to_csv("cks.csv")


#x=pd.read_csv("cks.csv")
#print(x)

z=x["per_Rank"]=x["per"].rank(ascending=0)
y=z.set_index("per_Rank")
print(y)'''


#---------------------------------------------------------------------
#read Excel sheet in pandas and create excel sheet in pandas


'''a={"Name":["prince","kumar","sharma","mohan"],"age":[23,21,24,25]}
x=pd.DataFrame(a)
#print(x)
x.to_excel("abc.xlsx",index=False)
print("done")'''


#how to create from sheet 1, sheet 2, sheet 3 in excel file

'''with pd.ExcelWriter("abc.xlsx") as f:
	x=pd.DataFrame({"fruits":["apple","hair","floor","pumpkin"],"veg":["brnjal","axe","xzxx","you"]})
	x.to_excel(f,sheet_name="fff",index=False)
	print("Done")
	a={"Name":["prince","kumar","sharma","mohan"],"age":[23,21,24,25]}
	b=pd.DataFrame(a)
	b.to_excel(f,sheet_name="www",index=False)
	print("Done")
	c=pd.DataFrame({"nu":[1,2,3,4,5,6],"em":[78,89,56,45,23,56]})
	c.to_excel(f,sheet_name="rrr",index=False)
	print("done")'''


'''
with pd.ExcelWriter("mom.xlsx") as x:
	a=pd.DataFrame({"Name":["prince","ankit","anmol","Manu"],"conatact_no":[98866558,789965545,5489665452,987456123]})
	a.to_excel(x,sheet_name="details",index=False)
	print("Done")
	b=pd.DataFrame({"State":["Bihar","punajb","gujrat","kolkata"],"capital":["patna","chndigarh","ghandinagar","westbengal"]})
	b.to_excel(x,sheet_name="state_capital",index=False)
	c=pd.DataFrame({"State":["Bihar","Delhi","Chennai","kerala","kolkata"],"Language":["BHojpuri","Hindi","Tamil","Maliyalam","bengali"]})
	c.to_excel(x,sheet_name="st_lan",index=False)
	print("Done")
	for i in range(1,11):
		y=i*5
	d=pd.DataFrame({"table":[y]})
	d.to_excel(x,sheet_name="table",index=False)
	print("done2")
	e=pd.Series([np.arange(1,11)])
	f=e*5
	f.to_excel(x,sheet_name="Table",index=False)'''


#This method is used to create and add by sheet to sheet
'''with pd.ExcelWriter("asd.xlsx") as f:
	a=pd.Series(["prince","kumar","sharma"])
	a.to_excel(f,sheet_name="name",index=False)'''

'''
#merge function
x=pd.DataFrame({"Name_1":["prince", "Kumar","sharma","sanvi"],"no":[56,89,78,50]})
y=pd.DataFrame({"Name_2":["prince","aman","sanvi","Rahul"],"no":[56,78,50,80]})
z=pd.merge(left=x,right=y,how="right",left_on="Name_1",right_on="Name_2")
print(z)'''

'''a={"Company":["google","google","HCL","HCL","acc","acc"],
"employee":["prince","rahul","ankit","manoj","radha","priya"],
"profit":[789,456,123,741,852,963]}
x=pd.DataFrame(a)
y=x.groupby("Company")
print(y.min())
print(y.max())

x.to_excel("qqq.xlsx")
print("done")'''
'''
data={"Name":['Jai','princi','Gaurav','anuj'],
"Age":[27,24,22,32],"Address":["Delhi","Kanpur","Allahabad","Kannauj"],
"Qualification":["Msc","MA","MCA","Phd"]}

x=pd.DataFrame(data)

1.
y=x.iloc[1,0:]
print(y,"\n")

2.
z=x.iloc[0::3,0:]
print(z,"\n")

m=x.loc[0,"Name":]
print(m)'''
'''3.
m=x.drop(["Age"],axis=1)
n=m.iloc[0,0:]
print(n)'''



#print(x)
#y=x.loc[(x["Name"]=="princi")]
#print(y)




'''a={"First_name":["prince","Ankit"],"Last_name":["Sharma","Kumar"]}
b={"First_name":["Arman"],"Last_name":["ray"]}
c={"surname":["mohan","ram"]}
x=pd.DataFrame(a)
y=pd.DataFrame(b)
d=pd.DataFrame(c)

z=pd.concat([x,y,d],ignore_index=True,axis=0)
print(z)'''


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
print(y.iloc[0:3,0:])


#t=df.nlargest(5,["Weight"])
#print(t)


#a=df["Name"]
#d=df.loc[0:,("Name")].tolist()
#print(d)

#print(df.columns)
#print(df.keys())
#m=df["Name"].tolist()
'''


'''a={"Name":["prince","priya","priyanshu"],"Year":[2020,2022,2021],"Rating":[9.2,8.5,7.7]}
x=pd.DataFrame(a)
print(x)

x["Rating_Rank"]=x["Rating"].rank()
x=x.set_index["Rating_Rank"]
print(x)'''

'''y=x["Year"].contains(2020)
print(y)

y=x[x["Year"].isnull()]
print(y)'''

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------

#x=pd.date_range("20220825",periods=10)
#print(x)
#x=np.random.randn(10,4)
#print(x)

#x=pd.DataFrame(np.random.randn(10,4),index=[1,2,3,4,5,6,7,8,9,10],columns=["A","B","C","D"])
#print(x)
'''
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


'''x=pd.DataFrame({"Name":["prince","Ankit","Rahul","Manu"],
	"Roll_No":[1,2,3,4],"Hnd":[78,89,56,88],"Eng":[85,96,74,52],"Math":[99,85,74,63]})
#print(x)
y=x.iloc[0:,2:]
z=y.sum(axis=1)
x["Mark_obt"]=z
a=z/300*100
x["Persantage"]=a
print(x)'''


'''if z>200:
	div=First
elif z>250:
	div=top
else:
	div=Fail
x["Divison"]=div
print(x)'''
'''
d=[]

marksheet=pd.DataFrame({"Result_Date":pd.Timestamp("2022-08-25"),
	"Students_Name":["Prince kumar","Amit kumar","Suraj kumar","Raman kumar","Ankit kumar"],
	"Roll_No":[4,3,5,1,2],"Marks":[380,330,255,290,401]})
#print(marksheet)

per=marksheet["Marks"]/500*100
#marksheet["Persantage"]=per
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
#y=marksheet.nlargest(5,["Roll_No"])
print(y) 
'''

m={"Name":["Prince","Annu","Sanvi","Suraj","Ankit"],"Roll_No":[5,2,1,4,3],
"HND":[98,74,85,96,52],"MATH":[99,52,41,71,58],
"SNK":[88,34,40,50,30],"SC":[95,45,65,35,47],"SST":[70,35,46,80,55]}

x=pd.DataFrame(m)
#print(x)

a=x.iloc[0:,2:]
#b=a.sum(axis=1)

b=x["HND"]+x["MATH"]+x["SNK"]+x["SC"]+x["SST"]
x["Marks_obt"]=b
c=b/500*100
x["Persantage"]=c
#print(x)
d=x["Marks_obt"]
e=[]
for i in d:
	if i<250:
		div="Third Divison"
	elif i<300:
		div="Second Divison"
	else:
		div="First Divison"
	e.append(div)

x["Divison"]=e
print(x)

























