# See https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/
# See also https://stackoverflow.com/questions/46385999/transform-an-image-to-a-bitmap

from PIL import Image
import numpy as np
import sys
import cv2
import os

for root, dirs, files in os.walk('/Users/apple/desktop/text_img'):
    for file in files:
        fname = os.path.join(root, file)
        _, fext = os.path.splitext(fname)
        if fext!='.jpg':
            continue

        # Do your task here

        img = Image.open(fname)
        ary = np.array(img)

        # Split the three channels
        r,g,b = np.split(ary,3,axis=2)
        r,g,b = r.reshape(-1),g.reshape(-1),b.reshape(-1)

        # Standard RGB to grayscale
        thres = 150 #
        bitmap = list(map(lambda x: 0.299*x[0]+0.587*x[1]+0.114*x[2], 
        zip(r,g,b)))
        bitmap = np.array(bitmap).reshape([ary.shape[0], ary.shape[1]])
        bitmap = np.dot((bitmap > thres).astype(float),255)
        im = Image.fromarray(bitmap.astype(np.uint8))
        im = im.convert('1')
        #im.show()

        # Resize the image to 120px height
        height = 120
        img_w, img_h = im.size
        width = int(img_w * height/img_h)
        dim = (width, height)
        resized = im.resize(dim)
        #resized = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)
        #resized.show()

        destdir = os.path.join(root, "resized")
        if not os.path.exists(destdir):
            os.mkdir(destdir)
        dstfile = os.path.join(destdir, os.path.splitext(file)[0]+".png")
        resized.save(dstfile)

        print(fname, '->', dstfile)

