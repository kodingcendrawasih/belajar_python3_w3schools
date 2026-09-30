# 🔰🔰 Karakter Escape

r'''
terkadang kitong perlu menyisipkan beberapa karakter kedalam string,
tapi de pu masalah, karakter yang ingin tong masukan itu dianggap
ilegal atau tra sah. Nah, Karakter Escape ini akan mengatasi hal tersebut.
de pu cara penggunaan simple, tinggal kasih backslash (\) barang de aman.
('r' diatas agar komentar ini tra error karna sz ada pake tanda backslash)
'''

# misalnya tanda kutip tunggal di dalam string yang diapit oleh
# kutip tunggal. jika tong paksa taruh akan, python akan mengembalikan error
# print('jum'at') -> error
print('jum\'at')

# ⚡ Baris Baru (\n)
print('----------')
print('Belajar\nPython3')
print('----------')

# ⚡ Tab Horizontal (\t)
print('Belajar\tPython')

# ⚡ Backslash (\\)
print('C:\\KodingCendrawasih\\belajar_python3\\w3schools')

# ⚡ Backspace (\b)
print('Pythoo\bn3') # di vscode akan menampilkan [esc], jalan di terminal 
#                     kalo mu liat de hasil

# ⚡ Carriage Return (\r)
print('Hai\rPython3') # hai akan dihapus

# ⚡ (\ooo) : untuk menampilkan niali dari bilangan oktal
print('\110\141\154\154\157')

# ⚡ (\hxx) : untuk menampilkan niali dari bilangan hex
print('\x48\x61\x6c\x6f')

