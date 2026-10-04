# 🔰🔰 REKURSI

counter = 5
while counter >= 1:
    print(counter)
    counter -= 1

print('seles!')

def hitungMundur(n):
    if n <= 0:
        print('seles!!')
    else:
        print('hitung mundur', n)
        hitungMundur(n - 1)

hitungMundur(5)

# ⚡ Kasus Dasar (Base Case) dan Kasus Rekursif (Recursif Case)

'''
kalo trda kedua kasus dasar ata base case, kitong akan
masuk ke dalam perulangan tanpa henti yang menyebabkan 
stack overflow.
'''

def faktorial(n):
    # base case
    if n == 0 or n == 1:
        # print(1)
        return 1
    # rekursif case
    else:
        # faktorial(n - 1)
        # print(f'Faktorial : {n}')
        return n * faktorial(n - 1)

# faktorial(5)
print('Faktorial 5 adalah', faktorial(5))

def fibonancci(n):
    if n <= 1:
        return n
    else:
        return fibonancci(n - 1) + fibonancci(n - 2)

print('Fibonacci dari 7 adalah', fibonancci(7))  


# ⚡ Rekursi Dengan List

def sum_list(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + sum_list(nums[1:])

my_list = [1,2,3,4]
print(sum_list(my_list)) # 10

def find_max(nums):
    if len(nums) == 1:
        return(nums[0])
    else:
        max_of_rest = find_max(nums[1:])

        return nums[0] if nums[0] > max_of_rest else max_of_rest

my_list = [3,2,6,7,3,9,2,1,2]
print(find_max(my_list)) # 9

# ⚡ Batas Kedalaman Rekursi
import sys 
# sys.setrecursionlimit(20032524624642642642246000)
sys.setrecursionlimit(10)
print(sys.getrecursionlimit())

