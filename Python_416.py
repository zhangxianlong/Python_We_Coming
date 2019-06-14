#encoding=utf-8

"""
掌握内容
1、chr()函数，用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符
2、了解ASCII对照表
3、字符串拼接
"""

#题目：生成字符串a1b2c3d4e5f6g7h8i9j10
def Str1():
    strr1 = ''
    for i in range(97,107):
      strr1  = strr1 + (chr(i) + str(i-96))
    return strr1
print (Str1())

#题目：生成字符串a1B2c3D4e5F6g7H8i9J10
def Str2():
    strr = ''
    for i in range(66,76):
        if i%2 == 0:
            strr = strr + chr(i+31) + str(i-65)
        else:
            strr = strr + chr(i-1) + str(i-65)
    return strr
print (Str2())
