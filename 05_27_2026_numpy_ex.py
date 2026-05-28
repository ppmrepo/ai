# import numpy as np

# # # # print("numpy version:", np.__version__)
# # # # # Create a 1D array
# # # # array_1d = np.array([1, 2, 3, 4, 5])
# # # # print("1D Array:")
# # # # print (type(array_1d))
# # # # print(array_1d)
# # # # print (array_1d.shape)
# # # # print (array_1d.ndim)   


# # # # list2 = [[1,2],[2,3],[3,4]]
# # # # print(type(list2))
# # # # print(list2)
# # # # n2dArray =np.array(list2)
# # # # print(type(n2dArray))
# # # # print(n2dArray) 
# # # # print(n2dArray.shape)
# # # # print(n2dArray.ndim)    

# # # # # Create a 2D array
# # # # array_2d = np.array([[1, 2, 3], [4, 5, 6]])
# # # # print("\n2D Array:")
# # # # print(array_2d)
# # # # print(array_2d.shape)
# # # # print(array_2d.ndim)    

# # # # # Create a 3D array 
# # # # array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# # # # print("\n3D Array:")  
# # # # print(array_3d)
# # # # print(array_3d.shape)

# # # # print (np.zeros((2,3))) # 2D array of zeros
# # # # print (np.ones((3, 4)))   # 2D array of ones    
# # # # print (np.eye(4))        # 4x4 identity matrix  

# # # # print(np.arange(0, 10, 2))  # Array of even numbers from 0 to 10

# # # # print(np.linspace(0, 1, 5))  # 5 evenly spaced numbers between 0 and 1

# # # # print(type(np.random.rand(3, 3)))  # 3x3 array of random numbers between 0 and 1


# # # # list1 = [1, 2, 3, 4, 5]
# # # # array1 = np.array(list1)

# # # # print (array1[0:3])  # Output: [1 2 3]
# # # # print (array1[::2])   # Output: [1 3 5]
# # # # print (array1[::-1])  # Output: [5 4 3 2 1]
# # # # print (array1[-1])
# # # # print (array1[-3:])  # Output: [3 4 5]
# # # # print(array1[4])


# # # array2 = np.array ([[1,2,3],[4,5,6]])
# # # print(array2.ndim)  # Output: 2
# # # print(array2.shape)  # Output: (2, 3)

# # # print (array2[0,2])  # Output: 3
# # # print (array2[1,0])  # Output:  4



# # # print(array2[0,:])  # Output: [[1 2 3]
# # #                     #          [4 5 6]] 

# # # print(array2[:,1])  # Output: [[1 2 3]

# # # print (array2[1:])

# # # print (f"Array Vectorization: {array2 +2}")

# # # print (f"Array min: {np.min(array2)}")

# # # print (f"Array Sum: {np.sum(array2)}")

# # # list1 = np.array([[2,3],[4,5]])
# # # list2 = np.array([[2,1],[1,1]])

# # # print (f"Array Addition: {list1 + list2}")
# # # print (f"Array Subtraction: {list1 - list2}")
# # # print (f"Array Element-wise Multiplication: {list1 * list2}")  # Element-wise multiplication

# # # print (f"Sum of list1: {np.sum(list1)}")
# # # print(f"Array Multiplication: {np.dot(list1, list2)}")  # Matrix multiplication

# # list1 = np.array([[1, 2], [3, 4]])

# # print (f"Original Array:\n{list1}")

# # #np.random.seed(1)  # Set seed for reproducibility
# # #print (np.random.rand(2,3))
# # print (np.random.randint(1,10,(2,3)))

# # print (np.random.rand(2))

# # list1 = np.array([1, 2,3, 4])


# # list2 =list1[list1>2]
# # print (f"Filtered Array: {list2}")



# list1 = np.array([[1, 2], [3, 4]])

# print (np.sum(list1,axis=0))

# list2 = np.array([[5, 6], [7, 8]])

# print (np.vstack((list1, list2)))  # Vertical stacking

# print (np.hstack((list1, list2)))  # Horizontal stacking

import numpy as np
list1 = np.array([1, 2,4,5,6,7])

#list2=list1
list2 = list1.copy()
list1[0] = 10

print (f"List1: {list1}")
print (f"List2: {list2}")

list4= np.reshape(list1,(2,3))

print(list4.T)