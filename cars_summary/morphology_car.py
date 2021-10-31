import cv2

cap = cv2.VideoCapture('video.mp4')

bgsubmog = cv2.bgsegm.createBackgroundSubtractorMOG()

#形态学kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

while True:
    ret, frame = cap.read()
    if(ret == True):     

        #灰度
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #去噪（高斯）去掉一些草，叶子
        blur = cv2.GaussianBlur(frame, (3,3), 5)

        #去背影 剩下运动的显眼的物体
        mask = bgsubmog.apply(blur)

        cv2.imshow('no bg', mask)

        # #腐蚀， 去掉图中外部小斑块，比如树枝，叶子
        # erode = cv2.erode(mask, kernel) 

        # #膨胀， 还原放大
        # dilate = cv2.dilate(erode, kernel, iterations = 3)

        # 等效的开操作
        dilate = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        cv2.imshow('open ex', dilate)

        #闭操作，去掉汽车物体内部的小块
        close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
        close = cv2.morphologyEx(close, cv2.MORPH_CLOSE, kernel)

        cv2.imshow('close ex', close)

    key = cv2.waitKey(1)
    if(key == 27):
        break

cap.release()
cv2.destroyAllWindows()