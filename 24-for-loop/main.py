# Perulangan (loop)

# for kondisi:
#     aksi

# ini dengan list
angka2_list = [0, 1, 2, 3, 4]

# i adalah angka/data didalam list angka2
# cara bacanya adalah untuk i (setiap data) didalam list angka2, maka lakukan operasi...
for i in angka2_list:
    print(f"i sekarang -> {i}")

print("akhir dari program 1 \n")

# ini dengan range
angka2_range = range(5)  # 0, 1, 2, 3, 4

for i in angka2_range:
    print(f"i sekarang -> {i}")

print("akhir dari program 2 \n")

angka2_range = range(1, 5)  # 1, 2, 3, 4

for i in angka2_range:
    print(f"i sekarang -> {i}")

print("akhir dari program 3 \n")

# menggunakan string atau perulangan terhadap data string
data_str = "saya ganteng abiees"

for huruf in data_str:
    print(huruf)

print("akhir dari program 4 \n")
