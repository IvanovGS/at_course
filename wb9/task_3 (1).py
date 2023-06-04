# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open(r'C:\my_git\wb9\test_file\task_3.txt', 'r', encoding='utf-8') as f:
    my_last_list, count = [], 0
    for i in f:
        if i != '\n':
            count += int(i[:-1])
        else:
            my_last_list.append(count)
            count = 0
            continue
    three_most_expensive_purchases = sum((sorted(my_last_list))[-3:])

assert three_most_expensive_purchases == 202346
print('Все ок')
