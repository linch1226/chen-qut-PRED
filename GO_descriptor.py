from scipy import sparse
import numpy as np
import pymysql
db = pymysql.connect(user='mysql', password='123456', database='go' )
cursor = db.cursor()
sql2="SELECT acc  FROM   term  WHERE  is_obsolete=0 and acc like 'GO:%' ORDER BY acc;"
cursor.execute(sql2)
row2=cursor.fetchall()
print(row2)

godict={}
i = 0
for t in row2:
    godict[t] = i
    i += 1
	d=[]
for i in range(1,‘the number of different  type proteins’’):
    f=open('the path of you store \\%s.txt'%i,'r')

    ls=[]
    qs=[]
    for line in f:
        s=line[0:6]
        ls.append(s)  
    f.close()
    for j in ls:
        sq1="SELECT distinct term.acc FROM   gene_product INNER JOIN dbxref ON (gene_product.dbxref_id=dbxref.id) INNER JOIN species ON (gene_product.species_id=species.id) JOIN association ON (gene_product.id=association.gene_product_id) INNER JOIN evidence ON (association.id=evidence.association_id) INNER JOIN term ON (association.term_id=term.id) WHERE term.is_obsolete=0  and   dbxref.xref_key ='%s' ORDER BY term.acc; "%j
        cursor.execute(sq1)
        if cursor.execute(sq1)!=0:
            qs.append(j)
    if len(qs)==0:
        print(i)
        continue   
    d.append(qs)
my_array = []
for i in d:
    print(i)
    for k in i:
        print(k)
        sq1="SELECT distinct term.acc FROM   gene_product INNER JOIN dbxref ON (gene_product.dbxref_id=dbxref.id) INNER JOIN species ON (gene_product.species_id=species.id) JOIN association ON (gene_product.id=association.gene_product_id) INNER JOIN evidence ON (association.id=evidence.association_id) INNER JOIN term ON (association.term_id=term.id) WHERE term.is_obsolete=0  and   dbxref.xref_key ='%s' ORDER BY term.acc; "%k
        cursor.execute(sq1)#
        row_1= cursor.fetchall()#将所查到的go信息放入row,这时候的row_1是一个元组
        print('row1',row_1)
        v = np.zeros((1,len(row2)+1))
        for g in row_1 :
            ind = godict[g]
            v[0,ind] = 1
            v[0,len(row2)]=6
        print(v)
        my_array.append(list(v))
        break   
b=np.array(my_array)
print(b.shape)
        #print(np.mean(b, axis=0))
#print(my_array1)
np.save('the path of GO descriptor  for proteins’’',sparse.lil_matrix(np.array(my_array)))
