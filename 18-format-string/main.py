# format string

# contoh generic
# string
nama = "marlene"
format_str = f"hello {nama}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
# integer bisa pake format :d
angka = 15
format_str = f"bilangan bulat = {angka:d}"

# bilangan ribuan
angka = 2000
format_str = f"ribuan = {angka:,}"  # 2,000
print(format_str)

angka = 2000000
format_str = f"ribuan = {angka:,}"  # 2,000,000
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"angka = {angka:.2f}"  # ada 2 angka dibelakang koma 2005.54
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:010.3f}"  # 02005.543
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10.1234
# keluar tanda minus -10. +d artinya desimal
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"  # keluar tanda plus +10.12

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"  # 4.50%
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5

format_string = f"harga total = Rp. {harga*jumlah}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)
