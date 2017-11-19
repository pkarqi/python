#coding=utf-8
import string
'''
1、定义一个func(name),该函数效果如下。
assert func('zhixinping') = 'Zhixinping'
assert func('pkarqi') = 'Pkarqi'
assert func('zhixihua') = 'Zhixinhua'

def capstr(name):
        return name.capitalize()
print capstr('zhixinping')
print capstr('pkarqi')
print capstr('zhixinhua')


2、定义一个函数func(name,callback=None),效果如下。
assert func('aaaa') == 'Aaaa'
assert func("BBBB",callback=string.low) == 'bbbb'
assert func("cccc",callback=string.upper') == 'CCCC'

print '*'*50

def swastr(name,callback=None):

    if callback == None:
        return name.capitalize()
    else:
        return callback(name)
print swastr('aaaa')
print swastr('BBBB')
print swastr('cccc')
print swastr('[dfdfdf]')




def func5(*args):
    return args
num1 = func5('3','4','6','8','9')  #调用函数
num2 = func5(1,2,3,4,5,6,7)
for i in num2:
    print i,
    print i
func5()

# 定义一个函数func(*karges)该函数效果如下

assert func(222,111,'xixi','hahhahhaha') == 'xixi'
assert func(7,'name','hahhahhaha') == 'name'
assert func(1,2,3,4) == 'None'



def shortstr(*kargs):
    lis = filter(lambda x:isinstance(x,str),kargs) #过滤非字符串


    len_lis=[len(x) for x in lis] #收集长度

    if len_lis:
        min_index = min(len_lis)
        return lis[len_lis.index(min_index)]
    return None
print shortstr(222,111,'xixi','hahhahhaha')

print shortstr(7,'name','hahhahhaha')

print shortstr(1,2,3,4)


'''
#5 、定义一个函数func(name=None,**kargs),实现如下效果

#assert func('zhixinping') == 'zhixinping'
#assert func('zhixinping',years=5) == 'zhixinping,years=5'
#assert func('zhixinping',years=5,body_weight=20) == ''zhixinping',years=5,body_weight=20'


def detail(name=None,**kargs):
    data = []
    for x,y in kargs.items():
        data.extend([',',str(x),':',str(y)])
    info = ''.join(data)
    return '%s%s' %(name,info)
print detail('zhixinping')


print detail('zhixinping',years=5)


print detail('zhixinping',years=5,body_weight=100)