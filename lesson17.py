#coding=utf-8

import urllib
import urllib2



'''
def func1(arg1,arg2):
    return arg1 + arg2
print func1(1,3)
print dir(func1.__doc__)
print dir(func1.__code__)

#作用域
global arg
arg = 1
def function():
    global arg
    arg= 3
function()
print arg



def function2():
    global arg
    arg = 5
print function2()
print arg
'''
#1.定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表：（注：列表里面的元素为偶数）。



def get_num(l):
    L=[]
    for i in l:
        if not isinstance(i,int):
            return 'Must be int type'
        elif i%2 == 0:
            L.append(i)
    return L
print get_num([1,2,3,4,5,6,7,8,9,10])


#2.定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的urllib模块）

def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except Exception as e:
        return 'Url Error'
print get_page('http://www.zhongchebaolian.com')


















