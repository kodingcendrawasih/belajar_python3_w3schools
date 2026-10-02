# 🔰🔰 FOR LOOP (PERULANGN FOR)

myList = ['Python', 'Java', 'C++', 'C#', 'JavaScript']
myTuple = ('Python', 'Java', 'C++', 'C#', 'JavaScript')
mySet = {'Python', 'Java', 'C++', 'C#', 'JavaScript'}
myDict = {'Python': 1, 'Java': 2, 'C++': 3, 'C#': 4, 'JavaScript': 5}

# 🔁 Iterasi melalui list
print('----------------------')
print(('Iterasi List'))

for item in myList:
    print(item)

print('----------------------')

# 🔁 Iterasi melalui tuple
print('----------------------')
print(('Iterasi Tuple'))

for item in myTuple:
    print(item)

print('----------------------')

# 🔁 Iterasi melalui set
print('----------------------')
print(('Iterasi Set'))

for item in mySet:
    print(item)
    
print('----------------------')

# 🔁 Iterasi melalui dictionary
print('----------------------')
print(('Iterasi Dictionary'))

for key, value in myDict.items():
    print(key, ':', value)

print('----------------------')

# ⚡ break statement

print(('Break Statement'))
print('......................')

for item in myList:
    if item == 'C++':
        break
    print(item)

# ⚡ continue statement
print('......................')
print(('Continue Statement'))

for item in myList:
    if item == 'C++':
        continue
    print(item)

# ⚡ range() function
print('......................') 
print(('Fungsi Range'))

for i in range(5):
    print(i)

# ⚡ range() with start and end
print('......................')
print(('Range dengan Start dan End'))

for i in range(2, 7):
    print(i)

# ⚡ range() with step
print('......................')
print(('Range dengan Step'))

for i in range(1, 10, 2):
    print(i)

# ⚡ else clause in for loop
print('......................')
print(('Else Clause in For Loop'))

for item in myList:
    print(item)
else:
    print('Loop selesai tanpa break')

# jika loop di break, else tidak akan dieksekusi
print('......................')
print(('Else Clause with Break'))
for item in myList:
    if item == 'C++':
        break
    print(item)
else:
    print('Loop selesai tanpa break')

# ⚡ Perluangan bersarang (Nested Loops)
print('......................')
print(('Nested Loops'))

for i in range(1, 4):
    for j in range(1, 4):
        print(f'({i}, {j})')

    
# pernyatan for tra boleh kosong
print('......................')
print(('For Loop Kosong'))

for item in myList:
    pass  # Tidak melakukan apa-apa. tapi dieksekusi