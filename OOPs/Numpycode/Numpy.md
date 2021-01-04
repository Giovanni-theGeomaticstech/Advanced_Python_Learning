## Numpy Learning
- [Numpy Lesson](https://www.w3schools.com/python/numpy_array_reshape.asp)

### Use

- For Working with Arrays
- Also has functions for working in the domain of lin alg, fourier transform and matrices
- Numpy stands for numerical python

### Why use Numpy

- Lists are slow to process
- 50x faster than traditional lists
- Array object in `Numpy` is called `ndarray`
- `Data Science` is a branch of computer science where we study how to store, use and analyze data for
- deriving information from it.

### Why Numpy is Faster than Lists
- Numpy items are faster due to be being stored in one continuous place in memory unlike lists
- so processes can access and manipulate them very efficiently
- This behaviour is called `locality of reference` in `Computer Science`
- Numpy is also optimized to work with latests `CPU architectures`
- Numpy is written partially in Python but faster computations in `C or C++`

### Create a NumPy ndarray Object
- NumPy is used to work with arrays. The object is called `ndarray`
- `np.array()` for the array object

### Nest arrays
- are arrays that have arrays as their elements
- `0-D` or Scalars, are `the elements in an array`, 0-D Array
- `np.array(42)`
- `numpy.mat` has a whole sub module dedicated towards matrix operations
- Number of Dimensions `ndarray.ndim
- Make sure the arrays in each dimensions have the same number of elements

### Higher Dimension Arrays
- `np.array([1,2,3], ndmin=5)` where 5 is the number of dimensions

### Slicing Arrays
- [start:end]
- [start:end:step]
- If we don't pass `start` its considered 0
- If we don't pass `end` its considered length of array in that dimension
- If we don't pass `step` its considered 1
- Every other element in an array k[::2]
- k[1, [1:4]] access array at index at then index it
- k[0:2, 2] accesses the second index in the arrays 0 and 1

### Numpy Data Types
- [List of types](https://www.w3schools.com/python/numpy_data_types.asp)
- check datatyoe of an array `arr.dtype

### NumPY Array Copy vs View
- The main difference is that copy is a new array vs view is just a view of the original array
- Copy owns the data thus any changes won't affect original
- View does not own the data and any change to the view will affect the original
- view and any changes to original array will affect the view
- `arr.copy()` and `arr.view()`
- `arr.base` to check if the array owns its data.
- `None` is returned if the array owns the data if it doesnt the original array is returned

### Shape of an Array Numpy
- `arr.shape`
- `Shape` returns a tuple with each index having the number of corresponding elements
- Each integer at index tells the number of elements the corresponding dimension
    - has
    
### Reshaping of An Array
- Changing the array shape
- The shape of an array is the number of elements in each dimension
- Reshaping we can add or remove dimensions
- Reshape from 1D to 2D
- The length of the shape tuple actually tells the number of dimensions
- The first item in the dimension corresponds to the largest dimension
- The last corresponds with smallest dimension
- You are allowed to pass -1 for an unknown dimension (one unknown)
- Only one unknown dimension
- Do arr.reshape(-1) flatten array

### Iteration in Array
-  We can use `nditer()`
- Helps to solve basic issues we face in iteration
- When we do arrays for very high dimensions it is difficult to use it to get `n`
- thus we can use np.nditer(arr)
- `Numpy` does not change the datatype of element in place (where the element is in array)
- It needs space to perform this is done by the buffer
- so we need the `flags=["buffered"]` before the `op_dtypes=['S']`
- REVISIT
- Iterate scalar element of the 2D array skipping 1 element `arr[:, ::2]`
- `np.ndenumerate(arr)`

### Joining Numpy Arrays
- Joining the contents of two or more arrays in a single array
- This is done on `axes` in numpy
- we `concatenate` arrays this way along an `axis`
- if `axis` is not defined it is taken as 0
- `np.concatenate((arr1, arr2), axis=#)`
- Note `concatenate` is based on the axis. The axis must be less than the dimension
- This is done in horizontal row by row basis

- Using `stack functions` for joining
- Stacking is done along a new axis vs `concatenate` putting them
- one over the other.
- done by `np.stack((arr1, arr2), axis=#)`
- If not passed automatically consider 0
- `hstack` to stack along rows
- `arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])`
- `arr = np.hstack((arr1, arr2))` = `[1 2 3 4 5 6]`
- `np.vstack()` stacking along columns
- `np.vstack((arr1, arr2))` = `[[1 2 3], [4 5 6]]`
- `np.dstack()` stacking along height which is the same as depth
- `arr = np.dstack((arr1, arr2))` = `[[[1 4], [2 5], [3 6]]]`

### Array Search
- Search an array for a certain value and return the `indexes` that get a match
- `np.where(arr == 4)`
- Search Sorted which performs binary search in array
- It returns the index where the specified value would be inserted to maintain the search order
- `np.searchsorted(arr, 7)` returns the index in which 7 should be placed
- [searchsorted](https://www.w3schools.com/python/numpy_array_search.asp)

### Array Sort
- `np.sort()`

### Array Filter
- `arr = np.array([41, 42, 43, 44])`
- `x = [True, False, True, False]`
- `arr[x]` = [41, 43]


### Randomization
- [Randomization](https://www.w3schools.com/python/numpy_random.asp)
#### Random Array
- `from numpy import random`
- `x=random.randint(100, size=(5))`
- Make an array containing 5 random integers from 0 to 100
- `x = random.randint(100, size=(3, 5))`
- Generate an Array 2D with 3 rows and 5 random integers
- Generate random number from an array
- `random.choice(array)`

### Random Data Distribution
- [Random Distribution](https://www.w3schools.com/python/numpy_random_distribution.asp)
- data distribution is a list of all possible values and how often each value occurs
- such lists are important when working with statistics and data science
- The random module offer methods that returns randomly generated data distributions

#### Random Distribution 
- A set of random numbers that follow a certain probability density function
- `Probability Density FUnction`: A function that describes a continuous probability
- i.e probability of all values in an array
- `0 and 1 probability` 0 will not and 1 will
- `x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))`
- For eg. The probability of 3 happening is 0.1 while 7 is 0.6
#### Distributions
#### Random Permutations
- [Random Permutations](https://www.w3schools.com/python/numpy_random_permutation.asp)



