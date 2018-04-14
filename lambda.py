#coding=utf-8
# lambda使用方法 jil

a = [1,2,3,4,5,7]
b = filter(lambda x :x!=5,a)
W = open('demo1.txt','w')
#print type(b)
for i in b:
    N=''.join(str(i))
    W.write(N)
W.close()









C = [1,2,3,4,5,6,7,8,9]
F = open('demo2.txt','w')
D = []
for i in C:
    if i !=5:
        M=''.join(str(i))
        F.write(M)
F.close()