from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlrd

#可参考项目https://github.com/wistbean/learn_python3_spider/blob/master/wechat_moment.py

desired_caps = {
  'platformName': 'Android',
  'noReset': True,
  'deviceName': '1c52020b',
  'platformVersion': '8.0.0',
  'appPackage': 'com.tencent.mm',
  'appActivity': 'com.tencent.mm.ui.LauncherUI'
 }

soursebook = xlrd.open_workbook('d:\\123.xlsx')
src_sheet = soursebook.sheet_by_index(0)
numbers = src_sheet.col_values(0)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
wait = WebDriverWait(driver, 5)
add_btn = wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/qk")))
add_btn.click()
add_frid_bn = wait.until(EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]")))
add_frid_bn.click()
btn1 = wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/den")))
btn1.click()

for num in numbers:
    strnum = str(int(num))
    btn2 = wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/li")))
    btn2.send_keys(strnum)
    btn3 = wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/nk")))
    btn3.click()
    try:
        btn4 = wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/dcj")))
        driver.save_screenshot(strnum + '.png')
        retn_btn = wait.until(EC.element_to_be_clickable((By.ID, "返回")))
        retn_btn.click()
    except:
        driver.save_screenshot(strnum + '.png')
        driver.keyevent(4)
        btn = wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/den")))
        btn.click()

driver.close()



