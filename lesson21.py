list=[[1,2,3],[4,5,6],[7,8,9]]
f=open('demo.txt','w')
for i in list:
    k=''.join([str(j) for j in i])
    f.write(k+"\n")



f.close()