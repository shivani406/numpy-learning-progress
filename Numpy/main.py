import numpy as np
a=np.random.rand(2,3) # to create array of random numbers given the size of it
print (a) 
print ("----------------")
a1=np.random.rand(3,2,3)# created a tensor 

zeroes=np.zeros((2,2,2))#fills array with 0
fullarr=np.full((2,2,2),7)#fills array with given number
onesarr=np.ones((2,2,2))#fills array with 1
print(a1,zeroes,fullarr,onesarr)

# to create a custom array
cus_arr=np.array([[2,3],[4,5]],np.int64)# 2-D array
# we can give size according to our requirement like np.int8, np.int32 etc
cus_arr1=np.array([[[2,3],[4,5]],[[5,6],[6,7]]])# 3-d array
print (cus_arr,"\n",cus_arr1)
rangearr=np.arange(15)
print(rangearr) # works similar to range function(0-14)
lspace=np.linspace(1,5,12)
print(lspace) # gives an array with 12 elements between 1-5 equally apced
print(rangearr.reshape(3,5)) # prints array reshaped with 3 rows and
# to check datatype of your array and its content
print(type(cus_arr))
print (cus_arr.dtype)
#to check the dimension of array
print(cus_arr.shape,cus_arr1.shape)
data=np.random.rand(2,2,2)
data=data.reshape(2,2,-1)# -1 states that last dimension can be anything
print(data.shape)

# to update any array
zeroes=np.zeros(8)
zeroes=np.append(zeroes,[3,4])# first give the array in whic you want to append then give the list of numbers u want to append
zeroes=np.insert(zeroes,2,1)#list,position, number

# to check the size of array
print(cus_arr.size,cus_arr1.size)

# to slice that array
print(cus_arr[0][1])# same as in  python, slicing can be performed in the same way as in python

# basic mathematical opreations
ar1=np.array([[2,2],[4,4]])
ar2=np.array([[5,5],[6,6]])
sum=np.add(ar1,ar2)
print(sum)
print(np.subtract(ar1,ar2))
print(np.multiply(ar1,ar2))
print(np.divide(ar1,ar2))
print(np.dot(ar1,ar2))
print(ar1+10)# adding 10 to each element

# statistical functions
print(np.sqrt(ar1))
print(np.power(12,4))
print(np.power(ar1,2))# each element raised to the power 2
print(np.abs(-2))# mod function
lst1=np.random.rand(10)
print(np.min(lst1),np.max(lst1)) 

# sorting an array
ar3=np.array([[2,1],[4,3]])
print(np.sort(ar3))
print(np.sort(ar3)[::-1])# to sort array in desending order (only for 1-d array)

print(np.delete(ar3,1,axis=0))# 3 parameters, first is name od arr, 2nd is the number of row or column , axis=0 : row, axis=1:column

# value of any element can be changed in the same way as we do in a list.