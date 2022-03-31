# Operasi Komparasi

# Setiap hasil dari operasi komparasi adalah boolean, artinya hanya True atau False

# ada >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# lebih besar dari (>)
print("========== lebih besar dari (>) ===========")
hasil = a > 3
print(a, '>', 3, '=', hasil)  # 4 > 3 = True
hasil = b > 3
print(b, '>', 3, '=', hasil)  # 2 > 3 = False

print("========== kurang dari (<) ===========")
hasil = a < 3
print(a, '<', 3, '=', hasil)  # 4 < 3 = False
hasil = b < 3
print(b, '<', 3, '=', hasil)  # 2 < 3 = True

print("========== lebih dari sama dengan (>=) ===========")
hasil = a >= 2
print(a, '>=', 2, '=', hasil)  # 4 >= 2 = True
hasil = b >= 2
print(b, '>=', 2, '=', hasil)  # 2 >= 2 = True

print("========== kurang dari sama dengan (<=) ===========")
hasil = a <= 2
print(a, '<=', 3, '=', hasil)  # 4 <= 2 = False
hasil = b <= 2
print(b, '<=', 3, '=', hasil)  # 2 <= 2 = True

print("========== sama dengan (==) ===========")
hasil = a == 2
print(a, '==', 3, '=', hasil)  # 4 == 2 = False
hasil = b == 2
print(b, '==', 3, '=', hasil)  # 2 == 2 = True

print("========== tidak sama dengan (!=) ===========")
hasil = a != 2
print(a, '!=', 3, '=', hasil)  # 4 != 2 = True
hasil = b != 2
print(b, '!=', 3, '=', hasil)  # 2 != 2 = False

# is berguna untuk membandingkan memory atau object
# is sebagai komparasi object identity
print("========== is ===========")
x = 5  # ini adalah assignment membuat object
y = 5
# x itu ada nilainya dan bisa dipanggil kapan saja
# makanya x itu disebut variable dan memakan memory
# sedangkan nilai 5 itu tidak memakan memory, atau disebut literal, karena hanya bertugas sebaris itu saja
print('nilai x =,', x, ',id = ', hex(id(x)))
print('nilai y =,', y, ',id = ', hex(id(y)))
# hasilnya x dan y itu sama, karena python sudah mengerti kalau nilainya 5 itu sama
# beda kalau java, hasilnya pasti beda, karena beda objectnya (ditaruh di memory yang berbeda)
hasil = x is y
print('x is y = ', hasil)  # true


print("========== is not ===========")
x = 5
y = 5
print('nilai x =,', x, ',id = ', hex(id(x)))
print('nilai y =,', y, ',id = ', hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)

x = 5
y = 6
print('nilai x =,', x, ',id = ', hex(id(x)))
print('nilai y =,', y, ',id = ', hex(id(y)))
hasil = x is not y
print('x is not y = ', hasil)
