from skimage import io
import matplotlib.pyplot as plt
import numpy as np

im = io.imread("Lenna.png")

print(im.shape)
lin,col,prof = im.shape

im2 = np.zeros((lin,col,prof), 'uint8')

filtro = np.ones((3,3))
filtro /= 9

for l in range(1, lin - 1):
    for c in range(1, col - 1):
        R = np.multiply(im[l-1:l+2, c-1:c+2, 0], filtro).sum()
        G = np.multiply(im[l-1:l+2, c-1:c+2, 1], filtro).sum()
        B = np.multiply(im[l-1:l+2, c-1:c+2, 2], filtro).sum()
        im2[l,c,:]=R,G,B
        
plt.figure()
plt.subplot(211)
plt.imshow(im)
plt.subplot(212)
plt.imshow(im2)

plt.show()