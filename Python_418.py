#encoding=utf-8

"""
掌握内容
1、字符串拼接
2、list.insert(index, obj):将对象插入列表
3、python3.x版本输出不换行格式：print(x, end=" ")
4、in、not in：成员运算符(字符串、列表、元组)
"""

#一个列表，排重，不能用set，也不能用字典
def Oper_list(original):
    result = []
    result1 = []
    result2 = []
    for i in original:
        if i not in result1:
            result1.append(i)
        else:
            result2.append(i)
    result.insert(0,result1)
    result.insert(1,result2)
    return result

original = [1,'q','w',1, 2,'q', 2, 3, 3, 4, 5, 6]
print ('不重复的：',end='')
print (Oper_list(original)[0])
print ('重复过的：',end='')
print (Oper_list(original)[1])
