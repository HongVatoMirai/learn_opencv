// capture_save.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
#include "opencv2/highgui.hpp"
#include "opencv2/highgui/highgui_c.h"
#include "opencv2/core.hpp"
#include "opencv2/videoio/videoio_c.h"
int main()
{
    cv::VideoCapture* capture = NULL;
    cv::VideoWriter* vw = NULL;
    cv::Mat frame;

    //获取摄像头
    capture = new cv::VideoCapture(0);
    //摄像头打开失败
    if (!capture) {
        std::cout << "can not open camera";
        return -1;
    }
    else {
        //获取VideoWriter
        cv::Size size(capture->get(cv::CAP_PROP_FRAME_WIDTH), capture->get(cv::CAP_PROP_FRAME_HEIGHT));
        vw = new cv::VideoWriter("cameara.avi", CV_FOURCC('X', 'V', 'I', 'D'), 25, size);
        //VideoWriter打开失败
        if (!vw) {
            std::cout << "can not open videowriter";
            capture->release();
            return -1;
        }
        //循环读取每一帧，显示，并写入文件
        while (true) {
            //frame = cvQueryFrame(capture);
            int ret = capture->read(frame);
            if (!ret) {
                std::cout << "read frame failed" << std::endl;
                break;
            }
            vw->write(frame);
            cv::imshow("video", frame);
            if (cvWaitKey(10) > 0) {
                break;
            }
        }
    }
    //释放资源
    if (capture) {
        printf("close capture\n");
        capture->release();
    }
    if (vw) {
        printf("close videowriter\n");
        vw->release();
    }
    cvDestroyAllWindows();
    return 0;
}
