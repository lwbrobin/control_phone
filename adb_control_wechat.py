# -*- coding: utf-8 -*-
import time
import subprocess
import xlrd
import numpy
from PIL import Image

#使用方法：修改第一列为手机号的excel文件的文件路径，再修改存放截图的文件路径。同时根据手机运行速度调整sleep_time值
# 判断图片是找到的还是没找到的
def is_image_find_or_not(image):  #image为numpy.array(Image.open(file_path))对象
    if (image[1000:2000].mean() < 248):  # 1000到2000行像素偏白则说明找到了
        return True
    else:       # 1000到2000行像素偏黑则说明没找到
        return False

sleep_time = 0.7    #每次操作的间隔时间取决于手机配置，配置越高时间越短

soursebook = xlrd.open_workbook('d:\\123.xlsx')
src_sheet = soursebook.sheet_by_index(0)
numbers = src_sheet.col_values(0)

#用popen设置shell=True不会弹出cmd框
process = subprocess.Popen('adb shell rm -r /sdcard/tmp/', shell=True)  #删除tmp文件夹
time.sleep(2 * sleep_time)
process = subprocess.Popen('adb shell mkdir /sdcard/tmp/', shell=True)  #创建tmp文件夹用于存放截图
#进入添加朋友界面
#回到桌面
process = subprocess.Popen('adb shell input keyevent 3', shell=True)
time.sleep(sleep_time)
#打开微信
process = subprocess.Popen('adb shell input tap 543 1945', shell=True)
time.sleep(sleep_time)
#点击+号搜索
process = subprocess.Popen('adb shell input tap 1010 144', shell=True)
time.sleep(sleep_time)
#点击添加朋友
process = subprocess.Popen('adb shell input tap 850 440', shell=True)
time.sleep(sleep_time)

for num in numbers:     #循环加好友
    strnum = str(int(num))
    #点到输入框
    process = subprocess.Popen('adb shell input tap 300 300', shell=True)
    time.sleep(sleep_time)
    #输入号码(输入比较慢故等待时间稍长)
    process = subprocess.Popen('adb shell input text ' + strnum, shell=True)
    time.sleep(2 * sleep_time)
    #点击搜索
    process = subprocess.Popen('adb shell input tap 500 300', shell=True)
    time.sleep(3*sleep_time)
    filepath =f'/sdcard/tmp/{strnum}.png'       #保存截图的sd卡路径
    process = subprocess.Popen('adb shell screencap '+ filepath, shell=True)    #截屏并保存到sd卡
    time.sleep(sleep_time)
    process = subprocess.Popen('adb pull '+ filepath + ' F:\\screencap', shell=True)    #把截屏从sd卡拷到F:\\screencap(需要先创建此文件夹)
    time.sleep(sleep_time)
    process = subprocess.Popen('adb shell input tap 70 132', shell=True)    #返回一次
    time.sleep(sleep_time*0.5)
    image = numpy.array(Image.open(f'F:\\screencap\\{strnum}.png'))
    if(is_image_find_or_not(image)):
        process = subprocess.Popen('adb shell input tap 70 132', shell=True)  # 找到的话需要再返回一次
        time.sleep(sleep_time)

