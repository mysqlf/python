#!/usr/bin/env python
__author__ = 'CQC'
# -*- coding:utf-8 -*-
import urllib
import urllib.request
import urllib.parse
import re
import os
import time
import random

# 处理页面标签类


class Tool:
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()将前后多余内容删除
        return x.strip()


# 百度贴吧爬虫类
class BDTB:

    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self, baseUrl):
        # base链接地址
        self.baseURL = baseUrl
        # 是否只看楼主
        #self.seeLZ = '?see_lz='+str(seeLZ)
        # HTML标签剔除工具类对象
        self.tool = Tool()
        # 全局file变量，文件写入操作对象
        self.file = None
        # 楼层标号，初始为1
        self.floor = 1
        # 默认的标题，如果没有成功获取到标题的话则会用这个标题
        self.defaultTitle = u"cc" + \
            str(time.strftime('%Y-%m-%d', time.localtime(time.time()))) + \
            str(random.randint(10, 20))
        # 是否写入楼分隔符的标记
        #self.floorTag = floorTag

    # 传入页码，获取该页帖子的代码
    def getPage(self, pageNum):
        try:
            # 构建URL
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            # 返回UTF-8格式编码内容
            return response.read().decode('utf-8')
        # 无法连接，报错
        except URLError as e:
            if hasattr(e, "reason"):
                print("连接百度贴吧失败,错误原因"), e.reason
                return None

    # 获取帖子标题
    def getTitle(self, page):
        # 得到标题的正则表达式
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>', re.S)
        result = re.search(pattern, page)
        if result:
            # 如果存在，则返回标题
            return result.group(1).strip()
        else:
            return None

    # 获取帖子一共有多少页
    def getPageNum(self, page):
        # 获取帖子页数的正则表达式
        pattern = re.compile(
            '<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    # 获取每一层楼的内容,传入页面内容
    def getContent(self, page):
        request = urllib.request.Request(page)
        response = urllib.request.urlopen(request)
        # 匹配所有楼层的内容
        pattern = re.compile(
            '<div class="tpc_content do_not_catch.*?>(.*?)</div>', re.S)
        #items = re.findall(pattern,response)
        return request
        contents = []
        for item in items:
            # 将文本进行去除标签处理，同时在前后加入换行符
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content)
        return contents

    def setFileTitle(self, title):
        # 如果标题不是为None，即成功获取到标题
        if title is not None:
            self.file = open(title + ".txt", "w+")
        else:
            self.file = open(self.defaultTitle + ".txt", "w+")

    def writeData(self, contents):
        # 向文件写入每一楼的信息
        for item in contents:
            # if self.floorTag == '1':
            #     #楼之间的分隔符
            #     floorLine = "\n" + str(self.floor) + u"-----------------------------------------------------------------------------------------\n"
            #     self.file.write(floorLine)
            # .decode('utf-8','ignore')
            self.file.write(item.decode('utf-8', 'ignore'))
            self.floor += 1

    # 获取页面所有图片
    def getAllImg(self, page):
        pattern = re.compile('<div id="read_tpc.*?>(.*?)</div>', re.S)
        # 个人信息页面所有代码
        content = re.search(pattern, page)
        return content
        # 从代码中提取图片
        patternImg = re.compile('<img.*?src="(.*?)"', re.S)
        images = re.findall(patternImg, content.group(1))
        return images

    # 写入图片
    def saveImg(self, imageURL, imgPath):
        request = urllib.request.Request(imageURL)
        u = urllib.request.urlopen(request)
        #u = urllib.request.urlopen(imageURL)
        data = u.read()
        name, ext = os.path.splitext(imageURL)
        fileName = str(imgPath + '.' + ext)
        f = open(fileName, 'wb')
        f.write(data)
        f.close()
        return fileName
    # 创建新目录

    def mkdir(self, path):
        path = path.strip()
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            return False

    def start(self):
        pageNum = 1
        #indexPage = self.getPage(1)
        #pageNum = self.getPageNum(indexPage)
        #title = self.getTitle(indexPage)
        # self.setFileTitle(title)
        if pageNum == None:
            print("URL已失效，请重试")
            return
        try:
            contents = self.getContent(self.baseURL)
            print("该帖子共有" + str(contents) + "页")
            # self.writeData(contents)
            # print ("该帖子共有" + str(pageNum) + "页")
            # for i in range(1,int(pageNum)+1):
            #     print ("正在写入第" + str(i) + "页数据")
            #     #page = self.getPage(i)
            #     contents = self.getContent(self.baseURL)
            #     self.writeData(contents)
            # image=self.getAllImg(self.baseURL)
            #print ("正在复制图片" + str(image))
            # if len(image)>0:
            #     for j in range(0,len(image)):
            #         #now = time.strftime("%Y")
            #         path='image/'+str(time.strftime("%Y"))+'/'+str(time.strftime("%m"))+'/'+str(time.strftime("%d"))+'/'
            #         self.mkdir(path)
            #         name=path+str(random.randint(10,20))+str(j)
            #         #name='image/'+str(i)+str(time.strftime('%Y-%m-%d',time.localtime(time.time())))+str(random.randint(10,20))+str(j)
            #         fileName=self.saveImg(image[j],name)
            #         print ("正在复制图片" + str(fileName))
        # 出现写入异常
        except OSError as e:
            print("写入异常，原因" + e.message)
        finally:
            print("写入任务完成")


print("请输入帖子代号")
baseURL = 'http://og.90cl.org/htm_data/20/1605/' + \
    str(input(u'http://og.90cl.org/htm_data/20/1605/'))
#seeLZ = input("是否只获取楼主发言，是输入1，否输入0\n")
#floorTag = input("是否写入楼层信息，是输入1，否输入0\n")
bdtb = BDTB(baseURL)
bdtb.start()
