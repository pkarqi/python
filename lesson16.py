#coding=utf-8
'''
#1、定义一个方法，该方法可以引入任意多的整形参数，结果返回其中最大与最小的值

def func(*num):
    for i in num:
        if  not isinstance(i,int):   #判断是否为整正数值

            return "输入的参数必须是整正数"
    a = sorted(num)


    #return "Max is %d and Min is %d" %(a[-1],a[0])
    return max(num), min(num)
print func(1,2,3,4,5,6,8,67687,0)
'''
#2、定义一个方法，该方法可以引入任意多的字符串参数，结果返回（长度）最长的字符串




def func1(*str):
    s = list(str)
    dic = dict([len(x),x] for x in s)
    return dic[max(dic)]
print func1('fdfdf','dfderere','123456789','1234567890poiuytrewqasdfg')













