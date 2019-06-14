#coding=utf-8
from appium import webdriver

desired_caps = {}                                       #初始化
desired_caps['platformName'] = 'Android'                #使用哪种移动平台
desired_caps['platformVersion'] = '8.0.0'               #Android版本
desired_caps['deviceName'] = 'HMKNW17923064077'         #真机标识码
desired_caps['appPackage'] = 'com.android.calculator2'  #包名
desired_caps['appActivity'] = '.Calculator'             #Activity名

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.find_element_by_id("com.android.calculator2:id/del").click()
#最多等待10秒（隐式等待）
driver.implicitly_wait(10)
driver.find_element_by_name("2").click()
driver.find_element_by_name("0").click()
driver.find_element_by_name("0").click()
driver.find_element_by_id("com.android.calculator2:id/op_div").click()
driver.find_element_by_name("0").click()
driver.find_element_by_name(".").click()
driver.find_element_by_name("5").click()
driver.find_element_by_id("com.android.calculator2:id/op_mul").click()
driver.find_element_by_name("3").click()
driver.find_element_by_id("com.android.calculator2:id/op_add").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("0").click()
driver.find_element_by_id("com.android.calculator2:id/op_sub").click()
driver.find_element_by_name("3").click()
driver.find_element_by_id("com.android.calculator2:id/eq").click()
result = driver.find_element_by_id("com.android.calculator2:id/formula").text
print (result)
driver.quit()