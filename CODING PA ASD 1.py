import pwinput
import os
import math
import mysql.connector


mydb = mysql.connector.connect(
    host="db4free.net",
    user="kelompok14pa",
    password="sukseskelompok14",
    database="kelompok14pa"    
)

########################### LINKED LIST ###########################
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

mycursor = mydb.cursor()
mycursor.execute("SELECT Judul, Episode, Genre, Tahun, Keterangan FROM drakor")
dramas = mycursor.fetchall()

linked_list = LinkedList()
for drama in dramas:
    data = f"Judul: {drama[0]}\nEpisode: {drama[1]}\nGenre: {str(drama[2])}\nTahun: {str(drama[3])}\nKeterangan: {drama[4]}"
    linked_list.add_node(data)


########################### SORTING ###########################
def merge_sort(cursor, drakor):
    # Mendapatkan data dari database
    cursor.execute(f"SELECT Judul FROM {drakor}")
    data = cursor.fetchall()

    # Mengkonversi data ke dalam list
    data_list = [item[0] for item in data]

    if len(data_list) <= 1:
        return data_list

    mid = len(data_list) // 2
    left = data_list[:mid]
    right = data_list[mid:]

    # Rekursif untuk melakukan pengurutan pada setiap bagian
    left = merge_sort(cursor, drakor)
    right = merge_sort(cursor, drakor)

    # Merge dua bagian yang telah diurutkan
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_watchlist():
    cursor = mydb.cursor()

    # Melakukan pengurutan dengan Merge Sort
    sorted_data = merge_sort(cursor, "watchlist")

    # Update data lama dengan data baru yang sudah diurutkan
    for i, item in enumerate(sorted_data):
        cursor.execute(f"UPDATE watchlist SET Judul = '{item}' WHERE id = {i+1}")

    mydb.commit()

    cursor.close()
    mydb.close()
    
########################### SEARCH ###########################
def jump_search(judul, watchlist):
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM {watchlist} ORDER BY Judul")
    data = cursor.fetchall()
    
    n = len(data)
    step = int(math.sqrt(n))
    prev = 0
    
    while data[min(step, n)-1][1] < judul:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    while data[prev][1] < judul:
        prev += 1
        
        if prev == min(step, n):
            return -1
    
    if data[prev][1] == judul:
        return data[prev]
    
    return -1
########################### FUNGSI MENU USER ###########################
def tambah_drama():
    os.system("cls")
    show_drama()
    judul = input("Masukkan Judul Drama Korea : ")
    query = "SELECT * FROM drakor WHERE Judul = %s"
    values = (judul,)
    mycursor = mydb.cursor()
    mycursor.execute(query, values)
    drakor = mycursor.fetchone()  
    if drakor:
        mycursor = mydb.cursor()
        sql = "SELECT * FROM watchlist WHERE Judul = %s"
        values = (judul,)
        mycursor.execute(sql, values)
        result = mycursor.fetchone()
        mydb.commit()
        if result:
            print("Drama Korea", judul, "Sudah Tersedia Di Watchlist")
        else:
            sql = "INSERT INTO watchlist (Judul, Episode, Genre, Tahun, Keterangan) VALUES (%s, %s, %s, %s, %s)"
            mycursor = mydb.cursor()
            mycursor.execute(sql, drakor)
            mydb.commit()
            print("Drama Korea Telah Ditambahkan")
    else:
        print("Drama Korea Tidak Tersedia")

def hapus_drama():
    os.system("cls")
    tampil_drama()
    judul = input("Masukkan judul Drama yang mau dihapus: ")
    mycursor = mydb.cursor()
    sql = "DELETE FROM watchlist WHERE Judul = %s"
    values = (judul,)
    mycursor.execute(sql, values)
    mydb.commit()
    if mycursor.rowcount > 0:
        print("Drama Korea", judul, "Sudah Di Hapus!")
    else:
        print("Drama Korea Tidak Tersedia")

def tampil_drama():
    os.system("cls")
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM watchlist")
    result = cursor.fetchall()
    if len(result) == 0:
        print("Tidak ada drama di watchlist saat ini.")
    else:
        print("===============================================================================================")
        print("                                         WATCHLIST                                             ")
        print("===============================================================================================")
        print("{:<30} {:<20} {:<20} {:<10} {:<30}".format('Judul', 'Episode', 'Genre', 'Tahun', 'Keterangan'))
        print("===============================================================================================")
        for data in result:
            print("{:<30} {:<20} {:<20} {:<10} {:<30}".format(data[0], data[1], data[2], data[3], data[4]))
        print("===============================================================================================")

def hapus_user():
    mycursor = mydb.cursor()
    sql = "DELETE FROM user "
    mycursor.execute(sql)
    mydb.commit()
def hapus_watchlist():
    mycursor = mydb.cursor()
    sql = "DELETE FROM watchlist"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "Anda Telah Keluar Dari Menu User")
    input("Tekan Enter Untuk Melanjutkan...")
    os.system("cls")

########################### FUNGSI MENU ADMIN ###########################
def show_drama():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM drakor")
    result = cursor.fetchall()
    if len(result) == 0:
        print("Tidak ada drama di watchlist saat ini.")
        print(input("Tekan Enter Untuk Melanjutkan..."))
        os.system("cls")
    else:
        print("===============================================================================================")
        print("{:<30} {:<20} {:<20} {:<10} {:<30}".format('Judul', 'Episode', 'Genre', 'Tahun', 'Keterangan'))
        print("===============================================================================================")
        for data in result:
            print("{:<30} {:<20} {:<20} {:<10} {:<30}".format(data[0], data[1], data[2], data[3], data[4]))
        print("===============================================================================================")

def add_drama():
    # buat cursor
    mycursor = mydb.cursor()
    # buat fungsi untuk menambah data ke database
    def tambah_data(judul, episode, genre, tahun, keterangan):
        # query untuk menambah data
        sql = "INSERT INTO drakor (Judul, Episode, Genre, Tahun, Keterangan) VALUES (%s, %s, %s, %s, %s)"
        # data yang akan dimasukkan
        val = (judul, episode, genre, tahun, keterangan)
        # eksekusi query
        mycursor.execute(sql, val)
        # commit perubahan ke database
        cursor = mydb.cursor()
        mydb.commit()
        cursor.execute("SELECT * FROM drakor")
        result = cursor.fetchall()
        if judul in result:
            print("Data Telah Tersedia")
            print(input("Tekan Enter Untuk Melanjutkan..."))
            os.system("cls")
        else:
            print(mycursor.rowcount, "Data Berhasil Ditambahkan")
            print(input("Tekan Enter Untuk Melanjutkan..."))
            os.system("cls")
    # meminta input dari pengguna
    judul = input("Masukkan judul: ")
    episode = input("Masukkan jumlah episode: ")
    genre = input("Masukkan genre: ")
    tahun = input("Masukkan tahun: ")
    keterangan = input("Masukkan keterangan: ")
    # memanggil fungsi untuk menambah data ke database
    tambah_data(judul, episode, genre, tahun, keterangan)

def delete_drama():
    mycursor = mydb.cursor()
    # Menampilkan data
    mycursor.execute("SELECT * FROM drakor")
    result = mycursor.fetchall()
    print("===============================================================================================")
    print("{:<30} {:<20} {:<20} {:<10} {:<30}".format('Judul', 'Episode', 'Genre', 'Tahun', 'Keterangan'))
    print("===============================================================================================")
    for data in result:
        print("{:<30} {:<20} {:<20} {:<10} {:<30}".format(data[0], data[1], data[2], data[3], data[4]))
    print("===============================================================================================")

    # Meminta input id yang akan dihapus
    hapus_judul = input("Masukkan judul yang akan dihapus: ")
    # Query untuk menghapus data berdasarkan id
    sql = "DELETE FROM drakor WHERE Judul = %s"
    val = (hapus_judul, )
    # Menjalankan query
    cursor = mydb.cursor()
    mycursor.execute(sql, val)
    cursor.execute("SELECT * FROM drakor")
    result = cursor.fetchall()
    # Melakukan commit untuk menyimpan perubahan
    mydb.commit()
    if hapus_judul in result:
        print(mycursor.rowcount, "Data Berhasil Di Hapus")
        print(input("Tekan Enter Untuk Melanjutkan..."))
        os.system("cls")
    else:
        print("Drama Korea Tidak Tersedia")
        print(input("Tekan Enter Untuk Melanjutkan..."))
        os.system("cls")

def update_drama():
    mycursor = mydb.cursor()
    # Mengambil data yang ingin diubah dari pengguna
    judul_lama = input("Masukkan judul drakor yang ingin diubah: ")
    tahun_lama = input("Masukkan tahun rilis drakor yang ingin diubah: ")
    # Menampilkan data yang ingin diubah kepada pengguna
    sql_select = "SELECT * FROM drakor WHERE Judul = %s AND Tahun = %s"
    val_select = (judul_lama, tahun_lama)
    mycursor.execute(sql_select, val_select)
    result = mycursor.fetchone()
    if result == None:
        print("Data yang ingin diubah tidak ditemukan.")
        print(input("Tekan Enter Untuk Melanjutkan..."))
        os.system("cls")
    else:
        print("Data yang ingin diubah adalah: ")
        print(result)

        # Mengambil data baru dari pengguna
        judul_baru = input("Masukkan judul baru: ")
        episode_baru = input("Masukkan jumlah episode baru: ")
        genre_baru = input("Masukkan genre baru: ")
        tahun_baru = input("Masukkan tahun rilis baru: ")
        keterangan_baru = input("Masukkan keterangan baru: ")

        # Memperbarui data di database
        sql_update = "UPDATE drakor SET Judul = %s, Episode = %s, Genre = %s, Tahun = %s, Keterangan = %s WHERE Judul = %s AND Tahun = %s"
        val_update = (judul_baru, episode_baru, genre_baru, tahun_baru, keterangan_baru, judul_lama, tahun_lama)
        mycursor.execute(sql_update, val_update)
        mydb.commit()
        print("Data telah berhasil diubah.")
        print(input("Tekan Enter Untuk Melanjutkan..."))
        os.system("cls")
        
# Fungsi login user
def login_user():
    os.system("cls")
    print("Silahkan Registrasi Terlebih Dahulu")  
    while True :
        try:
            while True:
                username = input('Silahkan Buat Username Anda :')
                if all(x.isspace() for x in username):
                    print("===========Username Tidak Boleh Kosong============")
                else:
                    break
            while True:
                password = pwinput.pwinput(prompt='Silahkan Buat Password Anda :', mask= '*')
                if all(x.isspace() for x in password):
                    print("==========Password Tidak Boleh Kosong============")
                else:
                    print(password)
                    break

            sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
            val = (username, password)
            cursor = mydb.cursor()
            cursor.execute(sql, val)
            mydb.commit()
            print('-----------------DATA DIKONFIRMASI-----------------')
            print("------------------Silahkan Login-------------------")
            username = input("Masukkan username: ")
            password = pwinput.pwinput("Masukkan password: ")
            # Query untuk memeriksa keberadaan username dan password di tabel user
            query = "SELECT * FROM user WHERE username = %s AND password = %s"
            values = (username, password)
            cursor = mydb.cursor()
            cursor.execute(query, values)
            user = cursor.fetchone()
            # Jika ditemukan user dengan username dan password yang sesuai
            if user:
                os.system("cls")
                print("Login berhasil. (＾▽＾) Selamat Datang di Aplikasi Drama Korea, {}! (＾▽＾)".format(user[0]))
                print(input("Tekan Enter Untuk Melanjutkan..."))
                os.system("cls")
                break
            else:
                print('=============Login Ditolak, Silahkan Coba Lagi=============')
                print(input("Tekan Enter Untuk Melanjutkan..."))
                os.system("cls")
        except ValueError:
            print("============Silahkan Masukan Data Dengan Benar=============")
    
# Fungsi login admin
def login_admin():
    os.system("cls")
    print("SILAHKAN LOGIN ADMIN")
    print("=" * 50)
    username = input("Username: ")
    password = pwinput.pwinput("Password: ")
    print("=" * 50)
    query = "SELECT * FROM admin WHERE username = %s AND password = %s"
    values = (username, password)
    cursor = mydb.cursor()
    cursor.execute(query, values)
    admin = cursor.fetchone()
    if admin:
        print("Login berhasil. (｡◕‿◕｡) SELAMAT DATANG, {}! (｡◕‿◕｡)".format(admin[0]))
        print(input("Tekan Enter Untuk Melanjutkan..."))
        os.system("cls")
        
    else:
        print("Login gagal. Silakan coba lagi.")
        print(input("Tekan Enter Untuk Melanjutkan..."))
        os.system("cls")

# MENU USER
def menu_user():
    while True:
        print("=" * 50)
        print("{:^50}".format("MENU USER"))
        print("="*50)
        print("1. Menambahkan Drama Korea ke dalam Watchlist")
        print("2. Menghapus Watchlist")
        print("3. Menampilkan Watchlist")
        print("0. Keluar dari Menu")
        print("="*50)
        try:
            menu = int(input('Masukan pilihan menu: '))
            if menu == 1 :
                tambah_drama()
                print(input("Tekan Enter Untuk Melanjutkan..."))
                os.system("cls")
            elif menu == 2:
                hapus_drama()
                print(input("Tekan Enter Untuk Melanjutkan..."))
                os.system("cls")
            elif menu == 3:
                tampil_drama()
                print(input("Tekan Enter Untuk Melanjutkan..."))
                os.system("cls")
            elif menu == 0:
                hapus_user()
                hapus_watchlist
                break
            else :
                print("Opsi tidak valid")
            
        except:
            print("Masukan Kode Dengan Angka!")
            
# MENU ADMIN
def menu_admin():
    while True:
        print("=" * 50)
        print("{:^50}".format("MENU ADMIN"))
        print("=" * 50)
        # Mencetak pilihan menu
        print("{:<3} {:<40}".format("1.", "Menampilkan Drama Korea"))
        print("{:<3} {:<40}".format("2.", "Menambahkan Drama Korea"))
        print("{:<3} {:<40}".format("3.", "Menghapus Drama Korea"))
        print("{:<3} {:<40}".format("4.", "Mengubah Drama Korea"))
        print("{:<3} {:<40}".format("0.", "Keluar dari Menu"))
        # Mencetak footer
        print("=" * 50)
        try:
            pilih = int(input('Masukan pilihan menu: '))
            if pilih == 1 :
                os.system("cls")
                show_drama()
                print(input("Tekan Enter Untuk Melanjutkan..."))
                os.system("cls")
            elif pilih == 2:
                os.system("cls")
                add_drama()
            elif pilih == 3:
                os.system("cls")
                delete_drama()
            elif pilih == 4:
                os.system("cls")
                update_drama()
            elif pilih == 0:
                os.system("cls")
                menu_utama()
            else :
                print("Opsi tidak valid")
            
        except:
            print("Masukan Kode Dengan Benar: 1/2/0")

def menu_utama():
    while True:
        print("======================================================")
        print("                    SELAMAT DATANG                    ")
        print("======================================================")
        print("                    1. LOGIN ADMIN                    ")
        print("                    2. LOGIN USER                     ")
        print("                    0. KELUAR                         ")
        print("======================================================")
        try:
            kode = int(input('Masukan pilihan menu: '))
            if kode == 1 :
                login_admin()
                menu_admin()
            elif kode == 2:
                login_user()
                menu_user()
            elif kode == 0:
                print("======================================================")
                print("                  SAMPAI JUMPA LAGI                   ")
                print("======================================================")
                break
            else :
                print("Opsi tidak valid")
            
        except:
            print("Masukan Kode Dengan Benar: 1/2/0")

menu_utama()
