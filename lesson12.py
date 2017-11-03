#coding=utf-8
import os
'''
print '2',
print '3',
print '4'

f = open('print.txt','w')

print >> f,"fdfdsfdfsf",
print >> f,"2323232323"
f.close()


if True:                     #分割条件
    print 'ok'               # 代码块

x = 3
if x:
    print 4



if x is True:
    print 5



print True or False
print True and False


print 4 if True else 3

print 2 if True else 3


if True:
    print 4
else:
    print 3



print  [4,3] [True]


x =1
while x<30:
    x+=1
#    continue
    print x
#    continue  #退出当前循环
#    if x>20:
#       break  #退出整个循环



else:
    print 'end'





for x in '12345，679abcd,erf'.split(' '):  #else 不能与break 合用
#    continue
    print x,
else:
    print x

#print x



print True and False and True and True
print True or False or False or True

a = 'aAbBcCdDeE3fFgG7H9hiIjJkkkkkkKpuy'
#print a.swapcase()
#print ''.join([s for s in a if s.isdigit()])

#print dict([(x,a.count(x)) for  x in set(a)])

####列表推导式
#for x in set(a):
#   print x

#    a.count(x)
#    print


#print dict([(x,a.count(x)) for x in set(a)])
a_list = list(a)
#print a_list
set_list = list(set(a_list))
set_list.sort(key=a_list.index)

print ''.join(set_list)

print a[::-1]

a = 'aaaASJKmmmnmn1213mnnLKLIOGHGTTmnioiuiuio989'
l = [ ]
for s in a:
    if s.isdigit():
        l.append(s)
#print ''.join(l)



#print ''.join([s for s in a if s.isdigit()])

#print dict([(x,a.count(x)) for x in set(a)])



#a_list = list(a)
#set_list = list(set(a_list))
#set_list.sort(key=a_list.index)
#print ''.join(set_list)
#print a[::-1]

L = sorted(a)
#print L

a_upper_list = [ ]
a_lower_list = [ ]

for x in L:

    if x.isupper():
       a_upper_list.append(x)

    elif x.islower():
        a_lower_list.append(x)

    else:
        pass

for y in a_upper_list:
    y_lower = y.lower()
    if y_lower in a_lower_list:
        a_lower_list.insert(a_lower_list.index(y_lower),y)
print ''.join(a_lower_list)

#print a_lower_list
#print a_upper_list



a = 'aaaASJKmmmnbmn1213mnnLKLIOGHGTTmnioiuiuio989'

u =set(a)
u.update(list(search))
print len(set(a)) == len(u)


a = 'aaaASJKmmmnbmn1213mnnLKLIOGHGTTmnioiuiboyuio989'

search = [ 'boy', 'girl' ,'bird', 'dirty']

b = set(a)
for i in search:
    b.update(list(i))


print len(b) == len(set(a))

'''


m = os.popen('python -m this').read()

m = m.replace('\n', '')
l = m.split(' ')
print [(x,l.count(x)) for  x in ['be','is','than']]



