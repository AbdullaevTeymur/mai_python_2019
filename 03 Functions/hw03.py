# ==================
# ДЗ №3: функции
# Дедлайн: 04 ноября 18:14
# Результат присылать на адрес nike64@gmail.com

# также прочитайте раздел "Функции" из книги "A byte of Python" (с.59)

# Задание: сделайте анализ возрастного состава группы студентов, используя функции.
# Помните, что а) у некоторых студентов отсутствуют данные по возрасту, б) возраст может быть задан диапазоном, например, 25-35. Поэтому не забывайте обрабатывать ошибки и исключения!

import csv

# помним, что в этот раз мы читаем не список списков, а список словарей!
# ключи в словаре для каждого студента называются по первой строчке из файла student_ages.csv: "Номер в списке", "Возраст"
ages_list = list()
with open('ages.csv', encoding="utf-8-sig") as csvfile:
    ages_dictreader = csv.DictReader(csvfile, delimiter=',')
    ages_list = list(ages_dictreader)

# подсказка: вот так мы можем получить данные из списка словарей
# именно так мы уже делали в коде лекции с квартирами
for al in ages_list:
    print(f'"Номер в списке": {al["Номер в списке"]}, "Возраст": {al["Возраст"]}')


# Задание 1: напишите функцию, которая разделяет выборку студентов на две части: меньше или равно указанного возраста и больше указанного возраста
# вернуться должна пара "Номер в списке, Возраст"
def filter_students_1(age):
    under_list = list()
    upper_list = list()
    unknownage_count = 0

    # TODO 1: напишите ваш код проверки.
    # не забудьте исключить студентов, у которых возраст не указан, и подсчитать их количество
    for al in ages_list:
        try:
            if al["Возраст"] == '':
                raise IndexError("Студент не указал свой возраст")
            if int(al["Возраст"]) <= age:
                under_list.append(al)
            else:
                upper_list.append(al)
        except:
            unknownage_count += 1
            continue


    # возвращаем результат из функции:
    return under_list, upper_list, unknownage_count


# вызываем функцию:
und_list, upp_list, unknwncount = filter_students_1(30)
# TODO 2: выведите результат:
print("Студенты с возрастом не более 30:")
for student in und_list:
    print(f"'Номер в списке': {student['Номер в списке']}, 'Возраст': {student['Возраст']}")

print("Студенты с возрастом более 30:")
for student in upp_list:
    print(f"'Номер в списке': {student['Номер в списке']}, 'Возраст': {student['Возраст']}")

print(f"Количество студентов, не указавших возраст {unknwncount}")

# Задание 2: улучшите функцию filter_students_1
# напишите функцию, которая принимает переменное количество параметров, каждый из которых может быть необязательным:
# Список и пример передачи параметров: age=30, warn=True, show_average=True
# 1) warn=True (False) - параметр, указывающий, что делать со студентами, которые не указали возраст:
# если возраст не указали значительно большее количество студентов, чем указали, выводите дополнительно предупреждение, что выборка неточная
# 2) show_average=True (False) нужно ли подсчитать и отобразить средний возраст студента.

# все параметры передавайте как **kwargs, т.е. пару "название параметра - значение параметра"
def filter_students_2(**kwargs):
    under_list = list()
    upper_list = list()
    unknownage_count = 0

    # TODO 3: получите остальные два параметра по аналогии:
    warn_if_toomany = kwargs.get("warn")
    age = kwargs.get("age")
    show_average = kwargs.get("show_average")

    if age is None:
        print("Забыли указать проверяемый возраст")
        return

    # TODO 4: скопируйте сюда текст функции filter_students_1, которую вы написали ранее, и измените ее так, чтобы она работала с параметрами **kwargs
    for al in ages_list:
        try:
            if al["Возраст"] == '':
                raise IndexError("Студент не указал свой возраст")
            if int(al["Возраст"]) <= age:
                under_list.append(al)
            else:
                upper_list.append(al)
        except:
            unknownage_count += 1
            continue

    # TODO 5: сделайте проверку. Если значение параметра warn, show_average = True, выполните соответствующую обработку. Например:
    if warn_if_toomany == True:
        # напишите здесь код проверки и вывод предупреждающего сообщения пользователю
        if (unknownage_count > len(und_list) + len(upper_list)):
            print("Возраст не указали значительно большее количество студентов, чем указали, "
                  "выборка неточная!")
    if show_average == True:
    # напишите здесь код подсчета и вывода среднего значения возраста студентов
        under_age = 0
        upper_age = 0

        for student in under_list:
            under_age += int(student["Возраст"])

        for student in upper_list:
            upper_age += int(student["Возраст"])

        avg_age = int((under_age + upper_age) / (len(und_list) + len(upper_list)))
        print(f"Средний возраст студента {avg_age}")

    # возвращаем результат из функции:
    return under_list, upper_list, unknownage_count


# вызываем функцию filter_students_2
und_list, upp_list, unknwncount = filter_students_2(age=30, warn=True, show_average=True)



