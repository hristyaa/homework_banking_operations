import pytest

from src.utils import get_transactions_list

def test_get_transactions_list_empty_file(empty_file_json):
    """ Тест при пустом файле"""
    result = get_transactions_list(empty_file_json)
    assert result == []


def test_get_transactions_list_empty_list(empty_list_json):
    """ Тест при файле, содержащем пустой список"""
    result = get_transactions_list(empty_list_json)
    assert result == []

def test_get_transactions_list(transactions_json, transactions):
    """ Тест при файле, содержащем транзакции"""
    result = get_transactions_list(transactions_json)
    assert result == transactions


def test_get_transactions_list_file_not_found():
    result = get_transactions_list('file_non_existent.json')
    assert result == []