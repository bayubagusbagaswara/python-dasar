# continue, pass, break

# pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi
angka = 0

while angka < 5:
    angka += 1

    if angka == 3:
        pass  # ini tidak akan dieksekusi

    print(angka)

print("Akhir perulangan")

# continue
angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")

# jadi ini akan men-skip loop sekarang, jadi kode program di bawah continue akan dilewatkan
    if angka == 3:
        print("nice!")
        continue  # akan membuat loop meloncat ke step selanjutnya

    print("whassup!")

print("Pinish!")
