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
- `.read_csv` file which are simple ways to store big files
  - `.read_json()`
- `df.to_string()` to print entire dataframe
- By default when you print a DataFrame you get first 5 rows and last 5 rows
- [DataFrames](https://www.w3schools.com/python/pandas_json.asp)

### Analyzing DataFrames
- Viewing the Data
- `df.head()` to get the headers and a specified number of rows starting from top
- `df.tail()` prints the last 5 rows of the DataFrame
- `df.info()` prints information about the data

### Data Cleaning
- Fixing bad data could involve
  - Empty Cells
  - Data in wrong format
  - Wrong data
  - Duplicates
#### Empty Cells  
- Empty Cells potentially give you a wrong result when you analyze data
  ##### Remove Rows
  - one way to deal with empty cells is to remove rows that contain empty cells
  - This is usually OK, since data sets can be very big and removing a few rows will
  - not have a big impact on the result
  - We can use `df.dropna()` also by default `dropna` returns a new dataframe
  - To change original dataframe do `df.dropna(inplace=True)`
  ##### Replace Empty Values
  - Another way of dealing with empty cells is to insert a new value instead
  - `df.fillna(130, inplace=True)` where 130 is the replacing value for NULL
  - Replacing Only For a Specified Columns
  - We have to specify the column name to do this
  - `df["column_name"].fillna(130, inplace=True)`
  - Replacing using `Mean, Median, Mode`
  - `x = df["column_name"].mean()`
  - `x = df["column_name"].median()`
  - `x = df["column_name"].mode()[0]`
  - `df["column_name"].fillna(x, inplace=True)`
  
#### Cleaning Data of Wrong Format
- You either remove the row
- Convert all cells in the columns into the same format
- Change a columns datatype to Date for example
- `df["Column_name"] = pd.datetime(df['Date'])`
- If we have an empty date we can drop the row `df.dropna(subset=['Date'], inplace=True)`
- in the date column

#### Fixing Wrong Data
- Wrong data can be `empty cells` or `wrong format` or wrong entry
  ##### Replacing Values
  - `df.index(7)` Gets row 7 
  - `df.index(7)["column_name"] = value` Does not work
  - `df8.loc[7, "column_name"] = 45` this is the fix
  - `row and column`
  - `df.drop` to remove the row
  - `df.index` gives the index for all rows
  
#### Removing Duplicates
- `df.duplicated()` to discover duplicates

### Data Correlations
- Finding Relationships
- Using the `df.corr()`
- Note `corr()` ignore `not numeric` columns
- The number varies from -1 to 1
- 1 (means 1 to 1) perfect correlation
- 0.9 pretty good correlation and if you increase one value, the other will probably increase as well
- -0.9 is just as good but means if you increase one value the other will probably go down
- 0.2 Means the correlation is low and increasing one value does not mean the other will
- `django-pandas`

### Data Plotting
- [Data Plotting](https://www.w3schools.com/python/pandas_plotting.asp)


