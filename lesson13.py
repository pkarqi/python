#coding=utf-8
# 20171104
'''
num_dic={'key1':'value1','key2':'value2','key3':'vlue3'}
print num_dic
for x,y in num_dic.items():            #循环字典
    print x,y

a = {'a':'hhah','b':'xixi','d':'qiqi','c':'xiaxia'}
print a['a']                           #取字典的值
print '*'* 10
print a['b']
print '##'*20
print a['c']
key_list=a.keys()
key_list.sort()
#print key_list
for x in key_list:
    print x,a[x]


a = {'a':'hahaha','b':'xixi','d':'qiqi','c':'xiaxia','e':'hahaha','f':'hahaha'}
search_values= 'hahaha'               #根据字典的值取字典的键
key_list = []
for x,y in a.items():
    if y == search_values:
        key_list.append(x)
print key_list



a = 'abcd123ABCDFELKZXPzbcd'
a = ''.join([x for x in  a if not  x.isdigit()])
print  sorted(a,key=string.upper)



a = 'i am lilei'
b = a.replace('lilei','ppp')
print b

'''


g = open('tmp.txt','w')
g.write('opopopopsdsdddsds')
g.close()






with open('tmp.txt','a') as g:
    g.write('dfdfdfdfd\nfdf\n121\n34\n56\n1212189898')















