#coding=utf-8
'''
def test(a,b,c,d,e):            #位置参数
    '这是一个测试数据'
    return "1,2,3,4,5"
print test(1,2,3,4,5)
#test.__doc__


def test1(a=4):                #可选参数
    'this is test1 function'
    return a
print test1()
print  test1(a=10)



b = [1,2,3]                     #修改函数
def test2(L):
    L.append(4)
    return L
print test2(b)


#b = test2(b)
#print b

'''

def test2(**pp):                  #两个＊＊是字典
    return pp
print test2(name='pkarqi',age=19,calsses=5,country='china')


def test3(*kk):                    #一个＊是元组
    return kk
print test3('a','b','c',[1,2,3,4],{'name':'pkarqi'})

def test4(*kk,**uu):                    #一个＊是元组
    return kk,uu
print test4('a','b','c',age='30',classes='69')






