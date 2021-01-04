## Pandas Learning

### What is Pandas?
- Used for working with data sets
- Used for analyzing, cleaning, exploring and manipulating data
- `Panel Data` and `Python Data Analysis` reference

### Why Use Pandas?
- Analyze big data and make conclusions based on statistical theories
- Can clean messy data sets and make them readable and relevant
- `Data Science` we store, analyze and deriving information from it

### What Pandas can do?
- Is there `correlation between two or more columns`
- What is average value
- Max value and min value
- You can delete rows that are not relevant, or contains wrong
- values, like empty or NULL values. (Data cleaning)

### What is a Series?
- Series is like a column in a table
- `a is a list` 
- `myvar = pd.Series(a, index = ["x", "y", "z"])`
- Now we can do it by `key reference x, y, z`
- `Key/Value Objects as Series`
- can use a dictionary 
- `myvar = pd.Series({"identifier1":value, "identifier2":value2})`
- `myvar = pd.Series({"identifier1":value, "identifier2":value2}, 
index=["identifier1"])` -> note index is the access row (row name)

### Dataframe from two series
- `data = {"calories": [420, 380, 390],
  "duration": [50, 40, 45]}`
- `myvar = pd.DataFrame(data)`
- A Pandas DataFrame is a 2 dimensional data structure, like a 2d array (RxC)
- `myvar.loc[0]` get the row, returns as a `Pandas Series`
- `myvar.loc[[0, 1]]` returns a `DataFrame` -> `[]` returns `rows 0 and 1`


### Load Files Into a DataFrame
- Pandas can load them into a DataFrame
- `read_csv` file which are simple ways to store big files
- `df.to_string()` to print entire dataframe
- By default when you print a DataFrame you get first 5 rows and last 5 rows
- [DataFrames](https://www.w3schools.com/python/pandas_json.asp)
