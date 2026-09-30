# 🔰🔰 OPERATOR BITWISE
'''
digunakan untuk membandingkan sebuah angak
deng cara membandingkan setiap bit
'''

# ⚡ AND (&)
n = 5
o = 3

'''
5     -> 0101
3     -> 0011
-------------- &
hasil -> 0001 = 1
'''
print(n & o) # 1

# ⚡ OR (|)

'''
5     -> 0101
3     -> 0011
-------------- |
hasil -> 0111 = 7
'''
print(n | o) # 7

# ⚡ XOR (^)

'''
7     -> 0111
5     -> 0101
-------------- ^
hasil -> 0101 = 5
'''
print(n | o) # 7

# ⚡ NOT (~)

'''
7     -> ~00000111 
hasil -> 111111000 = -8
'''
i = 7
print(~i) # -8

# ⚡ RIGHT SHIFT (>>)

i = 7
n = 2

'''
7  geser ke kanan sebanyak 2 
00000111 >> 2
00000001 = 1
'''
print(i >> n)

# ⚡ LEFT SHIFT(<<)

i = 8
n = 3
'''
8  geser ke kiri sebanyak 3
00001000 << 8
01000000 = 64
'''
print(i << n) # 64
