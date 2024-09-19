from typing import Any
list_dict_exam = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
                  ]

def filter_by_state(list_dict: list[dict[str, Any]], state_key: str = 'EXECUTED') -> list[dict[str, Any]]:
    """Функция, которая перебирает словари и возвращает их по заданному ключу"""

    list_dict_new = []
    for key in list_dict:
        if key.get('state') == state_key:
            list_dict_new.append(key)
    return list_dict_new

print(filter_by_state(list_dict_exam))


def sort_by_date (list_dict: list[dict[str, Any]], optional_param: bool = True) -> list[dict[str, Any]]:
    """Функция, которая перебирает словари и возвращает отсортированный список"""


    list_dict_sorted = sorted(list_dict, key=lambda x: x["date"], reverse =optional_param)
    return list_dict_sorted

print(sort_by_date(list_dict_exam))