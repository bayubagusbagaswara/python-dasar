# membuat gabungan area rentang dari angka

#  ++++++3------------10++++++

inputUser = float(input(
    "Masukkan angka yang bernilai kurang dari 3 atau lebih besar dari 10:"))

# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 = ", isKurangDari)

# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 = ", isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan: ", isCorrect)

# kasus irisan
inputUser = float(input(
    "Masukkan angka yang bernilai lebih dari 3 dan kurang dari 10:"))

# memeriksa lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 = ", isLebihDari)

# memerikan kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10 = ", isKurangDari)

isCorrect = isLebihDari and isKurangDari
print("angka yang anda masukkan: ", isCorrect)
