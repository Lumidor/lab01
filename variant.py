zakaz = input('Введите название заказа:')
ima = input('Введите имя заказчика:')
poz1 = input('Введите название позиции 1:')
klv1 = int(input('Введите количество товара в позиции:'))
zena1 = float(input('Введите цену одного товара в рублях:'))
poz2 = input('Введите название позиции 2:')
klv2 = int(input('Введите количество товара в позиции:'))
zena2 = float(input('Введите цену одного товара в рублях:'))
dost = float(input('Введите стоимость доставки:'))
vneseno = float(input('Введите внесенную стоимость:'))
stoim1 = zena1*klv1
stoim2 = zena2*klv2
stoim12 = stoim1+stoim2
stoim12dost = stoim12+dost
klv12 = klv1+klv2
sdacha = vneseno-stoim12dost
if klv1 >= 0 and klv2 >= 0 and zena1 >= 0 and zena2 >= 0 and dost >= 0 and vneseno >= stoim12dost:
    print(f'Заказ: {zakaz}')
    print(f'Имя заказчика: {ima}')
    print(poz1, klv1, zena1, stoim1, sep = " | ")
    print(poz2, klv2, zena2, stoim2, sep = " | ")
    print(f'Общая стоимость позиций: {(stoim12):.2f}')
    print(f'Стоимость с доставкой: {(stoim12dost):.2f}')
    print(f'Кол-во товаров: {klv12}')
    print(f'Сдача: {(sdacha):.2f}')
else:
    print('У вас где-то указано отрицательное число или внесенная сумма меньше стоимости')

