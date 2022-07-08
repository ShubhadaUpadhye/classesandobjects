class pattern:
    def pattern_1(self,n):
        try:
            for i in range(0,n):
                for j in range(i):
                    print("ineuron",end=" ")
                print(" ")
        except Exception as e:
            print(e)
    def pattern_2(self,n):
        try:
            for i in range(n,0,-1):
                print(end="    "*i)
                for j in range(n-i):
                    print("ineuron ",end=" ")
                print(" ")
            for i in range(n,0,-1):
                print(end="    "*(n-i))
                for j in range(i):
                    print("ineuron ",end=" ")
                print(" ")
        except Exception as e:
            print(e)

a=pattern()
a.pattern_2(int(input("enter value for n: ")))

'''import logging as log
#ldts=list,dictionary,tuple,set
log.basicConfig(filename="ldts.log",level=log.INFO,format='%(asctime)s %(levelname)s %(name)s %(message)s')
class ldts:
    def __init__(self,l):
        self.l=l

    def extract_ldts(self):
        log.info("extracting list,dictionary,tuple from list")
        try:
            for i in self.l:
                if type(i) == list:
                    log.info("the extracted list is %s",i)
                elif type(i)==dict:
                    log.info("the extracted dict is %s", i)
                elif type(i)==set:
                    log.info("the extracted set is %s",i)
                else:
                    if type(i)==tuple:
                        log.info("the extracted tuple is %s",i)
        except Exception as e:
            log.exception(e)

    def extract_integersldts(self):
        log.info("extracting integers from list,dictionary,tuple,set")
        l1=[]
        try:
            for i in self.l:
                if type(i) == list:
                    for j in i:
                        if type(j)==int:
                            l1.append(j)
                elif type(i) == tuple:
                    l1.extend(i)
                elif type(i)== set:
                    l1.extend(i)
                else:
                    if type(i)==dict:
                        for k, v in (i.items()):
                            if type(k) == int or type(v) == int:
                                l1.append(k)
                                l1.append(v)
            log.info("the extracted integers list is %s", l1)
        except Exception as e:
            log.exception(e)

    def extract_string(self):
        log.info("extracting string")
        try:
            for i in self.l:
                if type(i)==list:
                    for j in i:
                        if j=="ineuron":
                            log.info("the extracted string is %s",j)
                elif type(i)==dict:
                    for j in i.items():
                        if j[1]=="ineuron":
                            log.info("the extracted strings is %s",j[1])
        except Exception as e:
            log.exception(e)

    def num_keys(self):
        log.info("extracting number of keys from dict")
        try:
            for i in self.l:
                if type(i)==dict:
                    x=i.keys()
                    log.info("the number of keys is %s",len(x))
        except Exception as e:
                log.exception(e)

    def extract_stringldts(self):
        log.info("extracting string from list,dict")
        for i in self.l:
            try:
                if type(i) == list or type(i) == tuple:
                    for j in i:
                        if type(j)==str:
                            log.info("the extracted string from list is %s", j)
                elif type(i)==dict:
                    for k,v in i.items():
                        if type(k)== str or type(v)==str:
                            log.info("the extracted string from dict is %s,%s",k,v)
            except Exception as e:
                log.exception(e)

    def occurances_l(self):
        log.info("counting occurances of data in list l")
        count=0
        try:
            sl=[]
            slf=[]
            for i in self.l:
                if type(i) == list:
                    for j in i:
                        if type(j)==str:
                            sl.append(j)
                elif type(i)==dict:
                    for k,v in i.items():
                        if type(k)==str or type(v)==str:
                            sl.append(k)
                            sl.append(v)
            for i in set(sl):
                x=sl.count(i)
                log.info("the occurances are %s,%s",i,x)
        except Exception as e:
            log.exception(e)

    def alphanum(self):
        log.info("checking alphanumeric data")
        try:
            for i in self.l:
                if type(i)== list or type(i)==tuple:
                    for j in i:
                        if type(j)==str:
                            x=j.isalnum()
                            log.info("the string from list is %s and the boolean is %s", j, x)
                else:
                    if type(i)==dict:
                        for k,v in i.items():
                            if type(k)==str or type(v)==str:
                                x=k.isalnum()
                                y=v.isalnum()
                                log.info("the string from dict is %s ,%s and the boolean is %s,%s",k, v, x,y)
        except Exception as e:
            log.exception(e)

    def prodcut_listinetegers(self):
        log.info("extracting multiplication of all the numeric data from different dataset collection")
        m=1
        try:
            for i in self.l:
                if type(i)==list:
                    for j in i:
                        if type(j)==int:
                            m=m*j
            log.info("the product of numeric data in list is %s",m)
        except Exception as e:
            log.exception(e)
        n=1
        try:
            for i in self.l:
                if type(i)==tuple:
                    for j in i:
                        if type(j)==int:
                            n=n*j
            log.info("the product of numeric data in tuple is %s",n)
        except Exception as e:
            log.exception(e)
        p=1
        try:
            for i in self.l:
               if type(i)==set:
                   for j in i:
                    if type(j)==int:
                        p=p*j
                        print(p)
            log.info("the product of numeric data in set is %s",p)
        except Exception as e:
            log.exception(e)
        q=1
        r=1
        try:
            for i in self.l:
                if type(i)==dict:
                    for k,v in i.items():
                        if type(k)==int or type(v)==int:
                            q=q*k
                            r=r*v
            log.info("the peoduct of numeric data in dict is %s",q)
            log.info("the peoduct of numeric data in dict is %s", r)
        except Exception as e:
            log.exception(e)

    def flat_list(self):
        fl=[]
        try:
            for i in self.l:
                if type(i)==set or type(i)==tuple:
                    for j in i:
                        fl.append(j)
                elif type(i)==list:
                    for j in i:
                        fl.append(j)
                else:
                    if type(i)==dict:
                        for k,v in i.items():
                            fl.append(k)
                            fl.append(v)
            log.info(" the final merged list is %s",fl)
        except Exception as e:
            log.exception(e)

    def sum_listitems(self, l1):
        log.info("extracting summation of all numeric data in list l1")
        sum = 0
        try:
            for i in l1:
                sum = sum + i
            log.info("the list items count is %s", sum)
        except Exception as e:
            log.exception(e)

    def odd_numbers(self,l1):
        log.info("trying to extract odd numbers")
        l2=[]
        try:
            for i in l1:
                if i%2!=0:
                    l2.append(i)
            log.info("the extracted odd numbers are %s", l2)
        except Exception as e:
                log.exception(e)

    def occurance_l1(self,l1):
        log.info("counting occurannce of  items in list l1")
        try:
            for i in set(l1):
                x = l1.count(i)
                log.info("the occurance is %s,%s",i,x)
        except Exception as e:
            log.exception(e)

a=ldts(l=[[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), {23,4,5,45,4,4,5,45,45,4,5,} ,{"k1":"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron","data science"]])
l1=[1, 2, 3, 4, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 45, 4, 5, 23, 3, 6, 7, 8]
print(a.occurance_l1([1, 2, 3, 4, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 45, 4, 5, 23, 3, 6, 7, 8]))
print(a.num_keys())
'''