# # Perhitungan matrix perkalian
# mat1 = [
#     [9, 0],
#     [3, 6]
# ]

# mat2 = [
#     [6, 0],
#     [7, 2]
# ]
# mat3 = []

# for x in range(0, len(mat1)):
#     row = []
#     for y in range(0, len(mat1[0])):
#         total = 0
#         for z in range(0, len(mat1)):
#             total = total + (mat1[x][z] * mat2[z][y])

#         row.append(total)
#     mat3.append(row)

# for x in range(0, len(mat3)):
#     for y in range(0, len(mat3[0])):
#         print(mat3[x][y], end=" ")







# mat1 = [
#     [9, 0],
#     [3, 6]
# ]

# mat2 = [
#     [6, 0],
#     [7, 2]
# ]
# mat3 = []

# for x in range(0, len(mat1)):
#     row = []
#     for y in range(0, len(mat1[0])):
#         total = 0
#         for z in range(0, len(mat1)):
#             total = total + (mat1[x][z] * mat2[z][y])

#         row.append(total)
#     mat3.append(row)

# print(mat3)
# # Output: [[54, 0], [60, 12]]













mat1 = [
    [9, 0],
    [3, 6]
]

mat2 = [
    [6, 0],
    [7, 2]
]


hasil = []

for x in range(0, len(mat1)):
    for y in range(0, len(mat1)):
        total = 0
        for z in range(0, len(mat1)):
            total += mat1[x][z] * mat2[z][y]

        hasil.append(total)


# print(hasil)
# [54, 0, 60, 12]

for x in range(0, len(hasil)):
    print(hasil[x], end=" ")
print()