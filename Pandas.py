import pandas as pd

# pd.Series and its attributes
A = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print("Series A:")
print(A)
print("A.values:", A.values)
print("A.index:", A.index)

# Indexing and Slicing
print("A['c']:", A['c'])
print("A['b':'d']:")
print(A['b':'d'])

# Creating a series using a dictionary and displaying using dataframes
grades_marks = {'Grades': ['A', 'B', 'C', 'D', 'E'], 'Marks': [85, 75, 65, 55, 45]}
df = pd.DataFrame(grades_marks)
print("\nDataframe from dictionary:")
print(df)

# Add another key of scaled marks
df['Scaled Marks'] = df['Marks'] * 0.9
print("\nDataframe after adding Scaled Marks:")
print(df)

# Remove the scaled marks
del df['Scaled Marks']
print("\nDataframe after removing Scaled Marks:")
print(df)

# Only display the marks that are greater than 65
print("\nMarks greater than 65:")
print(df[df['Marks'] >= 65])

# 3. NaN values and handling them using DataFrame
A = pd.DataFrame([{'a': 1, 'b': 2}, {'a': 5, 'b': 3, 'c': 4}])
print("\nDataframe with NaN values:")
print(A)

# fillna function
A_filled = A.fillna(0)
print("\nDataframe after fillna(0):")
print(A_filled)

# dropna function
A_dropped = A.dropna()
print("\nDataframe after dropna():")
print(A_dropped)

# 4. Explicit and implicit indexing clash using loc and iloc
A = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
print("\nSeries: ")
print(A)

# Using loc (explicit)
print("\nUsing loc (explicit indexing):")
print(A.loc[3:5])

# Using iloc (implicit)
print("\nUsing iloc (implicit indexing):")
print(A.iloc[0:2])

# Apply loc and iloc with the marks and grades example
print("\nDataframe from dictionary (again):")
print(df)

# Using loc (explicit indexing) for DataFrame
print("\nUsing loc (explicit indexing) for DataFrame:")
print(df.loc[0:2])

# Using iloc (implicit indexing) for DataFrame
print("\nUsing iloc (implicit indexing) for DataFrame:")
print(df.iloc[0:2])
