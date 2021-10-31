import cv2

min_w = 90
min_h = 90

cap = cv2.VideoCapture('video.mp4')

bgsubmog = cv2.bgsegm.createBackgroundSubtractorMOG()

#形态学kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

def center(x, y, w, h):
    x1 = int(w/2)
    y1 = int(h/2)
    cx = x + x1
    cy = y + y1

    return cx, cy

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

        # cv2.imshow('open ex', dilate)

        #闭操作，去掉汽车物体内部的小块
        close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
        close = cv2.morphologyEx(close, cv2.MORPH_CLOSE, kernel)

        # cv2.imshow('close ex', close)
        cnts, h = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        #画一条检测线
        # cv2.line(frame, (10, line_high), (1200, line_high), (255, 255, 0), 3)

        # i是索引值， c是轮廓
        for (i, c) in enumerate(cnts):
            (x,y,w,h) = cv2.boundingRect(c)

            #对车辆的宽高进行判断
            #以验证是否是有效的车辆
            isValid = ( w >= min_w ) and ( h >= min_h) 
            if( not isValid):
                continue

            #到这里都是有效的车 
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)
            cpoint = center(x, y, w, h)
            # cars.append(cpoint) 
            cv2.circle(frame, (cpoint), 5, (0,0,255), -1)

        cv2.imshow('contours', frame)

    key = cv2.waitKey(1)
    if(key == 27):
        break

cap.release()
cv2.destroyAllWindows()