# import pandas as pd
# import numpy as np
# dict1 ={"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35] ,"Marks": [100,50,0]}
# df = pd.DataFrame(dict1)

# print(df)

# print ("name" , df["Name"])  # Output: 0      Alice

# print ("age",df["Age"])   # Output: 0    25

# print ("first row",df.loc[0])  # Output: Name    Alice

# data = [1,2,3,4,5]
# series1 = pd.Series(data)
# print (series1)  # Output: 0    1

# print(series1.loc[0])  # Output: 1

# print(series1.iloc[1])  # Output: 1

# print("DataFrame shape:", df.shape)   # Output: (3, 2)
# print("DataFrame columns:", df.columns)  # Output: Index(['Name', 'Age'], dtype='object')
# print("DataFrame info:", df.info())  # Output: <class 'pandas.core.frame.DataFrame'>\nRangeIndex: 3 entries, 0 to 2\nData columns (total 2 columns):\n #   Column  Non-Null Count  Dtype \n---  ------  --------------  ----- \n 0   Name    3 non-null      object\n 1   Age     3 non-null      int64 \ndtypes: int64(1), object(1)\nmemory usage: 176.0+ bytes
# print("DataFrame description:\n", df.describe())  # Output:              Age\ncount   3.000000\nmean   30.000000\nstd     5.000000\nmin    25.000000\n25%    27.500000\n50%    30.000000\n75%    32.500000\nmax    35.00000₀    
# print("Dataframe desc: \n", df.describe(include='all'))  # Output:         Name  Age\ncount       3  3.000000\nunique      3       NaN\ntop     Alice       NaN\nfreq        1       NaN\nmean      NaN  30.000000\nstd       NaN   5.000000\nmin       NaN  25.000000\n25%       NaN  27.500000\n50%       NaN  30.000000\n75%       NaN  32.500000\nmax       NaN  35.000000

# print ("Data", df.loc[0,"Name"])  # Output: Alice

# print ("Data \n", df.loc[0:2])  # Output: Alice

# print ("Data \n", df.iloc[0:2])

# list5 = np.array([1, 2, 3, 4, 5])
# print (list5[list5>2])  # Output: [1 2 3 4 5]

# print(df["Age"])

# print(df[df["Age"]>25])  # Output: Name  Age\n1    Bob   30\n2 Charlie   35

# print(df.loc[df["Age"]>25, "Name"])  # Output: 1        Bob\n2    Charlie\nName: Name, dtype: object

# print(df.loc[0])  # Output: Alice


import pandas as pd
# df = pd.read_csv("employee.csv")
# print (df)
# df["Salary"] = df["salary"]  # Create a new column 'Salary' with the same values as 'salary'
# print (df["name"])
# print(df.isnull())
# print(df.dropna())

# print(df [df["age"]>30])

df1 = pd.read_csv("employee.csv")
df2 = pd.read_csv("department.csv")
merged_df =pd.merge(df1,df2)

print (merged_df)
print (merged_df["name"])
print(merged_df.groupby("dept")["salary"].mean())

df1["bonus"] = df1["salary"] * 0.1
print (df1)
df2.replace("NY", "New York", inplace=True)