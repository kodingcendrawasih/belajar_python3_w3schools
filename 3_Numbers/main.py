# 🔰🔰 PYTHON NUMBERS

'''
python memiliki 3 jenis data angka
- int (Integer) :
    int adalah bilangan bulat, positif atau negatif
    tanpa desimal, deng panjang yang trada batas
- float (Floating-Point) :
    float adalah nilangan positif atau negatif yang 
    menggandung satu atau lebih angka desimal.
- complex (kompleks) :
    bilangan kompleks ditulis dengan huruf 'j' sebagai
    bagian imajiner
'''

# ⚡ int (Integer)

int1 = 10
int2 = -10
int3 = 12344567898765432123456789

print('int1 :', int1)
print('int2 :', int2)
print('int3 :', int3)

# ⚡ float (Floating-Point)

float1 = 1.0
float2 = -2.0
float3 = 3.12338202020

print('float1 :', float1)
print('float2 :',float2)
print('float3 :', float3)

# angka float juga bisa berupa angka ilmiah dengan huruf "e" -
# untuk menunjukan pangkat 10
float4 = 1e0
float5 = 1e3

print('float4 :', float4)
print('float5 :', float5)

# ⚡ complex (Kompleks)

kompleks1 = 3j
kompleks2 = -3j
kompleks3 = 3 + 5j

print('kompleks1 :', kompleks1)
print('kompleks2 :', kompleks2)
print('kompleks3 :', kompleks3)


# ⚡ Konversi Tipe Data

angka1 = 25
angka2 = 2.5
angka3 = 1j

konver1 = float(angka1) # konversi int ke float
konver2 = int(angka2) # konversi float ke int
konver3 = complex(angka1) # konversi int ke complex

print('konver1 :', konver1)
print('konver2 :', konver2)
print('konver3 :', konver3)

# ❗❗ kitong tra bisa mengkonversi bilangan kompleks -
#    ke bilangan lain

# konver4 = int(angka3) -> error
# print('konver4 :', konver4) -> error

# ⚡ Membuat Angka Acak
#-- python tra pu fungsi random() untuk membuat angka acak.
#   tapi de pu modul bawaan yang bisa kitong gunakan
import random

print(random.randrange(1, 10))

