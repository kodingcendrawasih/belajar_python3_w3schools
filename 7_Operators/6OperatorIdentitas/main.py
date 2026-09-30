# 🔰🔰 OPERATOR IDENTITAS
'''
Operator ini digunakan untuk membandingkan objek, apakah
objek tersebut sama bukan hanya nilai tapi de pu lokasi di
memori. berbeda deng (==) yang membandingkan nilai
'''

n = ['101', '102']
o = ['101', '102']
i = n

print(n is o) # False
print(n is i) # True
print(n == o) # True
print(n is not o) # True
# print(n not is o) # error
