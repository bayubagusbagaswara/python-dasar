# Operasi

# index 0, index 1, index 2
data = ["Ucup", "Otong", "Dudung"]

# mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_ucup = data[-3]
print(f"data ucup = {data_ucup}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# Manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")
# data.insert(posisi, item)

# asep akan ditambahkan ke index 1
data.insert(1, "Asep")
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list
data.append("Jajang")
print(f"data ditambah lagi = \n{data}")

# menambahkan list dengan list
data_baru = ["Ujang", "Usep", "Dadang"]
data.extend(data_baru)
print(f"data gabungan =\n{data}")

# mengubah data
# kita ubah data 2 menjadi michael
data[2] = "Michael"
print(f"data setelah diubah = \n{data}")

# remove data
data.remove("Ujang")
print(f"data setelah diremove = \n{data}")

# meremove data paling belakang
data_akhir = data.pop()
print(f"data akhir = \n{data}")

print(data_akhir)
