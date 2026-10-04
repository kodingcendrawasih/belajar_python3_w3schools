# 🔰🔰 RegEx (Regular Expression)

# Modul RegEx
import re

kalimat = 'a love python'
hasil = re.search('^a.*python$', kalimat)

print('hasil :', hasil)

if hasil:
    print('Hasil : benar, kalimat diawali ' \
    'dengan \n\t\thuruf a ' \
    'dan diakhiri dengan kata' \
    ' python')

# ⚡ Fungsi RegEx

# 🔖 metode findall() >>> list

str1 = 'belajar python bersama w3schools'
hasilFindAll = re.findall('python', str1)
print('Hasil FindAll :', hasilFindAll)

# 🔖 metode search() >>> objek match

hasilSearch = re.search('python', str1)
print(hasilSearch) # >>> Math object
print('Hasil Search :', hasilSearch.start()) # >>> posisi index 

# 🔖 metode split() >>> list

hasilSplit = re.split(r'\s', str1)
print('Hasil Split:', hasilSplit)

# 🔖 metode sub() >>> str

hasilSub = re.sub(r'\s', '-', str1)
print('Hasil Sub :', hasilSub)

# ⚡ Meta Karakter

# 🔖 [] >>> Set Karakter

str2 = 'Belajar Python'
hasilSetKar = re.findall('[a-g]', str2)
print('Hasil Set Karakter :', hasilSetKar)

# 🔖 \ >>> Escape / Urutan Khusus

str3 = 'umur saya 25 tahun'
hasilEscape = re.findall(r'\d', str3)
print('Hasil Escape :', hasilEscape)

# 🔖 . >>> Karakter Apa Saja

hasilKarBebas = re.findall('py...n', str1)
print('Hasil Karakter Apa Saja :', hasilKarBebas)

# 🔖 ^ >>> Diawali Dengan Pola Tertentu

# hasilAwalPola = re.findall('^Bel', str1)
hasilAwalPola = re.findall('^bel', str1)
print('Hasil Diawali Dengan :', hasilAwalPola)

# 🔖 $ >>> Diakhiri Dengan Pola Tertentu
hasilAkhirPola = re.findall('w3schools$', str1)
print('Hasil Diakhiri Dengan :', hasilAkhirPola)

