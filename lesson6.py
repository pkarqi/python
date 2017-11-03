#coding=utf-8
"""
#字典－－－元组－－－－字符串－－－－－列表
dict = {"name":"zhixinping", "age":"17", "class":"First"}
print "**********************START**********"
print tuple(dict)
print type(tuple(dict))
print tuple(dict.values())
print type(tuple(dict.values()))
print "**********"
"""
print  str(dict)
print type(str(dict))
print str(dict.values())
print type(str(dict.values()))
print "**********"

print list(dict)
print type(list(dict))
print list(dict.values())
print type(list(dict.values()))
print "************************END************"

#元组－－－－>字符串－－－－－－>列表
#不能转换字典
tup=(1,2,3,4,5,6)
print str(tup)
print type(str(tup))
print "***********"
print list(tup)
print type(list(tup))
print "************"
"""
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13]
列表－－－>元组----->字符串
不能转换成字典
print tuple(nums)
print type(tuple(nums))
print "************"
print str(nums)
print type(str(nums))
print "**************"

a="123456"
print tuple(a)
print type(tuple(a))
print "************"
print list(a)
print type(list(a))















