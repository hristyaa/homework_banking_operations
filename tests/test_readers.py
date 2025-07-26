from unittest.mock import patch

from src.readers import reader_csv_file, reader_excel_file


@patch("src.readers.pd.read_csv")
def test_reader_csv_file(mock_read_csv):
    """Тест при cvc файле c данными"""

    mock_read_csv.return_value.to_dict.return_value = """[
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404"
        }
    ]"""

    expected_result = """[
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404"
        }
    ]"""
    assert reader_csv_file("mock_file.cvs").replace(" ", "").replace("\n", "") == expected_result.strip().replace(
        " ", ""
    ).replace("\n", "")


def test_reader_csv_empty_file(cvs_empty_file):
    """Тест при пустом cvc файле"""
    result = reader_csv_file(cvs_empty_file)
    assert result == "Файл пустой."


def test_reader_csv_file_file_not_found():
    """Тест, если файл не найден"""
    result = reader_csv_file("file_non_existent.csv")
    assert result == "Файл не найден."


@patch("src.readers.pd.read_excel")
def test_reader_excel_file(mock_read_excel):
    """Тест при excel файле c данными"""

    mock_read_excel.return_value.to_dict.return_value = """[
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404"
        }
    ]"""

    expected_result = """[
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404"
        }
    ]"""
    assert reader_excel_file("mock_file.xlsx").replace(" ", "").replace("\n", "") == expected_result.strip().replace(
        " ", ""
    ).replace("\n", "")


def test_reader_excel_empty_file(excel_empty_file):
    """Тест при пустом excel файле"""
    result = reader_excel_file(excel_empty_file)
    assert result == "Файл пустой."


def test_reader_excel_file_file_not_found():
    """Тест, если файл не найден"""
    result = reader_excel_file("file_non_existent.xlsx")
    assert result == "Файл не найден."
