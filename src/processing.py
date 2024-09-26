from typing import Any


def filter_by_state(list_dict: list[dict[str, Any]], state_key: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция, которая перебирает словари и возвращает их по заданному ключу"""

    list_dict_new = []
    for key in list_dict:
        if key.get("state") == state_key:
            list_dict_new.append(key)
    return list_dict_new


def sort_by_date(list_dict: list[dict[str, Any]], optional_param: bool = True) -> list[dict[str, Any]]:
    """Функция, которая перебирает словари и возвращает отсортированный список"""

    list_dict_sorted = sorted(list_dict, key=lambda x: x["date"], reverse=optional_param)
    return list_dict_sorted
