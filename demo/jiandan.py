#!/usr/bin/env python
__author__ = 'CQC'
# -*- coding:utf-8 -*-
import urllib.request
import os
import re
class BDTB:
    #初始化，传入基地址，是否只看楼主的参数
    def __init__(self,url,path,page):
        #base链接地址
        self.url = url
        #base链接地址
        self.path = path
        #base链接地址
        self.page = page
    def url_open(self,url):
        req = urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
        response = urllib.request.urlopen(req)
        return response.read()

    def get_page(self):
        html = self.url_open(self.url).decode('utf-8')#self.url
        pattern = r'<span class="current-comment-page">\[(\d{4})\]</span>' #正则表达式寻找页面地址

        page = int(re.findall(pattern,html)[0])
        return page



    def find_imgs(self,page_url):
        pattern = r'<img src="(.*?\.jpg)"'
        html = self.url_open(page_url).decode('utf-8')
        img_addrs = re.findall(pattern,html)
        return img_addrs

    def saveImg(self,imageURL,imgPath):
        for i in range(0,int(len(imageURL))):
            print("原因"+str(imageURL[i]))
            request =urllib.request.Request(imageURL[i])
            u = urllib.request.urlopen(request)
            #u = urllib.request.urlopen(imageURL)
            data = u.read()
            name, ext = os.path.splitext(imageURL[i])
            fileName=str(imgPath+'.'+ext)
            f = open(fileName, 'wb')
            f.write(data)
            f.close()

    def save_imgs(self,img_addrs,page_num):
        self.mkdir(str(page_num))
        os.chdir(str(page_num))
        for i in img_addrs:
            pattern = r'sinaimg.cn/mw600/(.*?).jpg'
            filename = i.split('/')[-1]
            image = self.url_open(i)
            with open(filename,'wb') as f:
                f.write(image)
                f.close()
    def mkdir(self):
        path = self.path.strip()
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists=os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            return False

    def download_mm(self):
        self.mkdir() #新建文件夹
        os.chdir(self.path) #跳转到文件夹
        #print("连接百度贴吧失败,错误原因")
        folder_top = os.getcwd() #获取当前工作目录
        #url = 'http://jandan.net/ooxx/'
        page_num = self.get_page() #获取网页最新的地址
        for i in range(self.page):
            page_num -= i #递减下载几个网页
            page_url = self.url + 'page-' + str(page_num) + '#comments' #组合网页地址
            img_addrs = self.find_imgs(page_url) #获取图片地址
            print("原因"+str(len(img_addrs)))
            self.saveImg(img_addrs,page_num) #保存图片
            os.chdir(folder_top)

if __name__ == '__main__':
    folder = 'D:/python/image/1989/' #input("Please enter a folder(default is 'ooxx'): " )
    pages = 5#input("How many pages do you wan to download(default is 10): ")
    url = 'http://jandan.net/ooxx/'
    #download_mm(str(folder),int(pages))
    bdtb = BDTB(url,folder,pages)
    bdtb.download_mm()