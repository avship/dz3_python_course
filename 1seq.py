n = int(input('Введите количество элементов: '))

ar = []
for i in range(n):
    ar.append(int(input(f"Введите {i} элемент: ")))
ar.sort()
print(f"Вывод: {ar}")