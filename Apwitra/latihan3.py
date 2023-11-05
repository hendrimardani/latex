print("\n")
print("{:^50}".format("OMAN TRAVEL GELO"))
print("{:^50}".format("------------------------------------"))
pembeli=input("Input Nama Pembeli : ")
no_hp=input("Input No. Handphone : ")
jurusan=input("Input Jurusan [SBY/BL/LMP]: ")

#Proses
if jurusan=="SBY":
    namajurusan="Surabaya"
    harga=300000
elif jurusan=="BL":
    namajurusan="Bali"
    harga=350000
else :
    namajurusan="Lampung"
    harga=500000

print("\n")

#Cetak Hasil
print("------------------------------------")
print("PENJUALAN TIKET BUS")
print("XYZ")
print("------------------------------------")
print("Nama Pembeli : "+str(pembeli))
print("No. Handphone : "+str(no_hp))
print("Kode Jurusan yang dipilih : "+str(jurusan))
print("Nama Kota Tujuan : "+str(namajurusan))
print("Harga: ",+(harga))
print("Jumlah Beli: ",+(jumlah))
print("------------------------------------")

print("\n")

#Input Jumlah Beli
jumlah=int(input("Masukkan Jumlah Beli : ")) 
print("potongan yang didapat : ",+(potongan))
print("Total Bayar: ",+(total))
ubay=int(input("Masukkan Uang Bayar : "))
#proses potongan
uangkembali=ubay-total
if jumlah>=3 :
    print("Uang Kembali : ",+uangkembali)
    potongan=(jumlah*harga)*0.1
else:
    potongan=0
    total=(jumlah*harga)-potongan