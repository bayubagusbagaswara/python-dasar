# teknik menduplikat list

a = ["Ucup", "Otong", "Dudung"]
print(f"a = {a}")

# address b sama dengan address a, jadi reference satu list
# atau pass by references
b = a
print(f"b = {b}")

# kita akan mengubah member dari a
a[1] = "Michael"
b.sort()

print(f"a = {a}")
print(f"b = {b}")

# references untuk list
# caranya dengah kita meng-copy list nya
# address c dengan address a berbeda
c = a.copy()

# kita ubah data ke 0
c[0] = "Dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
