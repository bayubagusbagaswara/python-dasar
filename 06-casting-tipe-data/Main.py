# macam-macam tipe data = int, float, str, bool

print("======INTEGER=======")
data_int = 9
print("Data = ", data_int, ", type = ", type(data_int))

# casting from int to float
data_float = float(data_int)
data_str = str(data_int)
# boolean akan bernilai false, jika nilai integernya adalah 0
data_bool = bool(data_int)
print("Data = ", data_float, ", type = ", type(data_float))
print("Data = ", data_str, ", type = ", type(data_str))
print("Data = ", data_bool, ", type = ", type(data_bool))

# casting from float to int, str, bool
print("======FLOAT=======")
data_float = 9.5
print("data = ", data_float, ", type = ", type(data_float))

data_int = int(data_float)  # integer dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)
print("Data = ", data_int, ", type = ", type(data_int))
print("Data = ", data_str, ", type = ", type(data_str))
print("Data = ", data_bool, ", type = ", type(data_bool))


print("========BOOLEAN=========")
data_bool = True
print("data = ", data_bool, ", type = ", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("Data = ", data_int, ", type = ", type(data_int))
print("Data = ", data_str, ", type = ", type(data_str))
print("Data = ", data_float, ", type = ", type(data_float))

print("========STRING=========")
data_str = "bagaswara"
print("data = ", data_str, ", type = ", type(data_str))

# string tidak bisa diubah menjadi integer, atau bisanya hanya string angka
data_int = int(data_str)
data_float = float(data_str)  # bisanya hanya string angka
# true, baru false jika string nya bernilai blank (string kosong)
data_bool = bool(data_str)
print("Data = ", data_int, ", type = ", type(data_int))
print("Data = ", data_float, ", type = ", type(data_float))
print("Data = ", data_bool, ", type = ", type(data_bool))
