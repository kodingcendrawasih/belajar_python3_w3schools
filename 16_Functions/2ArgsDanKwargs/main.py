# 🔰🔰 *ARGS DAN *KWARGS

# ⚡ *args

def func1(*args):
    print(args)

func1('arg1', 'arg2', 'arg3')
# func1(p1='args1', p2='args2') -> error

# ⚡ **kwargs

def func2(**kwargs):
    print(kwargs)

# func2('arg1', 'arg2', 'arg3') -> error
func2(p1='args1', p2='args2') 

# ⚡ penggunaan sederhana

def jumlahkan(*angkaAngka):

    hasil = 0

    for angka in angkaAngka:
        hasil += angka

    return f'Hasil : {hasil}'

print(jumlahkan(1,4,3,2))
print(jumlahkan(2))
print(jumlahkan(1,2))

def cekAngkaTerbesar(*angkaAngka):
    if len(angkaAngka) == 0: None

    angkaTerbesar = angkaAngka[0]

    for angka in angkaAngka:
        if angka > angkaTerbesar:
            angkaTerbesar = angka

    return angkaTerbesar

print(cekAngkaTerbesar(2,1,4,21,35,21,6,3,0,23,12,))

# ⚡ Menggunakan **kwargs deng Argumen Reguler

def showTotalBelanja(namaPemesan, **hargaPerItem):

    total = 0

    for harga in hargaPerItem:
        total += hargaPerItem[harga]

    print('.' * 30)
    print('Total Pembayaran'.center(30))
    print('.' * 30)
    print(f'Atas Nama : {namaPemesan}')
    print(f'Total Pembayaran : {total:,}')



showTotalBelanja('KodingCen', item1=50000, item2=10000, item3=200000, item4=150000)

# ⚡ Menggunakan *args dan **kwargs 

def cekStatus1(namaKelompok, *namaAnggota, **poin):
    total_poin = 0

    for p in poin:
        total_poin += poin[p]
    
    print('=' * 30)
    print(f'{namaKelompok}'.center(30))
    print('.' * 30)
    print('Status :', 'Lulus') if total_poin >= 250 else print('Status :', 'Gagal')
    print('=' * 30)

cekStatus1('Kelompok1', 'Kevin', 'Karolina', 'Karlos', ct=100, komputerDasar=95, pemrogramanDasar=85)
cekStatus1('Kelompok2', 'Kevin', 'Karolina', 'Karlos', ct=90, komputerDasar=75, pemrogramanDasar=75)

# ⚡ Menggunakan *args dan **kwargs (untuk menguraikan 
#                                     list dan dict)

def showNama(nama_depan, nama_belakang):
    print('>' * 20)
    print(f'Halo {nama_depan} {nama_belakang}')
    print('<' * 20)

kamus = dict({'nama_depan':'koding', 'nama_belakang': 'cendrawasih'})
showNama(**kamus)


