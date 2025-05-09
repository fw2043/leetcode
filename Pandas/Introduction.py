# create a pandas dataframe
import pandas as pd

col = ["student_id", "age"]
df = pd.DataFrame(student_data, columns=col)

# select the first rows
df.head()
# size:
df.shape
print([df.shape[0], df.shape[1]])

# select data:
# .loc[row filter conditon, columns selection]
df.loc[:3] #
students.loc[students.student_id == 101, ["name", "age"]]
display(data.loc[(data.Brand == 'Maruti') & (data.Mileage > 25)])

# create a new column: bonus-------column-wise operations
employees["bonus"] = employees["salary"] * 2


# dropping passed values
data.drop(["Avery Bradley", "John Holland", "R.J. Hunter"], inplace = True)
# display
print(data)
# dropping passed columns
data.drop(["Team", "Weight"], axis = 1, inplace = True)

#Drop Duplicate Rows
customers.drop_duplicates(subset='email', keep='first', inplace=True)
df.drop_duplicates(subset=['brand', 'style'], keep='last')

# drop all duplicate rows
df.drop_duplicates( keep=False)

# drop missing value
students.dropna(subset=['name'],inplace=True)\

# rename columns
students.rename(columns={'id': 'student_id', 'first': 'first_name', 'last': 'last_name', 'age': 'age_in_years' }, inplace=True)

# change data type
students = students.astype({'grade': int})

# fill null values
values = {"A": 0, "B": 1, "C": 2, "D": 3}
df.fillna(value=values)

# concatenating df1 and df2 along rows
vertical_concat = pd.concat([df, df1], axis=0)

# concatenating df3 and df4 along columns
horizontal_concat = pd.concat([df1, df2], axis=1)

# pivot table


# sort by values:
df.sort_values(by=['author_id'], inplace=True)



#########################
""" For pandas objects (Series, DataFrame), the indexing operator [] only accepts

1. colname or list of colnames to select column(s)
2. slicing or Boolean array to select row(s), i.e. it only refers to one dimension of the dataframe.
For df[[colname(s)]], the interior brackets are for list, and the outside brackets are indexing operator, 
i.e. you must use double brackets if you select two or more columns. With one column name, single pair of brackets returns a Series, 
while double brackets return a dataframe.

Also, df.ix[df['A'] < 3,['A','C']] or df.loc[df['A'] < 3,['A','C']] is better than the chained selection for avoiding returning a copy versus a view of the dataframe.
"""