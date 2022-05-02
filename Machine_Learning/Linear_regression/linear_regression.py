import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 
from sklearn import linear_model

# Method 1: Draw Parabol
# # random data
# b = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46,42,39,31,30,28,20,15,10,6]
# A = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

# plt.plot(A,b,'ro')

# # Change row vector to column vector
# A = np.array([A]).T
# b = np.array([b]).T

# # create vector A square

# x_square = np.array([A[:,0]**2]).T
# A = np.concatenate((x_square,A), axis =1)


# # create vector 1
# ones = np.ones((A.shape[0],1), dtype=np.int8)

# #combine 1 and A
# A = np.concatenate((A, ones), axis =1)

# #Use fomular
# x = np.linalg.inv(A.transpose().dot(A)).dot(A.transpose()).dot(b)

# x0 = np.linspace(1,25,10000)
# y0 = x[0][0] * x0 * x0 + x[1][0] * x0 + x[2][0]

# #test predicting data
# x_test = 12
# y_test = x_test * x[0][0] + x[1][0]
# print(y_test)

#Method 2 : Use library draw line

# Random data
A = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
b = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

# Create model
lr = linear_model.LinearRegression()
# Fit (train the model)
lr.fit(A,b)
# Draw random data
plt.plot(A,b,'ro')
# Draw line: a: coefficient , b: intercept
x0 = np.array([[145,186]]).T
# x0 = np.linspace(145,186,2)
y0 = x0*lr.coef_ + lr.intercept_

# # Method 3 : Not use library draw line

# # Random data
# A = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# b = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T
# # Draw random data
# plt.plot(A,b,'ro')

# # creat ones
# ones = np.ones((A.shape[0],1), dtype = np.int8)

# # combine 1 and A
# A = np.concatenate((A,ones), axis=1)

# # Use fomular
# x = np.linalg.inv(A.transpose().dot(A)).dot(A.transpose()).dot(b)

# # Test data to draw
# # x0 = np.array([[1,180]]).T
# x0 = np.linspace(145,185,200)
# y0 = x0*x[0][0] + x[1][0]

plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')

x_test = 155
y_test = x_test* lr.coef_ + lr.intercept_

print("Weight: " + str(y_test))

plt.plot(x0,y0)
plt.show()