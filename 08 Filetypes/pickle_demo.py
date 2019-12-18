# пример использования https://pythonworld.ru/moduli/modul-pickle.html
# очень интересная техническая статья о небезопасностях pickle https://habr.com/ru/company/otus/blog/353480/
import pickle
import json

data = {(1, 2020): [1, 2, 3, 4, 5, 6, 7, 8],
        (2, 2020): [22, 23, 24]}

with open("dump.json", "w") as f:
    try:
        json.dump(data, f)
    except Exception as e:
        print(e)

# формат записи - обязательно бинарный
with open("dump.pickle", "wb") as f:
    pickle.dump(data, f)

with open("dump.pickle", "rb") as f:
    data_json= pickle.load(f)
    print(data_json)

json_data = {"1": [1,2, "3"]}
with open("dump2.json", "w") as f:
    f.write(json.dumps(json_data, indent=2, ensure_ascii=False, errors="ignore"))