# Latihan

# Kalkulator sederhana

print(20*"=")
print("Kalkulator Serderhana")
print(20*"=" + "\n")

angka_1 = float(input("masukkan angka 1 = "))
operator = input("operator (+, -, x, /) : ")
angka_2 = float(input("masukkan angka 2 = "))

# percabangannya
if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")

elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")

elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")

elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")

else:
    print("Salah memasukkan data")

print("Akhir dari program")
