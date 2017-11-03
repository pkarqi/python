#coding=utf-8
q = "abcdefdsdsdf'"
#w = '123456"'
##print q
#print w
r=q.replace("b","123")   #字符串不可变
#print q.find("f")
# ＃print r
# ＃help(q.find)
a = "This is %s %s" % ("my","apple")
#print a

b = "This is {1} {0}" .format("apple","my")
#print b

c = "This is {whose} {fruit} from {number} years" .format(fruit="apple",whose="my",number=100)
#print c


d = open("tmp.txt","w")
d.write("test121212\nwewewewe\newewewew\n32323232\n905960594")
d.close()

import linecache

d = open("tmp.txt", "r")
t=d.read(100)
lines = linecache.getlines("tmp.txt")
print lines











