#!/usr/bin/env python3
import json
from librip.ctxmngrs import Timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = "data_light.json"

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

# #{
#         "mobile-url": "https://trudvsem.ru/vacancy/card/1027739174033/6bf457e6-51d8-11e6-853e-037acc02728d",
#         "description": "<p>Умение общаться по телефону и лично,
#         доброжелательность, ответственность, стрессоустойчивость.</p>",
#         "update-date": "2016-10-02 01:33:38 MSK",
#         "employment": "Частичная занятость",
#         "job-name": "Администратор на телефоне",
#         "company": {
#             "email": "on.klinik@mail.ru",
#             "contact-name": "Светлана",
#             "hr-agency": True,
#             "phone": "+7(495)6084488",
#             "name": "ООО РОЯЛ КЛИНИК"
#         },
#         "term": "<p>Присутствуют по результатам работы</p>",
#         "addresses": {
#             "address": {
#                 "location": "г. Москва, Кузнецкий Мост улица, 1",
#                 "lat": 55.760808,
#                 "lng": 37.615713
#             }
#         },
#         "url": "https://trudvsem.ru/vacancy/card/1027739174033/6bf457e6-51d8-11e6-853e-037acc02728d",
#         "salary": "от 27000",
#         "duty": "<p>Консультирование клиентов по услугам медицинского центра и скидкам.
#                       Ориентирование клиента от метро до офиса.</p>",
#         "creation-date": "2016-10-02 00:00:00 MSK",
#         "requirement": {
#             "qualification": "<p>Неполный рабочий день (несколько часов в день) утро/вечер.
#               Стабильные выплаты каждые 2 недели. Работа по договору.
#               Фиксированный оклад 15 000 +бонусы.Дружный коллектив.</p>",
#             "education": "Среднее"
#         },
#         "currency": "«руб.»",
#         "schedule": "Неполный рабочий день",
#         "category": {
#             "industry": "Работы, не требующие квалификации"
#         }
#     }

with open(path) as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов


@print_result
def f1(arg):
    return sorted(unique([x for x in field(arg, "job-name")], ignore_case=True), key=str.lower)


@print_result
def f2(arg):
    return list(filter(lambda x: x.find('программист') >= 0 or x.find('разработчик') >= 0, arg)) #x.find('программист')+x.find('разработчик') != -2


@print_result
def f3(arg):
    return list(map(lambda x: x + ' c опытом Python', arg))


@print_result
def f4(arg):
    salaries = [i for i in gen_random(100000, 200000, len(arg))]
    return list(map(lambda x, y: x+', зарплата '+str(y)+' руб.', arg, salaries))


with Timer():
    f4(f3(f2(f1(data))))

