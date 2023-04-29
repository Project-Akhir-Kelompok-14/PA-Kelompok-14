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
### Linked List
Link List adalah struktur data yang terdiri dari urutan record data dimana setiapbrecord memilikifield yang menyimpan alamat/referensi dari record selanjutnya (dalam urutan).Elemen data yang dihubungkan dengan link pada linked list disebut Node.

di dalam Linked List memiliki 
- Head : Elemen yang berada pada posisi pertama 
- Tail : Elemen yang berada pada posisi terakhir 

Operasi yang kami gunakan dalam Linked List adalah "add" yang berfungsi untuk menambahkan data

Kami menggunakan Singly Linked List yang hanya memiliki satu variabel pointer untuk menyimpan banyak data

---
### Function

Kami menggunakan Fungsi Def dalam program yang kami buat 
Fungsi adalah kumpulan perintah atau baris kode yang dikelompokkan menjadi satu kesatuan untuk kemudian bisa dipanggil atau digunakan berkali-kali 

---


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
---
