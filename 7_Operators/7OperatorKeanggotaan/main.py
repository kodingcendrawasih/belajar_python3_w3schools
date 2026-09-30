# 🔰🔰 OPERATOR KEANGGOTAN
'''
operator ini digunakan untuk menguji apakah suatu nilai 
de terdapat di dalam sebuah objek
'''

# ⚡ in
daftarSobat = ['Andika', 'Bernika', 'Chika', 'Denia']
sobat = 'Denis'
print(sobat in daftarSobat) # False -> sobat trada dalam daftar

# ⚡ not in
print(sobat not in daftarSobat) # True -> sobat trada dalam daftar

# ⚡ mengecek apakah sebuah kata ada dalam string
teks = 'a love python3 oh, love yang awas punya'
cekKata = 'python'

print(cekKata in teks) # True
print(cekKata not in teks) # False