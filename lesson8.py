#coding=utf-8
"""
a = "abc"
print list(a)
print tuple(a)

a = xrange(1,10)       # 它生成一个xrange 对象，1、当我们操作一个非常大的数据而且内存比较吃紧的时候我们使用xrange来操作节省内存，2、xrange 一般是用在循环里面，比如我们只需要操作部分数据而不是返回全部元素来完成操作。
print a
b = range(1,10)        # 它生成一个range对象
print b
print a[0]
print b[0]

for m in range(1000):
    print "sss"
    break
for n in xrange(1000):
    print "mmmm"
    break

print  [x * x for x in range(1,100)]
print ["the %s" %d for d in xrange(1,101)]

print [(x,y) for x in range(2) for y in range(2)]

print dict([(x,y) for x in range(5) for y in range(5)]) #************


a = ["i", "an", "zhi"]
b = 2
b = a
a[2] = "xinping"
#print a
#print b

#del b
#del a

#print a
#print b


w = [1,2,3,4]
n = w
c = n
del c[:]           # 清空元素
print w
del w              # 删除列表对象的引用
#del n
print n
print type(c)

"""

a = [1,2,3,4]
a1 = (1,2,3,4)
a2 ="123456"
a3={"name":"xin", "age":18}
print type(a)
print type(a1)
print type(a2)
print type(a3)
print dir(a)
print dir(a1)
print dir(a2)
print dir(a3)
print "###########"
help(a.append)
print "###########"
help(a1.count)
print "###########"
help(a2.encode)
print "###########"
help(a3.copy)











