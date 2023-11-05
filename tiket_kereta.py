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
DISKON = 10/100
list_input_nama = []
list_input_noktp = []
list_input_kelas = []
list_input_tiket = []
list_harga = []
list_total = []
list_uang = []

jamSekarang = waktuSekarang.strftime(waktuSekarang.strftime("%H%M%S"))
jamSekarang_2 = waktuSekarang.strftime(waktuSekarang.strftime("%X"))
print(f"Sekarang pukul {jamSekarang_2}")

print()

if int(jamSekarang) in range(0000, 235900):    #  00:00 s/d 23:59
    if int(jamSekarang) in range(110300, 130700):   # 11:03 s/d 13:07
        print("Mohon maaf belum ada jadwal stasiun kereta saat ini")
    else:
        input_tiket = int(input("Masukkan jumlah tiket jika membeli lebih dari 3 mendapat potongan diskon 10%: "))
        if input_tiket > 3:  # Jika membeli lebih dari 3
            for x in range(1, input_tiket + 1):
                print(f"Data Ke - {x}")
                input_nama = input(f"Masukkan nama anda sebanyak {input_tiket} kali: ")
                input_noktp = int(input("Masukkan No KTP anda:"))
                input_kelas = int(input("Masukkan kode kelas\n[1] Eksekutif\n[2] Bisnis\n[3] Ekonomi: "))
                list_input_nama.append(input_nama)
                list_input_noktp.append(input_noktp)
        else:
            input_nama = input("Masukkan nama Anda: ")
            input_noktp = int(input("Masukkan No KTP anda:"))
            input_kelas = int(input("Masukkan kode kelas\n[1] Eksekutif\n[2] Bisnis\n[3] Ekonomi: "))
            list_input_nama.append(input_nama)
            list_input_noktp.append(input_noktp)

        if int(jamSekarang) in range(25800, 53600) and int(jamSekarang) in range(10200, 110100): # 02:58 s/d 05:36 dan 01:02 s/d 11:01
            print("Jadwal stasiun kereta saat ini yang tersedia adalah\n[1] Stasiun Kiaracondong (KAC) Bandung\n" +
            "[2] Stasiun Kediri (KD) Kediri")
            print()

            input_tujuan = int(input("Masukkan kode kereta yang tersedia:\n[1] Stasiun Kiaracondong (KAC) Bandung\n[2] Stasiun Kediri (KD) Kediri: "))
            if input_tujuan == 1: # Stasiun KAC Bandung
                if input_kelas == 1:
                    input_uang = int(input("Masukkan jumlah uang anda: "))
                    input_kelas = "Eksekutif"
                    HARGA = 135000
                    if input_tiket > 3:
                        total = HARGA - (HARGA * DISKON)
                        totalBayar = input_uang - total
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                    else:
                        total = HARGA
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
            
                elif input_kelas == 2:
                    input_uang = int(input("Masukkan jumlah uang anda: "))
                    input_kelas = "Bisnis"
                    HARGA = 84000
                    if input_tiket > 3:
                        total = HARGA - (HARGA * DISKON)
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                    else:
                        total = HARGA
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)

                elif input_kelas == 3:
                    input_uang = int(input("Masukkan jumlah uang anda: "))
                    input_kelas = "Ekonomi"
                    HARGA = 63000
                    if input_tiket > 3:
                        total = HARGA - (HARGA * DISKON)
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                    else:
                        total = HARGA
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)

            elif input_tujuan == 2: # Stasiun Kediri
                if input_kelas == 1:
                    input_uang = int(input("Masukkan jumlah uang anda: "))
                    input_kelas = "Eksekutif"
                    HARGA = 275000
                    if input_tiket > 3:
                        total = HARGA - (HARGA * DISKON)
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                    else:
                        total = HARGA
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)

                elif input_kelas == 2:
                    input_uang = int(input("Masukkan jumlah uang anda: "))
                    input_kelas = "Bisnis"
                    HARGA = 185000
                    if input_tiket > 3:
                        total = HARGA - (HARGA * DISKON)
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                    else:
                        total = HARGA
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)

                elif input_kelas == 3:
                    input_uang = int(input("Masukkan jumlah uang anda: "))
                    input_kelas = "Ekonomi"
                    HARGA = 135000
                    if input_tiket > 3:
                        total = HARGA - (HARGA * DISKON)
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                    else:
                        total = HARGA
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                else:
                    print("Kode yang anda masukkan tidak ada")

        elif int(jamSekarang) in range(10200, 110100):  # 01:02 s/d 11:01
            print("Jadwal stasiun kereta saat ini yang tersedia adalah hanya Stasiun Kediri (KD) Kediri")
            print()

            input_tujuan = int(input("Masukkan kode kereta yang tersedia:\n[1] Stasiun Kediri (KD) Kediri: "))
            if input_tujuan == 1: # Stasiun Kediri
                if input_kelas == 1:
                    input_uang = int(input("Masukkan jumlah uang anda: "))
                    input_kelas = "Eksekutif"
                    HARGA = 275000
                    if input_tiket > 3:
                        total = HARGA - (HARGA * DISKON)
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                    else:
                        total = HARGA
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)

                elif input_kelas == 2:
                    input_uang = int(input("Masukkan jumlah uang anda: "))
                    input_kelas = "Bisnis"
                    HARGA = 185000
                    if input_tiket > 3:
                        total = HARGA - (HARGA * DISKON)
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                    else:
                        total = HARGA
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)

                elif input_kelas == 3:
                    input_uang = int(input("Masukkan jumlah uang anda: "))
                    input_kelas = "Ekonomi"
                    HARGA = 135000
                    if input_tiket > 3:
                        total = HARGA - (HARGA * DISKON)
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                    else:
                        total = HARGA
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                else:
                    print("Kode yang anda masukkan tidak ada")

        elif int(jamSekarang) in range(130800, 231100) and int(jamSekarang) in range(204600, 355000): # 13:08 s/d 23:11 dan 20:46 s/d 03:55
            print("Jadwal stasiun kereta saat ini yang tersedia adalah\n[1] Stasiun Pasar senen (PSE) Jakarta\n" +
            "[2] Stasiun Mojokerto (MR) Mojokerto\n[3] Stasiun Jatinegara Jakarta")
            print()

            input_tujuan = int(input("Masukkan kode kereta yang tersedia:\n[1] Stasiun Pasar senen (PSE) Jakarta\n[2] Stasiun Mojokerto (MR) Mojokerto\n" + 
            "[3] Stasiun Jatinegara Jakarta: "))
            if input_tujuan == 1: # Stasiun PSE Jakarta
                if input_kelas == 1:
                    input_uang = int(input("Masukkan jumlah uang anda: "))
                    input_kelas = "Eksekutif"
                    HARGA = 135000
                    if input_tiket > 3:
                        total = HARGA - (HARGA * DISKON)
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                    else:
                        total = HARGA
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)

                elif input_kelas == 2:
                    input_uang = int(input("Masukkan jumlah uang anda: "))
                    input_kelas = "Bisnis"
                    HARGA = 84000
                    if input_tiket > 3:
                        total = HARGA - (HARGA * DISKON)
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                    else:
                        total = HARGA
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)

                elif input_kelas == 3:
                    input_uang = int(input("Masukkan jumlah uang anda: "))
                    input_kelas = "Ekonomi"
                    HARGA = 63000
                    if input_tiket > 3:
                        total = HARGA - (HARGA * DISKON)
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                    else:
                        total = HARGA
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)

            elif input_tujuan == 2: # Stasiun Mojokerto
                if input_kelas == 1:
                    input_uang = int(input("Masukkan jumlah uang anda: "))
                    input_kelas = "Eksekutif"
                    HARGA = 150000
                    if input_tiket > 3:
                        total = HARGA - (HARGA * DISKON)
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                    else:
                        total = HARGA
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)

                elif input_kelas == 2:
                    input_uang = int(input("Masukkan jumlah uang anda: "))
                    input_kelas = "Bisnis"
                    HARGA = 120000
                    if input_tiket > 3:
                        total = HARGA - (HARGA * DISKON)
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                    else:
                        total = HARGA
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)

                elif input_kelas == 3:
                    input_uang = int(input("Masukkan jumlah uang anda: "))
                    input_kelas = "Ekonomi"
                    HARGA = 75000
                    if input_tiket > 3:
                        total = HARGA - (HARGA * DISKON)
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                    else:
                        total = HARGA
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)

            elif input_tujuan == 3: # Stasiun Jatinegara Jakarta
                if input_kelas == 1:
                    input_uang = int(input("Masukkan jumlah uang anda: "))
                    input_kelas = "Eksekutif"
                    HARGA = 275000
                    if input_tiket > 3:
                        total = HARGA - (HARGA * DISKON)
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                    else:
                        total = HARGA
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)

                elif input_kelas == 2:
                    input_uang = int(input("Masukkan jumlah uang anda: "))
                    input_kelas = "Bisnis"
                    HARGA = 185000
                    if input_tiket > 3:
                        total = HARGA - (HARGA * DISKON)
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                    else:
                        total = HARGA
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)

                elif input_kelas == 3:
                    input_uang = int(input("Masukkan jumlah uang anda: "))
                    input_kelas = "Ekonomi"
                    HARGA = 135000
                    if input_tiket > 3:
                        total = HARGA - (HARGA * DISKON)
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
                    else:
                        total = HARGA
                        list_input_kelas.append(input_kelas)
                        list_input_tiket.append(input_tiket)
                        list_harga.append(HARGA)
                        list_total.append(total)
                        list_uang.append(input_uang)
            else:
                print("Kode yang anda masukkan tidak ada")
                
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
                    if input_kelas == 1:
                        input_uang = int(input("Masukkan jumlah uang anda: "))
                        input_kelas = "Eksekutif"
                        HARGA = 140000
                        if input_tiket > 3:
                            total = HARGA - (HARGA * DISKON)
                            list_input_kelas.append(input_kelas)
                            list_input_tiket.append(input_tiket)
                            list_harga.append(HARGA)
                            list_total.append(total)
                            list_uang.append(input_uang)
                        else:
                            total = HARGA
                            list_input_kelas.append(input_kelas)
                            list_input_tiket.append(input_tiket)
                            list_harga.append(HARGA)
                            list_total.append(total)
                            list_uang.append(input_uang)

                    elif input_kelas == 2:
                        input_uang = int(input("Masukkan jumlah uang anda: "))
                        input_kelas = "Bisnis"
                        HARGA = 100000
                        if input_tiket > 3:
                            total = HARGA - (HARGA * DISKON)
                            list_input_kelas.append(input_kelas)
                            list_input_tiket.append(input_tiket)
                            list_harga.append(HARGA)
                            list_total.append(total)
                            list_uang.append(input_uang)
                        else:
                            total = HARGA
                            list_input_kelas.append(input_kelas)
                            list_input_tiket.append(input_tiket)
                            list_harga.append(HARGA)
                            list_total.append(total)
                            list_uang.append(input_uang)

                    elif input_kelas == 3:
                        input_uang = int(input("Masukkan jumlah uang anda: "))
                        input_kelas = "Ekonomi"
                        HARGA = 70000
                        if input_tiket > 3:
                            total = HARGA - (HARGA * DISKON)
                            list_input_kelas.append(input_kelas)
                            list_input_tiket.append(input_tiket)
                            list_harga.append(HARGA)
                            list_total.append(total)
                            list_uang.append(input_uang)
                        else:
                            total = HARGA
                            list_input_kelas.append(input_kelas)
                            list_input_tiket.append(input_tiket)
                            list_harga.append(HARGA)
                            list_total.append(total)
                            list_uang.append(input_uang)

                elif input_tujuan == 2: # Stasiun Kediri (KD) Kediri
                    if input_kelas == 1:
                        input_uang = int(input("Masukkan jumlah uang anda: "))
                        input_kelas = "Eksekutif"
                        HARGA = 275000
                        if input_tiket > 3:
                            total = HARGA - (HARGA * DISKON)
                            list_input_kelas.append(input_kelas)
                            list_input_tiket.append(input_tiket)
                            list_harga.append(HARGA)
                            list_total.append(total)
                            list_uang.append(input_uang)
                        else:
                            total = HARGA
                            list_input_kelas.append(input_kelas)
                            list_input_tiket.append(input_tiket)
                            list_harga.append(HARGA)
                            list_total.append(total)
                            list_uang.append(input_uang)

                    elif input_kelas == 2:
                        input_uang = int(input("Masukkan jumlah uang anda: "))
                        input_kelas = "Bisnis"
                        HARGA = 185000
                        if input_tiket > 3:
                            total = HARGA - (HARGA * DISKON)
                            list_input_kelas.append(input_kelas)
                            list_input_tiket.append(input_tiket)
                            list_harga.append(HARGA)
                            list_total.append(total)
                            list_uang.append(input_uang)
                        else:
                            total = HARGA
                            list_input_kelas.append(input_kelas)
                            list_input_tiket.append(input_tiket)
                            list_harga.append(HARGA)
                            list_total.append(total)
                            list_uang.append(input_uang)

                    elif input_kelas == 3:
                        input_uang = int(input("Masukkan jumlah uang anda: "))
                        input_kelas = "Ekonomi"
                        HARGA = 135000
                        if input_tiket > 3:
                            total = HARGA - (HARGA * DISKON)
                            list_input_kelas.append(input_kelas)
                            list_input_tiket.append(input_tiket)
                            list_harga.append(HARGA)
                            list_total.append(total)
                            list_uang.append(input_uang)
                        else:
                            total = HARGA
                            list_input_kelas.append(input_kelas)
                            list_input_tiket.append(input_tiket)
                            list_harga.append(HARGA)
                            list_total.append(total)
                            list_uang.append(input_uang)

                elif input_tujuan == 3: # Stasiun Yogyakarta
                    if input_kelas == 1:
                        input_uang = int(input("Masukkan jumlah uang anda: "))
                        input_kelas = "Eksekutif"
                        HARGA = 222000
                        if input_tiket > 3:
                            total = HARGA - (HARGA * DISKON)
                            list_input_kelas.append(input_kelas)
                            list_input_tiket.append(input_tiket)
                            list_harga.append(HARGA)
                            list_total.append(total)
                            list_uang.append(input_uang)
                        else:
                            total = HARGA
                            list_input_kelas.append(input_kelas)
                            list_input_tiket.append(input_tiket)
                            list_harga.append(HARGA)
                            list_total.append(total)
                            list_uang.append(input_uang)

                    elif input_kelas == 2:
                        input_uang = int(input("Masukkan jumlah uang anda: "))
                        input_kelas = "Bisnis"
                        HARGA = 150000
                        if input_tiket > 3:
                            total = HARGA - (HARGA * DISKON)
                            list_input_kelas.append(input_kelas)
                            list_input_tiket.append(input_tiket)
                            list_harga.append(HARGA)
                            list_total.append(total)
                            list_uang.append(input_uang)
                        else:
                            total = HARGA
                            list_input_kelas.append(input_kelas)
                            list_input_tiket.append(input_tiket)
                            list_harga.append(HARGA)
                            list_total.append(total)
                            list_uang.append(input_uang)

                    elif input_kelas == 3:
                        input_uang = int(input("Masukkan jumlah uang anda: "))
                        input_kelas = "Ekonomi"
                        HARGA = 111000
                        if input_tiket > 3:
                            total = HARGA - (HARGA * DISKON)
                            list_input_kelas.append(input_kelas)
                            list_input_tiket.append(input_tiket)
                            list_harga.append(HARGA)
                            list_total.append(total)
                            list_uang.append(input_uang)
                        else:
                            total = HARGA
                            list_input_kelas.append(input_kelas)
                            list_input_tiket.append(input_tiket)
                            list_harga.append(HARGA)
                            list_total.append(total)
                            list_uang.append(input_uang)
else:
    print("Mohon maaf belum ada jadwal stasiun kereta saat ini")


print(list_input_nama)
a
dsaas