#coding=utf-8
"""
a=(1,2,3,4,5,6,6)
print a[0]
print a[1::2]
print dir(a)
print a.count()
print help(a.index)
print a.index(2)
b = list(a)
b[0] = 5
print type(b)
print b


def info(a):
    print  'id %d' %id(a)
a=[1,2,3]

print 'start'
print id(a)

info(a)



a = set('abc')
a.add('python')
a.update('shellll')
a.remove('python')
a.remove('a')

print 'c' in a
print 'python'  not in a
print a


B = set('abcde')
F = set('123de')
print B & F
print B | F


W = [1,2,3]
W.append(1)
W.append(3)
print set(W)



a = frozenset('abc')
a.add('222')
print a

"""








