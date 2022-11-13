import json
import os
import pytest
from pathlib import Path
from . import ColumnExtractTestData


column_extractor_test_cases_directory = Path(os.path.dirname(os.path.realpath(__file__))) / 'column-extractor-test-cases'
column_extractor_test_case_paths = [dir for dir in column_extractor_test_cases_directory.iterdir() if dir.is_dir()]
column_extractor_test_case_names = [path.name for path in column_extractor_test_case_paths]


@pytest.fixture(
    scope='module',
    params=column_extractor_test_case_paths,
    ids=column_extractor_test_case_names
)
def test_column_extract_data(request: pytest.FixtureRequest) -> ColumnExtractTestData:
    test_case_dir: Path = request.param
    given_sql_file = test_case_dir / 'given.sql'
    expected_columns_file = test_case_dir / 'expected-columns.json'

    given_sql = given_sql_file.read_text()
    with open(expected_columns_file, 'r') as ecf:
        expected_columns = set(json.load(ecf))

    return ColumnExtractTestData(sql=given_sql, columns=expected_columns)
