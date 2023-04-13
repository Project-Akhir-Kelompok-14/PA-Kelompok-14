import pwinput
import sys
import math
import os
import mysql.connector

mydb = mysql.connector.connect(
    host="db4free.net",
    user="kelompok14pa",
    password="sukseskelompok14",
    database="kelompok14pa"    
)
#LINKED LIST
class NodeDrakor:
    def __init__(self, Judul, Episode, Genre,
                 Tahun, Keterangan):
        self.Judul = Judul
        self.Episode = Episode
        self.Genre = Genre
        self.Tahun = Tahun
        self.Keterangan = Keterangan
        self.next = None

class LinkedDrakor:
    def __init__(self):
        self.head = None
        self.count = 0

    def getData(self, index):
        if index < 0 or index > self.count - 1:
            print("           Data tersebut tidak tersedia")
            return False
        else:
            nodeTampil = self.head
            for i in range(index):
                nodeTampil = nodeTampil.next
            LinkedDrakor.printData(nodeTampil)

    def updateDrakor(self, index):
        nodeUpdate = self.head
        for i in range (index):
            nodeUpdate = nodeUpdate.next
        updateJudul = input('Judul: ')
        updateEpisode = input('Episode: ')
        updateTahun = int(input('Tahun: '))
        updateKeterangan = input('Keterangan: ')

        nodeUpdate.Judul = updateJudul
        nodeUpdate.Episode = updateEpisode
        nodeUpdate.Keterangan = updateKeterangan
        nodeUpdate.Tahun = updateTahun
        print()
        print(">>> Berhasil Memperbarui Data <<<")

    def deleteNode(self, key):
        # Store head node
        temp = self.head
        if (temp is not None):
            if (temp.Judul == key):
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.Judul == key:
                break
            prev = temp
            temp = temp.next
            
        if(temp == None):
            return
 
        prev.next = temp.next
 
        temp = None
    
    def insertData(self, Judul, Episode, Genre, Tahun, Keterangan):
        if self.head is None:
            self.head = NodeDrakor(Judul, Episode, Genre, Tahun, Keterangan)
            self.count += 1

        else:
            nodeAkhir = self.head
            while nodeAkhir.next is not None:
                nodeAkhir = nodeAkhir.next
            nodeAkhir.next = NodeDrakor(Judul, Episode, Genre, Tahun, Keterangan)
            self.count += 1

    def tambah_drama(self, drama):
        if not self.head: # jika head kosong
            self.head = drama # drama akan menjadi head
        else: # jika head tidak kosong
            current = self.head # current akan menjadi head
            while current.next: # jika current.next tidak kosong
                current = current.next # current akan menjadi current.next
            current.next = drama # drama akan menjadi current.next

    def hapus_drama(self, judul): # parameter judul
        if not self.head:
            print("Tidak ada drama.")
            return
        if self.head.judul == judul:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.judul == judul:
                current.next = current.next.next
                return
            current = current.next
        print("Judul drama itu udah nggada.")


    # method untuk menampilkan drama berdasarkan halaman
    # default halaman = 1 dan per_halaman = 5
    # dengan menampilkan 5 drama per halaman
    def tampil_drama(self, halaman = 1, per_halaman = 5):
        start = (halaman - 1) * per_halaman # start = (halaman - 1) * per_halaman
        end = start + per_halaman # end = start + per_halaman
        current = self.head # current akan menjadi head
        drama_list = [] # drama_list akan menjadi list kosong
        while current: # jika current tidak kosong
            drama_list.append(current) # current akan ditambahkan ke drama_list
            current = current.next # current akan menjadi current.next
        if start >= len(drama_list): # jika start lebih besar atau sama dengan panjang drama_list
            return None # mengembalikan nilai None
        else: # jika start tidak lebih besar atau sama dengan panjang drama_list
            return drama_list[start:end] # mengembalikan nilai drama_list[start:end]


    def duplicate(self, judul):
        current = self.head
        while current is not None: #First loop
            if current.Judul.lower() == judul: 
                return True 
            current = current.next
        return False
    
    def printList(self):
        if self.head is None:
            print('Data Masih Kosong')
        else:
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
            print("                       LIST DRAKOR                      ")
            print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
            nomor = 1
            nodeTampil = self.head
            while nodeTampil is not None:
                print(" {}. {}".format(nomor, nodeTampil.Judul))
                nomor += 1
                nodeTampil = nodeTampil.next

    def iterate_item(self):
        current_item = self.tail
        while current_item:
            val = current_item.Name
            current_item = current_item.next
            yield val

    def printData(self, node):
        print("                     DETAIL DRAKOR")
        print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
        print(" Judul         : {}".format(node.Judul))
        print(" Episode       : {}".format(node.Episode))
        print(" Genre         : {}".format(node.Genre))
        print(" Tahun         : {}".format(node.Tahun))
        print(" Keterangan    : {}".format(node.Keterangan))

# SORT
    def sortedMerge(self, a, b):
        result = None
        if a == None:
            return b
        if b == None:
            return a
        if a.Judul < b.Judul:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result
     
    def mergeSort(self, h):
        if h == None or h.next == None:
            return h
        middle = self.getMiddle(h)
        nexttomiddle = middle.next
        middle.next = None
        left = self.mergeSort(h)
        right = self.mergeSort(nexttomiddle)
        sortedlist = self.sortedMerge(left, right)
        return sortedlist

    def getMiddle(self, head):
        if (head == None):
            return head
 
        slow = head
        fast = head
 
        while (fast.next != None and
               fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
             
        return slow

    def searchKey(self, index):
        if index < 0 or index > self.count - 1:
            print("")
            print(">>> Data tersebut tidak tersedia <<<")
            
        else:
            nodeTampil = self.head
            for i in range(index):
                nodeTampil = nodeTampil.next
                
            return nodeTampil.Judul
    
    def makeList(self): #Membuat List Data
        values = []
        current = self.head
        while current is not None: #First loop
            values.append({"Judul":(current.Judul), "Episode":(current.Episode), "Genre":(current.Genre), "Tahun":(current.Tahun), "Keterangan":(current.Keterangan)})
            current = current.next
        return values

def printDict(array,indexDrakor):
    print("Detail Drakor")
    print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
    print(" Judul        : {}".format(array[indexDrakor]["Judul"]))
    print(" Episode      : {}".format(array[indexDrakor]["Episode"]))
    print(" Genre        : {}".format(array[indexDrakor]["Genre"]))
    print(" Tahun        : {}".format(array[indexDrakor]["Tahun"]))
    print(" Keterangan   : {}".format(array[indexDrakor]["Keterangan"]))

def tambah_drama():
    judul = input("Masukkan judul drama: ")

    query = "SELECT * FROM drakor WHERE Judul = %s"
    values = (judul,)

    cursor = mydb.cursor()
    cursor.execute(query, values)

    drakor = cursor.fetchone()
    if drakor:
        sql = "INSERT INTO watchlist (Judul, Episode, Genre, Tahun, Keterangan) VALUES (%s, %s, %s, %s, %s)"
        cursor = mydb.cursor()
        cursor.execute(sql, drakor)
        mydb.commit()
        print("Drama Korea Telah Ditambahkan")
    else:
        print("Drama Korea Tidak Tersedia")

def hapus_drama():
    judul = input("Masukkan judul Drama yang mau dihapus: ")

    mycursor = mydb.cursor()
    sql = "DELETE FROM watchlist WHERE Judul = %s"
    values = (judul,)
    mycursor.execute(sql, values)

    mydb.commit()
    print("Drama ", judul, "udah dihapus!")
    # else:
    #     print("Drama ", judul, " udah dihapus!.")

def tampil_drama():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM watchlist")
    result = cursor.fetchall()
    if len(result) == 0:
        print("Tidak ada drama di watchlist saat ini.")
    else:
        print("===============================================================================================")
        print("{:<30} {:<20} {:<20} {:<10} {:<30}".format('Judul', 'Episode', 'Genre', 'Tahun', 'Keterangan'))
        print("===============================================================================================")
        for data in result:
            print("{:<30} {:<20} {:<20} {:<10} {:<30}".format(data[0], data[1], data[2], data[3], data[4]))
        print("===============================================================================================")

# SEARCH
def jumpSearch( array , namadrakor , n ):
    x = namadrakor
    step = math.sqrt(n)
    prev = 0
    
    while array[int(min(step, n)-1)]["Judul"].lower() < x.lower():
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    while array[int(prev)]["Judul"].lower() < x.lower():
        prev += 1
        if prev == min(step, n):
            return -1

    if array[int(prev)]["Judul"].lower() == x.lower(): 
        return prev
     
    return -1

class menuAdmin:
    def pilih1(self):
        LinkedDrakor.head = LinkedDrakor.mergeSort(LinkedDrakor.head) #MergeSort
        LinkedDrakor.barang() #printList

LinkedDrakor=LinkedDrakor()

def ulang(): #Opsi Pengulangan
    if True:
        yt=input("Kembali ke Menu? (y/t): ")
        if yt=="y":
            pass
        elif yt=="t":   
            sys.exit("SEE YOU LATER~~")
        else:
            print("Maaf input tidak benar!")
            ulang()

# Fungsi login user
def login_user():
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
                print("Login berhasil. Selamat Datang di Aplikasi Drama Korea, {}!".format(user[0]))
                menu_user()
                break
            else:
                print('=============Login Ditolak, Silahkan Coba Lagi=============')    
        except ValueError:
            print("============Silahkan Masukan Data Dengan Benar=============")
    
        # Fungsi login admin
def login_admin():
    os.system("cls")
    print("Silahkan Login")
    print("=" * 50)
    username = input("Masukkan username admin: ")
    password = pwinput.pwinput("Masukkan password admin: ")

            # Query untuk memeriksa keberadaan username dan password di tabel admin
    query = "SELECT * FROM admin WHERE username = %s AND password = %s"
    values = (username, password)

    cursor = mydb.cursor()
    cursor.execute(query, values)

    admin = cursor.fetchone()

            # Jika ditemukan admin dengan username dan password yang sesuai
    if admin:
        print("Login berhasil. Selamat datang, {}!".format(admin[0]))
        menu_admin()
    else:
        print("Login gagal. Silakan coba lagi.")



# MENU USER
def menu_user():
    while True:
        print("="*50)

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
            elif menu == 2:
                hapus_drama()
            elif menu == 3:
                tampil_drama()
            elif menu == 0:
                menu_utama()
            else :
                print("Opsi tidak valid")
            
        except:
            print("Masukan Kode Dengan Angka!")
            
# MENU ADMIN
def menu_admin():
    while True:
        print("="*50)
        
        print("="*50)
        print("1. Menampilkan Drama Korea")
        print("2. Menambahkan Drama Korea")
        print("3. Menghapus Drama Korea")
        print("4. Mengubah Drama Korea")
        print("0. Keluar dari Menu")
        print("="*50)
        try:
            pilih = int(input('Masukan pilihan menu: '))
            if pilih == 1 :
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM drakor")
                result = cursor.fetchall()
                if len(result) == 0:
                    print("Tidak ada drama di watchlist saat ini.")
                else:
                    print("===============================================================================================")
                    print("{:<30} {:<20} {:<20} {:<10} {:<30}".format('Judul', 'Episode', 'Genre', 'Tahun', 'Keterangan'))
                    print("===============================================================================================")
                    for data in result:
                        print("{:<30} {:<20} {:<20} {:<10} {:<30}".format(data[0], data[1], data[2], data[3], data[4]))
                    print("===============================================================================================")

            elif pilih == 2:
                break
            
            elif pilih == 3:
                LinkedDrakor.head = LinkedDrakor.mergeSort(LinkedDrakor.head) #MergeSort
                LinkedDrakor.printList() #printList
                try:
                    print("—————————————————————————————————————————————————————")
                    hapusDrakor = int(input("Masukkan pilihan: "))
                    index = hapusDrakor - 1
                    key = LinkedDrakor.searchKey(index)
                    if key != None:
                        print()
                        confirm = input("Apakah Anda ingin Menghapus {} (y/t)? ".format(key))
                        print()
                        if confirm.lower() == "y":
                            LinkedDrakor.deleteNode(key)
                            print(">>> Data berhasil di hapus <<<")
                        else:
                            print(">>> Penghapusan data dibatalkan <<<")
                except ValueError :
                            print("—————————————————————————————————————————————————————")
                            print("                Pilihan tidak tersedia               ")      

            elif pilih == 4:
                pilih1 = True
                LinkedDrakor.head = LinkedDrakor.mergeSort(LinkedDrakor.head) #MergeSort
                LinkedDrakor.printList() #printList
                while pilih1 == True:
                    try:
                        print("")
                        editDrakor = int(input("Masukkan pilihan: "))
                        index = editDrakor - 1
                        dataDrakor = LinkedDrakor.getData(index) #print Data
                        if dataDrakor != False:
                            print("")
                            updateDrakor = input("Ingin Ubah Data? (y/t) -> ")
                            if updateDrakor.lower() == "y":
                                LinkedDrakor.updateDrakor(index)
                                pilih1 == False
                            break
                    except ValueError :
                        print("—————————————————————————————————————————————————————")
                        print("               PILIHAN TIDAK TERSEDIA             ")
                        print("—————————————————————————————————————————————————————")
                        ulang()
                    break
            elif pilih == 0:
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
            elif kode == 2:
                login_user()
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

mycursor = mydb.cursor()

sql = "INSERT INTO drakor (Judul, Episode, Genre, Tahun, Keterangan) VALUES (%s, %s, %s, %s, %s)"
val = [
("Hotel del Luna", "16 Episode", "Drama", "2019", "Completed"),
("Reborn Rich", "16 Episode", "Drama", "2022", "Completed"),
("The Law Cafe","16 Episode", "Drama", "2022", "Completed"),
("Doom At Your Service","16 Episode","Fantasy", "2021", "Completed"),
("Strong Woman Do Bong Soon","16 Episode","Comedy","2017", "Completed"),
("Goblin","16 Episode", "Romance","2016", "Completed"),
("Mouse","20 Episode","Thriller","2021", "Completed"),
("Class of Lies","16 Episode","Mystery","2019", "Completed"),
("Extraordinary You","32 Episode","Fantasy","2019", "Completed"),
("Legend of the Blue Sea","20 Episode","Romance","2016", "Completed"),
("School 2017","16 Episode","School","2017", "Completed"),
("Sky Castle","20 Episode","Drama","2018", "Completed"),
("School 2015","16 Episode","School","2015", "Completed"),
("Dr. Romantic","20 Episode","Romance", "2016", "Completed"),
("Pinocchio","20 Episode","Comedy","2014", "Completed"),
("Summer Strike","12 Episode","Slice of Life","2022", "Completed"),
("Run On","16 Episode","Romance","2020", "Completed"),
("Reply 1988","20 Episode","Comedy","2015", "Completed"),
("Hell is Other People","10 Episode","Mystery","2019", "Completed"),
("Extracurricular","10 Episode","Criminal","2020", "Completed"),
]
mycursor.executemany(sql, val)
mydb.commit()