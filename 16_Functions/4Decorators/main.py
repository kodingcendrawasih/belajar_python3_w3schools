# 🔰🔰 DECORATOR (DEKORATOR)

def ubahHuruf(fungsi):
    def keLower():
        return fungsi().lower()
    return keLower

@ubahHuruf
def f1():
    return 'PYTHON'

@ubahHuruf
def f2():
    return 'JAVASCRIPT'

print(f1())
print(f2())

def gandakan(fungsi):
    def angkaAngka(n):
        return fungsi(n) * 2

    return angkaAngka

@gandakan
def f3(n):
    return n

print(f3(5))
# print(f3(5. 2, 3)) >>> error

def changecase(func):
    def toUpper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return toUpper

@changecase
def myFunc1(string):
    return string

print(myFunc1('belajar python bersama w3schools'))

# ⚡ Dekorator Deng Argumen

def ubahhuruf(ke):
    def ubahhuruf(fungsi):
        def ubahKe():
            if ke == 'lower':
                n = fungsi().lower()
            elif ke == 'upper':
                n = fungsi().upper()

            return n
        return ubahKe
    return ubahhuruf

@ubahhuruf('upper')
def fungsi1():
    return 'python3'

print(fungsi1())

@ubahhuruf('lower')
def fungsi2():
    return 'PYTHON3'

print(fungsi2())

# ⚡ Beberapa Dekorator

def changeCase(func):
    def innerFunc():
        return func().title()

    return innerFunc()

def addGreeting(func):
    def innerFunc():
        return f'hai {func()}, have a good day'

    return innerFunc

@changeCase
@addGreeting
def func1():
    return 'KODINGCEN'

print(func1)

# ⚡ Mempertahankan Metadata Fungsi

# 🔖 nama fungsi dapat dikembalikan

def sayhai(nama):
    print('Hai', nama)

print('Nama Fungsi di Atas :', sayhai.__name__)

'''
tapi klo fungsi tersebut dikasih dekorasi
metadata-nya akan hilang
'''
# def CHANGECASE(func):
#     def inner_func():
#         return func().lower()
#     return inner_func

# @CHANGECASE
# def myFUNC():
#     return 'W3SCHOOLS'

# print(myFUNC.__name__) # >>> inner_func

# 🔖 Mempertahankan Nama Fungsi dan DocString Asli

import functools

def CHANGECASE(func):
    @functools.wraps(func)
    def inner_func():
        return func().lower()
    return inner_func

@CHANGECASE
def myFUNC():
    return 'W3SCHOOLS'

print(myFUNC.__name__) # >>> myFUNC


