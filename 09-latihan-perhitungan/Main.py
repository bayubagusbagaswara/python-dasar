# Latihan konversi temperature
#  Celcius, Reamur, Fahrenheit, Kelvin

# Program Konversi Celcius ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukkan suhu dalam Celcius : '))
print("Suhu adalah ", celcius, " Celcius")

# Reamur = (4/5)*Celcius
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ", reamur, " Reamur")

# Fahrenheit = ((9/5)*Celcius)+32
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah ", fahrenheit, " Fahrenheit")

# Kelvin = Celcius + 273
kelvin = celcius + 273
print("Suhu dalam kelvin adalah ", kelvin, " Kelvin")
