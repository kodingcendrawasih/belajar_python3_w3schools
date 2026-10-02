# 🔰🔰 PERULANGAN WHILE (WHILE LOOP)

counter = 1
while counter <= 5:
    print('Perulangan ke -', counter)
    counter += 1
print('Perulangan selesai')

# ⚡ Loop tak terbatas (infinite loop) 

# while True:
#     print('Perulangan tak terbatas')  

# ⚡ break statement

counter = 1
while counter <= 5:
    print('Perulangan ke -', counter)
    if counter == 3:
        print('Perulangan dihentikan')
        break
    counter += 1
print('Perulangan selesai')

# ⚡ continue statement

counter = 0
while counter < 5:
    counter += 1
    if counter == 3:
        continue
    print('Perulangan ke -', counter)   
print('Perulangan selesai')

# ⚡ else statement
counter = 1
while counter <= 5:
    print('Perulangan ke -', counter)
    counter += 1    
else:
    print('Perulangan selesai')


