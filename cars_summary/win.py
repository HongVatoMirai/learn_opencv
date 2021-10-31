import cv2

# 创建一个 window, (windowname, windowflags), 需要调用 destroyAllWindows 释放资源
cv2.namedWindow('new', cv2.WINDOW_NORMAL)
# 设置window大小 (width, height)
cv2.resizeWindow('new', 640, 480)
# 等待展示时长，单位毫秒，填0就会一直显示
cv2.imshow('new', 0)

# 等待键盘事件
key = cv2.waitKey(0)
if (key & 0xFF == ord('q')):
    print('close')
    cv2.destroyAllWindows()
