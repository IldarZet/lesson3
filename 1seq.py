numbers = []
count = int(input('Введите количество элементов: '))

for i in range(1, count + 1):
    numbers.append(int(input('Введите ' + str(i) + ' элемент: ')))
    
numbers.sort()
print(numbers)