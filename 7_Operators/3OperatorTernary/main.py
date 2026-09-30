# 🔰🔰 OPERATOR TERNARY
'''
operator ini digunakan untuk menetapkan satu nilai
jika suatu kondisi benar, dan nilai lain jika kondisinya
salah. Operator ini bukanlah operator sungguhan, ekpresi
kondisional, atau pernyataan if yang disingkat.
'''

nama = 'KodingCendrawasih'

isAdmin = True if nama == 'KodingCen' else False
print(isAdmin)

#- bisa juga sebagai pengganti elif
isMember = True if nama == 'KodingCen' else True if nama == 'KodingCendrawasih' else False
print(isMember)