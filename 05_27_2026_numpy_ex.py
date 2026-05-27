import numpy as np

print("numpy version:", np.__version__)
# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print (type(array_1d))
print(array_1d)
print (array_1d.shape)
print (array_1d.ndim)   


list2 = [[1,2],[2,3],[3,4]]
print(type(list2))
print(list2)
n2dArray =np.array(list2)
print(type(n2dArray))
print(n2dArray) 
print(n2dArray.shape)
print(n2dArray.ndim)    

# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(array_2d)
print(array_2d.shape)
print(array_2d.ndim)    

# Create a 3D array 
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Array:")  
print(array_3d)
print(array_3d.shape)