# -*- coding: utf-8 -*-
import time
import subprocess
import xlrd

#每次操作的间隔时间取决于手机配置，配置越高时间越短
sleep_time = 0.5
#用popen设置shell=True不会弹出cmd框

soursebook = xlrd.open_workbook('d:\\123.xlsx')
src_sheet = soursebook.sheet_by_index(0)
numbers = src_sheet.col_values(0)

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
    time.sleep(2*sleep_time)
    #截屏并保存到sd卡
    process = subprocess.Popen('adb shell screencap /sdcard/pp/' + strnum + '.png', shell=True)
    time.sleep(sleep_time)
    #返回
    process = subprocess.Popen('adb shell input tap 70 132', shell=True)
    time.sleep(sleep_time)

#把截屏图片拷贝到电脑F:\\screencap文件夹下
process = subprocess.Popen('adb pull /sdcard/pp/ F:\\screencap', shell=True)
#soursebook.close()





