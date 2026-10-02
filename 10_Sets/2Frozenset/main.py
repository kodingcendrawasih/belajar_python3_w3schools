# 🔰🔰 FROZENSET
'''
sama seperti set, tapi de bersifat immutable,
itemnya tra bisa tong tambah atau hapus
'''

# ⚡ Membuat Frozenset
frozenset1 = frozenset({1, 2, 3, 4, 2, 3})
print('forzenset :', frozenset1, end= ' tipe -> ')
print(type(frozenset1))

# ⚡ Metode Frozenset

# 🔖 metode copy()

fsCopy = frozenset1.copy()

print('FS Copy :', fsCopy)

# 🔖 metode difference()

FSa = frozenset({1,2,3,4})
FSb = frozenset({3,4,5})

print(FSa.difference(FSb))
print(FSa - FSb)

# 🔖 metode intersection()

FSa = frozenset({1,2,3,4})
FSb = frozenset({3,4,5})

print(FSa.intersection(FSb))
print(FSa & FSb)

# 🔖 metode isdisjoint()

FSa = frozenset({1,2,3})
FSb = frozenset({4,5,6})
FSc = frozenset({1,7,8})

print(FSa.isdisjoint(FSb)) # True
print(FSa.isdisjoint(FSc)) # False

# 🔖 metode issubset()

FSa = frozenset({1,2})
FSb = frozenset({1,2,3})
FSc = frozenset({5})
FSd = frozenset({5,6})

print(FSa.issubset(FSb)) # True
print(FSa.issubset(FSc)) # False
print(FSb.issubset(FSc)) # False
print(FSc.issubset(FSd)) # True

print(FSa <= FSb) # True
print(FSa < FSb) # True

# 🔖 metode issuperset()

print(FSa.issuperset(FSb)) # False
print(FSa.issuperset(FSc)) # False
print(FSa >= FSb) # False
print(FSb > FSa) # True

