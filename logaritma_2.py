# n = int(input("Masukkan N data: "))
# counter = 5

# print("Tek kotek kotek kotek, anak ayam turun berkotek")

# for i in range(n, 0, -1):
#     counter -= 1

#     if counter == 0 :
#         print(f"anak ayam turunlah {i} mati satu tinggallah induknya")
#     else:
#         print(f"anak ayam turunlah {i} mati satu tinggallah {counter}")






# n = int(input("Masukkan Jumlah bintang: "))

# print("\n")

# for x in range(n, 0, -1):
#     for j in range(0, x):
#         print("*",end="")
#     print(" ")
# print("\n")





# n = int(input("Masukkan jumlah N: "))

# for i in range(0, n):
#     if i == 0:
#         for j in range(i + 1):
#             print(f"{j} ", end="")
#     elif i == 1:
#         for j in range(i + 1):
#             print("$ ", end="")
#     elif i == 2:
#         for j in range(i + 1):
#             print("& ", end="")
#     else:
#         for j in range(i + 1):
#             print("* ", end="")
#     print(" ")
    




# n = int(input("N: ? "))

# for i in range(0, n):
#     for j in range(0, i+1):
#         print("* ", end="")
#     print(" ")







# n = int(input("Masukkan jumlah N: "))

# baris = n

# for i in range(0, baris):
#     # looping bintang
#     for j in range(n, i, -1):
#         print("*", end="")
    
#     print(" ", end="")

#     # looping angka
#     for x in range(0, i + 1):
#         print("1", end="")

#     # looping angka
#     print(" ", end="")
#     for x in range(0, i + 1):
#         print("@", end="")

#     # looping pagar
#     print(" ", end="")
#     for x in range(n, i, -1):
#         print("#", end="")
#     print(" ")





# # Seigitga Sama Kaki
# n = int(input("Masukkan jumlah N: "))

# baris = n

# print()
# for i in range(1, baris):

#     # Looping kiri
#     for spasi in range(i, n):
#         print(" ", end="")
    
#     # Rumus ganjil 2(n)-1
#     for bintang in range(0, (i * 2) - 1):
#         print("*", end="")

#     print()

# print()







# # Seigita Sama kaki spasi
# n = int(input("Masukkan jumlah N: "))

# baris = n

# print()
# for i in range(1, baris+1):

#     # Looping kiri
#     for spasi in range(i, n):
#         print(" ", end="")
    
#     # Rumus ganjil 2(n)-1
#     for bintang in range(0, (i * 2) - 1):
#         # Jika bintang ganjil
#         if bintang % 2 == 1:
#             print(" ", end="")
#         else:
#             print("*", end="")

#     print()

# print()







# # Segitiga sama kaki terbalik spasi
# n = int(input("Masukkn jumlah N: "))

# baris = n

# print()
# for i in range(baris, 0, -1):
#     for spasi in range(n, i, -1):
#         print(" ", end="")

#     for bintang in range(0, (i * 2) - 1):
#         if bintang % 2 == 1:
#             print(" ", end="")
#         else: 
#             print("*", end="")
#     print()
# print()




# # Segitiga sama kaki terbalik
# n = int(input("Masukkn jumlah N: "))

# baris = n


# for i in range(baris, 0, -1):
#     for spasi in range(n, i, -1):
#         print(" ", end="")

#     for bintang in range(0, (i * 2) - 1):
#         print("*", end="")
#     print()







# # Segitiga terbalik spasi
# n = int(input("Masukkn jumlah N: "))

# baris = n

# for i in range(baris, 0, -1):
#     for spasi in range(n, i, -1):
#         print(" ", end="")

#     for bintang in range(0, (i * 2) - 1):
#         if bintang % 2 == 1:
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print()







# # Diamond
# def segitigaSatu():
#     baris = n

#     print()
#     for i in range(1, baris):

#         # Looping kiri
#         for spasi in range(i, n):
#             print(" ", end="")
        
#         # Rumus ganjil 2(n)-1
#         for bintang in range(0, (i * 2) - 1):
#             print("*", end="")

#         print()

# def segitigaDua():
#     baris = n

#     for i in range(baris, 0, -1):
#         for spasi in range(n, i, -1):
#             print(" ", end="")

#         for bintang in range(0, (i * 2) - 1):
#             print("*", end="")
#         print()
    
# n = int(input("Masukkn jumlah N: "))
# jumlah = int(input("Masukkan jumlah looping: "))
# print()
# for x in range(0, jumlah):
#     segitigaSatu()
#     segitigaDua()
# print()








# Diamond bintang spasi
def segitigaSatu():
    baris = n

    for i in range(1, baris+1):

        # Looping kiri
        for spasi in range(i, n):
            print(" ", end="")
        
        # Rumus ganjil 2(n)-1
        for bintang in range(0, (i * 2) - 1):
            # Jika bintang ganjil
            if bintang % 2 == 1:
                print(" ", end="")
            else:
                print("*", end="")

        print()


def segitigaDua():
    baris = n

    for i in range(baris, 0, -1):
        for spasi in range(n, i, -1):
            print(" ", end="")

        for bintang in range(1, (i * 2) - 1):
            if bintang % 2 == 1:
                print(" ", end="")
            else: 
                print("*", end="")
        print()

n = int(input("Masukkn jumlah N: "))
jumlah = int(input("Masukkan jumlah looping: "))
print()
for x in range(0, jumlah):
    segitigaSatu()
    segitigaDua()
print()