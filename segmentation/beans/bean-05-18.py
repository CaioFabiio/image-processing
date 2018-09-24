import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from skimage import io
from skimage.segmentation import slic
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from sklearn.cluster import KMeans, MeanShift, estimate_bandwidth

white_bean = io.imread('white_bean.png')[200:-280, 200:-380]
black_bean = io.imread('black_bean.png')

wbean_slic = slic(white_bean, n_segments = 2)
bbean_slic = slic(black_bean, n_segments = 2)

w, h, d = white_bean.shape
img_array1 = np.reshape(white_bean, (w * h, d))

kmeans = KMeans(n_clusters = 3).fit(img_array1)
labels = kmeans.predict(img_array1)
white_seg = np.reshape(labels, (w, h))

plt.figure()

plt.subplot(121)
plt.imshow(wbean_slic)
plt.subplot(122)
plt.imshow(white_bean)

plt.imshow(white_seg)

plt.show()
