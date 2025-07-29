# List методы
# list.append(x), list.count(x), list.sort([key=функция]), list.clear(), list.reverse()
# ,'kiwi','tagerine',
from operator import index
from typing import Any

list = ['apple','orange','banana','pinapple']

list.append('kiwi')	#Добавляет элемент в конец списка
vegetables = ['potato','carrot']
list.extend(vegetables)	#Расширяет список list, добавляя в конец все элементы списка L
list.insert(1, 'tagerine')	#Вставляет на i-ый элемент значение x
list.remove('banana')	#Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
list.pop(3)	#Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
index_l = list.index('potato', 1,5)	#Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
#print(index_l)
list.append('orange')
list_count = list.count('orange')	#Возвращает количество элементов со значением x
#print(list_count)

#list.sort(reverse=True)	# Сортирует список на основе функции
list.reverse()	#Разворачивает список

list_copy = list.copy()
print(list_copy)

# list.copy()	#Поверхностная копия списка
# list.clear()	#Очищает список
list.clear()
print(list)
print(list_copy)


# Dict
# dict.items(), dict.values(), dict.keys(), dict.update([other]), dict.copy()

person = {'name': 'Garry', 'age': 15, 'city': 'London', 'surname': 'Potter'}
# dict.copy() - возвращает копию словаря.
dict_copy = person.copy()
print(dict_copy)
# classmethod dict.fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value (по умолчанию None).
dict_fromkeys = dict.fromkeys(list_copy,10)
print(dict_fromkeys)
# dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).
print(person.get('name'))

# dict.items() - возвращает пары (ключ, значение).
print(person.items())
# dict.keys() - возвращает ключи в словаре.
print(person.keys())
# dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).
print(person.items())
# dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.
# dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ со значением default (по умолчанию None).
# dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
# dict.values() - возвращает значения в словаре.


# Set
# set.copy(), set.add(elem), set.remove(elem), set.clear(), set.union(other, ...)
set_fruts= set()
set_fruts = {'apple','orange','banana','pinapple'}

list = ['apple','orange','banana','pinapple','banana']
set_fruts = set(list)
print(len(set_fruts))
print('carrot' in set_fruts)
set_vegetables = {'potato','carrot','banana'}
print(set_fruts.isdisjoint(set_vegetables))
print(set_fruts == set_vegetables)
set_round_fruts = {'apple','orange'}
print(set_fruts.issuperset(set_round_fruts))
print(set_fruts.issubset(set_round_fruts))
set_products = set_fruts.union(set_vegetables)
print(set_products)
set_products = set_fruts.intersection(set_vegetables)
print(set_products)
set_products = set_fruts.difference(set_vegetables)
print(set_products)
set_products.update(set_vegetables)
print(set_products)
set_round_fruts.difference_update(set_vegetables)
print(set_round_fruts)
set_round_fruts.add('banana')
print(set_round_fruts)
set_round_fruts.pop()
print(set_round_fruts)

# Str
# S.split(символ), S.replace(шаблон, замена), len(S), S.join(список), S.lower()

str_word = 'banana'
print(str_word.upper())
str_word = ' banana    '
print(str_word.strip())
str_word = 'banana'
print(str_word.replace('ban', 'lal'))
str_word = 'banana'
print(len(str_word))
list = ['apple','orange','banana','pinapple']
print(';'.join(list))
