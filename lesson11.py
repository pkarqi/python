#coding=utf-8
#print bin(3)

#print 0b11 >> 1
#print 0b11 << 1

a = (1,2,3,4)
a = list(a)
print type (a)

b = [1,2,3,4,5]
b = tuple(b)

print type(b)

c = [(1,3)]

c = dict(c)

print c
d = [(1,3),(2,4),(5,6)]
d = dict(d)
print  d

x = [x for x in xrange(101)]
#part1 []
#part2  x
#part3  for x in xrange(101)
print x

new_list = [ ]
for n in xrange(101):
    new_list.append(n)
print new_list


#help(sorted)

print sorted([5, 2, 3, 1, 4])


F = [3,4,5,6,7]

F = sorted(F,reverse=True)
print F

print '%s am is a %s' %('I', 'BOY')
print '%(who)s am is a %(gender)s' %{'who':'i','gender':'boy'}
print "{who} am is a {gender}" .format(who='I',gender='boy')


















