# LIST

# Kumpulan data numbers
data_angka = [1, 5, 2, 3]
print(data_angka)

# Kumpulan data string
data_string = ["ucup", "otong", "odah"]
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# Kumpulan data campuran
data_campuran = [1, "bala-bala", 2, "cireng", "ucup", True, "otong", False]
print(data_campuran)

# cara alternatif membuat list
data_range = range(0, 10, 2)  # range(start,stop,stop)
print(data_range)

data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
list_pake_for = [i**2 for i in range(0, 10)]  # i akan dikuadratkan
print(list_pake_for)

# membuat list pake for pake if
# misal kita ingin menghilangkan angka 5
list_pake_for_if = [i for i in range(0, 10) if i != 5]
print(list_pake_for_if)

# misal hanya mencetak i yang genap
list_pake_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(list_pake_for_if)

# misal hanya mencetak i yang ganjil
list_pake_for_if = [i for i in range(0, 10) if i % 2 != 0]
print(list_pake_for_if)
