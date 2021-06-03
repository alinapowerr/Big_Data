"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

# input_inf = input("Введите данные: ")
# with open("File", "w") as file:
#     while input_inf:
#         file.write(input_inf+'\n')
#         input_inf = input("Введите данные: ")

"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
"""

# with open("File") as file:
#     file_lines = file.readlines()
#     print("Количество строк: ", len(file_lines))
#     for line_number, line in enumerate(file_lines, 1):
#         print(f"Количество слов в строке {line_number}", len(line.split()))

"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
"""

# sum = 0
#
# with open("File2") as file:
#     lines = file.readlines()
#     for line in lines:
#         name, salary = line.split()
#         sum += int(salary)
#         if int(salary) < 20000:
#             print("Имеет оклад менее 20 тыс.: ", name)
#
#     print("Средняя велечина дохода сотрудников: ", sum/len(lines))

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""

# my_dict = {"One": "Один",
#            "Two": "Два",
#            "Three": "Три",
#            "Four": "Четыре"}
#
# with open("File3") as file_read, open("File3_new", "w") as file_write:
#     for line in file_read.readlines():
#         text_number, number = line.rstrip().split(' - ')
#         file_write.write(f'{my_dict[text_number]} - {number}\n')


"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

# with open("File4", "w") as file_write:
#     input_numbers = input("Введите числа через пробел: ")
#     print(input_numbers, file=file_write)
#
# with open("File4") as file:
#     content_list = file.read().rstrip().split()
#     numbers_list = [int(number) for number in content_list if number.isdigit()]
#     print("Сумма чисел в файле: ", sum(numbers_list))

"""
6. Необходимо создать (не программно) текстовый файл, 
где каждая строка описывает учебный предмет и наличие лекционных, 
практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

# result_dict = {}
# with open("File5") as file:
#     for line in file:
#         lesson_type, *lessons = line.split()
#         lesson_count = [int(lesson.rstrip('(л)(пр)(лаб)')) for lesson in lessons if lesson != '—']
#         result_dict.update({lesson_type: sum(lesson_count)})
#
# print(result_dict)

"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: 
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

# import json
#
# result_list = []
# dict_plus_profit = {}
# dict_minus_profit = {}
#
# with open("File6") as file:
#     average_profit_list = []
#     for line in file.readlines():
#         name, _, revenue, costs = line.rstrip().split()
#         profit = int(revenue) - int(costs)
#         if profit > 0:
#             average_profit_list.append(profit)
#             dict_plus_profit.update({name: profit})
#         else:
#             dict_minus_profit.update({name: profit})
#         result_list.append(dict_plus_profit)
#         result_list.append(dict_minus_profit)
#         result_list.append({"average_profit": sum(average_profit_list)/len(average_profit_list)})
#
# with open("File6.json", "w") as file:
#     json.dump(result_list, file)

