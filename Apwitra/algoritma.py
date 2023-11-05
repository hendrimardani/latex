print("\n")
print("           ===== Lagu anak ayam =====")

n = int(input("Masukan N angka 5 nya: "))
counter = 5
print("\n")
print("           === Mangga sok gera nyanyi ===")
print("\n")
print("Tek kotek kotek kotek, anak ayam turun berkotek")

for i in range(n, 0, -1):
    counter -= 1

    if counter == 0 :
        print(f"Anak ayam turunlah {i} mati satu tinggallah induknya")
    else:
        print(f"Anak ayam turunlah {i} mati satu tinggallah {counter} ")
print("\n")
print("           === Haturnuhun ===")