%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from pandas.plotting import scatter_matrix
df=pd.read_csv('demographic.csv')
print("HEAD\n",df.head())
print("COLUMN\n",df.columns)
print("DESCRIBE\n",df.describe())

#AGE 
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return 
x=[]
i=0;
count=0
for index, row in df.AGE.iteritems():
    if(is_number(row)==False or np.isnan(row)):
        df.AGE.loc[index]=math.ceil(np.mean(df.AGE));
    count=count+1
    if(count==10176):
        break;
count=0
for index, row in df.AGE.iteritems():
    x.append(row);
    count=count+1
    if(count==10176):
        break;
count=0
for index, row in df.IN_MONTHS.iteritems():
    if(is_number(row)==False or np.isnan(row)):
        row=0
    df.IN_MONTHS.loc[index]=x[i]*12;
    i=i+1;
    count=count+1
    if(count==10176):
        break;
x=[]
count=0;
for index, row in df.AGE.iteritems():
    if(np.isnan(row)):
        break
    count=count+1
    if(count==10176):
        break
    x.append(int(row))
plt.hist(x)
plt.show()

#GENDER
count=0;
count1=0;
for index, row in df.GENDER.iteritems():
    if(row==1):
        count=count+1
    if(row==2):
        count1=count1+1
x=["MALE","FEMALE"];
value=[count,count1]

x_pos = [i for i, _ in enumerate(x)]
plt.bar(x,value)

#MARTIAL STATUS
for index, row in df.MARTIAL_STATUS.iteritems():
    if(is_number(row)==False or np.isnan(row)):
        df.MARTIAL_STATUS.loc[index]=5;
    if(row>7):
        df.MARTIAL_STATUS.loc[index]=5;
count=0;
x=[]
for index, row in df.MARTIAL_STATUS.iteritems():
    x.append(row)
    count=count+1
    if(count==10176):
        break
plt.hist(x)
plt.show()

#BIRTH PLACE
count=0
for index, row in df.BIRTH_PLACE.iteritems():
    if(np.isnan(row) or row>2):
        df.BIRTH_PLACE.loc[index]=2;
    count=count+1
    if(count==10176):
        break
count=0
for index, row in df.BIRTH_PLACE.iteritems():
    if(count==10176):
        break;
    count=count+1
    df.BIRTH_PLACE.loc[index]=int(row)

#FAMILY,INCOME,RATIO
for index, row in df.FAMILY_SIZE.iteritems():
    if(row>7):
        df.FAMILY_SIZE.loc[index]=7
for index, row in df.TOTAL_FAMILY_INCOME.iteritems():
    if(np.isnan(row)):
        df.TOTAL_FAMILY_INCOME.loc[index]=100;
for index, row in df.RATIO_TO_POVERTY_LINE.iteritems():
    if(np.isnan(row)):
        df.RATIO_TO_POVERTY_LINE.loc[index]=100;
for index, row in df.TOTAL_FAMILY_INCOME.iteritems():
    if(is_number(row)==False or np.isnan(row) or row>15):
        df.TOTAL_FAMILY_INCOME.loc[index]=np.median(df.TOTAL_FAMILY_INCOME)
d=dict();
for index, row in df.TOTAL_FAMILY_INCOME.iteritems():
    if(row not in d.keys()):
        d[row]=list()
    d[row].append(df.RATIO_TO_POVERTY_LINE.loc[index])
for index, row in df.RATIO_TO_POVERTY_LINE.iteritems():
    if(is_number(row)==False or np.isnan(row) or row>99):
        x=df.TOTAL_FAMILY_INCOME.loc[index]
        df.RATIO_TO_POVERTY_LINE.loc[index]=np.median(d[x]);
for index, row in df.TOTAL_FAMILY_INCOME.iteritems():
    print(row)
count=0;
x=[]
for index, row in df.TOTAL_FAMILY_INCOME.iteritems():
    if(np.isnan(row)):
        break
    if(row>15):
        continue
    x.append(int(row))
    count=count+1
plt.hist(x)
plt.show()

#HEALTH
d=dict()
for index, row in df.SEQUENCE_2.iteritems():
    if(row not in d.keys()):
        d[row]=1;
    d[row]=d[row]+1;
print(d)
count=0
for index, row in df.HEALTH.iteritems():
    if(np.isnan(row)):
        df.HEALTH.loc[index]=1
    count=count+1
    if(count==10176):
        break
    df.HEALTH.loc[index]=d[df.SEQUENCE.loc[index]]
x=list(d.values())
i=0
for index, row in df.HEALTH.iteritems():
    df.HEALTH.loc[index]=x[i]
    i=i+1;
    if(i==10175):
        break
count=0;
x=[]
for index, row in df.HEALTH.iteritems():
    if(np.isnan(row)):
        break
    if(row!=1):
        count=count+1;
z=[]
for i in range(1,25):
    z.append(x.count(i))
plt.bar(range(1,25),z)