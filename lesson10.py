#coding=utf-8
#pkarqi
"""
字典是无序的，，字典的key必须是不可变的数据类型 比如 数字、字符串、元组，列表不能是Key，如下例子
#info={"a":1,"b":2}
#print info
#print info['a']
binfo = {'a':[1,2,3], 'b':[4,5,6]}
binfo['b'][0] = 9
print binfo
cinfo = {'22':'222','aa':11}
print cinfo
einfo = {(123):'ss',('b','c'):'222'}
print einfo
finfo = {[1,2,3]:'ww'}
print finfo


binfo = {'name':'lilie' ,'age':20}  #  命名方法一

print binfo

cinfo = dict(name='lili', age=20)    # 命名方法二
print cinfo



#字典的操作
ainfo = dict(name='lilie', age=20)
#ainfo['phone'] = 'iphone5'              #add key
print ainfo

#ainfo['phone'] = 'htc'

#print ainfo                              #replace key


#ainfo.update({'city':'bj','desc':'hd'})

#print ainfo

#del ainfo['name']                  #删除一个元素
#print ainfo

#del ainfo                        # 删除一个字典
#print ainfo

#ainfo.clear()                    # 清空一个字典
#print ainfo

a = [1,2,3,4]
#print a.pop(5)
#print ainfo.pop('city','ha')



print 'name' in ainfo
print 1 in a


print 'city' in ainfo

print '3' in a





print ainfo.keys()
print ainfo.values()

print ainfo.items()

print ainfo.get('name')
print type(ainfo.get('city'))


b = [23,45,22,44,25,66,78]
print [m for m in b if m % 2 == 1]                 #生成列表中所有基数组成的列表

print ["the sss %s" % m for m in b[0:2:1]]         #输出['the sss 23', 'the sss 45']


for m in b:
    print m+2
print [m+2 for m in b]
print range(11,36,11)
print [m * 11 for m in range(1,4,1)]
a = (1,4,5,6,7)
c = list(a)
#print c
c[1] = 8
print c

d=tuple(c)
print d

"""


studentinfo={'liming':{'name':'李明','age':20,'fenshu':{'chinese':80,'math':'75','english':85}}}
#print studentinfo
studentinfo['zhangqiang'] = {'name':'张庆','age':30,'fenshu':{'chinese':85,'math':90,'english':100}}

studentinfo['liming']['fenshu']['python'] = 90
studentinfo['zhangqiang']['fenshu']['python'] = 85
#print studentinfo
studentinfo['zhangqiang']['fenshu']['math'] = 89
del studentinfo['liming']['age']

b = studentinfo['zhangqiang']['fenshu'].values()
b.sort()
print b

print  studentinfo.pop('city','BeiJing')
#print studentinfo











