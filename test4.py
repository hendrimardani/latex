# import math

# n = int(input("Masukkan nilai N: "))

# faktorial = math.factorial(n)

# print(f"{n}! = {faktorial}")




# def faktorial(n):
#     if n < 1:
#         return 1

#     return n * faktorial(n - 1)

# print(faktorial(5))






# def pangkat(x, y):
#     if y == 0:
#         return 1
#     else:
#         return x * pangkat(x, y-1)

# x = int(input("Masukkan Nilai Utama: "))
# y = int(input("Masukkan Nilai Pangkat: "))

# print(f"{x} dipangkatkan {y} = {pangkat(x, y)}")




# def fibonacci(n):
#     if n < 1:
#         return [n]

#     listSebelumN = fibonacci(n - 1)
#     angka1 = listSebelumN[-2] if len(listSebelumN) > 2 else 0
#     angka2 = listSebelumN[-1] if len(listSebelumN) > 2 else 1

#     return listSebelumN + [angka1 + angka2]

# panjang = int(input("Masukkan panjang deret: "))
# print(fibonacci(panjang - 1))





# def towerOfHanoi(n, source, destination, auxiliary):
#     if n == 1:
#         return print(f"Move disk 1 from source {source}, to destination {destination}")

#     towerOfHanoi(n-1, source, auxiliary, destination)
#     print(f"Move disk {n} from source {source} to destination {destination}")
#     towerOfHanoi(n-1, auxiliary, destination, source)
 
# n = 2

# towerOfHanoi(n, "A", "B", "C")



# class Hitung:
#     def faktorial(n):
#         if n < 1:
#             return 1

#         return n * Hitung.faktorial(n - 1)

#     def deretJumlah(n):
#         if n == 0:
#             return 0

#         return n + Hitung.deretJumlah(n - 1)

# faktorial = Hitung.faktorial(5)
# print(faktorial)

# deretJumlah = Hitung.deretJumlah(5)
# print(deretJumlah)
