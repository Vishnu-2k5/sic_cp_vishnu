import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the dataset
df = pd.read_csv('C:\\Learning\\Python\\sic\\sic_cp_vishnu\\Hackathon\\Engineering_Branch_Analytics.csv')

# Reading the data
print(df)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Which branch offers the best combination of internships and placements? (Compare internship percentage and placement percentage)
data={'Internship(%)':df['Internships (%)'],'Placement(%)':df['Placements (%)']} #Dictionary with data
dataframe=pd.DataFrame(data) #creating a dataframe
dataframe.plot(kind='bar',figsize=(10,10)) #plotting of dataframe

plt.bar(df['Internships (%)'],df['Placements (%)'])
plt.xticks(ticks=range(len(df['Branch Name'].values)), labels=df['Branch Name'].values,rotation=0) #printing of branch name in x axis
plt.xlabel("Interships (%)") #x axis name
plt.ylabel("Placements (%)") #y axis name
plt.title("Internship vs Placement") #plot title
plt.show()

df['Best Combination'] = df[['Internships (%)', 'Placements (%)']].mean(axis=1) #for finding average of placement and internship data
print(df)
max_name = df.loc[df['Best Combination'].idxmax(), 'Branch Name'] #to find branch name with max  value of combination data
print("The branch that offers the best combination of internships and placements:",max_name)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Which branch provides the best career prospects? (Consider average salary, placements)
df['Placements (%)']=df['Placements (%)']/10 #dividing placement value with 10 because lpa values are in integer form(single/double digit), so get better graph, it is divided by 10
data2={'Average Salary (LPA)':df['Average Salary (INR)'],'Placement(%) out of 100':df['Placements (%)']} #Dictionary with data
dataframe2=pd.DataFrame(data2) #creating a dataframe
dataframe2.plot(kind='bar',figsize=(10,10)) #plotting of dataframe
plt.bar(df['Average Salary (INR)'],df['Placements (%)'])
plt.xticks(ticks=range(len(df['Branch Name'].values)), labels=df['Branch Name'].values,rotation=0) #printing of branch name in x axis
plt.xlabel("Average Salary (LPA)") #x axis name
plt.ylabel("Placements (%)") #y axis name
plt.title("Average Salary and Placement with Job Stability") #plot title 
plt.show()
df['Placements (%)']=df['Placements (%)']*10 #changing back to original value by multiplying it back with 10

max_value1 = df['Average Salary (INR)'].max() #to find max of average salary
max_value2 = df['Placements (%)'].max()#to find max of placement percentage
max_branch = df[(df['Average Salary (INR)'] == max_value1) & (df['Placements (%)'] == max_value2)]['Branch Name'].iloc[0]# Get the branch name where both values are the maximum
print(f"The branch that provides best career prospects: {max_branch}")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Which branch has the lowest Dropout Rate ?
colors = ['blue', 'red', 'green', 'purple','orange'] #colors
bn=df['Branch Name'].values #creating a list of branch names in order
plt.pie(df['Dropout Rates (%)'], labels=bn, colors=colors, autopct='%1.1f%%', startangle=140) #creating pie chart
plt.title("Pie Chart") #chart title
plt.show() 
min_dr = df.loc[df['Dropout Rates (%)'].idxmin()] # Find the row with the minimum value in the 'V' column
min_bn = min_dr['Branch Name'] # Get the corresponding name for the least value
print(f"The branch with the least Dropout Rate is: {min_bn}")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
