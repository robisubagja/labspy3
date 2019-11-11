<h1> Program 1 ( menghitung hasil laba selama 8 bulan ) </h1>

1. alur algoritma nya :

   - uang = 100000000 pengusaha mempunyai modal sebesar 100 juta dan uang adalah variable nya
   - SUM = 0 perintah SUM digunakan untuk menjumlah 
   - y = 0 dan variable y digunakan untuk bulan 
   - laba = (int(0),int(0),int(uang) * .1,int(uang) * .1, int(uang) * .5,int(uang) * .5,int(uang) * .5,int(uang) * .2)
   - laba pada bulan 1 dan 2 yaitu 0 = int(0),
   - laba pada bulan ke 3 dan 4 sebesar 1% = int(uang) * .1,
   - laba pada bulan ke 5 6 dan 7 sebesar 5% = int(uang) * .5,
   - dan laba pada bulan 8 sebesar 2% = int(uang) * .2,
   - symbol * berfungsi sebagai perkalian dipisahkan oleh koma (,) dan dideklarasikan oleh integer ( int )
   - for i in laba berfungsi sebagai perulangan yang terhitung sesuai dengan jumlah bulan pada laba di atas
	- sum = sum+i adalah hasil dari perkalian dari index ( i )
	- y+=1 menampilkan jumlah bulan
	- print("laba bulan ke - ",y,"sebesar : ",i) digunakan untuk menampilkan hasil variable y dan hasil penjumlahan 
	  dari index
   - print("total laba yang di dapatkan : ",sum) digunakan untuk menampilkan jumlah total dari laba yang di dapat selama 8 bulan 
  

2. Hasil program :

    ![photo1](https://user-images.githubusercontent.com/56831922/68442234-fd3c5080-0202-11ea-81fc-bd2de4b45da8.jpg)



<h2> Latihan2 (menampilkan bilangan terbesar dari program perulangan)</h2>

1. Alur algoritma nya : 

   - x=1 //variable x diisi 1, agar bisa masuk ke syarat while max=0 //variable max diisi 0
   - while x!=0 : perulangan while dengan syarat x bukan 0
   - if x > max : max = x proses if untuk mencari nilai terbesar
   - x = int(input("Masukan bilangan : ")) input nilai x dengan tipe data integer
   - if x == 0 : break jika inputan x diisi angka 0 maka proses perulangan akan berhenti
   - print("Bilangan terbesar adalah : ",max) print nilai terbesar, variabel max
   
 2. Flowchart
 
    ![Screenshot_2019-11-11-18-50-00-810_com google android apps docs](https://user-images.githubusercontent.com/56831922/68585265-58e13500-04b4-11ea-9986-7a13bf40bd84.png)

   
 3. hasil program :
 
 	![photo](https://user-images.githubusercontent.com/56831922/68460123-9dad6780-0239-11ea-9901-4171ff122a92.jpg)
	

<h3> Latihan1 ( menampilkan bilangan acak dibawah bilangan 0,5 ) </h3>

 1. Alur algoritma nya :
    - n=int(input("masukan bilangan N :  ")) = fungsi nya agar bisa melakukan input bilangan bulat dengan dideklarasikan 
      oleh intiger ( int )
    - for i in range(n): syntax ini berfungsi untuk menampilkan perulangan bilangan sesuai dengan jumlah variable yang di
      masukan di awal
    - import random  berfungsi untuk menampilkan bilangan secara acak
    - print("data ke -",i,"=>",random.uniform(0.1,0.5)) random.uniform digunakan untuk menampilkan bilangan float random 
      dengan batas awal bilangan x dan batasan akhir bilangan y pada syntax ini batas awal bilangan nya adalah 0.1 dan
      batas akhir nya 0.5
      
 2. Flowchart
 
    ![Screenshot_2019-11-11-21-56-10-834_com google android apps docs](https://user-images.githubusercontent.com/56831922/68596716-3f4ce700-04ce-11ea-80a7-4938c33b2e52.png)

      
 3. hasil program :
 	
	![photo3](https://user-images.githubusercontent.com/56831922/68460542-b79b7a00-023a-11ea-8a65-2c39322f41bd.jpg)

