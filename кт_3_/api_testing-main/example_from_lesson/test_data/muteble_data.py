a = 1
b = a
a += 1
print(a, b)

list1 = [1, 2, 3, 4]
list2 = list1
list2.append(5)
print(list1)
print(list2)

from copy import copy, deepcopy

list3 = [1, 2, 3, 4]
list4 = copy(list3)
list4.append(5)
print(list3)
print(list4)

my_dict = {'a': 1, 'b': {'c': 2}}
my_dict2 = copy(my_dict) # deepcopy
my_dict2['b']['c'] = 3
print(my_dict)
print(my_dict2)
