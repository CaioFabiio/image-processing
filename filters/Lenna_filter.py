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
        
im3 = im2.astype('float')

"""filtro = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
for l in range(1, lin - 1):
    for c in range(1, col - 1):
        R = np.multiply(im2[l-1:l+2, c-1:c+2, 0], filtro).sum()
        G = np.multiply(im2[l-1:l+2, c-1:c+2, 1], filtro).sum()
        B = np.multiply(im2[l-1:l+2, c-1:c+2, 2], filtro).sum()
        im3[l,c,:]=R,G,B"""

filtro = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
for l in range(1, lin - 1):
    for c in range(1, col - 1):
        R = np.multiply(im2[l-1:l+2, c-1:c+2, 0], filtro).sum()
        G = np.multiply(im2[l-1:l+2, c-1:c+2, 1], filtro).sum()
        B = np.multiply(im2[l-1:l+2, c-1:c+2, 2], filtro).sum()
        im3[l,c,:]=R,G,B
        
plt.figure()
plt.subplot(231)
plt.imshow(im)
plt.subplot(232)
plt.imshow(im2)
plt.subplot(233)
plt.imshow(abs(im3).astype("uint8"))

plt.show()