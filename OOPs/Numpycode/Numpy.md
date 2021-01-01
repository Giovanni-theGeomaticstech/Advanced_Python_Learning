## Numpy Learning

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