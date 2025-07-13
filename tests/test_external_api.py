from unittest.mock import Mock, patch

import pytest

from src.external_api import get_amount_of_transaction


def test_get_amount_of_transaction(transaction_rub):
    """Тестирование обработки транзакции в рублях"""
    result = get_amount_of_transaction(transaction_rub)
    assert result == '43318.34'


def test_get_amount_of_transaction_usd(transaction_usd):
    """ Тестирование обработки транзакции в USD"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 6175436.115844}

    with patch('requests.get', return_value=mock_response):
        result = get_amount_of_transaction(transaction_usd)
        assert result == 6175436.115844


def test_get_amount_of_transaction_failed_request(transaction_usd):
    """ Проверка обработки ошибки при неудачном запросе к API"""
    mock_response = Mock()
    mock_response.status_code = 500

    with patch('requests.get', return_value=mock_response):
        with pytest.raises(ValueError, match="Failed to get currency rate"):
            get_amount_of_transaction(transaction_usd)
