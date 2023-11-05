# nama = input("Masukkan Nama Mahasiswa/i : ")
# nis = input("Masukkan NIS : ")
# jurusan = input("Masukkan Kode Jurus[SI/SIA] : ")
# kelas = input("Masukkan Pilihan Kelas [Pagi/Malam] : ")


# def proses(nama, nis, jurusan, kelas):
#     bisa = False

#     if jurusan == "SI" or jurusan == "si":
#         harga = 2400000
#         nama_jurusan = "Sistem Informasi"

#         if kelas == "MALAM" or kelas == "malam":
#             harga += 500000
#         elif kelas == "pagi" or kelas == "pagi":
#             harga = 2400000
#         else:
#             bisa = True
#             dataKosong = "Data yang diinputkan tidak ada"
#     elif jurusan == "SIA" or jurusan == "sia":
#         harga = 2000000
#         nama_jurusan = "Sistem Informasi Akuntansi"

#         if kelas == "MALAM" or kelas == "malam":
#             harga += 500000
#         elif kelas == "pagi" or kelas == "PAGI":
#             harga = 2000000
#         else:
#             bisa = True
#             dataKosong = "Data yang diinputkan tidak ada"
#     else:
#         bisa = True
#         dataKosong = "Data yang dinputkan tidak ada"

#     if bisa:
#         print("\n")
#         print(dataKosong)
#     else:
#         print("\n")
#         print("==BUKTI PENDAFTARAN MAHASISWA BARU==")
#         print(f"Nama Anda : {nama}")
#         print(f"NIS Anda : {nis}")
#         print(f"Kode Jurusan yang anda pilih : {jurusan}")
#         print(f"Kelas yang anda pilih : {kelas}")
#         print(f"Nama Prodi yang anda pilih : {nama_jurusan}")
#         print(f"Biaya Yang Harus Anda Bayar : {harga}")
#         print("\n")

# proses(nama, nis, jurusan, kelas)







def proses():
    bisa = False

    hitung_2 = 1
    hitung = int(input("Bade nginput sabaraha kali Teh/Kang ? : "))
    while hitung > 0:
        print(f"Input Ke- {hitung_2}")

        nama = input("Masukkan Nama Mahasiswa/i : ")
        nis = input("Masukkan NIS : ")
        jurusan = input("Masukkan Kode Jurus[SI/SIA] : ")
        kelas = input("Masukkan Pilihan Kelas [Pagi/Malam] : ")

        if jurusan == "SI" or jurusan == "si":
            harga = 2400000
            nama_jurusan = "Sistem Informasi"

            if kelas == "MALAM" or kelas == "malam":
                harga += 500000
            elif kelas == "pagi" or kelas == "pagi":
                harga = 2400000
            else:
                bisa = True
                dataKosong = "Data yang diinputkan tidak ada"
        elif jurusan == "SIA" or jurusan == "sia":
            harga = 2000000
            nama_jurusan = "Sistem Informasi Akuntansi"

            if kelas == "MALAM" or kelas == "malam":
                harga += 500000
            elif kelas == "pagi" or kelas == "PAGI":
                harga = 2000000
            else:
                bisa = True
                dataKosong = "Data yang diinputkan tidak ada"
        else:
            bisa = True
            dataKosong = "Data yang dinputkan tidak ada"

        if bisa:
            print("\n")
            print(dataKosong)
        else:
            print("\n")
            print("==BUKTI PENDAFTARAN MAHASISWA BARU==")
            print(f"Input Ke- {hitung_2}")
            print(f"Nama Anda : {nama}")
            print(f"NIS Anda : {nis}")
            print(f"Kode Jurusan yang anda pilih : {jurusan}")
            print(f"Kelas yang anda pilih : {kelas}")
            print(f"Nama Prodi yang anda pilih : {nama_jurusan}")
            print(f"Biaya Yang Harus Anda Bayar : {harga}")
            print("\n")

        if hitung_2 == hitung:
            break

        hitung_2 += 1

proses()