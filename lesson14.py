#coding=utf-8
'''
def test(a,b,c,d,e):     #位置参数
    '这是一个测试数据'
    return "1,2,3,4,5"
print test(1,2,3,4,5)
#test.__doc__
'''

def test1(a=4):
    'this is test1 function'
    return a
print test1()
print  test1(a=10)