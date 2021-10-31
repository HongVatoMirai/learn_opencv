import cv2

cv2.namedWindow('video', cv2.WINDOW_AUTOSIZE)
# cv2.resizeWindow('video', 640, 480)
# 获取视频设备，通过设备id获取，一般填0，会自动获取可用的摄像头设备
cap = cv2.VideoCapture(0)
# 从视频文件读取视频帧
# cap = cv2.VideoCapture('video.mp4')

while True:
    ret, frame = cap.read()
    
    cv2.imshow('video', frame)
    key = cv2.waitKey(40)
    if (key & 0xFF == ord('q')):
        print('close')
        break

# 释放VideoCapture
cap.release()

cv2.destroyAllWindows()