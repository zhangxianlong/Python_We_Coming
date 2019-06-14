#encoding=utf-8

"""
掌握内容
1、判断变量数据类型：isinstance(变量名，类型)
2、python3.x版本输出不换行格式：print(x, end=" ")
3、**：幂，x**y，返回x的y次幂
题目
一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第n次落地时，共经过多少米？第n次反弹多高？
"""

def Height_list(n):
    height_list = [100]     #100为初始高度，列表记录每次的高度
    if isinstance(n,int):   #判断变量n是否为整数
        if n>0:             #判断变量n为正整数
            for i in range(1,n+1):
                height_i = 100/(2**i)
                height_list.append(height_i)
            return height_list
        else:
            return '次数需大于0'
    else:
        return '次数不合法'

#第n次落地时，共经过多少米
def Height_sum(n):
    Height_sum = 0
    if isinstance(Height_list(n),list):
        for j in range((len(Height_list(n)))-1):
            Height_sum = Height_sum + Height_list(n)[j]
        Height_sum = Height_sum*2-100
        return Height_sum
    else:
        return ('次数不合法')

#第n次反弹多高
def Height_n(n):
    if isinstance(Height_list(n),list):
        Height_n = Height_list(n)[-1]
        return Height_n
    else:
        return ('次数不合法')

n = 8
print (Height_list(n))
print ('第'+str(n)+'次落地时共经历多少米：',end='')
print (Height_sum(n))
print ('第'+str(n)+'次反弹时，弹起多少米：',end='')
print (Height_n(n))