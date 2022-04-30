import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
import numpy
img = plt.imread(r"D:\Python_Code\Machine_Learning\K-Means_ Image Processing\a.jpg")

width = img.shape[0]
height = img.shape[1]

img = img.reshape(width*height,3)

kmeans = KMeans(n_clusters=4).fit(img)
labels = kmeans.predict(img)
clusters = kmeans.cluster_centers_

# method 1
img2 = numpy.zeros_like(img)

for i in range(len(img2)):
	img2[i] = clusters[labels[i]]

img2 = img2.reshape(width,height,3)

# # method 2

# img2 = numpy.zeros((width,height,3), dtype = numpy.uint8)
# index = 0
# for i in range(width):
# 	for j in range(height):
# 		img2[i][j] = clusters[labels[index]]
# 		index += 1

plt.imshow(img2)
plt.show()