import pandas as pd
'''
# series data structure
data_series = [1, 4, 7, 9, 80]
print(pd.Series(data_series))

# changing index value in series
print(pd.Series(data_series, index=['1', '11', '10', '5', '6']))


# dataframe data structure
personal_info = {
    'name': ['Shristi', 'Ashu', 'Wina'],
    'surname': ["Shrestha", 'Pradhan', 'Mulmi']

}
my_var = pd.DataFrame(personal_info)
# result is  a Pandas series
print('locating first item in row:', my_var.loc[0])
# result pandas dataframe as it gives both row and column as a table
print('locating 1st two rows:', my_var.loc[[0, 1]])

# creating own index values
my_index = pd.DataFrame(personal_info, index=['Official', 'Nick', 'Classy'])
print('Values with own indedx values:', my_index)
print(my_index.loc['Official'])

my_series = pd.Series(personal_info)
print(my_var)
print(my_series)  # key of the dictionary become index in series data structure


# loading files into dataframe
df = pd.read_csv('data.csv')
print(df)
print(df.to_string())  # print entire dataframe of csv file
print('viewing 1st 10 data:', df.head(10))  # viewing data
print('viwing last data:', df.tail())
# checking system's maximum rows
print(pd.options.display.max_rows)
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)

#same for json file


# Pandas- Cleaning data
# 1.cleaning empty cels
#   a.remove rows that cotain empty cells
df = pd.read_csv('data.csv')
df_removerow = df.dropna()  # wont change original dataframe
df.dropna(inplace=True)  # change original dataframe
print('Original one:', df_removerow.to_string())
print('df with change original dataframe:', df.to_string())

# b. replace empty values
df = pd.read_csv('data.csv')
df.fillna(130, inplace=True)  # empty celss will be replaced by 130
print(df.to_string())


# c. replace only for specified columns
df = pd.read_csv('data.csv')
# in column calories, empty cells will be replaced by 130
df['Calories'].fillna(130,  inplace=True)
print(df.to_string())


# d. Replace Using Mean, Median, or Mode of specified column
df = pd.read_csv('data.csv')
x = df['Calories'].mean()
y = df['Calories'].median()
z = df['Calories'].mode()
df['Calories'].fillna(x, inplace=True)
df['Calories'].fillna(y, inplace=True)
df['Calories'].fillna(z, inplace=True)
print('Replace with mean value', df.to_string())
print('Replace with median value', df.to_string())
print('Replace with mode value', df.to_string())
'''

# solving above creating funtion


def replace_with_summary(df, column_name):
    # Calculate mean, median, and mode values for the specified column
    x = df[column_name].mean()
    y = df[column_name].median()
    # In case there are multiple modes, we take the first one
    z = df[column_name].mode()[0]

    # Fill empty cells in the specified column with the calculated values
    df[column_name].fillna(x, inplace=True)
    df[column_name].fillna(y, inplace=True)
    df[column_name].fillna(z, inplace=True)

    # Print the DataFrame with each replacement method
    print('Replace with mean value:')
    print(df.to_string())

    print('\nReplace with median value:')
    print(df.to_string())

    print('\nReplace with mode value:')
    print(df.to_string())


# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Call the function for the 'Calories' column
replace_with_summary(df, 'Calories')
