from copy import deepcopy
data_0 = [1, 2]
data_1 = [3, 4]

data_2D = [data_0, data_1]
data_2D_copy = data_2D.copy()

print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

# mengambil data dari nested list
data = data_2D[0][1]
print(f"data = {data}")

# address semuanya
print(f"address asli = {hex(id(data_2D))}")
print(f"address copy = {hex(id(data_2D_copy))}")

print("address dari member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_copy[0]))}")

# kita gunakan deep copy

data_2D = [data_0, data_1, 10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"address asli = {hex(id(data_2D))}")
print(f"address deep = {hex(id(data_2D_deepcopy))}")

print("address dari member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_deepcopy[0]))}")

# kita coba ubah data milik nested list data_2D
# di posisi list ke 1, dan index ke 0 menjadi nilai 30
# tapi data nested list copy yakni data_2D_copy tidak ikut berubah
data_2D[1][0] = 30
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
