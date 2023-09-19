import numpy as np

a = np.array([1,2,3])
print(a)
b = np.array([[1,2,3,3,6],[3,4,4,5,1],[2,1,1,2,1]], dtype='int16')    #you can setup different data type. default is int32
print(b[1,1])
print(b.ndim)   # dimension
print(a.shape)  # shape and size of the matrix
print(b.shape)
print(a.dtype)  # type of variable.

print(b[0, :]) # first colomn all lines
print(b[:,0])  # first line all colomns. etc
print(b[2, 0:5:2])  # start:end:step
b[2,0] = 69
print(b[2, 0:5:2])

c = np.zeros((2,3,4))    # initiate a matrix full of zeroes. in this case, 4 numbers, three times, twice.
print(c)
d = np.ones((2,3,4))     # initiate a matrix full of ones. in this case, 4 numbers, three times, twice.
print(d)
e = np.full((2,3,4), 99) # initiate a matrix full of any number. in this case, 4 numbers, three times, twice.
print(e)
f = np.full_like(c, 5)   # same shape as C, but full of 5's.
print(f)
g = np.random.rand(3,4)  # makes a matrix of given shape, full of random numbers 0 to 1
print (g)
for i in range(4):
    g[0,i] = int(g[0,i] * 10)
print(g)

h = np.random.randint(1,3, size=(3,3))   # random ints, start and end, exclusive, and specify the shape
print(h)

test_matrix = np.full((5,5),1)
test_matrix[1:4,1:4] = 0
test_matrix[2,2] = 9
print(test_matrix)

a = np.array([1,2,3])
b = a
b[0] = 100  #this chances a aswell
print(a)    

c = a.copy()   #this makes a copy
c[0] = -2
print(a,b,c)
 
c += 2    # applies to every element within
print(c)

# you can also get min and max. and sum.

quiz_matrix = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
print(quiz_matrix)
print(quiz_matrix[2:4,0:2])
print(quiz_matrix[0:4:1,1:5:1])
print(quiz_matrix[[0,1,2,3],[1,2,3,4]])
print(quiz_matrix[[0,4,5],3:])