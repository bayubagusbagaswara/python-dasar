# Operasi logika atau boolean

# not, or, and , xor
a = True
c = not a

# NOT
print('data boolean = ', a)
print('--------------NOT')
print('data c = ', c)


# OR
# Jika salah satu atau kedua nilainya bernilai true, maka hasilnya akan true
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)
print('---------------NOT')
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
print('---------------NOT')

# AND
# Jika dua-dua nya bernilai true, maka hasilnya true
a = True
b = True
c = a and b
print(a, 'AND', b, '=', c)
print('---------------NOT')
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)
print('---------------NOT')
a = True
b = False
c = a and b
print(a, 'AND', b, '=', c)
print('---------------NOT')

# XOR
# Dia akan menghasilkan nilai true, jika HANYA SALAH SATU saja yang bernilai True
# Jika dua-dua nya bernilai true, maka akan menghasilkan nilai False
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
print('---------------XOR')

a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
print('---------------XOR')

a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)
print('---------------XOR')
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
print('---------------XOR')
