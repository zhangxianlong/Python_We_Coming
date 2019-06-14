#coding=utf-8

import os
"""
题目
1、实现adb几个命令的封装
"""

# 获取Android手机系统版本
def get_android_version():
    command = 'adb shell getprop ro.build.version.release'
    result = str(os.popen(command).read())
    if result != '':
        version = result
        return version
    else:
        return None

# 获取Android手机序列号
def get_android_device():
    command = 'adb devices'
    device_list = []
    result = os.popen(command)
    for line in result.readlines():
        if not line.startswith("List"):
            device = str(line).split("	")[0]
            device_list.append(device)
            return device_list

#获取Android手机上的包名
def get_activity_name():
    command = 'adb shell pm list packages'
    activity_name_list = []
    result = os.popen(command)
    for i in result.readlines():
        activity_name = i.strip('package')
        activity_name = activity_name.strip(':')
        activity_name = activity_name.strip('\n')
        activity_name_list.append(activity_name)
    return activity_name_list

print (get_android_version())
print (get_android_device())
print (get_activity_name())
