import numpy as np

# np.array for an array structure
arr = np.array([1, 3, 5, 6])
print(arr)

# We can pass a list, tuple or any array-like object into the array()
# It will be converted to ndarray


# Dimensions in Arrays
# A dimension in arrays is one level of array depth (nested arrays)

# O-D array
arr0D = np.array(43)
print(arr0D)

# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array
# 1-D array
arr1D = np.array([1, 2, 3, 5])
print(arr1D)

# 2-D Arrays
# An nd array with 1D Arrays
arr2D = np.array([[3, 4, 5, 0], [1, 2, 3, 5]])
print(arr2D)

# 3-D arrays
# An array that has 2-D arrays (matrices) as its elements is called 3-D array
# Often used to represent 3rd order tensor
arr3D = np.array([[[3, 4, 5, 9], [1, 2, 3, 5]], [[5, 4, 0, 98], [9, 2, 3, 5]]])

# Check Number of Dimensions
print(arr0D.ndim)
print(arr1D.ndim)
print(arr2D.ndim)
print(arr3D.ndim)

# Higher Dimensional Arrays

arr4D = np.array([1, 2, 3, 5], ndmin=4)
print(arr4D)
print(arr4D.ndim)

# We can do normal indexing
# Access the 2nd element on 1st dim
arr2Dtest = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Way 1 :", arr2Dtest[0][1])
print("Way 2: ", arr2Dtest[0, 1])

arr3Dtest = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3Dtest[0, 1, 2])

# Use negative indexing to access an array from the end

# SLicing

# Negative Slicing

arr1Dtest = np.array([1, 2, 3, 4, 5, 6, 7])



# Checking the Data Tyoe of an Array
print("Data type of an array int: ", arr1D.dtype)
print("Data type of an array str: ", np.array(["fj", "fig"]).dtype)

# Creating array with defined datatype
arrS = np.array([1,2,3,4,5], dtype='S')
print(arrS)

# We can also define size too for
# i, u, f, S, U

arrayInt4 = np.array([1,2,3,4], dtype='i4')
print(arrayInt4)

# Converting Data Type on Existing Arrays
# The best way to change the data type of an existing array is to make a copy
# of the array with astype() method
# Astype() creates a copy of the array and allows you to specify the data type as a parameter

arrayfloat = arrayInt4.astype('f')
print(arrayfloat)
print(arrayfloat.dtype)

arraybool = arrayInt4.astype(bool)
print(arraybool)
print(arraybool.dtype)


# View vs Copy

arrOrig = np.array([0, 0, 0], dtype=float)
print(arrOrig)
arrCopy = arrOrig.copy()
arrView = arrOrig.view()
print(arrCopy)
arrOrig[0] = 42
print(arrOrig)
print(arrView)

print("Arrcopy owns its data:", arrCopy.base)
print("Arrview owns its data:", arrView.base)


# Array shape
print("\n")
arrshp0 = np.array([1, 2, 3, 4, 5]).astype("U")
print(arrshp0.shape)
# Shape prints the array dimensions and elements within the dimension
arrshp1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arrshp1.shape)

arrshp2 = np.array([1, 2, 3, 4], dtype="S", ndmin=5)
print(arrshp2)
print(arrshp2.shape)
