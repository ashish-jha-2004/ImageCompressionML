import sys
from skimage import io
from sklearn.cluster import KMeans
import numpy as np

filename = sys.argv[1]
image = io.imread(filename)
rows, cols = image.shape[0], image.shape[1]
image = image.reshape(rows * cols, 3)
print('Compressing...')
print('Note: This can take a while for a large image file.')
kMeans = KMeans(n_clusters = 16)
kMeans.fit(image)
centers = np.asarray(kMeans.cluster_centers_, dtype=np.uint8)
labels = np.asarray(kMeans.labels_, dtype = np.uint8)
labels = np.reshape(labels, (rows, cols))
print('Almost done.')
newImage = np.zeros((rows, cols, 3), dtype=np.uint8)

for i in range(rows):
    for j in range(cols):
            newImage[i, j, :] = centers[labels[i, j], :]
io.imsave(filename.split('.')[0] + '-compressed.png', newImage)

print('Image has been compressed sucessfully.')
