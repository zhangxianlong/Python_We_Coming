#encoding=utf-8

"""
1、冒泡排序列表，然后再合并两个列表，实现由小到大排列
2、extend(list)：在列表末尾一次性追加另一个列表中的多个值
   append(obj)：在列表中添加一个对象
"""

#冒泡排序
def maopao(L):
    for i in range(len(L)-1):
        for j in range(len(L)-1-i):
            if L[j]>L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
    return L

#合并两个有序数组,有小到大排列
def hebing(L1,L2):
    temp = []
    while len(L1)>0 and len(L2)>0:
        if L1[0] > L2[0]:
            temp.append(L2[0])
            del L2[0]
        else:
            temp.append(L1[0])
            del L1[0]
    temp.extend(L1)
    temp.extend(L2)
    return temp

L1 = [100,2,20,5,8]
L2 = [3,1,7,5,9]
print (maopao(L1))
print (maopao(L2))
print (hebing(L1,L2))
