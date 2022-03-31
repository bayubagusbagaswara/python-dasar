# operator bitwise, operator biner, binary
# bitwise -> operasi masing-masing bit

# operator OR itu artinya JUMLAH antara dua bitwise
a = 9
b = 5

#  bitwise OR (|)
c = a | b
print('\n====OR======')
print('nilai : ', a, ', binary : ', format(a, '08b'))
print('nilai : ', b, ', binary : ', format(b, '08b'))
# lalu kita OR kan antara biner a dan biner b
print('--------------------------------- (|)')
print('nilai : ', c, ', binary : ', format(c, '08b'))

# bitwise AND (&) antara 2 biner (bukan perkalian)
c = a & b
print('\n====AND======')
print('nilai : ', a, ', binary : ', format(a, '08b'))
print('nilai : ', b, ', binary : ', format(b, '08b'))
print('--------------------------------- (&)')
print('nilai : ', c, ', binary : ', format(c, '08b'))

# bitwise XOR (^)
c = a ^ b
print('\n====XOR======')
print('nilai : ', a, ', binary : ', format(a, '08b'))
print('nilai : ', b, ', binary : ', format(b, '08b'))
print('--------------------------------- (^)')
print('nilai : ', c, ', binary : ', format(c, '08b'))

# bitwise NOT (~)
c = ~a
print('\n====NOT======')
print('nilai : ', a, ', binary : ', format(a, '08b'))
print('--------------------------------- (~)')
print('nilai : ', c, ', binary : ', format(c, '08b'))
# kita XOR kan
print('--------------------------------- (^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :', e ^ d, ', binary : ', format(e ^ d, '08b'))

# shifting

# geser ke kanan (>>)
c = a >> 1  # akan bergeser ke kanan 1 kali
print('nilai : ', a, ', binary : ', format(a, '08b'))
print('--------------------------------- (>>)')
print('nilai : ', c, ', binary : ', format(c, '08b'))

# geser ke kiri (<<)
c = a << 1  # akan bergeser ke kiri 1 kali
print('nilai : ', a, ', binary : ', format(a, '08b'))
print('--------------------------------- (<<)')
print('nilai : ', c, ', binary : ', format(c, '08b'))
