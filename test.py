print("\n")

print("="*10, "GEROBAK FRIED CHIKKEN", "="*10)
print("-"*40)
print("Kode     JenisPotong Harga")
print("D        Dada        Rp.2500")
print("P        Paha        Rp.2000")
print("S        Sayap       Rp.1500")


daftar = ("dada", "d", "paha", "p", "sayap", "s")
daftar_harga = {"Dada": 2500, "Paha": 2000, "Sayap": 1500}

hasil_daftar = []
hasil_potong = []
hasil_bPajak = []

dada = 2500
paha = 2000
sayap = 1500
counter = 0

total = 0
bPajak = 0
pajak = 0.1
gantiJenis = False
ulang = False

n = int(input("Banyak Jenis: "))


while counter < n:
    print("\n")
    print(f"Jenis Ke- {counter+1}")

    kJenis = input("Kode Potong [D=Dada/P=Paha/S=Sayap] ")
    

    if kJenis.lower() == "dada" or kJenis.lower() == "d":
        bjPotong = int(input("Masukkan banyak jenis potong: "))
        bPajak = bjPotong * dada
        # aPajak = bPajak * pajak
        # total = bPajak + aPajak
        hSatuan = dada

        hasil_potong.append(bjPotong)
        hasil_bPajak.append(bPajak)

        gantiJenis = True

        if gantiJenis:
            kJenis = "Dada"

    elif kJenis.lower() == "paha" or kJenis.lower() == "p":
        bjPotong = int(input("Masukkan banyak jenis potong: "))
        bPajak = bjPotong * paha
        # aPajak = bPajak * pajak
        # total = bPajak + aPajak
        hSatuan = paha

        hasil_potong.append(bjPotong)
        hasil_bPajak.append(bPajak)
        gantiJenis = True

        if gantiJenis:
            kJenis = "Paha"

    elif kJenis.lower() == "Sayap" or kJenis.lower() == "s":
        bjPotong = int(input("Masukkan banyak jenis potong: "))
        bPajak = bjPotong * sayap
        # aPajak = bPajak * pajak
        # total = bPajak + aPajak
        hSatuan = sayap

        hasil_potong.append(bjPotong)
        hasil_bPajak.append(bPajak)
        gantiJenis = True

        if gantiJenis:
            kJenis = "Sayap"
    else:   
        print("DATA TIDAK ADA !!!!")
        continue

    hasil_daftar.append(kJenis)
    counter += 1

uang = float(input("Masukkan jumlah uang: "))
aPajak = int(sum(hasil_bPajak)) * pajak
jBayar = int(sum(hasil_bPajak))
total = aPajak + jBayar
kembalian = uang - total


print("\n")
print("="*10, "GEROBAK FRIED CHIKKEN", "="*10)
print("-"*70)
print(f"No      Jenis Potong        Harga Satuan        Banyak Beli      Jumlah Harga")

for k, v in enumerate(hasil_daftar):
    print(f"{k+1}\t {hasil_daftar[k]} \t\t\t Rp.{daftar_harga[v]} \t {hasil_potong[k]} \t\tRp.{hasil_bPajak[k]}")

print("-"*70)
print("\t" * 6, f"Jumlah Bayar \tRp.{sum(hasil_bPajak)}")
print("\t" * 6, f"Pajak 10% \tRp.{int(sum(hasil_bPajak) * pajak)}")
print("\t" * 6, f"Total Bayar \tRp.{int(total)}")
print("\t" * 6, f"Uang Anda \tRp.{int(uang)}")
print("\t" * 6, f"Kembalian \tRp.{int(kembalian)}")
print()