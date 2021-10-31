import cv2

cap = cv2.VideoCapture('video.mp4')

bgsubmog = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret, frame = cap.read()
    if(ret == True):     

        #灰度
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #去噪（高斯）去掉一些草，叶子
        blur = cv2.GaussianBlur(gray, (3,3), 5)

        #去背影 剩下运动的显眼的物体
        mask = bgsubmog.apply(blur)

        cv2.imshow('origin', frame)
        cv2.imshow('gray', gray)
        cv2.imshow('GaussianBlur', blur)
        cv2.imshow('mask', mask)


        key = cv2.waitKey(1)
    if(key == 27):
        break

cap.release()
cv2.destroyAllWindows()