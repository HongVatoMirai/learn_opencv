# todo: 不同系统的编码格式是否有特定要求？

import cv2

# 创建窗口
cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 640, 480)

# 获取视频设备，通过设备id获取，一般填0，会自动获取可用的摄像头设备
cap = cv2.VideoCapture(0)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(size)

# 指定视频编码格式
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# 创建VideoWriter
vw = cv2.VideoWriter('out.avi', fourcc, 25, size)
if (vw):
    print('vw create success')

# 判断摄像头是否打开
while cap.isOpened():
    # 从摄像头读取帧
    ret, frame = cap.read()
    
    if ret == True:
        cv2.imshow('video', frame)

        # 写文件
        vw.write(frame)

        # 等待键盘事件
        key = cv2.waitKey(1)
        if (key & 0xFF == ord('q')):
            print('close')
            break
    else:
        break

# 释放VideoCapture
cap.release()
# 释放videowriter
vw.release()

cv2.destroyAllWindows()