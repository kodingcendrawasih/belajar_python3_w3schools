# 🔰🔰 DATETIME (TANGGAL dan Waktu)

# ⚡ DateTime Modul Bawaan Python
import datetime as dt

# ⚡ Mendapatkan Tanggal dan Waktu Saat Ini
tanggalSekarang = dt.datetime.now()

print('waktu sekarang :', tanggalSekarang)

# 🔖 kembalikan tahun dan nama hari dalam seminggu

t = dt.datetime.now()

print('tahun sekarang :', t.year)
print('bulan sekarang :', t.month)
print('hari sekarang :', t.day)
print('nama hari :', t.strftime("%A"))
print('nama bulan :', t.strftime("%B")) 

# 🔖 membuat objek tanggal

# setWaktu = dt.datetime(2026, 9, 19)
setWaktu = dt.datetime(2026, 10, 4)
print('set waktu :', setWaktu)

# ⚡ Metode srtftime() 

# 🔖 kode format %A
print('kode format %A untuk nama hari (full):', t.strftime("%A"))

# 🔖 kode format %a 
print('kode format %a untuk nama hari (singkat):', t.strftime("%a"))

# 🔖 kode format %B
print('kode format %B untuk nama bulan (full):', t.strftime("%B"))

# 🔖 kode format %b
print('kode format %b untuk nama bulan (singkat):', t.strftime("%b"))

# 🔖 kode format %c
print('kode format %c untuk tanggal dan waktu:', t.strftime("%c"))

# 🔖 kode format %C
print('kode format %C untuk abad (2 digit):', t.strftime("%C"))

# 🔖 kode format %d
print('kode format %d untuk tanggal:', t.strftime("%d"))

# 🔖 kode format %m
print('kode format %m untuk bulan:', t.strftime("%m"))

# 🔖 kode format %y
print('kode format %y untuk tahun (2 digit):', t.strftime("%y"))

# 🔖 kode format %Y
print('kode format %Y untuk tahun (4 digit):', t.strftime("%Y"))

# 🔖 kode format %M
print('kode format %M untuk menit:', t.strftime("%M"))

# 🔖 kode format %S 
print('kode format %S untuk detik:', t.strftime("%S"))

# 🔖 kode format %x
print('kode format %x untuk tanggal (locale):', t.strftime("%x"))

# 🔖 kode format %X
print('kode format %X untuk waktu (locale):', t.strftime("%X"))

# 🔖 kode format %%
print('kode format %% untuk tanda persen:', t.strftime("%%"))

# 🔖 kode format %G
print('kode format %G untuk tahun ISO 8601:', t.strftime("%G"))

# 🔖 kode format %V
print('kode format %V untuk nomor minggu ISO 8601:', t.strftime("%V"))

# 🔖 kode format %u
print('kode format %u untuk nomor hari dalam seminggu (1-7):', t.strftime("%u"))