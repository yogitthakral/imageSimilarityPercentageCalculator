from builtins import print

import sys

import cv2
import numpy as np



originalImage = sys.argv[1]
changedImage = sys.argv[2]


img1 = cv2.imread(originalImage, 0)
img2 = cv2.imread(changedImage, 0)

#--- take the absolute difference of the images ---
res = cv2.absdiff(img1, img2)

#--- convert the result to integer type ---
res = res.astype(np.uint8)


#--- find percentage difference based on number of pixels that are not zero ---
percentage = (np.count_nonzero(res) * 100)/ res.size

print(str((100 - percentage)) + "%")