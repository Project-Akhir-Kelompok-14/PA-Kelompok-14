import json
from prettytable import PrettyTable
import pwinput
import sys
import math

# DATA DRAKOR
#LOKASI BERDASARKAN LETAK PENYIMPANAN FILE YANG TERHUBUNG DI PERANGKAT YANG DIGUNAKAN
loc = r"C:\Users\ASUS\PA ASD SEM 2\111.json"
with open (loc, 'r') as data:
    drakor = json.load(data)

tabel_drakor = PrettyTable()
tabel_drakor.field_names = ["JUDUL DRAMA", "EPISODE", "TAHUN RILIS", "KETERANGAN"]
tabel_drakor.clear_rows()

nama = drakor.get("judul")
eps = drakor.get("episode")
tanggal = drakor.get("tahun")
ket = drakor.get("keterangan")

def barang():
          for i in range(len(nama)):
              tabel_drakor.add_row([nama[i], eps[i], tanggal[i], ket[i]])
          print(tabel_drakor)
          tabel_drakor.clear_rows()


#LINKED LIST
class NodeDrakor:
    def __init__(self, Judul, Episode,
                 Tahun, Keterangan):
        self.Judul = Judul
        self.Episode = Episode
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
    
    def insertData(self, Judul, Episode,
                 Tahun, Keterangan):
        if self.head is None:
            self.head = NodeDrakor(Judul, Episode,
                 Tahun, Keterangan)
            self.count += 1

        else:
            nodeAkhir = self.head
            while nodeAkhir.next is not None:
                nodeAkhir = nodeAkhir.next
            nodeAkhir.next = NodeDrakor(Judul, Episode,
                 Tahun, Keterangan)
            self.count += 1

    def newData(self, JudulBaru): #Tambah data Drakor
        try:
            EpisodeBaru = input("Episode: ")
            tahunBaru = int(input("Tahun Terbit: "))
            KeteranganBaru = input("Keterangan: ")

            LinkedDrakor.insertData( JudulBaru, EpisodeBaru,
                                tahunBaru, KeteranganBaru)
            print()
            print(">>> Data baru berhasil ditambahkan <<<!")
            print()
            return True
        except ValueError:
            print('Input Dengan Benar! ')
            return False

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
            values.append({"Judul":(current.Judul), "Episode":(current.Episode),"Tahun":(current.Tahun),"Keterangan":(current.Keterangan)})
            current = current.next
        return values

def printDict(array,indexDrakor):
    print("Detail Drakoe")
    print("┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")
    print(" Judul        : {}".format(array[indexDrakor]["Judul"]))
    print(" Episode      : {}".format(array[indexDrakor]["Episode"]))
    print(" Tahun        : {}".format(array[indexDrakor]["Tahun"]))
    print(" Keterangan   : {}".format(array[indexDrakor]["Keterangan"]))


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
LinkedDrakor.insertData("Reborn Rich", "16 Episode", "2022", "Completed")
LinkedDrakor.insertData("The Law Cafe","16 Episode","2022", "Completed")
LinkedDrakor.insertData("Doom At Your Service","16 Episode","2021", "Completed")
LinkedDrakor.insertData("Strong Woman Do Bong Soon","16 Episode","2017", "Completed")
LinkedDrakor.insertData("Goblin","16 Episode","2016", "Completed")
LinkedDrakor.insertData("Mouse","20 Episode","2021", "Completed")
LinkedDrakor.insertData("Class of Lies","16 Episode","2019", "Completed")
LinkedDrakor.insertData("Hotel del Luna","16 Episode","2019", "Completed")
LinkedDrakor.insertData("Extraordinary You","32 Episode","2019", "Completed")
LinkedDrakor.insertData("Legend of the Blue Sea","20 Episode","2016", "Completed")
LinkedDrakor.insertData("School 2017","16 Episode","2017", "Completed")
LinkedDrakor.insertData("Sky Castle","20 Episode","2018", "Completed")
LinkedDrakor.insertData("School 2015","16 Episode","2015", "Completed")
LinkedDrakor.insertData("Dr. Romantic","20 Episode","2016", "Completed")
LinkedDrakor.insertData("Pinocchio","20 Episode","2014", "Completed")
LinkedDrakor.insertData("Summer Strike","12 Episode","2022", "Completed")
LinkedDrakor.insertData("Run On","16 Episode","2020", "Completed")
LinkedDrakor.insertData("Reply 1988","20 Episode","2015", "Completed")
LinkedDrakor.insertData("Hell is Other People","10 Episode","2019", "Completed")
LinkedDrakor.insertData("Extracurricular","10 Episode","2020", "Completed")

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

#LOKASI BERDASARKAN LETAK PENYIMPANAN FILE YANG TERHUBUNG DI PERANGKAT YANG DIGUNAKAN
loc = r"C:\Users\ASUS\PA ASD SEM 2\222.json"

with open (loc, 'r') as lihat_admin:
    admin = json.load(lihat_admin)

username = admin.get ("admin")
sandi = admin.get ("pass")

def login_user():
    print("-----------Silahkan Registrasi Terlebih Dahulu---------")  
    while True :
        try:
            while True:
                user_1 = input('Silahkan Buat Username Anda :')
                if all(x.isspace() for x in user_1):
                    print("===========Username Tidak Boleh Kosong============")
                else:
                    break
            while True:
                pw_1 = pwinput.pwinput(prompt='Silahkan Buat Password Anda :', mask= '*')
                if all(x.isspace() for x in pw_1):
                    print("==========Password Tidak Boleh Kosong============")
                else:
                    print(pw_1)
                    break
            print('-----------------DATA DIKONFIRMASI-----------------')
            print("------------------Silahkan Login-------------------")
            user_2 = input('Masukan Username Anda: ')
            pw_2 = pwinput.pwinput(prompt='Masukan Password Anda: ', mask= '*')
        
            if user_2 == user_1 and pw_2 == pw_1:
                print("======================Berhasil Login=======================")
                print('-----Selamat Datang di Apotek PTD ' + user_1 +'-----')
                print('Apakah Ada Yang Bisa Dibantu?')
                break
            else:
                print('=============Login Ditolak, Silahkan Coba Lagi=============')    
        except ValueError:
            print("============Silahkan Masukan Data Dengan Benar=============")

def login_admin():
    print("------------------Silahkan Login-------------------")
    nama = input ("Masukkan nama: ")
    password = pwinput.pwinput(prompt="Masukkan password: ", mask= '*')
    try:
        cari = username.index(nama)
        if (nama == username[cari] and password == sandi[cari]):
            print ("===================Berhasil Login===================")
            menu_admin()
        else:
            print ("===============Password Anda Salah==================")
            print ("================Silahkan Coba Lagi==================")
    except ValueError:
        print ("===================Username tidak ada===================")
        print ("===================Silahkan Coba Lagi===================")

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
                menu_admin()
            elif menu == 2:
                menu_user()
            elif menu == 3:
                break
            elif menu == 4:
                break
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
                LinkedDrakor.head = LinkedDrakor.mergeSort(LinkedDrakor.head) #MergeSort
                LinkedDrakor.printList() 

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
                menu_admin()
            elif kode == 2:
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