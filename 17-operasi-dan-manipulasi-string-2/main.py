# operator dalam bentuk methods

# merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay = "aKu KeCe AbieezZzZZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

# pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower()  # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()  # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- untuk huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline \n
# istitle() <-- semua kata dimulai dengna huruf besar

# title harus Capital kata-kata nya
judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()  # hasilnya bool

print(judul + " is title = " + str(cek_judul))

# ngecek komponen startswith() endswith() dan ini case sensitive
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))

# penggabungan komponen join() split()
pisah = ['aku', 'sayang', 'kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = ' ehm '.join(pisah)
print(gabung)

gabung = "akuehmsayangehmkamu"
# ehm akan dihilangin, dan jadinya dalah array of string
print(gabung.split('ehm'))

# alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(10)  # rata kanan dengan total string 10
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10)
print("'"+tengah+"'")

tengah = "tengah".center(20, ":")
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = tengah.strip(":")  # menghilangkan tanda :
print("'"+tengah+"'")
