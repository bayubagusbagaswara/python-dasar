# latihan perulangan membuat segitiga

sisi = 5

# 1. Menggunakan For
# dummy variable
print("awal For")
count = 1
for i in range(sisi):
    # ini akan menurun ke bawah dan jumlahnya sesuai dengan nilai count nya
    print("*"*count)
    count += 1

print("akhir dari for")
# 2. Menggunakan While

print("awal While")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("akhir While")

# 3. Hanya ganjil saja
print("awal While")
count = 1
while True:
    # akan kembali ke atas jika ganjil
    if count % 2:
        # print jika ganjil
        print("*"*count)
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("akhir While")

# 4. hanya ganjil saja
print("awal while")
count = 1
spasi = 5
while True:
    if(count % 2):
        # print jika ganjil
        print(" "*spasi, "+"*count)
        spasi -= 1
        spasi += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("akhir while")
