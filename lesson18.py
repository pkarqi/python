#coding=utf-8
d=lambda x:x+1 if x > 0 else 'Error'

g = lambda x:[(x,i) for i in xrange(0,10)]

print g(0)

print 'x'*10
print d(9)
print d(10)


def e(x):
    return x+1
print e(12)

print d(-0)

# 函数的参数总结
# 1、位置匹配
def func(arg1,arg2):
    return arg1,arg2
print func(1,2)

#2、关键字匹配
def func1(k1='',k2='None',k3=''):
    return k1,k2,k3
print func1(k1='2',k3='5')
print func1(k3='5',k1='2')
print func1(k1='2',k2='3',k3='5')
''''
#3、收集匹配
    1）、元组收集
    2）、字典收集
'''
def func3(a,b,u,*kargs,**kwargs):
    return kargs
print func3('w','e','t',1,2,3,4,5,{'d':1,'u':2})
#位置参数  先是位置匹配的参数  再是关键字匹配的参数  收集匹配的元组的参数  收集匹配的字典的参数
＊＊＊＊＊＊＊＊Next 递归＊＊＊＊＊＊＊＊＊