#encoding=utf-8
"""
掌握内容
1、chr()函数，用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符
2、了解ASCII对照表
"""

#题目：输出大写字母到列表中,ASCII对照表中，大写字母对应65-90，
def Big_letter():
    big_list = []
    for i in range(65,91):
        big = chr(i)
        big_list.append(big)
    return big_list
print (Big_letter())

#题目：输出小写字母到列表中，ASCII对照表中，小写字母对应97-122，
def Small_letter():
    small_list = []
    for i in range(97,123):
        small = chr(i)
        small_list.append(small)
    return small_list
print (Small_letter())

#题目：输出大小写字母到列表，大写与小写相差32
def Big_Small_letter():
    Big_Small_list = []
    for i in range(97,123):
        big = chr(i-32)
        small = chr(i)
        Big_Small_list.append(big+small)
    return Big_Small_list
print (Big_Small_letter())

#题目：输出大写字母+数字
def Big_letter_num():
    letter_num_list = []
    for i in range(65,91):
        big = chr(i)
        num = str(i)
        letter_num_list.append(big+num)
    return letter_num_list
print (Big_letter_num())

#题目：输出小写字母+数字
def Small_letter_num():
    letter_num_list = []
    for i in range(97,123):
        small = chr(i)
        num = str(i)
        letter_num_list.append(small+num)
    return letter_num_list
print (Small_letter_num())