numbers = {}

flag = False
s = input("Введите элементы списка через запятую: ")
for sep in ",;/":
    try:
        for num in list(map(int, s.split(sep))):
            num = int(num)
            numbers[num] = numbers.get(num, 0) + 1

        print("Результат:", " ".join([str(key) for key,value in numbers.items() if value == 1]))
        flag = True
        break
    except Exception as err:
        continue
if not flag:
    print('Разделитель один из списка: ,;/')


