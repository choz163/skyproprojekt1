import re
from collections import Counter


def find_transactions_by_description(transactions, search_string):
    """Находит и возвращает список транзакций, в описании которых содержится указанная строка."""
    result = []
    for transaction in transactions:
        if re.search(search_string, transaction["description"], re.IGNORECASE):
            result.append(transaction)
    return result


def count_transactions_by_category(transactions: list[dict], categories: list[str]) -> dict[str, int]:
    """Подсчитывает и возвращает количество транзакций по категориям.
    Категории определяются по первому слову в описании транзакции."""
    result = Counter()
    for transaction in transactions:
        category = transaction.get("description", "").split(" ")[0]  # Получаем первую часть описания как категорию
        if category in categories:
            result[category] += 1
    return dict(result)
