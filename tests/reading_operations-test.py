import pytest
from unittest.mock import mock_open, patch
import pandas as pd
from src.reading_operations import read_csv, read_excel



def test_read_csv():
    mock_data = "id;state;date;amount;currency_name;currency_code;from;to;description\n" \
                "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n" \
                "3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту"

    with patch("builtins.open", mock_open(read_data=mock_data)):
        expected = [
            {
                'id': '650703',
                'state': 'EXECUTED',
                'date': '2023-09-05T11:30:32Z',
                'amount': '16210',
                'currency_name': 'Sol',
                'currency_code': 'PEN',
                'from': 'Счет 58803664561298323391',
                'to': 'Счет 39745660563456619397',
                'description': 'Перевод организации'
            },
            {
                'id': '3598919',
                'state': 'EXECUTED',
                'date': '2020-12-06T23:00:58Z',
                'amount': '29740',
                'currency_name': 'Peso',
                'currency_code': 'COP',
                'from': 'Discover 3172601889670065',
                'to': 'Discover 0720428384694643',
                'description': 'Перевод с карты на карту'
            }
        ]
        result = read_csv("dummy_path.csv")
        assert result == expected



def test_read_excel():
    mock_data = {
        'id': [650703, 3598919],
        'state': ['EXECUTED', 'EXECUTED'],
        'date': ['2023-09-05T11:30:32Z', '2020-12-06T23:00:58Z'],
        'amount': [16210, 29740],
        'currency_name': ['Sol', 'Peso'],
        'currency_code': ['PEN', 'COP'],
        'from': ['Счет 58803664561298323391', 'Discover 3172601889670065'],
        'to': ['Счет 39745660563456619397', 'Discover 0720428384694643'],
        'description': ['Перевод организации', 'Перевод с карты на карту']
    }

    df = pd.DataFrame(mock_data)

    with patch("pandas.read_excel", return_value=df):
        expected = [
            {
                'id': 650703,
                'state': 'EXECUTED',
                'date': '2023-09-05T11:30:32Z',
                'amount': 16210,
                'currency_name': 'Sol',
                'currency_code': 'PEN',
                'from': 'Счет 58803664561298323391',
                'to': 'Счет 39745660563456619397',
                'description': 'Перевод организации'
            },
            {
                'id': 3598919,
                'state': 'EXECUTED',
                'date': '2020-12-06T23:00:58Z',
                'amount': 29740,
                'currency_name': 'Peso',
                'currency_code': 'COP',
                'from': 'Discover 3172601889670065',
                'to': 'Discover 0720428384694643',
                'description': 'Перевод с карты на карту'
            }
        ]
        result = read_excel("dummy_path.xlsx")
        assert result == expected


if __name__ == "__main__":
    pytest.main()



