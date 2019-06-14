#encoding=utf-8

"""
掌握内容
1、chr()函数，用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符
2、了解ASCII对照表，大写字母对应65-90，小写字母对应97-122
3、字符串拼接
4、list.insert(index, obj):将对象插入列表
5、python3.x版本输出不换行格式：print(x, end=" ")
"""

#题目：输出奇数字母和偶数字母到列表中
def Letter_list():
    Letter_list = []        #奇数字母和偶数字母列表
    Odd_letter_list = []    #奇数字母列表
    Even_letter_list = []   #偶数字母列表
    for i in range(65,91):
        if i%2>0:
            Odd_letter_list.append(chr(i)+chr(i+32))
        else:
            Even_letter_list.append(chr(i)+chr(i+32))

    Letter_list.insert(0,Odd_letter_list)
    Letter_list.insert(1, Even_letter_list)
    return Letter_list
print ("奇数字母列表：",end=" ")
print (Letter_list()[0])
print ("偶数字母列表：",end=" ")
print (Letter_list()[1])

