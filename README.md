<h1> Program 1 ( menghitung hasil laba selama 8 bulan ) </h1>

1. alur algoritma nya :

  - uang = 100000000 pengusaha mempunyai modal sebesar 100 juta uang sebagai variable
  - SUM = 0 perintah SUM digunakan untuk menjumlah 
  - y = 0 dan variable y digunakan untuk bulan 
  - laba = (int(0),int(0),int(uang)*.1,int(uang)*.1, int(uang)*.5,int(uang)*.5,int(uang)*.5,int(uang)*.2)
  - laba pada bulan 1 dan 2 yaitu 0 = int(0),
  - laba pada bulan ke 3 dan 4 sebesar 1% = int(uang)*.1,
  - laba pada bulan ke 5 6 dan 7 sebesar 5% = int(uang)*.5,
  - dan laba pada bulan 8 sebesar 2% = int(uang)*.2,
  - symbol * berfungsi sebagai perkalian dipisahkan oleh koma (,) dan dideklarasikan oleh integer ( int )
  - for i in laba berfungsi sebagai perulangan yang terhitung sesuai dengan jumlah bulan pada laba di atas
	sum = sum+i adalah hasil dari perkalian dari index ( i )
	y+=1 menampilkan jumlah bulan
	print("laba bulan ke - ",y,"sebesar : ",i) digunakan untuk menampilkan hasil variable y dan hasil penjumlahan dari index
  - print("total laba yang di dapatkan : ",sum) digunakan untuk menampilkan jumlah total dari laba yang di dapat selama 8 bulan 
  
2. code program : 

    <br>uang = 100000000</br>
    <br>sum=0</br>
    <br>y =0</br>
    <br>laba = (int(0),int(0),int(uang)*.1,int(uang)*.1, int(uang)*.5,int(uang)*.5,int(uang)*.5,int(uang)*.2)</br>
    <br>print ("modal awal seorang pengusaha  = " ,uang)</br>
    <br>for i in laba:</br>
      sum=sum+i
      y+=1
      print ("laba bulan ke",y,"sebesar : ",i)
    
    <br>print ("total laba yang di dapatkan :",sum)</br>

3. Hasil program :

    ![photo1](https://user-images.githubusercontent.com/56831922/68442234-fd3c5080-0202-11ea-81fc-bd2de4b45da8.jpg)
