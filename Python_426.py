#encoding=utf-8
"""
掌握内容
1、学习取模、幂、取整除的运算符
2、掌握阿莫斯特朗数规律：如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数
"""
#检测用户输入的数字是否为阿姆斯特朗数
def Amstl(num):
    sum = 0
    n = len(str(num))
    temp = num
    while temp>0:
        per = temp%10   #取模，返回除法的余数
        sum = sum + per**n  #幂 - 返回per的n次幂
        temp = temp//10     #取整除 - 向下取接近除数的整数
    if sum == num:
        return str(num)+'：这是一个阿莫斯特朗数'
    else:
        return str(num)+'：这不是一个阿姆斯特朗数'

num = int(input('请输入一个整数'))
print (Amstl(num))