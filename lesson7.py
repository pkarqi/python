#coding=utf-8
""""
＃ 索引
a = [1,2,3,4]
b = [[1,2,3],[4,5,6]]
print b
print a[-1]
a = [1,2,3,4,5,6,7]
print a[0:4:1]       #步长 是 1
print a[-1:-4:-1]    #步长 是 －1
print a[0:]
print a[0::2]
print a[1:]
print a[1::2]       #步长 是 2

# 添加操作
a = [1,2,3]
b = [4,5,6]
print a + b        # 生成一个新的列表
a.extend(b)        # 接受参数并将该参数的每一个元素都添加到原有的列表中
print a
a.append(4)        # 添加任意对象到列表的末端
a.append([8,9,0])
print a
a.insert(1,'ab')
print a

# 修改
a = [1,2,3,4]
a[0] = 'python'
a[1] = "is"
a[2] = "nb"
a[3] = "....."
print a
# 删除操作　
a = [1,2,3,4,6,7]
#del a[0]
#print a
#a.remove(4)
#print a
#a.remove(9)
# 不存在就会抛出异常
#print a
a.pop(1)
#a.pop(1)
#a.pop(2)
print a
# in  ---- not in
a = [1,2,3,4,5]
print 2 in a
print 6 not in a
print 5 not in a
print 5 in a
# 列表的推到式
print [x for x in range(1,21)]
print  range(1,11)
print range(1,11,1)
print range(1,11,2)
print range(1,10,3)
print range(1,11,2)
print [x for  x in range(1,11) if x %2 == 1]
"""
# 列表的排序和翻转

a = [ 12,24,35,48,59,56,"re","444"]
#a.sort()     #对列表中的参数进行整理就需要用到列表sort正序排序
#a.reverse() #reverse列表反转排序：是把原列表中的元素顺序从左至右的重新存放，而不会对列表中的参数进行排序整理

print a
print a









