#coding=utf-8
from  copy import deepcopy

import psutil
''''

import  time
a= "1"
b = [ "HU","be","huu" ]
c = ("fff","www","rrr")

time.sleep(10)

print type(a)
print type(b)
print type(c)

people = {
    'Alice': {
        'phone':'234','addr':'Fool drive 23'
    },
    'Beth':{'phone':'9120','addr':'Bar,street 43'
            },
    'Cecil':{'phone':'3145','addr':'Baz acenue 90'
                                   }
}
labels = {
    'phone':'phone number' ,
    'addr': 'address'
}
name = raw_input('name: ')


request = raw_input('phone number(p) or address(a)?')

if request == 'p':key = 'phone'
if request == 'a':key = 'addr'



if name in people: print "%s's %s is %s." %(name, labels[key], people[name][key])

x =  {'username':'admin', 'machines':['foo','bar','baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')

print x
print y
'''
d = {}
d['names'] = ['zhixinping', 'pkarqi']
c = d.copy()
dc= deepcopy(d)
d['names'].append('Clive')
print c



































