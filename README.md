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

Tampilan awal akan menampilkan menu Login Admin, Login User dan Keluar 

![image](https://user-images.githubusercontent.com/122278611/235304175-30fd28ed-6c08-40d3-b29d-3d43114b90e2.png)

Login Admin :
Didalam login admin akan diminta untuk memasukan username dan password admin 
setelah login berhasil dapat melanjutkan ke langkah selanjutnya dengan menekan enter 

![image](https://user-images.githubusercontent.com/122278611/235304674-e51fb310-a903-44c2-a15b-e114df56f5d8.png)




Menu Admin : 
Setelah menekan enter pada login admin, maka akan ditampilkan menu admin 
Admin dapat menampilkan, Menambah, Menghapus, Mengubah, serta mencari Drama. Admin juga dapat keluar dari menu admin dan kembali pada menu awal yaitu menu login 

![image](https://user-images.githubusercontent.com/122278611/235304806-555a9a4c-c443-437f-881e-5740b65894f7.png)



1. Menampilkan Drama Korea 

![image](https://user-images.githubusercontent.com/122278611/235304897-013c386b-18aa-42ca-803c-6fe86fb33916.png)

menu ini akan menampilkan semua list drama korea yang ada, urut per abjad
drama korea yang ditampilkan juga lengkap dengan Judul, Episode, Genre, Tahun dan Keterangan apakah drama tersebut telah selesai(completed) atau sedang berjalan(on going)



2. Menambah Drama Korea
![image](https://user-images.githubusercontent.com/122278611/235305848-b24e9047-16f5-4f7c-8072-9d1d423cd72f.png)

Dalam Menu ini admin diminta untuk memasukan judul, jumlah, genre, tahun, dan keterangan. setelah itu data akan dimasukan dalam data

![image](https://user-images.githubusercontent.com/122278611/235305935-510282db-708b-4170-ae18-6b63608f840f.png)



3. Menghapus Drama Korea 
dalam menu ini admin diminta untuk memasukan judul drama yang akan dihapus, menu ini juga menampilkan list drama korea yang ada agar memudahkan admin untuk mencari judul drama yang ingin dihapus.

![image](https://user-images.githubusercontent.com/122278611/235306172-5cd06bef-7ff3-4185-894a-3b6511946911.png)

setelah memasukan judul drama yang akan dihapus maka drama akan terhapus 

![image](https://user-images.githubusercontent.com/122278611/235306220-ded7a245-bbd3-4085-b3ed-d5886a1bcc65.png)
















---
