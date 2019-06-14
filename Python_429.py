#encoding=utf-8

#计算字符串中每个字符出现的次数
def str(st):
    st_dic = {}
    for i in st:
        if i in st_dic:                 #pyhton2写法：if st_dic.has_key(i),python3没有has_key()方法
            st_dic[i] = st_dic[i]+1
        else:
            st_dic[i] = 1
    return st_dic           #返回字典，记录每个字符串的出现次数

#倒置字符串
def daozhi(str):
    str_dao = ''
    for i in range(len(str)):
        str_dao = str_dao + str[-i-1]
    return str_dao


st = 'asdsad  sadddd   as  daaaasd'
print (str(st))
key_name_max = max(str(st), key=str(st).get)
key_name_min = min(str(st), key=str(st).get)
print (key_name_max,key_name_min)

print (daozhi(st))