# Dokumentasi Program Watchlist Drakor
## Anggota Kelompok 14:
- Siti Solikah Yosi Karinda (2209116029)
- Remanda Dheva (2209116034)
- Stephanie Elfriede Ginting (2209116037)


## Deskripsi Program
Program Watchlist adalah program yang memungkinkan pengguna untuk mencatat daftar drama, film atau acara yang ingin mereka tonton. Dalam kasus Watchlist Drama Korea, program ini difokuskan pada daftar drama Korea yang ingin ditonton. Program ini memudahkan pengguna untuk menambah, menghapus, dan memperbarui daftar drama Korea yang ingin mereka tonton. Program Watchlist Drama Korea ini menggunakan struktur data linked list dan database MySQL untuk menyimpan data pengguna dan data drama Korea yang dipilih oleh pengguna. Dengan program ini, pengguna dapat dengan mudah mengelola daftar drama Korea yang ingin mereka tonton. Program ini juga memiliki beberapa fungsi yang hanya bisa diakses oleh admin, sehingga pengguna atau user tidak dapat mengubah data asli pada program ini.

## Struktur Project
### Database
- MySQL: MySQL digunakan untuk menyimpan dan mengelola data pengguna, admin, data drama korea yang tersedia dan data drama Korea yang ingin ditonton oleh pengguna. 
### Modul
- Pwinput: Pwinput digunakan untuk mengamankan password agar tidak terlihat oleh orang lain saat melakukan login. 
- Os: Os digunakan untuk membersihkan layar terminal, sehingga tampilan menjadi lebih rapi dan mudah dibaca. 
- MySQL Connector: MySQL Connector digunakan untuk menghubungkan program Python dengan database MySQL. 
- Math: Math digunakan untuk melakukan operasi matematika di dalam program Python.

### Linked List
Linked List adalah struktur data yang terdiri dari urutan record data dimana setiap record memiliki field yang menyimpan alamat/referensi dari record selanjutnya (dalam urutan). Elemen data yang dihubungkan dengan link pada linked list disebut Node.
Di dalam Linked List memiliki:
- Head : Elemen yang berada pada posisi pertama 
- Tail : Elemen yang berada pada posisi terakhir 

Operasi yang kami gunakan dalam Linked List adalah "add" yang berfungsi untuk menambahkan data dan digunakan untuk menyimpan data dari tabel drakor dalam database. Kami menggunakan Singly Linked List yang hanya memiliki satu variabel pointer untuk menyimpan banyak data. 

### Function

Kami menggunakan Fungsi Def dalam program yang kami buat. Fungsi adalah kumpulan perintah atau baris kode yang dikelompokkan menjadi satu kesatuan untuk kemudian bisa dipanggil atau digunakan berkali-kali.
Berikut adalah function-function yang kami buat:
- def merge sort: untuk mengurutkan list data list dengan algoritma Merge Sort.
- def merge: untuk menggabungkan dua list yang terurut, yaitu list left dan right.
- def jump search: untuk mencari data dalam sebuah list yang terurut.
- def tambah drama: untuk menambahkan drama ke dalam watchlist.
- def hapus drama: untuk menghapus drama dari database watchlist.
- def tampil drama: untuk menampilkan data drama.
- def hapus user: untuk menghapus semua data dari tabel user di database.
- def hapus watchlist: untuk menghapus semua data dari tabel watchlist di dalam database. 
- def show drama: untuk menampilkan daftar drama Korea yang tersedia dalam database, termasuk judul, episode, genre, tahun, dan keterangan dari masing-masing drama. 
- def add drama: untuk menambah data drama baru ke dalam database. 
- def delete drama: untuk menghapus data drama Korea dari database berdasarkan judul yang dimasukkan oleh pengguna.
- def cari drakor: untuk mencari data drama korea berdasarkan judul yang diinputkan oleh pengguna.
- def update drama: untuk mengubah data drama Korea dalam database. 
- def login user: untuk melakukan proses login pengguna ke dalam program Drama Korea. 
- def login admin: untuk melakukan proses login bagi admin pada program Drama Korea.
- def menu user:untuk menampilkan menu-menu yang dapat dilakukan oleh pengguna dalam program Drama Korea.
- def menu admin:untuk menampilkan menu-menu yang dapat dilakukan oleh admin dalam program Drama Korea.
- def menu utama: untuk menampilkan pilihan untuk login sebagai admin atau user dan keluar dari program. 


## Fitur dan Fungsionalitas
Fitur dan Fungsionalitas Watchlist Drakor terbagi menjadi 2 bagian, yaitu untuk pengguna dan untuk admin.

Untuk Pengguna:
1. Menambahkan Drama Korea ke dalam Watchlist: Pengguna dapat menambahkan judul drama Korea ke dalam daftar Watchlist dengan memasukkan judul drama.
2. Menghapus Watchlist: Pengguna dapat menghapus judul drama Korea dari daftar Watchlist jika ingin menghapusnya atau sudah menontonnya.
3. Menampilkan Watchlist: Pengguna dapat melihat daftar drama Korea yang telah ditambahkan ke dalam Watchlist beserta informasi tontonannya.

Untuk Admin:
1. Menampilkan Drama Korea: Admin dapat melihat daftar seluruh drama Korea yang tersimpan di database.
2. Menghapus Drama Korea: Admin dapat menghapus drama Korea dari database jika dianggap tidak relevan.
3. Menambahkan Drama Korea: Admin dapat menambahkan judul drama Korea baru ke dalam database dengan memasukkan informasi seperti judul, jumlah episode, genre, tahun rilis, dan keterangan (on going atau completed).
4. Mengubah Drama Korea: Admin dapat mengubah informasi dari judul drama Korea yang telah tersimpan di database, seperti judul, jumlah episode, genre, tahun rilis, dan keterangan (on going atau completed).
5. Mencari Drama Korea: Admin dapat melakukan pencarian drama korea yang tersimpan di database, dengan memasukkan informasi judul drama yang diinginkan.

## Cara Penggunaan

- Tampilan awal akan menampilkan menu Login Admin, Login User dan Keluar 

![image](https://user-images.githubusercontent.com/122278611/235304175-30fd28ed-6c08-40d3-b29d-3d43114b90e2.png)

- Login Admin :
Didalam login admin akan diminta untuk memasukan username dan password admin sesuai dengan data yang ada pada database admin.Setelah login berhasil dapat melanjutkan ke langkah selanjutnya dengan menekan enter 

![image](https://user-images.githubusercontent.com/122278611/235304674-e51fb310-a903-44c2-a15b-e114df56f5d8.png)


- Login User :
Pengguna akan diminta untuk registrasi terlebih dahulu dengan memasukkan username dan password. Setelah data dikonfirmasi atau data masuk pada database, pengguna akan diminta melakukan login sesuai dengan username dan password yang telah dibuat sebelumnya. Setelah login berhasil, pengguna akan diminta untuk menekan tombol enter untuk melanjutkan ke menu selanjutnya.

Registrasi 
![image](https://user-images.githubusercontent.com/122278611/235309739-2345b5af-4ee8-4c7e-b4b2-647ee93c101f.png)

Login
![image](https://user-images.githubusercontent.com/122278611/235309825-3e5b38a5-cefc-4605-8af6-59dda550085d.png)
![image](https://user-images.githubusercontent.com/122278611/235309912-4d31ff9b-13a2-4284-ac3f-c06abb495463.png)





- Menu Admin : 
Setelah menekan enter pada login admin, maka akan ditampilkan menu admin 
Admin dapat menampilkan, Menambah, Menghapus, Mengubah, serta mencari Drama. Admin juga dapat keluar dari menu admin dan kembali pada menu awal yaitu menu login 

![image](https://user-images.githubusercontent.com/122278611/235304806-555a9a4c-c443-437f-881e-5740b65894f7.png)




1. Menampilkan Drama Korea 

![image](https://user-images.githubusercontent.com/122278611/235310668-bbc5b333-d9a8-43fe-b528-a0c15c3c38dc.png)

Menu ini akan menampilkan semua list drama korea yang ada, urut per abjad
drama korea yang ditampilkan juga lengkap dengan Judul, Episode, Genre, Tahun dan Keterangan apakah drama tersebut telah selesai(completed) atau sedang berjalan(on going)




2. Menambah Drama Korea

![image](https://user-images.githubusercontent.com/122278611/235310808-4e2e7c14-1340-468c-930b-6547696d37b3.png)

Dalam Menu ini admin diminta untuk memasukan judul, jumlah, genre, tahun, dan keterangan. setelah itu data akan dimasukan dalam data

![image](https://user-images.githubusercontent.com/122278611/235310820-ff8e79af-c9fb-4051-9785-8b44c969138b.png)




3. Menghapus Drama Korea 


Dalam menu ini admin diminta untuk memasukan judul drama yang akan dihapus, menu ini juga menampilkan list drama korea yang ada agar memudahkan admin untuk mencari judul drama yang ingin dihapus.

setelah memasukan judul drama yang akan dihapus maka drama akan terhapus 

![image](https://user-images.githubusercontent.com/122278611/235310857-6c6de397-5ea9-4e29-a894-b4baba317db8.png)




4. Mengubah Drama Korea 


Dalam menu ini admin diminta untuk memasukan judul dan tahun rilis drama yang akan diubah. setelah itu program akan mencari drama yang telah di input 


![image](https://user-images.githubusercontent.com/122278611/235310952-5908f3b9-9873-4e52-9ef6-7bc7ba7a8b75.png)




setelah menemukan drama yang akan diubah admin akan diminta untuk memasukan judul, jumlah episode, genre, tahun rilis, dan keterangan drama yang akan diubah


![image](https://user-images.githubusercontent.com/122278611/235311097-a233c602-cc68-4f2a-9943-d52d20d53d5e.png)



setelah itu drama akan diubah 


![image](https://user-images.githubusercontent.com/122278611/235311126-b601cd98-5160-4617-b1ca-ba63fb7f1ad2.png)










5. Mencari Drama Korea 


untuk mencari drama admin diminta untuk memasukan judul drama, setelah itu akan menampilkan keterangan dari drama yang dicari 

![image](https://user-images.githubusercontent.com/122278611/235311151-e897bdca-d2bf-41eb-9573-763fa69856d9.png)








0. Keluar dari Menu 

jika admin ingin keluar dari menu maka akan kembali pada menu awal yaitu menu login 


![image](https://user-images.githubusercontent.com/122278611/235307565-35846b54-7229-4842-9931-167571333521.png)









- Menu User :
Setelah pengguna berhasil login maka akan ditampilkan menu user yang dimana pengguna dapat menambahkan, menghapus maupun menampilkan Drama Korea yang ada dalam database watchlist.

![image](https://user-images.githubusercontent.com/122278611/235309985-9a759902-1bbe-4f80-a10d-6217a1a402cc.png)





1. Menambahkan Drama Korea ke dalam Watchlist 


![image](https://user-images.githubusercontent.com/122278611/235310042-d8418770-0f6b-43be-909b-fa26700eb011.png)






Pada menu ini pengguna dapat menambahkan Drama Korea yang ada dalam database ke dalam Watchlist nya sendiri. Dengan mencantumkan judul drama Korea yang diinginkan, maka drama tersebut akan masuk ke dalam database watchlist pengguna.


Drama setelah ditambahkan 


berikut adalah tampilan drama korea yang telah ditambahkan ke dalam Watchlist pengguna.


![image](https://user-images.githubusercontent.com/122278611/235310278-2751afb7-6544-4593-a38f-52e1dd537298.png)






2. Menghapus Drama Korea Dalam Watchlist 



![image](https://user-images.githubusercontent.com/122278611/235310378-32ffcd29-a647-44c6-9480-81fa71955493.png)



Pada menu ini pengguna dapat menghapus drama Korea yang ada di dalam watchlist dengan memasukkan judul drama yang ingin di hapus dan drama tersebut akan di hapus dari database watchlist pengguna.



3. Menampilkan Watch List


Berikut merupakan tampilan saat pengguna memilih menu ketiga ini, yaitu akan ditampilkan watchlist pengguna


![image](https://user-images.githubusercontent.com/122278611/235310416-bf932ca9-df7f-42a1-aeea-7b54e78eaf25.png)






0. keluar dari menu 


Jika memilih menu ini, pengguna akan keluar dari menu user dan data pengguna akan ikut terhapus dalam database dan pengguna akan kembali ke menu awal.


![image](https://user-images.githubusercontent.com/122278611/235310461-4fbb7aad-8a26-4064-b76f-cadb082c4a0f.png)






- Keluar dari menu awal 


Jika memilih menu ini pengguna akan keluar dari menu dan program ini berakhir.

![image](https://user-images.githubusercontent.com/122278611/235310498-7f08d171-7c36-463d-ad70-4f3cc9c29dd8.png)





---
