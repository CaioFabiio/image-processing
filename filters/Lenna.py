from skimage import io
import matplotlib.pyplot as plt
import numpy as np

im = io.imread("Lenna.png")

print(im.shape)
lin,col,prof = im.shape

im2 = np.zeros((lin,col,prof), 'uint8')

for l in range(lin):
    for c in range(col):
        R,G,B = im[l,c,:]
        C = 1 - ( R / 255 )
        M = 1 - ( G / 255 )
        Y = 1 - ( B / 255 )
        im2[l,c,:]=C*255,M*255,Y*255
        
plt.figure()
plt.subplot(241)
plt.imshow(im)
plt.subplot(242)
plt.imshow(im[:,:,0],cmap="gray", vmin=0, vmax=255) #R
plt.subplot(243)
plt.imshow(im[:,:,1],cmap="gray", vmin=0, vmax=255) #G
plt.subplot(244)
plt.imshow(im[:,:,2],cmap="gray", vmin=0, vmax=255) #B

plt.subplot(245)
plt.imshow(im2)
plt.subplot(246)
plt.imshow(im2[:,:,0],cmap="gray", vmin=0, vmax=255) #C
plt.subplot(247)
plt.imshow(im2[:,:,1],cmap="gray", vmin=0, vmax=255) #M
plt.subplot(248)
plt.imshow(im2[:,:,2],cmap="gray", vmin=0, vmax=255) #Y

plt.show()