#encoding=utf-8

import os

"""
掌握内容
1、学习os模块、file模块
2、open(file, mode='')方法用于打开用于打开一个文件，并返回文件对象
题目
新建一个txt文件，添加10行数据,然后再删除第8行数据
"""

#新建一个txt文件
def Creat_txt(name):
    current_path = os.getcwd()
    file_path = current_path + '\\' + name + '.txt'
    file = open(file_path,'w')
    file.close()
    return file_path

#在新建的txt文件中增加10行数据
def Add_txt(name):
    if Creat_txt(name):
        add_file = open(Creat_txt(name), 'w')
        for i in range(1,11):
            add_file.write('这是第'+str(i)+'行'+'\n')
        return add_file
        file.close()
    else:
        return '文件不存在'

#删除第8行
def Del_txt(name):
    with open(name+".txt", "r", encoding="GBK") as old:
        lines = old.readlines()
        # print(lines)
    with open(name+".txt", "w", encoding="GBK") as new:
        for line in lines:
            if "这是第8行" in line:
                continue
            new.write(line)

name = 'test_txt'
print (Creat_txt(name))
Add_txt(name)
Del_txt(name)