#coding=utf-8
from string import  Template
from math import pi
#from math import abs
#from math import floor
#from math import pow
#help(math.pow)
#import csv
#print csv
#help(csv)
#print dir(csv.reader)
'''
"＋＋＋＋这是一个练习课程脚本＋＋＋＋＋＋"
a = "1234"
b = "45679"


if len(a) == 4:
    print "1"
else:
    print "0"
"＋＋＋＋＋＋＋＋＋＋end＋＋＋＋＋＋＋＋＋"

print "中国同学们好"

print "hhdjshkdahdkhakjdh"


if 1==2:
    print 'one equal two'
if 1==1:
    print 'one equal two'


print floor(90)
print pow(2,3)

name =raw_input('Please Enrter name')
if name == '1':
        print 'ok'

print math.abs(1)


greeting0='abcd'
greeting1=['zhixinping','pkarqi','a', 'a']
greeting2=('163.com','sina.com')
greeting3={'183.com':'162','189.com':'189'}
greeting4=[1,2,3,4,5]
print greeting0[0]
print greeting1[0]
print greeting2[0]
#print greeting3[0]
print len(greeting0)

#fourth = raw_input('year: ')[3]
#print fourth

greeting1.append(4)

print greeting1.count('a')
greeting1.extend(greeting3)
print  greeting1
print greeting1.index('pkarqi')
print greeting2.index('163.com')
greeting1.insert(0,'ppppp')
print greeting1
print '***' * 10
#greeting4.pop()
greeting4.remove(3)
#print greeting4
print '*' * 10
print greeting4
greeting4.reverse()
print greeting4.reverse()
'''

format = "Pi with three decimals: %.3f"
print format %pi
s = Template('$x,glorious $x!')
print s.substitute(x='slurm')

lit=['z','h','i','x','i','n','p','i','n','g']
lits = ''.join(lit)
print lits

print '*' * 10
#sep1 = '2+2222+22222'
url = 'http://www.baidu.com/user/passwd'

#print url.split('.')
url1 =  url.split('//')
print url1[1]