uang = 100000000
sum=0
y =0
laba = (int(0),int(0),int(uang)*.1,int(uang)*.1, int(uang)*.5,int(uang)*.5,int(uang)*.5,int(uang)*.2)
print ("modal awal seorang pengusaha  = " ,uang)
for i in laba:
    sum=sum+i
    y+=1
    print ("laba bulan ke",y,"sebesar : ",i)
    
print ("total laba yang di dapatkan :",sum)
