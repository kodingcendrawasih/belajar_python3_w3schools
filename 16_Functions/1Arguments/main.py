# 🔰🔰 ARGUMENTS (ARGUMEN)

def sayHai(nama):
    print(f'hai {nama}, poster...')

# sayHai() -> error
sayHai('KodingCen')

# ⚡ Perbedaan Argumen dan Parameter

# cara baca : buat fungsi say_hai deng parameter nama
def say_hai(nama): # -> disini ia disebut parameter
    print('hai', nama) 

say_hai('Andika') # -> disini ia disebut argumen 
# cara baca : jalankan fungsi say_hai deng argumen 'Andika'

def jumlahkan(num1, num2):
    return num1 + num2

# jumlah1 = jumlahkan(2) -> error -> butuh 2 argumen
penjumlahan_1 = jumlahkan(2, 3)
print('Hasil :', penjumlahan_1)

# ⚡ Nilai Parameter Default

def sapa(nama='anonymous'):
    print('Hai', nama)

sapa()

# ⚡ Keyword Arguments (Argumen Kata Kunci) 

def f1(p1, p2, p3):
    print(f'{p1} | {p2} | {p3}')

f1(p2='arg2', p3='arg3', p1='arg1') # urutan tra masalah

# ⚡ Positional Arguments (Argumen Posisional)

f1('ar2', 'ar3', 'arg1') 


# ⚡ Mencampur Argumen Posisi dan Argumen Kata Kunci

f1('arg1', p3='arg3', p2='arg2') # urutan pertama keyword, 
#                                  berikutnya positional.
# f1(p3='arg3', p2='arg2', 'arg1') -> error

# ⚡ Return Mengembalikan Segalanya

def fRetList():
    return []

def fRetTuple():
    return ()

def fRetSet():
    return set()

def fRetDict():
    return dict()


print(fRetDict())
print(fRetList())
print(fRetTuple())
print(fRetSet())

# ⚡ Menetapkan Argumen Hanya Boleh Argumen Posisional

def funcPos(nama, /):
    print('Haooooo', nama)

funcPos('sobat')
# funcPos(nama='ferlin') error

# ⚡ Menetapkan Argumen Hanya Boleh Argumen Kata Kunci

def funcKeyWord(*, nama):
    print('Haoo', nama)

# funcKeyWord('sobat') -> error
funcKeyWord(nama='ferlin') 

