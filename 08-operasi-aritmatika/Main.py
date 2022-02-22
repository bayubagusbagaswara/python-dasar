# operasi aritmatika

from re import X


a = 10
b = 3

# operasi penjumlahan (+)
hasil = a + b
print(a, '+', b, '=', hasil)

# operasi pengurangan (-)
hasil = a - b
print(a, '-', b, '=', hasil)

# operasi perkalian (*)
hasil = a * b
print(a, '*', b, '=', hasil)

# operasi pembagian (/)
hasil = a / b
print(a, '/', b, '=', hasil)  # hasilnya float/pecahan

# operasi eksponen atau pangkat (**)
hasil = a ** b
print(a, '**', b, '=', hasil)

# operasi modulus atau sisa bagi (%)
hasil = a % b
print(a, '%', b, '=', hasil)

# operasi floor division (pembagian tapi hasilnya dibulatkan kebawah)
hasil = a // b
print(a, '//', b, '=', hasil)

# prioritas operasi, operasi precedence
'''
1. tanda kurung didahulukan ()
2. exponen **
3. perkalian dan teman-teman * / ** % //
4. penjumlahan dan pengurangan + - 
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(hasil)
