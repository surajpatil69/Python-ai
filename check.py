import numpy as np

# l1 = [10, 20, 30, 50]
# n1 = np.array(l1)
# print(n1)
# print(type(n1))

# n2 = np.array([[20, 30, 60, 70], [50, 89, 67, 56]])
# print(n2)
# type(n2)


#zeros method
# n3 = np.zeros((2, 3))
# print(n3)


# n4 = np.zeros((3, 3))
# print(n4)

# # full

# n1=np.full((3,3),44)
# print(n1)

# n5=np.arange(50,101)
# print(n5)

# # n5=np.arange(50,500,10)
# # print(n5)

# n6=np.random.randint(100,200,10)
# print(n6)

# #shape of numpy array 
# n7=np.array([[1,2,3,4,5,6],[9,8,7,6,3,2]])
# print((n7.shape))

# n7.shape=(3,4)
# print(n7)

# joining numpy array 

# n1=np.array([10,20,30])
# n2=np.array([40,50,60])
# n3=np.vstack((n1,n2))
# print(n3)

# n3=np.hstack((n1,n2))
# print(n3)

# n3=np.column_stack((n1,n2))
# print(n3)

#intersection and difference in numpy

# n1=np.array([10,20,30,40])
# n2=np.array([50,70,30,20])
# n3=np.intersect1d(n1,n2)
# print(n3)

# n4=np.setdiff1d(n1,n2)
# n4=np.setdiff1d(n2,n1)
# print(n4)

#numpy array mathematics
    # addition of numpy array 

# n1=np.array([1,2])
# n2=np.array([3,4])
# n3=np.sum([n1,n2])
# print(n3)

# n3=np.sum([n1,n2],axis=0)
# print(n3)
# n3=np.sum([n1,n2],axis=1)
# print(n3)
# # adding element in each element 
# n1=np.array([10,30,40])
# n1=n1+1
# print(n1)

# basic multiplication
# n1 = np.array([10, 30, 40])
# n1=n1*4
# print(n1)
# # basic substraction
# n1 = np.array([10, 30, 40])
# n1=n1-4
# print(n1)
# # basic division
# n1 = np.array([10, 30, 40])
# n1=n1/4
# print(n1)

# numpy  mathematic function

# mean 

# n1=np.array([1,3,4,5,6])
# n2=np.mean(n1)
# print(n2)

# #medain

# n1 = np.array([1, 3, 4, 5, 6])
# n2 = np.median(n1)
# print(n2)

# #standard deviation
# n1 = np.array([1, 3, 4, 5, 6])
# n2 = np.std(n1)
# print(n2)

# numpy save and load
n1 = np.array([1, 3, 4, 5, 6])
n3 = np.save("my array",n1)
n3=np.load("my array.npy")
print(n3)
myarray =np.array([50,40,60])
print(myarray)
