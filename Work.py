# подключаем стандартный модуль python, для работы с регулярными выражениями
import re
# подключаем стандартный модуль python, для работы с JSON
import json
# подключаем стандартный модуль python, для работы с датой и временем
from datetime import datetime, date

# Создаём пустой словарь для вывода остортированных сотрудников
dic1 = {}

# Открываем файл datafile.py на чтение, сорируем данные по убываню и записываем их в словарь dic1
with open("datafile.py", "r") as data:
    for line in data.readlines():
        line = re.split(" = |,", line)
        dic1[line[0]] = line[1].replace('"', '').replace('\n', '')
ordered_data = sorted(dic1.items(), key=lambda x: datetime.strptime(x[1], '%Y-%m-%d'), reverse=True)
print('Список сотрудников отсортированный по уменьшению возраста:')

# создаём пустой словарь, для записи json файла
dic2 = {}
for i in ordered_data:
    print(i[1], '-', i[0])
    dic2[i[0]] = i[1]

DOB_of_the_youngest = datetime.strptime(list(dic2.values())[0], '%Y-%m-%d')

json_data = []
for i in ordered_data:
    DOB = datetime.strptime(i[1], '%Y-%m-%d')
    now = datetime.now()
    days_to_current_date = now - DOB
    age_in = (DOB_of_the_youngest - DOB).days // 365
    list_json = {
        "Name": i[0],
        "Days to current date": days_to_current_date.days,
        "Age": age_in,
    }
    json_data.append(list_json)

with open('result.json', 'a') as outfile:
    json.dump(json_data, outfile, indent=4, sort_keys=True)
    outfile.close()