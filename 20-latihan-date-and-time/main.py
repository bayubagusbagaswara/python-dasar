# Date and Time

# ada library datetime bawaan python
# kita harus import dahulu
import datetime as dt


# tanggal_hari_ini = dt.date.today()
# hari_ini = dt.datetime.today()

# print(tanggal_hari_ini)
# print(hari_ini)
# print(f"Hari ini adalah hari = {hari_ini:%A}")

# tanggal = dt.date(1996, 8, 12)
# print(tanggal)
# print(f"Hari {tanggal} adalah hari = {tanggal:%A}")

print("Silahkan masukkan tanggal, \nbulan dan tahun lahir anda")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah: {tanggal_lahir}")
print(f"Hari nya adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Hari nya adalah : {tanggal_lahir:%A}")
print(f"umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")
