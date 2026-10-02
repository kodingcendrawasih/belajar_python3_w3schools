# #🧶🎫🚀🔰🔰⚡🏷🔖📖🚩❗✔❌ 
# 🔰🔰 FUNCTION (FUNGSI)

# ⚡ Membuat Fungsi

def myFunc():
    print('ditampilkan melalui fungsi')

# ⚡ Memanggil / Menjalankan Fungsi
myFunc()

#- memanggil fungsi berkali-kali
myFunc()
myFunc()
myFunc()

# ⚡ Penamaan Fungsi
'''
- nama harus diawali deng huruf atau garis bawah
- nama hanya boleh berisi huruf, angka atau garis bawah
- nama case sensitive
- nama harus deskriptif
contoh :
    >> tampilkanNama()
    >> tampilkan_nama()
    >> _fungsi_privat()
'''

def celciusKeFarenheit(celcius):
    print(f'{celcius} Celcius >>> Farenheit : {(celcius * 1.8 + 32):.0f}')

celciusKeFarenheit(20)
celciusKeFarenheit(22)
celciusKeFarenheit(47)

# ⚡ Return Value

def sayHai():
    return 'Hai'

say_hai = sayHai()
print(say_hai)
print(sayHai())

# ⚡ Pass

def f1():
    pass # dieksekusi

# def f2(): >>> error
#     # pass -> tidak dikesekusi


