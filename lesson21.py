list = [1,2,3,4,6,7,8]
f = open('demo.txt','w')
for i in list:
    k=''.join([str(j) for j in str(i)])
    f.write(k)




f.close(k)