# 🔰🔰 Operator Penugasan
'''
operator ini digunakan untuk penetapkan nilai ke variabel
'''

# ⚡ Operator (=)

n = 'Koding'
o = 2

# ⚡ Operator (+=)
n = 2
print('n awal :', n)

n = n + 2
print('n diubah :', n)

n += 1
print('n diubah menggunakan operator += :', n)


# ⚡ Operator (*=)

o = 2
print('o awal :', o)

o = o * 2
print('o diubah :', o)

o *= 2
print('o diubah menggunakan operator *= :', o)

# ⚡ Operator (/=)

i = 20
print('i awal :', i)

i = i / 2
print('i diubah :', i)

i /= 2
print('i diubah menggunakan operator /= :', i)

# ⚡ Operator (%=)

n = 10
print('n awal :', n)

n %= 3
print('n diubah menggunakan operatorn %= :', n)

# ⚡ Operator (//=)

o = 10
print('o awal :', o)

o //= 2
print('o diubah menggunakan operator //= :', o)


# ⚡ Operator (**=)

i = 10
print('i awal :', i)

i **= 2
print('i diubah menggunakan operator **= :', i)

# ⚡ Operator (&=)
n = 5
print('n awal :', n)

n &= 3
print('n diubah menggunakan operator &= :', n)

# ⚡ Operator (|=)

o = 10
print('o awal :', o)

o |= 2
print('o diubah menggunakan operator |= :', o)

# ⚡ Operator (^=)

i = 7
print('i awal :', i)

i ^= 5
print('i diubah menggunakan operator =^ :', i)

# ⚡ Operator (>>=)

n = 5
print('n awal :', n)

n >>= 2
print('n diubah menggunakan operator >>= :', n)

# ⚡ Operator (<<=)

o = 5
print('o awal :', o)

o <<= 2
print('o diubah menggunakan operator <<= :', o)

# ⚡ Operator Walrus
'''
operator ini diperkenalkan pada python 3.8.
operator ini menetapkan nilai ke variabel sebagai bagian dari 
ekpresi
'''
daftarSobat = ['Andika', 'Bernad', 'Chia', 'Denia']
if (sobat := len(daftarSobat)) > 0:
    print(f'terdapat {sobat} sobat di dalam daftar')

