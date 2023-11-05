import pandas as pd

list_nomer = []
list_nim = []
list_nama = []
list_uts = []
list_uas = []
list_total = []

ulang = 2
for x in range(ulang):
    print(f"data Ke - {x + 1}")
    list_nomer.append(x+1)
    list_nim.append(input("NIM: "))
    list_nama.append(input("Nama: "))
    list_uts.append(int(input("Nilai UTS: ")))
    list_uas.append(int(input("NIlai UAS: ")))

for x in range(ulang):
    list_total.append((list_uas[x] + list_uts[x]) / 2)

data_tamu = pd.DataFrame({
    "No": list_nomer,
    "NIM": list_nim,
    "Nama Lengkap": list_nama,
    "Nilai UTS": list_uts,
    "Nilai UAS": list_uas,
    "Rata-rata": list_total
}, index=None)

print()
print("="*20, " Daftar Nilai ", "="*20)
print(data_tamu)
print("="*56)
print()