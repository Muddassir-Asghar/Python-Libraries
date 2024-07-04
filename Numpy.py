import numpy as np

# Array creation
arr = np.arange(24).reshape((4, 6))

print("Original array:")
print(arr)

# Operations on ndarrays
print("\n.ndim:", arr.ndim)  # Number of dimensions

print("\n.dtype:", arr.dtype)  # Data type of the array elements

print("\n.shape:", arr.shape)  # Shape of the array

print("\n.reshape:")
reshaped_arr = arr.reshape((6, 4))
print(reshaped_arr)  # Reshape the array

# Indexing
print("\nIndexing:")
print("Element at [2, 3]:", arr[2, 3])  # Accessing element at specific index

# Using np.arange and np.random.permutation
print("\nnp.arange:")
arrange_arr = np.arange(10)
print(arrange_arr)

print("\nnp.random.permutation:")
permutation_arr = np.random.permutation(arrange_arr)
print(permutation_arr)

# Slicing
print("\nSlicing:")
print("array[1:3]:", arr[1:3])  # Slicing from index 1 to 2
print("array[:3]:", arr[:3])  # Slicing from start to index 2
print("array[2:]:", arr[2:])  # Slicing from index 2 to end
print("array[::-1]:", arr[::-1])  # Reversing the array
print("array[:, ::2]:", arr[:, ::2])  # Slicing with step

# Indexing with lists
print("\nIndexing with lists:")
indexing_arr = np.array([1, 2, 3, 4, 5])
print("array[[0, 2, 4]]:", indexing_arr[[0, 2, 4]])  # Elements at index 0, 2, 4

bool_arr = np.array([True, False, True, False, True])
print("array[[True, False, True, False, True]]:", indexing_arr[bool_arr])

# Conditional indexing
print("\nConditional indexing:")
cond_indexing_arr = np.array([1, 2, 3, 4, 5])
print("array[array < 3]:", cond_indexing_arr[cond_indexing_arr < 3])
print("array[(array > 1) & (array < 4)]:", cond_indexing_arr[(cond_indexing_arr > 1) & (cond_indexing_arr < 4)])

# Broadcasting
print("\nBroadcasting:")
broadcasting_arr = np.array([1, 2, 3, 4, 5])
print("array + 5:", broadcasting_arr + 5)

# Stacking
print("\nnp.hstack:")
hstack_arr = np.hstack((arrange_arr, arrange_arr))
print(hstack_arr)

print("\nnp.vstack:")
vstack_arr = np.vstack((arrange_arr, arrange_arr))
print(vstack_arr)

# Sorting
print("\nnp.sort:")
sort_arr = np.sort(permutation_arr)
print(sort_arr)

print("\nufuncs:")
ufunc_arr = np.arange(5)
print("ufunc_arr: ", ufunc_arr)
print("np.sqrt(array):", np.sqrt(ufunc_arr))
print("np.exp(array):", np.exp(ufunc_arr))
print("np.sin(array):", np.sin(ufunc_arr))
