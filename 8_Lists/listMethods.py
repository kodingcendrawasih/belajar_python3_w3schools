# 🔰🔰 Metode Pada Daftar (List)
#- append()
list1 = [1,2]
list1.append(3)
print(list1)

#- clear()
list1.clear()
print(list1)

#- copy()
list1 = [1,2]
list2 = list1.copy()
print(list2)

#- count()
list1 = [1,2,3,1,4,6,4,2,1,1,6]
print(list1.count(1))

#- extend()
list1 = ['a', 'b']
list2 = ['c', 'd']
list1.extend(list2)
print(list1)

#- index()
list1 = ['a', 'b', 'c']
# print(list1.index(4)) -> error
print(list1.index('b'))

#- insert()
list1 = ['a', 'b', 'c']
list1.insert(1, 'd')
print(list1)

#- pop()
list1 = ['a', 'b', 'c']
list1.pop()
print(list1)

#- remove()
list1 = ['a', 'b', 'c']
list1.remove('b')
print(list1)

#- reverse()
list1 = ['a', 'b', 'c']
list1.reverse()
print(list1)

#- sort()
list1 = ['c', 'b', 'a', 'e', 'd']
list1.sort()
print(list1)