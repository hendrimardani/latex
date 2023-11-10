import datetime
import random
import sys
import time

# Warna dalam kode Style Karakter
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Fungsi mencetak dengan delay yang ditentukan
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)


waktuSekarang = datetime.datetime.now()

daftar_harga = (
    "Rp.135.000", # Bandung
    "Rp.84.000",
    "Rp.63.000",
    "Rp.300.000", # Jakarta (Pasar Senen)
    "Rp.200.000",
    "Rp.100.000",
    "Rp.220.000", # Yogya
    "Rp.150.000",
    "Rp.110.000"
)

kota = (
    "Stasiun Kiaracondong (KAC) Bandung", 
    "Stasiun Pasar senen (PSE) Jakarta",
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

print(f"+ {'-'*140} +")
print("| {}{:^140}{} |".format(Color.PURPLE, "DAFTAR TIKET KERETA", Color.END))
print(f"+ {'-'*140} +")
print("| {:^2} | {:^21} | {:^50} | {:^15} | {:^15} | {:^21} |"
    .format("No", "Dari", "Kota Tujuan", "Harga", "Kelas", "Jam Keberangkatan/Tiba"))
print(f"+ {'-'*140} +")


for baris in range(0, len(daftar_tujuan)):
    print("| {:^2} | {:^21} | {:^50} | {:^15} | {:^15} | {:^22} |"
    .format(baris + 1, dari[baris], daftar_tujuan[baris], daftar_harga[baris], daftar_kelas[baris], daftar_jam[baris]))
print(f"+ {'-'*140} +")



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
belumAdaJadwal = False

jamSekarang = waktuSekarang.strftime(waktuSekarang.strftime("%H%M%S")) # 052655
jamSekarang_2 = waktuSekarang.strftime(waktuSekarang.strftime("%X")) # 05:26:55
tglSekarang = waktuSekarang.strftime(waktuSekarang.strftime("%d")) # 08
tglSekarang_2 = waktuSekarang.strftime(waktuSekarang.strftime("%d %B %Y")) # 08 November 2023

print(f"Sekarang tanggal {Color.RED}{tglSekarang_2}{Color.END}")
print(f"Sekarang pukul {Color.RED}{jamSekarang_2}{Color.END}")

if int(jamSekarang) in range(0000, 235900):    #  00:00 s/d 23:59
    inpTgl = int(input("Masukkan Tanggal: "))
    if inpTgl == int(tglSekarang):   # Jika tanggal sekarang
        belumAdaJadwal = True
        print(f"{Color.RED}Mohon maaf belum ada jadwal stasiun kereta saat ini, silahkan ganti tanggal!!!{Color.END}")
        exit()
    elif inpTgl < int(tglSekarang):   # Jika kurang dari tanggal sekarang
        belumAdaJadwal = True
        print(f"Memasukkan tanggal tidak boleh kurang dari tanggal saat ini!, sekarang tanggal {Color.RED}{tglSekarang}{Color.END}")
        exit()
    else:
        try:
            tiket = int(input(f"Masukkan jumlah tiket jika membeli lebih dari 3 mendapat potongan " +
                              f"diskon {Color.RED}10%{Color.END}: "))
            if tiket > 3:  # Jika membeli lebih dari 3
                for x in range(1, tiket + 1):
                    print(f"Data Ke - {Color.RED}{x}{Color.END}")
                    input_nama = input(f"Masukkan nama anda sebanyak {Color.RED}{tiket}{Color.END} kali: ")
                    input_noktp = int(input("Masukkan No KTP anda:"))
                    list_input_nama.append(input_nama)
                    list_input_noktp.append(input_noktp)
            elif tiket <= 3 and tiket != 0:  # Jika membeli kurang dari sama dengan 3, dan jika tiket tidak samadengan 0s
                if tiket == 1:
                    input_nama = input("Masukkan nama Anda: ")
                    input_noktp = int(input("Masukkan No KTP anda:"))
                    list_input_nama.append(input_nama)
                    list_input_noktp.append(input_noktp)
                else: # Jika tiket adalah 2 atau 3
                    for x in range(1, tiket + 1): 
                        print(f"Data Ke - {Color.RED}{x}{Color.END}")
                        input_nama = input(f"Masukkan nama anda sebanyak {Color.RED}{tiket}{Color.END} kali: ")
                        input_noktp = int(input("Masukkan No KTP anda:"))
                        list_input_nama.append(input_nama)
                        list_input_noktp.append(input_noktp)
            else:
                print("Tidak boleh memasukkan angka nol!!!")
                exit()


            if int(jamSekarang.removeprefix("0")) in range(25800, 53600): # 02:58 s/d 05:36
                if int(jamSekarang.removeprefix("0")) in range(25800, 35500): # 02:58 s/d 03:55
                    # Selain stasiun kac bandung, pse jakarta, jatinegara jakarta, dan kediri
                    print("Jadwal stasiun kereta saat ini yang tersedia adalah\n" +
                    "[1] Stasiun Yogyakarta")

                    input_tujuan = int(input(f"Masukkan kode kereta yang tersedia:\n" +
                    f"{Color.RED}[1] Stasiun Yogyakarta{Color.END}: "))
                    if input_tujuan == 1:
                        kelas = int(input(f"Masukkan kode kelas\n{Color.RED}[1] Eksekutif{Color.END}\n{Color.YELLOW}" +
                                        f"[2] Bisnis{Color.END}\n{Color.GREEN}[3] Ekonomi{Color.END}: "))
                        if kelas == 1:
                            kelas = "Eksekutif"
                            harga = 275000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 2:
                            kelas = "Bisnis"
                            harga = 185000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 3:
                            kelas = "Ekonomi"
                            harga = 135000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon
                        else:
                            print("Pilihan tidak ada dalam daftar kode")
                            exit()
                    else:
                        print("Pilihan tidak ada dalam daftar kode")
                        exit()                    
                else:
                    # Selain stasiun kac bandung
                    print("Jadwal stasiun kereta saat ini yang tersedia adalah\n" +
                    "[1] Stasiun Pasar Senen (PSE) Jakarta\n" +
                    "[2] Stasiun Yogyakarta")

                    input_tujuan = int(input(f"Masukkan kode kereta yang tersedia:\n" +
                    f"{Color.RED}[1] Stasiun Pasar Senen (PSE) Jakarta{Color.END}\n" +
                    f"{Color.GREEN}[2] Stasiun Yogyakarta{Color.END}: "))
                    if input_tujuan == 1:
                        kelas = int(input(f"Masukkan kode kelas\n{Color.RED}[1] Eksekutif{Color.END}\n{Color.YELLOW}" +
                                        f"[2] Bisnis{Color.END}\n{Color.GREEN}[3] Ekonomi{Color.END}: "))
                        if kelas == 1:
                            kelas = "Eksekutif"
                            harga = 275000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 2:
                            kelas = "Bisnis"
                            harga = 185000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 3:
                            kelas = "Ekonomi"
                            harga = 135000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon
                        else:
                            print("Pilihan tidak ada dalam daftar kode")
                            exit()

                    elif input_tujuan == 2:
                        kelas = int(input(f"Masukkan kode kelas\n{Color.RED}[1] Eksekutif{Color.END}\n{Color.YELLOW}" +
                                        f"[2] Bisnis{Color.END}\n{Color.GREEN}[3] Ekonomi{Color.END}: "))
                        if kelas == 1:
                            kelas = "Eksekutif"
                            harga = 275000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 2:
                            kelas = "Bisnis"
                            harga = 185000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 3:
                            kelas = "Ekonomi"
                            harga = 135000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon
                        else:
                            print("Pilihan tidak ada dalam daftar kode")
                            exit()
                    else:
                        print("Pilihan tidak ada dalam daftar kode")
                        exit()


            elif int(jamSekarang.removeprefix("0")) in range(0, 35500): # 20:46 s/d 03:55
                if int(jamSekarang.removeprefix("0")) in range(0, 24400): # 23:32 s/d 02:44
                    # Selain stasiun yogyakarta
                    print("Jadwal stasiun kereta saat ini yang tersedia adalah\n" +
                    "[1] Stasiun Kiaracondong (KAC) Bandung\n" +
                    "[2] Stasiun Pasar Senen (PSE) Jakarta")

                    input_tujuan = int(input(f"Masukkan kode kereta yang tersedia:\n" +
                    f"{Color.RED}[1] Stasiun Kiaracondong (KAC) Bandung{Color.END}\n" +
                    f"{Color.YELLOW}[2] Stasiun Pasar Senen (PSE) Jakarta{Color.END}: "))                
                    if input_tujuan == 1:
                        kelas = int(input(f"Masukkan kode kelas\n{Color.RED}[1] Eksekutif{Color.END}\n{Color.YELLOW}" +
                                        f"[2] Bisnis{Color.END}\n{Color.GREEN}[3] Ekonomi{Color.END}: "))
                        if kelas == 1:
                            kelas = "Eksekutif"
                            harga = 275000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 2:
                            kelas = "Bisnis"
                            harga = 185000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 3:
                            kelas = "Ekonomi"
                            harga = 135000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon
                        else:
                            print("Pilihan tidak ada dalam daftar kode")
                            exit()

                    elif input_tujuan == 2:
                        kelas = int(input(f"Masukkan kode kelas\n{Color.RED}[1] Eksekutif{Color.END}\n{Color.YELLOW}" +
                                        f"[2] Bisnis{Color.END}\n{Color.GREEN}[3] Ekonomi{Color.END}: "))
                        if kelas == 1:
                            kelas = "Eksekutif"
                            harga = 275000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 2:
                            kelas = "Bisnis"
                            harga = 185000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 3:
                            kelas = "Ekonomi"
                            harga = 135000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon
                        else:
                            print("Pilihan tidak ada dalam daftar kode")
                            exit()
                    else:
                        print("Pilihan tidak ada dalam daftar kode")
                        exit()
                else:
                    # Selain stasiun pse jakarta
                    print("Jadwal stasiun kereta saat ini yang tersedia adalah\n" +
                    "[1] Stasiun Kiaracondong (KAC) Bandung\n" +
                    "[2] Stasiun Yogyakarta")

                    input_tujuan = int(input(f"Masukkan kode kereta yang tersedia:\n" +
                    f"{Color.RED}[1] Stasiun Kiaracondong (KAC) Bandung{Color.END}\n" +
                    f"{Color.GREEN}[2] Stasiun Yogyakarta{Color.END}: "))                  
                    if input_tujuan == 1:
                        kelas = int(input(f"Masukkan kode kelas\n{Color.RED}[1] Eksekutif{Color.END}\n{Color.YELLOW}" +
                                        f"[2] Bisnis{Color.END}\n{Color.GREEN}[3] Ekonomi{Color.END}: "))
                        if kelas == 1:
                            kelas = "Eksekutif"
                            harga = 275000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 2:
                            kelas = "Bisnis"
                            harga = 185000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 3:
                            kelas = "Ekonomi"
                            harga = 135000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon
                        else:
                            print("Pilihan tidak ada dalam daftar kode")
                            exit()

                    elif input_tujuan == 2:
                        kelas = int(input(f"Masukkan kode kelas\n{Color.RED}[1] Eksekutif{Color.END}\n{Color.YELLOW}" +
                                        f"[2] Bisnis{Color.END}\n{Color.GREEN}[3] Ekonomi{Color.END}: "))
                        if kelas == 1:
                            kelas = "Eksekutif"
                            harga = 275000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 2:
                            kelas = "Bisnis"
                            harga = 185000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 3:
                            kelas = "Ekonomi"
                            harga = 135000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon
                        else:
                            print("Pilihan tidak ada dalam daftar kode")
                            exit()
                    else:
                        print("Pilihan tidak ada dalam daftar kode")
                        exit()


            elif int(jamSekarang.removeprefix("0")) in range(0, 24400): # 23:32 s/d 02:44
                # Selain stasiun yogyakarta             
                print("Jadwal stasiun kereta saat ini yang tersedia adalah\n" +
                "[1] Stasiun Kiaracondong (KAC) Bandung\n" +
                "[2] Stasiun Pasar Senen (PSE) Jakarta")

                input_tujuan = int(input(f"Masukkan kode kereta yang tersedia:\n" +
                f"{Color.RED}[1] Stasiun Kiaracondong (KAC) Bandung{Color.END}\n" +
                f"{Color.GREEN}[2] Stasiun Pasar Senen (PSE) Jakarta{Color.END}: "))
                kelas = int(input(f"Masukkan kode kelas\n{Color.RED}[1] Eksekutif{Color.END}\n{Color.YELLOW}" +
                                f"[2] Bisnis{Color.END}\n{Color.GREEN}[3] Ekonomi{Color.END}: "))
                if input_tujuan == 1:
                    if kelas == 1:
                        kelas = "Eksekutif"
                        harga = 275000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                        else:
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon

                    elif kelas == 2:
                        kelas = "Bisnis"
                        harga = 185000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                        else:
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon

                    elif kelas == 3:
                        kelas = "Ekonomi"
                        harga = 135000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                        else:
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon
                    else:
                        print("Pilihan tidak ada dalam daftar kode")
                    exit()

                elif input_tujuan == 2:
                    if kelas == 1:
                        kelas = "Eksekutif"
                        harga = 275000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                        else:
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon

                    elif kelas == 2:
                        kelas = "Bisnis"
                        harga = 185000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                        else:
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon

                    elif kelas == 3:
                        kelas = "Ekonomi"
                        harga = 135000
                        if tiket > 3:
                            diskon = 10/100
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                        else:
                            hargaSebelumDiskon = harga * tiket
                            total = hargaSebelumDiskon
                    else:
                        print("Pilihan tidak ada dalam daftar kode")
                        exit()
                else:
                    print("Pilihan tidak ada dalam daftar kode")
                    exit()

            elif int(jamSekarang.removeprefix("0")) in range(53700, 204600): # 05:37 s/d 20:46
                if int(jamSekarang.removeprefix("0")) in range(60000, 204600): # 06:00 s/d 20:46
                    # stasiun ada semua
                    print("Jadwal stasiun kereta saat ini yang tersedia adalah\n" +
                    "[1] Stasiun Kiaracondong (KAC) Bandung\n" +
                    "[2] Stasiun Pasar Senen (PSE) Jakarta\n" +
                    "[3] Stasiun Yogyakarta")

                    input_tujuan = int(input(f"Masukkan kode kereta yang tersedia:\n" +
                    f"{Color.RED}[1] Stasiun Kiaracondong (KAC) Bandung{Color.END}\n" +
                    f"{Color.GREEN}[2] Stasiun Pasar Senen (PSE) Jakarta{Color.END}\n" +
                    f"{Color.YELLOW}[3] Stasiun Yogyakarta{Color.END}: "))
                    if input_tujuan == 1:
                        kelas = int(input(f"Masukkan kode kelas\n{Color.RED}[1] Eksekutif{Color.END}\n{Color.YELLOW}" +
                                        f"[2] Bisnis{Color.END}\n{Color.GREEN}[3] Ekonomi{Color.END}: "))
                        if kelas == 1:
                            kelas = "Eksekutif"
                            harga = 275000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 2:
                            kelas = "Bisnis"
                            harga = 185000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 3:
                            kelas = "Ekonomi"
                            harga = 135000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon
                        else:
                            print("Pilihan tidak ada dalam daftar kode")
                            exit()

                    elif input_tujuan == 2:
                        kelas = int(input(f"Masukkan kode kelas\n{Color.RED}[1] Eksekutif{Color.END}\n{Color.YELLOW}" +
                                        f"[2] Bisnis{Color.END}\n{Color.GREEN}[3] Ekonomi{Color.END}: "))
                        if kelas == 1:
                            kelas = "Eksekutif"
                            harga = 275000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 2:
                            kelas = "Bisnis"
                            harga = 185000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 3:
                            kelas = "Ekonomi"
                            harga = 135000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon
                        else:
                            print("Pilihan tidak ada dalam daftar kode")
                            exit()

                    elif input_tujuan == 3:
                        kelas = int(input(f"Masukkan kode kelas\n{Color.RED}[1] Eksekutif{Color.END}\n{Color.YELLOW}" +
                                        f"[2] Bisnis{Color.END}\n{Color.GREEN}[3] Ekonomi{Color.END}: "))
                        if kelas == 1:
                            kelas = "Eksekutif"
                            harga = 275000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 2:
                            kelas = "Bisnis"
                            harga = 185000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 3:
                            kelas = "Ekonomi"
                            harga = 135000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon
                        else:
                            print("Pilihan tidak ada dalam daftar kode")
                            exit()
                    else:
                        print("Pilihan tidak ada dalam daftar kode")
                        exit()
                else:
                    # stasiun kac bandung sedang istirahat
                    print("Jadwal stasiun kereta saat ini yang tersedia adalah\n" +
                    f"[1] Stasiun Kiaracondong (KAC) Bandung {Color.RED}(Sedang Istirahat){Color.END}\n" +
                    "[2] Stasiun Pasar Senen (PSE) Jakarta\n" +
                    "[3] Stasiun Yogyakarta")

                    input_tujuan = int(input(f"Masukkan kode kereta yang tersedia:\n" +
                    f"{Color.GREEN}[1] Stasiun Pasar Senen (PSE) Jakarta{Color.END}\n" +
                    f"{Color.YELLOW}[2] Stasiun Yogyakarta{Color.END}: "))
                    if input_tujuan == 1:
                        kelas = int(input(f"Masukkan kode kelas\n{Color.RED}[1] Eksekutif{Color.END}\n{Color.YELLOW}" +
                                        f"[2] Bisnis{Color.END}\n{Color.GREEN}[3] Ekonomi{Color.END}: "))
                        if kelas == 1:
                            kelas = "Eksekutif"
                            harga = 275000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 2:
                            kelas = "Bisnis"
                            harga = 185000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 3:
                            kelas = "Ekonomi"
                            harga = 135000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon
                        else:
                            print("Pilihan tidak ada dalam daftar kode")
                            exit()

                    elif input_tujuan == 2:
                        kelas = int(input(f"Masukkan kode kelas\n{Color.RED}[1] Eksekutif{Color.END}\n{Color.YELLOW}" +
                                        f"[2] Bisnis{Color.END}\n{Color.GREEN}[3] Ekonomi{Color.END}: "))
                        if kelas == 1:
                            kelas = "Eksekutif"
                            harga = 275000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 2:
                            kelas = "Bisnis"
                            harga = 185000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon

                        elif kelas == 3:
                            kelas = "Ekonomi"
                            harga = 135000
                            if tiket > 3:
                                diskon = 10/100
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon - (hargaSebelumDiskon * diskon)
                            else:
                                hargaSebelumDiskon = harga * tiket
                                total = hargaSebelumDiskon
                        else:
                            print("Pilihan tidak ada dalam daftar kode")
                            exit()

                    else:
                        print("Pilihan tidak ada dalam daftar kode")
                        exit()

        except ValueError:
            print("Input yang dimasukkan harus bentuk Angka bukan Huruf!!!")
            exit()
else:
    print("Mohon maaf belum ada jadwal stasiun kereta saat ini")


# Keluaran (Output)
if belumAdaJadwal:
    exit()
else:
    print()
    mengetik(f"+ {'-'*135} +")
    mengetik("| {}{:^135}{} |".format(Color.DARKCYAN, "STRUK PEMBAYARAN TIKET", Color.END))
    mengetik(f"+ {'-'*135} +")
    mengetik("| {:^2} | {:^20} | {:^15} | {:^15} | {:^15} | {:^25} | {:^25} |"
    .format("NO","NAMA", "NIK", "KELAS", "JUMLAH TIKET", "HARGA SATUAN TIKET", "HARGA TOTAL"))
    mengetik(f"+ {'-'*135} +")
    
    mengetik("| {:^2} | {:^20} | {:^15} | {:^15} | {:^15} |  {:^24} | {:^25} |"
    .format(1, list_input_nama[0], list_input_noktp[0], kelas, tiket, f"Rp.{harga}", f"Rp.{hargaSebelumDiskon}"))
    for x in range(1, len(list_input_nama)):
        mengetik("| {:^2} | {:^20} | {:^15} | {:^15} | {:^15} | {:^25} | {:^25} |"
        .format(x+1, list_input_nama[x], list_input_noktp[x], "-", "-", "-", "-", "-"))
    mengetik("-" * 139)
    mengetik("{:>96} {:>16} {}Rp.{}{} {:>15}".format("| Harga total yang harus dibayar", "=", Color.RED, hargaSebelumDiskon, Color.END, "|"))
    mengetik("{:>72} {:>40} {:>2}% {:>21}".format("| Diskon", "=", int(diskon * 100), "|")) # Kali dalam bentuk persen
    mengetik("{:>111} {} Rp.{} {:>15}".format("| Harga total yang harus dibayar setelah diskon", "=", int(total), "|"))
    
    uang = int(input("Masukkan jumlah uang anda: "))
    kembalian = uang - total

    mengetik("{:>86} {:>26} Rp.{} {:>14}".format("| Uang yang dibayarkan", "=", uang, "|"))
    mengetik("{:>75} {:>37} {}Rp.{}{} {:>14}".format("| Kembalian", "=", Color.GREEN, int(kembalian), Color.END, "|"))
    mengetik("{:>139}".format("-"*75))
    mengetik("{}{:^130}{}".format(Color.PURPLE, "TERIMA KASIH !!!", Color.END))