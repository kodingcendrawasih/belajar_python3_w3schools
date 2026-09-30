# 🔰🔰 CASTING

'''
casting kitong pake kalo ingin menentukan tipe
dari sebuah variabel. berhubung python nhi de juga
menganut paradigma OOP, kitong bisa pake fungsi kontraktor 
utnuk menangani hal tersebut
- int() :
    membuat bilangan bulat dari :
    * literal bilangan bulat, 
    * literal bilangan pecahan (akan menghilangkan semua angka 
      desimal),
    * atau literal string (asalkan, stringnya adalah bilangan bulat)
- float() :
    membuat bilangan floating-point dari,
    * literal bilangan bulat 
    * literal float
    * atau literal string (asalkan, stringnya adalah bilangan bulat atau 
      floating-point)
- str() :
    membuat string dari berbagai macam tipe data.
'''

# ⚡ int()

print('konvers ke int:', int(1))
print('konvers ke int:', int(1.2))
print('konvers ke int:', int('9'))
# print(int('4.5')) -> error
# print(int('')) -> error

# ⚡ float()

print('konvers ke float:', float(1))
print('konvers ke float:', float(1.5))
print('konvers ke float:', float('2.5'))

# ⚡ str()

print('konvers ke str:', str(1))
print('konvers ke str:', str(1.5))
print('konvers ke str:', str('2.5'))
print('konvers ke str:', str(True))
print('konvers ke str:', str(5j))
print('konvers ke str:', str(['KodingCen', 27, True]))
