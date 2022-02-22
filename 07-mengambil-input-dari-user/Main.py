data = input("Masukkan data: ")  # langsung isi inputnya di terminal

print("Data = ", data)  # tampilkan isi datanya yang sudah kita input di terminal

# tapi tipe data yang kita inputkan adalah pasti string
print("data = ", data, ",type = ", type(data))

# jika kita ingin mengambil tipe data integer, maka kita harus casting
angka = int(input("Masukkan angka: "))
angka = float(input("Masukkan angka: "))

print("data = ", angka, ", type = ", type(angka))

# bagaimana dengan boolean, harus casting dulu ke integer
biner = bool(int(input("Masukkan nilai boolean: ")))

print("data = ", biner, ", type = ", type(biner))
