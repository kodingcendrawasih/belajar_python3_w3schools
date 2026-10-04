# 🔰🔰 GENERATOR FUNCTION (FUNGSI GENERATOR)

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

# ⚡ Kata Kunci Yield

def count_up_to(n):
    count = 10

    while count <= n:
        yield count
        count += 10

for num in count_up_to(50):
    print(num)


def large_sequence(n):
    for i in range(n):
        yield i

gen = large_sequence(15000000000)
print(next(gen))
print(next(gen))
print(next(gen))

def simple_gen():
    yield 'Python'
    yield 'JavaScript'
    yield 'C++'

gen = simple_gen()

print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) >>> error : StopIteration

# ⚡ EKpresi Generator

gen_exp = (x * x for x in range(3))

print(gen_exp)
print(list(gen_exp))

total = sum(x * x for x in range(3))
print(total)

# ⚡ Generator Deret Fibonancci

def fibonancci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonancci()

print('--------------')
for _ in range(10):
    print(next(gen))
print('--------------')

# ⚡ Metode Generator

# 🔖 metode send()

def echo_generator():
    while True:
        recevied = yield
        print('Received :', recevied)

gen = echo_generator()
next(gen)
gen.send('Python')
gen.send('Py')

# 🔖 metode close()

def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print('Generator Closed')

gen = my_gen()
print(next(gen))
gen.close()

