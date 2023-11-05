import datetime
import pandas as pd


waktuSekarang = datetime.datetime.now()

daftar_harga = (
    "Rp.135.000", # Bandung
    "Rp.84.000",
    "Rp.63.000",
    "Rp.300.000", # Jakarta (Pasar Senen)
    "Rp.200.000",
    "Rp.100.000",
    "Rp.150.000", # Mojokerto
    "Rp.120.000",
    "Rp.75000",
    "Rp.275.000", # Jakarta (Jarinegara)
    "Rp.175.000",
    "Rp.135.000",
    "Rp.140.000", # Banyumas
    "Rp.100.000",
    "Rp.70.000",
    "Rp.275.000", # Kediri
    "Rp.185.000",
    "Rp.135.000",
    "Rp.220.000", # Yogya
    "Rp.150.000",
    "Rp.110.000"
)

kota = (
    "Stasiun Kiaracondong (KAC) Bandung", 
    "Stasiun Pasar senen (PSE) Jakarta",
    "Stasiun Mojokerto (MR) Mojokerto",
    "Stasiun Jatinegara Jakarta",
    "Stasiun Sumpiuh (SPH) Banyumas",
    "Stasiun Kediri (KD) Kediri",
    "Stasiun Yogyakarta"
)

kelas = (
    "Eksekutif",
    "Bisnis",
    "Ekonomi"
)

daftar_kelas = []
for x in range(0, len(kota)):
    for y in range(0, len(kelas)):
        daftar_kelas.append(kelas[y])


daftar_tujuan = []
for x in range(0, len(kota)):
    for y in range(0, len(kelas)):
        daftar_tujuan.append(kota[x])

jam = (
    "02:58 s/d 05:36",
    "20:46 s/d 03:55",
    "13:08 s/d 23:11",
    "20:46 s/d 03:55",
    "23:32 s/d 02:44",
    "01:02 s/d 11:01",
    "23:32 s/d 02:44",
)

daftar_jam = []
for x in range(0, len(kota)):
    for y in range(0, len(kelas)):
        daftar_jam.append(jam[x])

dari = []
nama = "Stasiun Tasikmalaya"
for x in range(0, len(daftar_tujuan)):
    dari.append(nama)


# Daftar Tiket Kereta
print("+", "-"*140, "+")
print("| {:^140} |".format("DAFTAR TIKET KERETA"))
print("+", "-"* 140, "+")
print("| {:^2} | {:^21} | {:^50} | {:^15} | {:^15} | {:^21} |".format("No", "Dari", "Kota Tujuan", "Harga", "Kelas", "Jam Keberangkatan/Tiba"))
print("+", "-"*140, "+")

for baris in range(0, len(daftar_tujuan)):
    print("| {:^2} | {:^21} | {:^50} | {:^15} | {:^15} | {:^22} |".format(baris + 1, dari[baris], daftar_tujuan[baris], daftar_harga[baris], daftar_kelas[baris], daftar_jam[baris]))
print("+", "-"* 140, "+")



# Proses
print()
diskon = 0
harga = 0
total = 0
uang = 0
hargaSebelumDiskon = 0
kembalian = 0
tiket = 0
kelas = ""
list_input_nama = []
list_input_noktp = []

jamSekarang = waktuSekarang.strftime(waktuSekarang.strftime("%H%M%S"))
jamSekarang_2 = waktuSekarang.strftime(waktuSekarang.strftime("%X"))
print(f"Sekarang pukul {jamSekarang_2}")

print()

if int(jamSekarang) in range(0000, 235900):    #  00:00 s/d 23:59
    if int(jamSekarang) in range(110300, 130700):   # 11:03 s/d 13:07
        print("Mohon maaf belum ada jadwal stasiun kereta saat ini")
    else:
        try:
            tiket = int(input("Masukkan jumlah tiket jika membeli lebih dari 3 mendapat potongan diskon 10%: "))
            if tiket > 3:  # Jika membeli lebih dari 3
                for x in range(1, tiket + 1):
                    print(f"Data Ke - {x}")
                    input_nama = input(f"Masukkan nama anda sebanyak {tiket} kali: ")
                    input_noktp = int(input("Masukkan No KTP anda:"))
                    list_input_nama.append(input_nama)
                    list_input_noktp.append(input_noktp)
            elif tiket <= 3 and tiket != 0:  # Jika membeli kurang dari sama dengan 3, dan jika tiket tidak samadengan 0s
                if tiket == 1:
                    input_nama = input("Masukkan nama Anda: ")
                    input_noktp = int(input("Masukkan No KTP anda:"))
                    list_input_nama.append(input_nama)
                    list_input_noktp.append(input_noktp)
                else:
                    for x in range(1, tiket + 1):
                        print(f"Data Ke - {x}")
                        input_nama = input(f"Masukkan nama anda sebanyak {tiket} kali: ")
                        input_noktp = int(input("Masukkan No KTP anda:"))
                        list_input_nama.append(input_nama)
                        list_input_noktp.append(input_noktp)
            else:
                print("Tidak boleh memasukkan angka nol!!!")
                exit()

            if int(jamSekarang) in range(25800, 53600) and int(jamSekarang) in range(10200, 110100): # 02:58 s/d 05:36 dan 01:02 s/d 11:01
                print("Jadwal stasiun kereta saat ini yang tersedia adalah\n[1] Stasiun Kiaracondong (KAC) Bandung\n" +
                "[2] Stasiun Kediri (KD) Kediri")
                print()

                input_tujuan = int(input("Masukkan kode kereta yang tersedia:\n[1] Stasiun Kiaracondong (KAC) Bandung\n[2] Stasiun Kediri (KD) Kediri: "))
                if input_tujuan == 1: # Stasiun KAC Bandung
                    kelas = int(input("Masukkan kode kelas\n[1] Eksekutif\n[2] Bisnis\n[3] Ekonomi: "))
                    if kelas == 1:
                        uang = int(input("Masukkan jumlah uang anda: "))
                        kelas = "Eksekutif"
                        harga = 135000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            kembalian = uang - total
                        else:
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon
                            kembalian = uang - total
                
                    elif kelas == 2:
                        uang = int(input("Masukkan jumlah uang anda: "))
                        kelas = "Bisnis"
                        harga = 84000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            kembalian = uang - total
                        else:
                            total = harga * tiket
                            kembalian = uang - total

                    elif kelas == 3:
                        uang = int(input("Masukkan jumlah uang anda: "))
                        kelas = "Ekonomi"
                        harga = 63000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            kembalian = uang - total
                        else:
                            total = harga * tiket
                            kembalian = uang - total
                    else:
                        print("Pilihan tidak ada dalam daftar kode")
                        exit()


                elif input_tujuan == 2: # Stasiun Kediri
                    kelas = int(input("Masukkan kode kelas\n[1] Eksekutif\n[2] Bisnis\n[3] Ekonomi: "))
                    if kelas == 1:
                        uang = int(input("Masukkan jumlah uang anda: "))
                        kelas = "Eksekutif"
                        harga = 275000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            kembalian = uang - total
                        else:
                            total = harga * tiket
                            kembalian = uang - total

                    elif kelas == 2:
                        uang = int(input("Masukkan jumlah uang anda: "))
                        kelas = "Bisnis"
                        harga = 185000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            kembalian = uang - total
                        else:
                            total = harga * tiket
                            kembalian = uang - total

                    elif kelas == 3:
                        uang = int(input("Masukkan jumlah uang anda: "))
                        kelas = "Ekonomi"
                        harga = 135000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            kembalian = uang - total
                        else:
                            total = harga * tiket
                            kembalian = uang - total
                    else:
                        print("Pilihan tidak ada dalam daftar kode")
                        exit()


            elif int(jamSekarang) in range(10200, 110100):  # 01:02 s/d 11:01
                print("Jadwal stasiun kereta saat ini yang tersedia adalah hanya Stasiun Kediri (KD) Kediri")
                print()

                input_tujuan = int(input("Masukkan kode kereta yang tersedia:\n[1] Stasiun Kediri (KD) Kediri: "))
                if input_tujuan == 1: # Stasiun Kediri
                    kelas = int(input("Masukkan kode kelas\n[1] Eksekutif\n[2] Bisnis\n[3] Ekonomi: "))
                    if kelas == 1:
                        uang = int(input("Masukkan jumlah uang anda: "))
                        kelas = "Eksekutif"
                        harga = 275000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            kembalian = uang - total
                        else:
                            total = harga * tiket
                            kembalian = uang - total

                    elif kelas == 2:
                        uang = int(input("Masukkan jumlah uang anda: "))
                        kelas = "Bisnis"
                        harga = 185000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            kembalian = uang - total
                        else:
                            total = harga * tiket
                            kembalian = uang - total

                    elif kelas == 3:
                        uang = int(input("Masukkan jumlah uang anda: "))
                        kelas = "Ekonomi"
                        harga = 135000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            kembalian = uang - total
                        else:
                            total = harga * tiket
                            kembalian = uang - total
                else:
                    print("Pilihan tidak ada dalam daftar kode")
                    exit()

            elif int(jamSekarang) in range(130800, 231100) and int(jamSekarang) in range(204600, 355000): # 13:08 s/d 23:11 dan 20:46 s/d 03:55
                print("Jadwal stasiun kereta saat ini yang tersedia adalah\n[1] Stasiun Pasar senen (PSE) Jakarta\n" +
                "[2] Stasiun Mojokerto (MR) Mojokerto\n[3] Stasiun Jatinegara Jakarta")
                print()

                input_tujuan = int(input("Masukkan kode kereta yang tersedia:\n[1] Stasiun Pasar senen (PSE) Jakarta\n[2] Stasiun Mojokerto (MR) Mojokerto\n" + 
                "[3] Stasiun Jatinegara Jakarta: "))
                if input_tujuan == 1: # Stasiun PSE Jakarta
                    kelas = int(input("Masukkan kode kelas\n[1] Eksekutif\n[2] Bisnis\n[3] Ekonomi: "))
                    if kelas == 1:
                        uang = int(input("Masukkan jumlah uang anda: "))
                        kelas = "Eksekutif"
                        harga = 135000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            kembalian = uang - total
                        else:
                            total = harga * tiket
                            kembalian = uang - total

                    elif kelas == 2:
                        uang = int(input("Masukkan jumlah uang anda: "))
                        kelas = "Bisnis"
                        harga = 84000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            kembalian = uang - total
                        else:
                            total = harga * tiket
                            kembalian = uang - total

                    elif kelas == 3:
                        uang = int(input("Masukkan jumlah uang anda: "))
                        kelas = "Ekonomi"
                        harga = 63000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            kembalian = uang - total
                        else:
                            total = harga * tiket
                            kembalian = uang - total
                    else:
                        print("Pilihan tidak ada dalam daftar kode")
                        exit()


                elif input_tujuan == 2: # Stasiun Mojokerto
                    if kelas == 1:
                        uang = int(input("Masukkan jumlah uang anda: "))
                        kelas = "Eksekutif"
                        harga = 150000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            kembalian = uang - total
                        else:
                            total = harga * tiket
                            kembalian = uang - total

                    elif kelas == 2:
                        uang = int(input("Masukkan jumlah uang anda: "))
                        kelas = "Bisnis"
                        harga = 120000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            kembalian = uang - total
                        else:
                            total = harga * tiket
                            kembalian = uang - total

                    elif kelas == 3:
                        uang = int(input("Masukkan jumlah uang anda: "))
                        kelas = "Ekonomi"
                        harga = 75000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            kembalian = uang - total
                        else:
                            total = harga * tiket
                            kembalian = uang - total
                    else:
                        print("Pilihan tidak ada dalam daftar kode")
                        exit()
                

                elif input_tujuan == 3: # Stasiun Jatinegara Jakarta
                    if kelas == 1:
                        uang = int(input("Masukkan jumlah uang anda: "))
                        kelas = "Eksekutif"
                        harga = 275000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            kembalian = uang - total
                        else:
                            total = harga * tiket
                            kembalian = uang - total

                    elif kelas == 2:
                        uang = int(input("Masukkan jumlah uang anda: "))
                        kelas = "Bisnis"
                        harga = 185000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            kembalian = uang - total
                        else:
                            total = harga * tiket
                            kembalian = uang - total

                    elif kelas == 3:
                        uang = int(input("Masukkan jumlah uang anda: "))
                        kelas = "Ekonomi"
                        harga = 135000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            kembalian = uang - total
                        else:
                            total = harga * tiket
                            kembalian = uang - total
                    else:
                        print("Pilihan tidak ada dalam daftar kode")
                        exit()
                else:
                    print("Pilihan tidak ada dalam daftar kode")
                    exit()
                
                    
            elif int(jamSekarang) in range(24400, 233200): # 02:44 s/d 23:32
                if int(jamSekarang) in range(110100, 130800):   # 11:03 s/d 13:07
                    print("Mohon maaf belum ada jadwal stasiun kereta saat ini")
                else:
                    print("Jadwal stasiun kereta saat ini yang tersedia adalah\n[1] Stasiun Sumpiuh (SPH) Banyumas\n" +
                    "[2] Stasiun Kediri (KD) Kediri\n[3] Stasiun Yogyakarta")
                    print()

                    input_tujuan = int(input("Masukkan kode kereta yang tersedia:\n[1] Stasiun Sumpiuh (SPH) Banyumas\n[2] Stasiun Kediri (KD) Kediri\n" + 
                    "[3] Stasiun Yogyakarta: "))
                    if input_tujuan == 1: # Stasiun Sumpiuh (SPH) Banyumas
                        kelas = int(input("Masukkan kode kelas\n[1] Eksekutif\n[2] Bisnis\n[3] Ekonomi: "))
                        if kelas == 1:
                            uang = int(input("Masukkan jumlah uang anda: "))
                            kelas = "Eksekutif"
                            harga = 140000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                                kembalian = uang - total
                            else:
                                total = harga * tiket
                                kembalian = uang - total

                        elif kelas == 2:
                            uang = int(input("Masukkan jumlah uang anda: "))
                            kelas = "Bisnis"
                            harga = 100000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                                kembalian = uang - total
                            else:
                                total = harga * tiket
                                kembalian = uang - total

                        elif kelas == 3:
                            uang = int(input("Masukkan jumlah uang anda: "))
                            kelas = "Ekonomi"
                            harga = 70000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                                kembalian = uang - total
                            else:
                                total = harga * tiket
                                kembalian = uang - total
                        else:
                            print("Pilihan tidak ada dalam daftar kode")
                            exit()


                    elif input_tujuan == 2: # Stasiun Kediri (KD) Kediri
                        if kelas == 1:
                            uang = int(input("Masukkan jumlah uang anda: "))
                            kelas = "Eksekutif"
                            harga = 275000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                                kembalian = uang - total
                            else:
                                total = harga * tiket
                                kembalian = uang - total

                        elif kelas == 2:
                            uang = int(input("Masukkan jumlah uang anda: "))
                            kelas = "Bisnis"
                            harga = 185000
                            if tiket > 3:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                                kembalian = uang - total
                            else:
                                total = harga * tiket
                                kembalian = uang - total

                        elif kelas == 3:
                            uang = int(input("Masukkan jumlah uang anda: "))
                            kelas = "Ekonomi"
                            harga = 135000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                                kembalian = uang - total
                            else:
                                total = harga * tiket
                                kembalian = uang - total
                        else:
                            print("Pilihan tidak ada dalam daftar kode")
                            exit()
                            

                    elif input_tujuan == 3: # Stasiun Yogyakarta
                        if kelas == 1:
                            uang = int(input("Masukkan jumlah uang anda: "))
                            kelas = "Eksekutif"
                            harga = 222000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                                kembalian = uang - total
                            else:
                                total = harga * tiket
                                kembalian = uang - total

                        elif kelas == 2:
                            uang = int(input("Masukkan jumlah uang anda: "))
                            kelas = "Bisnis"
                            harga = 150000
                            if tiket > 3:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                                kembalian = uang - total
                            else:
                                total = harga * tiket
                                kembalian = uang - total

                        elif kelas == 3:
                            uang = int(input("Masukkan jumlah uang anda: "))
                            kelas = "Ekonomi"
                            harga = 111000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                                kembalian = uang - total
                            else:
                                total = harga * tiket
                                kembalian = uang - total
                        else:
                            print("Pilihan tidak ada dalam daftar kode")
                            exit()
                    else:
                        print("Kode yang anda masukkan tidak ada")
                        exit()

        except ValueError:
            print("Input yang dimasukkan harus bentuk Angka bukan Huruf!!!")
            exit()
else:
    print("Mohon maaf belum ada jadwal stasiun kereta saat ini")


# Keluaran (Output)
print()
print("-" * 139)
print("| {:^135} |".format("STRUK PEMBAYARAN TIKET"))
print("+", "-" * 135, "+")
print("| {:^2} | {:^20} | {:^15} | {:^15} | {:^15} | {:^25} | {:^25} |".format("NO","NAMA", "NIK", "KELAS", "JUMLAH TIKET", "HARGA SATUAN TIKET", "HARGA TOTAL"))
print("+", "-" * 135, "+")

print("| {:^2} | {:^20} | {:^15} | {:^15} | {:^15} |  {:^24} | {:^25} |".format(1, list_input_nama[0], list_input_noktp[0], kelas, tiket, f"Rp.{harga}", f"Rp.{hargaSebelumDiskon}"))
for x in range(1, len(list_input_nama) + 1):
    print("| {:^2} | {:^20} | {:^15} | {:^15} | {:^15} | {:^25} | {:^25} |".format(x+1, list_input_nama[x-1], list_input_noktp[x-1], "-", "-", "-", "-", "-"))
print("-" * 139)
print("{:>120} = {}".format("Harga total yang harus dibayar", hargaSebelumDiskon))
print("{:>120} = {} %".format("Diskon", int(diskon * 100))) # Kali dalam bentuk persen
print("{:>120} = {}".format("Harga total yang harus dibayar setelah diskon", total))
print("{:>120} = Rp.{} ".format("Uang yang dibayarkan", uang))
print("{:>120} = Rp.{}".format("Kembalian", kembalian))