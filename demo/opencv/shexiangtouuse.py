from cv2 import *
import time
import sys,pygame
pygame.init()

size = width, height = 620, 485
speed = [2, 2]
black = 0, 0, 0

pygame.display.set_caption('视频窗口@dyx1024') 
screen = pygame.display.set_mode(size)
SLEEP_TIME_LONG = 0.1
# 加载摄像头
cam = VideoCapture(0)   # 0 -> 摄像头序号，如果有两个三个四个摄像头，要调用哪一个数字往上加嘛
# 抓拍十张小图片
while True:
    #抓图
    s, img = cam.read()
    if s:
        imwrite("test.jpg",img)
    #加载图像
    image = pygame.image.load('test.jpg')
    #传送画面
    screen.blit(image, speed)
    #显示图像
    pygame.display.flip()
    #休眠一下，等待一分钟
    time.sleep(SLEEP_TIME_LONG)
