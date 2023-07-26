import pandas as pd
import matplotlib.pyplot as plt

'''
# 2. Cleaning data of wrong format
# a.Conveert into a correct format
df = pd.read_csv('data.csv')
df['Duration'] = pd.to_datetime(df['Duration'])
print(df.to_string())

# b. removing rows
df.dropna(subset=['Duration'], inplace=True)
print(df.to_string())


# 3.Fixing wrong data
# a. replacing values
df = pd.read_csv('data.csv')
df.loc[7, 'Duration'] = 45
print(df.to_string())

# using conditional statement
df = pd.read_csv('data.csv')
for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.loc[x, 'Duration'] = 120
print(df.to_string())

# b. removing rows
# removing rows 'dyration' where value is higher than 120
df = pd.read_csv('data.csv')
for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.drop(x, inplace=True)
print(df.to_string())


# 4.Removing duplicates
# a. discovering duplicates
df = pd.read_csv('data.csv')
print(df.duplicated())
print(df.drop_duplicates(inplace=True))  # to remove duplicates


# Data Correlations
df = pd.read_csv('data.csv')
print(df.corr())
df.plot()
plt.show()


# Scatter plot
df = pd.read_csv('data.csv')
df.plot(kind='scatter', x='Duration', y='Calories')

df.plot(kind='scatter', x='Duration', y='Maxpulse')  # no relationship between the columns
plt.show()
'''

# Histogram
df = pd.read_csv('data.csv')
df['Duration'].plot(kind='hist')
plt.show()
