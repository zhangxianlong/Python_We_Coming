#coding=utf-8
import sys

"""
掌握内容
1、迭代器有两个基本的方法：iter() 和 next()
2、生成器的yield函数
3、str.strip()把字符串(str)的头和尾的空格，以及位于头尾的\n \t之类给删掉,
"""

#使用生成器处理文件，用户指定要查找的内容，将文件中匹配到的行输出到屏幕
def read_file(filename,test):
    with open(filename) as file:
        for line in file:
            if test in line:
                yield line

RR = read_file('asd.txt','ds')
for readli in RR:
    print (readli.strip())

#使用生成器，从文件中读取内容，在每一行前加上指定str
def modify_file(filename,str):
    with open(filename) as file:
        for line in file:
            yield str + line

MM = modify_file('asd.txt','#####')
for modifyli in MM:
    print (modifyli.strip())

#用生成器实现裴波那契数列
def fibonacci(n):  # 生成器函数 - 斐波那契
    a = 0
    b = 1
    counter = 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
