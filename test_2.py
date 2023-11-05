print("\n")

gp = 300_000
nama = input("Nama Anda?: ")
golongan = int(input("Golongan Anda? [1/2/3]: "))
pendidikan = input("Pendidikan Anda? [sma/d1/d3/s1]: ")
jam_kerja = int(input("Jumlah Jam kerja anda?: "))
lembur = 0
tunjangan_golongan = 0
tunjangan = 0
jam_normal = 8

if pendidikan == "sma":
    tunjangan = gp * 2.5/100
elif pendidikan == "d1":
    tunjangan = gp * 5/100
elif pendidikan == "d3":
    tunjangan = gp * 20/100
elif pendidikan == "s1":
    tunjangan = gp * 30/100
else:
    print("Data Tidak ada")

if golongan == 1:
    tunjangan_golongan = gp * 5/100
elif golongan == 2:
    tunjangan_golongan = gp * 10/100
elif golongan == 3:
    tunjangan_golongan = gp * 15/100
else:
    tunjangan_golongan = 0

if jam_kerja > jam_normal:
    lembur = (jam_kerja - jam_normal) * 3500
else:
    lembur = 0

tunjangan_total = tunjangan + tunjangan_golongan

total_gaji = gp + tunjangan_total + lembur

print("\n")

print("="*25, "PROGRAM HITUNG GAJI KARYAWAN", "="*25)
print("\n")
print(f"Nama Karyawan = {nama}")
print("Honor yang diterima:")
print(f"Tunjangan Jabatan = {golongan}")
print(f"Pendidikan = {tunjangan}")
print(f"Jumlah Jam Kerja = {jam_kerja}")
print(f"Honor Lembur = {lembur}")
print(f"Total Gaji  {total_gaji}")