def menu():
  print('''
==================================
Data Harga Kendaraan Bermotor
==================================

  [1] Tampilkan Data Kendaraan
  [2] Tambahkan Data Kendaraan
  [3] Mengedit Data Kendaraan
  [4] Hapus Data Kendaraan
  ''')

  no = int(input("\nMasukkan nomor menu yang ingin anda piih: "))

  no_index(no)

def no_index(a):
  if a == 1:
    tampilkan_data()
  elif a == 2:
    tambah_data()
  elif a == 3:
    edit_data()
  elif a == 4:
    hapus_data()
  else:
    print("Pilihan tersebut tidak tersedia!")

def tampilkan_data():
  print('''
  ============================
         Tampilan Data
  ============================
  ''')

  f = open("database.txt")
  isi = f.readlines()
  isi.sort()
  if len(isi) == 0:
    print("Data masih kosong")
  else:
    i = 1
    for x in isi:
      pisah = x.split(",")
      print("Data ke-", str(i))
      print("Nama Kendaraan: " +pisah[0])
      print("Tahun: " +pisah[1])
      print("Harga: " +pisah[2])
      i +=1

  print("Tekan [enter] untuk melanjutkan")
  f.close()
  input()
  menu()

def tambah_data():
  print('''
  =======================
  Menambah Data Kendaraan
  =======================
  ''')

  n = input("Nama Kendaraan: ")
  t = input("Tahun kendaraan: ")
  h = input("Harga kendaraan: ")

  f = open("database.txt", "a")
  f.writelines([n + ',' + t + ',' + h + '\n'])

  print("\nData berhasil ditambah")
  print()
  print("Tekan [enter] untuk melanjutkan")
  f.close()
  input()
  menu()

def edit_data():
  print(''' 
  ==============================
    Mengedit Data Kendaraan
  ==============================
  ''')

  upnama = input("Masukkan nama kendaraan yang ingin anda ubah: ")
  
  f = open("database.txt")
  isi = f.readlines()
  idx = 0
  for x in isi:
    data = x.split(",")
    if data[0] == upnama:
      print("Masukkan data baru")
      print("--------------------")
      nb = input("nama kendaraan: ")
      tb = input("Tahun kendaraan: ")
      hb = input("Harga Kendaraan: ")
      data[0] = nb
      data[1] = tb
      data[2] = hb +"\n"

      datax = ",".join(data)
      isi[idx] = datax
      break
    else:
      print("\nData tersebut tidak tersedia!")
      print("\nTekan [enter] untuk melanjutkan")
      f.close()
      input()
      menu()

    idx +=1
  f.close()

  f = open("database.txt", "w")
  isi = f.writelines(isi)
  print()
  print("Data berhasil diubah")
  print("\nTekan [enter] untuk melanjutkan")
  f.close()
  input()
  menu()

def hapus_data():
  print(''' 
  ==============================
     Menghapus Data Kendaraan
  ==============================
  ''')

  hapus = input("Masukkan nama kendaraan yang ingin anda hapus: ")

  f = open("database.txt")
  isi = f.readlines()
  isi.sort()

  idx = 0
  for i in isi:
    h = i.split(",")
    if h[0] == hapus:
      del(isi[idx])
      print("\nData telah berhasil dihapus")
      break
    else:
      print("\nData tersebut tidak tersedia!")
      print("\nTekan [enter] untuk melanjutkan")
      f.close()
      input()
      menu()
    idx +=1
  f.close()

  f = open("database.txt", "w")
  isi = f.writelines(isi)

  print("\nTekan [enter] untuk melanjutkan")
  f.close()
  input()
  menu()


menu()




  
  


