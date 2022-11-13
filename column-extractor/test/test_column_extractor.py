from column_extractor import extract_column
from . import ColumnExtractTestData


def test_column_extract(test_column_extract_data: ColumnExtractTestData):
    assert extract_column(test_column_extract_data.sql) == test_column_extract_data.columns
