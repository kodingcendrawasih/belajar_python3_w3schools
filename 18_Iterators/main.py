# 🔰🔰 ITERATORS (Iterasi)

'''
iterators adalah objek yang dapat diulang (iterable) dan dapat 
digunakan untuk mengakses elemen-elemen dari koleksi data satu per satu.
'''

myTuple = ("apple", "banana", "cherry")
# create an iterator from the tuple
itereasi = iter(myTuple)

# access the elements one by one
print(next(itereasi))  # Output: apple
print(next(itereasi))  # Output: banana
print(next(itereasi))  # Output: cherry

str1 = "Python"

# create an iterator from the string
itereasi_str = iter(str1)

# access the characters one by one
print(next(itereasi_str))  # Output: P
print(next(itereasi_str))  # Output: y 
print(next(itereasi_str))  # Output: t
print(next(itereasi_str))  # Output: h
print(next(itereasi_str))  # Output: o
print(next(itereasi_str))  # Output: n
# print(next(itereasi_str))  # Output: StopIteration error

# ⚡ Membuat Iterator

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter), end = ' | ')  # Output: 1   
print(next(myiter), end = ' | ')  # Output: 2
print(next(myiter), end = ' | ')  # Output: 3
print(next(myiter), end = ' | ')  # Output: 4
print(next(myiter), end = ' | ')  # Output: 5
print(next(myiter), end = ' | ')  # Output: 6
print(next(myiter), end = ' | ')  # Output: 7
print(next(myiter), end = ' | ')  # Output: 8
print(next(myiter), end = ' | ')  # Output: 9
print(next(myiter))  # Output: 10

# for x in myiter:
#     print(x)   >>> looping forever

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)


for x in myiter:
    print(x, end = ' | ')  # Output: 1 | 2 | 3 | 4 | 5 |

