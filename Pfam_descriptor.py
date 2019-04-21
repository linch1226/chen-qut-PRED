#-*- coding: utf-8 -*-
import xlrd,xlwt,requests,xlsxwriter,re,numpy as NP,os,time
import aiohttp
import asyncio
from itertools import *
from bs4 import BeautifulSoup
class Smartclass(object):
    def __init__(self):
        self.SmartId=[]
        self.Source={}
        self.Domain=[]
        self.dict={}
        self.numssecc = 0
        self.dictnul=0
    def GetSmartId(self):
        FilePath = r'C:\GO\Homotrimer\\Homotrimer3.fasta'
        FId = open(FilePath)
        LineData = FId.readlines()
        for i in LineData:
            if (i.count('>')):
             self.SmartId.append(i.replace('>', '').split(' ')[0])

    def getData(self,Id,isdir=0):
      
#         proxies = {
#             "http": "http://162.105.87.211:8118"
#         }
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8'}
        
        try:
         html = requests.get("http://pfam.xfam.org/protein/{}".format(Id), headers=headers, timeout=200).text
        except Exception as e:
            print(Id,"爬取错误!",e)
        bf = BeautifulSoup(html,'html5lib')
        
        texts = bf.find_all(attrs={'id':'imageKey'})
        trhtmlstr = BeautifulSoup(str(texts), 'html5lib')
        #print(trhtmlstr.find_all('tr'))
        _namearr = ""
        if(isdir==1):
         for item in trhtmlstr.find_all('tr',class_='odd'):
            tdinfo=item.find_all('td')
            if(tdinfo[1].string!='n/a'):
             _namearr += tdinfo[0].string+tdinfo[1].string + ','
             self.dict.update({tdinfo[0].string+tdinfo[1].string:tdinfo[0].string+tdinfo[1].string})
            else:
                _namearr += tdinfo[0].string+ ','
                self.dict.update({tdinfo[0].string:tdinfo[0].string})
        self.numssecc += 1
        self.Source.update({Id:_namearr.rstrip(',')})
if __name__ == '__main__':
    dl = Smartclass()
    dl.GetSmartId()
    enddir = {}
    nadir=[]
    dictnum=0
    dictvalue = {}
    dicfrom = {}
    strlist=[]
    start = time.time()
    print(dl.SmartId)
    def addDirfrom():
         for key,values in dl.dict.items():
          for idx,strvalues in enumerate(str(values).strip(',').split(',')):
           dictvalue.update({strvalues: strvalues})
         for inx,val in enumerate(dictvalue.values()):
           if val!='':
             dicfrom.update({inx: val})
         f=open(r'E:\dic.txt','w')
         f.write(str(dicfrom))
    
    if os.access(r"E:\dic.txt", os.F_OK):
        for Id in dl.SmartId:
            dl.getData(Id,1)
            print("completed：：", dl.numssecc, '/', len(dl.SmartId))
        print('success:')
        s = open(r'E:\dic.txt', 'r')
        a = s.read()
        dicfrom = eval(a)
    else:
        for Id in dl.SmartId:
            dl.getData(Id)
            print("completed：", dl.numssecc, '/', len(dl.SmartId))
        print('succss：')
        addDirfrom()
    print("key",dl.Source)
    print("dic",dicfrom)
    def Getdir(Id, item):
        corr = ""
        _num=0
        for key, values in dicfrom.items():
            num=0
            for i in item:
                if (values==i):
                    num=1
            corr+=str(num)+'.'
        enddir.update({Id: corr})
        strlist.append(corr.strip('.'))


    _num = 0
    for Id in dl.SmartId:
      Getdir(Id,str(dl.Source[Id]).split(','))
      _num+=1
    print("dic：",enddir)
    listts=[[] for i in range(_num)]
    for i in range(len(listts)):
      listts[i].append(strlist[i])
    for iten in listts:
        print(str(iten).replace("'",""))
    print("none：", nadir)
    print('time：%s' % (time.time() - start),"S")
import numpy as np
my_array=[]
num=['0','1']

for item in listts:
    c=[]
    d=str(item).replace("'","")
    f=list(d)
    for i in f:
        if i in num:
            c.append(int(i))
    c.append('lable')
#     print(c)
    d=np.array(c)
    my_array.append(d)
    print(d)
np.save('your path for pfam predictor',np.array(my_array))







