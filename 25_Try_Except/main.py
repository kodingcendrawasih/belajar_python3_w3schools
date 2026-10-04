# #🧶🎫🚀🔰🔰⚡🏷🔖📖🚩❗✔❌
# 🔰🔰 TRY EXCEPT

# print(x)  error 
# print('tidak akan ditampilakan karena program terhenti')

try:
    print(x)
except:
    print('variabel belum didefinisikan')

print('Tampil!!!, karena error ditangani')

# print(n) -> nama error -> NameError 

# menangani NameError Secara Khusus

try:
    print('string' + 12)
except NameError:
    print('Ups! Variabel Belum Ada...')
except:
    print('Hmm, Nampaknya Ada Error Lain...')

# "else" untuk menangani jika trada kesalahan

try:
    print('Hai Python')
except:
    print('ups! ada error')
else:
    print('Trada Error')

# finally, berjalan tra peduli erorr kh trada

try:
    print('kode aman')
except:
    print('ada masalah')
finally:
    print('Berhasil Melakukan Pengecekan Kode')

