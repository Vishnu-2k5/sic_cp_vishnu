import numpy as numpy
import scipy
import math 
import random 
import pandas as pd
def p1():
    array = np.array([[1, 1, 3, 3, 4, 4, 4, 5, 7, 7, 8, 9, 12]])
    mean   = np.mean(array)
    median = np.median(array)
    mode   = scipy.mode(array)
    print(f'Mean = ', mean)
    print(f'Median = ', median)
    print(f'Mode = ', mode)

def p2():
    array1 = np.array([[1, 2], [3, 4]]) 
    array2 = np.array([[1, 2], [3, 4]]) 
    print(array1 == array2)
    comparison = (array1 == array2)
    equal_arrays = comparison.all()
    print(equal_arrays)

def p3():
    week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])
    high_spend = np.where(spendings > 100)
    print(high_spenders)

def p4():
    week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])
    highest_spending = max(week_spendings)
    print(high_spending)

def p5():
    week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])
    index = 1
    big_spending = week_spendings[0]
    index = np.argmax(week_spendings)
    days = {1:'mon', 2:'tue', 3:'wed', 4:'thus', 5:'fri', 6:'sat', 7:'sun'}
    print(big_spending, days[index])

def p6():
    expenses = np.array([20, 60, 5, 80, 45, 90])
    modified_expenses = np.where(expenses < 50, 0, expenses)
    print(modified_expenses)

def p7():
    random_data = np.random.rand(3, 4)
    print(random_data)

def p8():
    user_number = int(input('Enter a number of your choice between [0 and 9]: '))
    system_number = math.random(10)
    if system_number == user_number:
        print('CrorePati')
    else:
        print('RoadPati')

def p9():
    def read_excel_file():
        file_path = './students.xlsx'
        df = pd.read_excel(file_path)
        print(df.count())
        print(df.head())
        print(df.tail())

    def read_excel_file1():
        file_path = './students.xlsx'
        df = pd.read_excel(file_path)
        for index, row in df.iterrows():
            print(row[0], '  ', row[1])

    def read_excel_file2():
        file_path = './students.xlsx'
        df = pd.read_excel(file_path)
        for row in df.iterrows():
        print(row[1][0], row[1][1])

def p10():
    sequence_arange = np.arange(1, 10, 3)
    sequence_linspace = np.linspace(0, 100, 5)
    print("Using arange:", sequence_arange)
    print("Using linspace:", sequence_linspace)

def p11():
    sequence = np.arange(1, 10, 3)
    print(sequence)
    values = np.linspace(0, 100, 23)
    print("Generated values:", values)
    print("Total count:", len(values))

def p12():
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
    df = pd.DataFrame(data)
    print(df)

def p13():
    df = pd.read_csv('data.csv')
    df.head()
    print(df.isnull().sum())

def p14():
    high_salary = df[df['Salary'] > 50000]
    print(high_salary)

def p15():
    df_sorted = df.sort_values(by='Salary', ascending=False)
    print(df_sorted)

def p16():
    grouped = df.groupby('Age')['Salary'].mean() 
    print(grouped)

