'''
    Tugas Mandiri 1 dan 2 Logika dan Algoritma
    Nama    :   Aprillian Dwi Putra
    NIM     :   19230163
    Prodi   :   Sistem Informasi
    Kelas   :   1C
'''

print("\n")

print("{:^50}".format("TRANSPORTASI"))
print("{:^50}".format("================"))

print("\n")

uangangkot = int(input("Masukan Uang Angkot = "))
byr_angkot = int(input("Uang Ibu = "))
pro_uang = byr_angkot - uangangkot
print("Uang Kembali = ",pro_uang)

print("\n")

print("{:^50}".format("TOKO FEBRI"))
print("{:^50}".format("========^_^========="))
meli = input("Nama Pembeli = ")
mainan = input("Kode Barang = ")
harga = int(input("Harga = "))
sabaraha = int(input("Jumblah Beli = "))

total = harga * sabaraha

print("{:^50}".format("NOTA TRANSAKSI"))
print("{:^50}".format("========^_^========="))
print("Nama Pembeli = "+str(meli))
print("Kode Barang = "+str(mainan))
print("Harga = ", harga)
print("Jumblah Beli = ", harga)
print("Tolat = ", total)

print("\n")

uangbayar = int(input("Masukan Uang Bayar = "))
proses_uang = uangbayar - total
print("Uang Kembali = ",proses_uang)

print("\n")

print("{:^50}".format("==================================="))
print("{:^50}".format("HATUR NUHUN:)"))
print("{:^50}".format("==================================="))

print("\n")

print("{:^50}".format("TRANSPORTASI"))
print("{:^50}".format("================"))

print("\n")

uangangkot1 = int(input("Masukan Uang Angkot = "))
byr_angkot1 = int(input("Uang Ibu = "))
pro_uang1 = byr_angkot1 - uangangkot1
print("Uang Kembali = ",pro_uang1)
print("\n")
print(f"Jadi sisa uang ibu dari {byr_angkot} ribu adalah {pro_uang1} ribu")
print("\n")