
ar1 = list(map(int, input('Введите элементы первого списка: ').split(',')))
ar2 = list(map(int, input('Введите элементы второго списка: ').split(',')))


print("Результат:", ",".join([str(i) for i in ar1 if not i in ar2]))