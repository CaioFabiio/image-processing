from skimage import io, filters
import matplotlib.pyplot as plt
import numpy as np

im = io.imread("page.png")

im2 = np.zeros(im.shape)

im2[im <= 80] = 1

im3 = filters.median(im, np.ones((15, 15)))

im4 = (im/im3) * 220

t = filters.threshold_otsu(im4)
im5 = np.zeros(im.shape)
im5[im4<t] = 1

plt.figure()
plt.subplot(331)
plt.imshow(im, cmap="gray")

plt.subplot(332)
plt.imshow(im2, cmap="gray")

plt.subplot(333)
plt.imshow(im3, cmap="gray")

plt.subplot(334)
plt.imshow(im4, cmap="gray")

plt.subplot(335)
plt.imshow(im5, cmap="gray")

plt.show()
