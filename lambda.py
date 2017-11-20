#coding=utf-8
# lambda使用方法 jil

a = [1,2,3,4,5,7]
b = filter(lambda x :x!=5,a)
print b








C = [1,2,3,4,5,6,7,8,9]
D = []
for i in C:
    if i !=5:
        D.append(i)
print D