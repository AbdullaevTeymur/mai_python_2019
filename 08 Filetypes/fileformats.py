# красивый вывод (с форматированием отступов)
from pprint import pprint
import sys

# CSV
# конвертируется в Excel, самый распространенный формат для публикации данных в интернет.
# удобно хранить большие файлы
# хорошая защита от потери данных, т.к. файл можно записывать построчно
import csv
with open("files/flats.csv", newline="") as datafile:
  flats_csv = csv.reader(datafile, delimiter=";")
  flats_list = list(flats_csv)
print(flats_list[:5])

def read_by_one():
  with open("files/flats.csv", newline="") as datafile:
    flats_csv = csv.reader(datafile, delimiter=";")
    for flat in flats_csv:
      yield flat

iter_flats = iter(read_by_one())
for row in iter_flats:
  print(row[0])

# csv DictReader
# https://docs.python.org/3/library/csv.html#csv.DictReader

with open("files/flats.csv", newline="") as datafile:
  flats_csv = csv.DictReader(datafile, delimiter=";")
  for i, flat in enumerate(flats_csv):
    print(flat["Метро"], flat["Количество комнат"], flat["Цена"])
    if i == 5:
      break

# csv настройка форматирования
# https://docs.python.org/3/library/csv.html#csv-fmt-params
csv.register_dialect('customcsv', delimiter=',', quoting=csv.QUOTE_ALL, quotechar='"', escapechar='\\')
with open("files/flats2.csv", "w") as datafile:
  datafile_csv = csv.writer(datafile, 'customcsv')
  datafile_csv.writerows(flats_list[:5])

# JSON
# для обмена данными с БД (BSON - для MongoDB)
# https://stackoverflow.com/questions/39719689/what-is-the-difference-between-json-load-and-json-loads-functions-in-python
# https://docs.python.org/3/library/json.html
import json
with open("files/newsafr.json") as datafile:
  json_data = json.load(datafile)
print(json_data)
pprint(json_data)

# json ensure_ascii=False - чтобы избежать сохранения кириллицы вот в таком виде:
# "\u0441\u0438\u0441\u0442\u0435\u043c\u0430 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438 \u043f\u0438\u0449\u0435\u0432\u044b\u0445 \u043a\u043e\u043c\u043f\u043e\u043d\u0435\u043d\u0442\u043e\u0432"
# прочитать вручную такую строку можно в https://dencode.com/string/unicode-escape

with open("files/newsafr2.json", "w") as datafile:
  json.dump(json_data, datafile, ensure_ascii=False, indent=2)
print(json_data)

# YAML https://pyyaml.org/wiki/PyYAMLDocumentation
# pip install pyyaml - по умолчанию в питон не включается
import yaml
with open("files/newsafr.yml") as datafile:
  yaml_data = yaml.load(datafile)
  pprint(yaml_data)

with open("files/newsafr2.yml", "w") as datafile:
  yaml.dump(yaml_data, datafile, allow_unicode=True, default_flow_style=False)

# XML
# наследие Microsoft. часто используется для обмена данными в сервисах
# и XML (и построенный на нем протокол SOAP), и JSON активно используются при создании API. но сравните читаемость и сложность в использовании: https://habr.com/company/sberbank/blog/421693/
# Центробанк РФ уже много лет отдает кучу интересных данных именно в формате XML (ресурс для самостоятельного исследования) http://cbr.ru/development/

# чтение XML
# https://docs.python.org/3/library/xml.etree.elementtree.html
# как работать с XML https://gitjournal.tech/python_xml/#_XML-4
# если парсер падает - проверьте и при необходимости исправьте кодировку файла. Кодировка в заголовке должна совпадать с фактической кодировкой. В ДЗ в файле XML записано encoding='windows-1251'. Исправить кодировку можно, например, через Notepad++
import xml.etree.ElementTree as ET
tree = ET.parse("files/newsafr.xml")
titles = []
# что такое корневой элемент xml
root = tree.getroot()
# теги и атрибуты
print(root.tag)
print(root.attrib)
# поиск в XML
xml_title = root.find("channel/title")
print(type(xml_title))
print(xml_title.text)
xml_items = root.findall("channel/item")
print(len(xml_items))
for xmli in xml_items:
  print(xmli.attrib["id"])
  # print(xmli.find("title").text)
# # ... и почему не работает вот так
# xml_items = tree.findall("rss/channel/item")

# # что такое XML DOM
# # https://ru.wikipedia.org/wiki/Document_Object_Model
# # получить значение тега <title> можно только в цикле
# for item in xml_items:
#   title = item.find("title")
#   titles += title.text.split(" ")
#   # получить значение тега - функция text
#   print(title.text, "\n")

# # функция сортировки слов в списке по длине
# # подробнее https://habr.com/post/138535/
# def sortByLength(inputStr):
#         return len(inputStr)

# titles.sort(key=sortByLength, reverse=True)
# print(titles)

# КОДИРОВКИ
# encoding="utf_8_sig"
# encoding="utf_8"
# encoding="cp1251"
