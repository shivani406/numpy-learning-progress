import numpy as np
# multiply 2 matrix of 3x3 order
a1=np.random.rand(3,3)
a2=np.random.rand(3,3)
print("matrix a is:",a1,"\n","matrix b is:",a2)
print("multiplication is",np.dot(a1,a2))


#Create a 1D array of numbers from 0 to 9.
print(np.arange(10))
#Create a 3x3 array filled with zeros.
zeroarr=np.zeros((3,3))
print(zeroarr)
#Create a 4x4 identity matrix.
onearr=np.ones((4,4))
print(onearr)

#Find the shape, size, and data type of an array.
samplearr=np.random.rand(3,4,4)
print("dimension of array is:",samplearr.shape)
print("number of elments in array is:",samplearr.size)
print("data type of the elements in the array is:", samplearr.dtype)

#Reshape a 1D array of 12 elements into a 3x4 array.
arr_1d=np.arange(12)
print("array before:",arr_1d)
arr_1d=arr_1d.reshape(3,4)
print("array after rehshaping:",arr_1d)

#Add, subtract, multiply, and divide two 1D arrays element-wise.
arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])
print("Additon is:",np.add(arr1,arr2))
print("Subtraction is:",np.subtract(arr1,arr2))
print("Mutltiplication is:",np.multiply(arr1,arr2))
print("Division is:",np.divide(arr1,arr2))
#Square every element in a NumPy array.
print(np.power(arr1,2))
#Access the 3rd element of a 1D array.
print(arr1[2])
#Access the element at row 2, column 3 in a 2D array.
arr_2d=np.random.rand(3,3)
print(arr_2d[1][2])
#Slice a 1D array to get elements from index 2 to 6.
justanarr=np.arange(15)
print(justanarr[2:6])

#Find all elements in an array greater than 5.

a=np.array([[1, 6, 3], [8, 5, 10], [2, 7, 4]])
for i in a:
    for j in i:
        if j>5:
            print(j," ")
#Replace all negative values in an array with 0.
neg_arr=np.array([[-3, 6, -1], [8, 0, -5], [-2, 7, 4]])
for i in range(neg_arr.shape[0]): #iterate on rows
    for j in range(neg_arr.shape[1]): # iterate on columns
        if neg_arr[i][j]<0:
            neg_arr[i][j]=0
print("final array is:",neg_arr)

#Calculate the mean, median, standard deviation, and sum of an array.
np_array=np.random.rand(10)
print("original array is:", np_array)
print("mean of array is:",np.mean(np_array))
print("median of array is:",np.median(np_array))
print("std dev of array is:",np.std(np_array))

#Normalize an array so that its values range between 0 and 1 in a 3x3 array
np_arr=np.array([[[1, 6, 3], [8, 5, 10], [2, 7, 4]],
                      [[3, 1, 5], [9, 2, 8], [6, 4, 7]],
                      [[7, 3, 9], [4, 6, 2], [5, 8, 1]]])
minm=np.min(np_arr)
maxm=np.max(np_arr)
print("array before:",np_arr)
for i in range(np_arr.shape[0]):
    for j in range(np_arr.shape[1]):
        for k in range(np_arr.shape[2]):
            np_arr[i][j][k]=((np_arr[i][j][k])-minm)/(maxm-minm)
           
print("array after normalization",np_arr)
#Perform matrix multiplication between two 2D arrays.
#Find the determinant and inverse of a square matrix.
#Sort a 1D array in ascending and descending order.
#Find the indices of the top 3 largest elements in a 1D array.
