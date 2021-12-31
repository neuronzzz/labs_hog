#!/usr/bin/env python

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read image
img = cv2.imread('runner.jpg')
img = np.float32(img) / 255.0  # 归一化

# 计算x和y方向的梯度
gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=1)
gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=1)

# 计算合梯度的幅值和方向（角度）
mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)

# plt.imshow(gx)
# plt.imshow(gy)
# plt.imshow(mag)
plt.imshow(angle)

plt.title("angle")
plt.show()
# plt.savefig("gx.png", bbox_inches='tight')
