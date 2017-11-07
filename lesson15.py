#coding=utf-8
'''
def func1():
#    print 1
    return 1
test=func1()
print test
print type(test)
'''
#必须参数 def add(num,num2)中num  num2是必须参数没有默认值
#可选阐述 def add(num=1,num=2)中num  num2是可选阐述是有默认值
#默认值和没有默认值的区别在于 "＝"
def add(*num):
    print type(num)
    d=0
    for i in num:
        d += i
    return d
print add(1,2,3,4)

def add1(num=2,num2=10):
    return num+num2
print add1()
print add1(9,10)