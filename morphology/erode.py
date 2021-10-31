
import cv2
import numpy as np

#开操作
# img = cv2.imread('./dotj.png')
#闭操作
# img = cv2.imread('./dotinj.png', 0)
#梯度操作
# img = cv2.imread('./j.png')
#顶帽操作
# img = cv2.imread('./tophat.png')
#黑帽操作
img = cv2.imread('./dotinj.png', 0)

# img = cv2.imread('./j.png')


#kernel = np.ones((7,7), np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
print(kernel)

#腐蚀
# dst = cv2.erode(img, kernel, iterations=1)

#膨胀
# dst1 = cv2.dilate(img, kernel, iterations=1)

#开运算 去掉白色噪点
# dst1 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

#闭运算 去掉里面的黑色噪点
# dst1 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

#梯度 原图-腐蚀 用来提取轮廓
# dst1 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

#顶帽 提取白色噪点 原图-开运算
# dst1 = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# 黑帽 提取字符内噪点 原图-闭运算
dst1 = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# ret,binary=cv2.threshold(img,0,255,cv2.THRESH_BINARY)
# dst1 = cv2.ximgproc.thinning(binary,thinningType=cv2.ximgproc.THINNING_ZHANGSUEN)

# cv2.imshow('dst', dst)
cv2.imshow('img', img)
# cv2.imshow('binary', binary)
cv2.imshow('dst1', dst1)
cv2.waitKey()