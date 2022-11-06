import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

pic = np.array(Image.open('Einstein_tongue.jpg'))

U,S,V = np.linalg.svd(pic)

comps = np.arange(0,5)
recon_pic = U[:,comps] @ np.diag(S[comps]) @ V[comps,:]

# plotting
plt.figure(figsize=(5,10))
plt.subplot(1,2,1)
plt.imshow(pic, cmap='gray')
plt.title("Original doggo")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(recon_pic, cmap='gray')
plt.title("Components %s-%s" %(comps[0], comps[-1]))
plt.axis('off')

plt.show()