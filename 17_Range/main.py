# 🔰🔰 RANGE (RENTANG)

# sintaks : range(start, stop, step)

n = range(3)

print(n)
print(list(n))

o = range(1, 10, 2)

print(o)
print(list(o))

i = range(10, 1, -2)

print(i)
print(list(i))

n = range(2)

for i in n:
    print('i :', i)

o = list(range(1, 10, 2))

print('o :', o)
print('o index 0 :', o[0])
print('o[:3] :', o[:3])
print('angka 3 di variabel o :', 3 in o)
print('panjang variabel o :', len(o))

