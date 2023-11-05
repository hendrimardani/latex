print("\n")

print("{:^50}".format("TPendaftaran Mahasiswa/i Baru"))
print("{:^50}".format("="*25))
nama = input("Masukkan Nama Mahasiswa/i : ")
nis = input("Masukkan NIS : ")
jurusan = input("Masukkan Kode Jurus[SI/SIA] : ")
kelas = input("Masukkan Pilihan Kelas [Pagi/Malam] : ")

harga = 0
# Proses
if jurusan == "SI":
    nama_jurusan = "Sistem Informasi"
    harga = 2400000
    
    if kelas == "Malam" or kelas == "malam":
        harga += 500000
elif jurusan == "SIA":
    nama_jurusan = "Sistem Informasi Akuntansi"
    harga = 2000000

    if kelas == "Malam" or kelas == "malam":
        harga += 500000
else:
    print("DATA YANG ANDA MASUKKAN TIDAK ADA")

print("\n")

print("==BUKTI PENDAFTARAN MAHASISWA BARU==")
print(f"Nama Anda : {nama}")
print(f"NIS Anda : {nis}")
print(f"Kode Jurusan yang anda pilih : {jurusan}")
print(f"Kelas yang anda pilih : {kelas}")
print(f"Nama Prodi yang anda pilih : {nama_jurusan}")
print(f"Biaya Yang Harus Anda Bayar : {harga}")
print("="*25)