# 🔰🔰 MATCH STATEMENT (PERNYATAAN MATCH)

'''
match ekpresi:
    case n1:
        blok kode
    case n2:
        blok kode
    case n3:
        blok kode
    case _: --->>>> (default jika trda case yang cocok)
        blok kode
'''

kodeHari = 6

match kodeHari:
    case 1:
        print('Hari Senin')
    case 2:
        print('Hari Selasa')
    case 3:
        print('Hari Rabu')
    case 4:
        print('Hari Kamis')
    case 5:
        print('Hari Jum\'at')
    case 6:
        print('Hari Sabtu')
    case 7:
        print('Hari Minggu')
    case _:
        print('Kode Hari Salah')

# gabung nilai

match kodeHari:
    case 1 | 2 | 3 | 4 | 5:
        print('Waktu Kerja')
    case 6 | 7:
        print('Waktu Libur')

# memeriksa deng if
mapel = 'Pemrograman'
materi = 'Python'

match mapel:
    case 'Pemrograman' if materi == 'Python':
        print('waktu belajar : senin pagi')
    case 'Pemrograman' if materi == 'JavaScript':
        print('waktu belajar : selasa pagi ')
    case 'Pemrograman' if materi == 'Go':
        print('waktu belajar : rabu pagi')
        
    