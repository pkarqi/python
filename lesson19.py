#coding=utf-8

def add0(x,y):
    z =x + y
    #return z
add0(4,5)



def add1(a,b):
    c =a + b
    #return c
add0(3,4)



def add3():
    return 10
add3()



def add2():
    new_add = add0(4,5) + add1(8,9) + add3()
    return new_add
print add2()




# def test():
#     num = 7
#     num +=1
#     return num
# def test2():
#     new_test = test()
#     return new_test
# print test2()
