#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 图片操作
# from PIL import Image
# # 打开当前路径一张图片
# im = Image.open('test.jpg')
# # 获取图片的宽高
# w, h = im.size
# print(w, h)
# # 缩放50%
# im.thumbnail((w // 2, h // 2))
# # 存储
# im.save('thumbnail.jpg', 'jpeg')
#
#
#
# 模糊效果
# from PIL import Image, ImageFilter

# im = Image.open('test.jpg')
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('Blur.jpg', 'jpeg')
#
#
# 生成验证码
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机数字


def rndChar():
    return chr(random.randint(65, 90))
# 随机颜色


def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60
# 创建图像
image = Image.new('RGB', (width, height), (255, 255, 255))
# 设置字体
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
# 创建画笔
draw = ImageDraw.Draw(image)
# 填充每个像素#背景
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 填充字符
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
#image = image.filter(ImageFilter.BLUR)
# 保存
image.save('code.jpg', 'jpeg')
