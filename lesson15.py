#coding=utf-8
'''
def func1():
#    print 1
    return 1
test=func1()
print test
print type(test)

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
#print add1('a',(qwqw))
'''
#函数的健壮性1、你永远知道你的方法返回的是什么（异常处理，条件判断）2、返回你想要的结果
def add2(num1,num2):
    if isinstance(num1,int) and isinstance(num2,int):
        return num1+num2
    else:
        return 'input not int type \n参数里含有非数字类型'
print add2(2,3)

print add2('ss',('d','c'))




