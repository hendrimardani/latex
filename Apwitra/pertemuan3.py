'''
var1 = 'Hello Nada'
var2 = 'Hendri Love Nada'
print('\n')
print('var1[0]', var1[6:10]+ ' Cantik')
print('var2[7:11]', var2[7:11])

print('\n')

nama = "{}, {} dan {}".format("Nada", "Hendri", "Anton")
print(nama)
print('\n')
nama = "{2}, {1} dan {0}".format("Nada", "Hendri", "Anton")
print(nama)

print('\n')

nomor = "{0}, {4}, {2}, {3}, {1}".format("2", "4", "6", "8", "10")
print(nomor)
print("\n")

print("|{:<10}|{:^10}|{:>10}|".format('Asin', 'Tahu', 'Tempe'))
'''
print('\n')

print("{:^50}".format("TOKO MAININAN"))
print("{:^50}".format("========^_^========="))
meli = input("Nama Pembeli = ")
mainan = input("Kode Mainan = ")
harga = int(input("Harga = "))
sabaraha = int(input("Jumblah Beli = "))

total = harga * sabaraha

print("{:^50}".format("NOTA TRANSAKSI"))
print("{:^50}".format("========^_^========="))
print("Nama Pembeli = "+str(meli))
print("Kode Mainan = "+str(mainan))
print("Harga = ", harga)
print("Jumblah Beli = ", harga)
print("Tolat = ", total)

print("\n")

uangbayar = int(input("Masukan Uang Bayar = "))
proses_uang = uangbayar - total
print("Uang Kembali = ",proses_uang)

print("\n")

print("{:^50}".format("==================================="))
print("{:^50}".format("HATUR NUHUN SING AWET BARANGNA :)"))
print("{:^50}".format("==================================="))
