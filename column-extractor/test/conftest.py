import json
import os
import pytest
from pathlib import Path
from . import ColumnExtractTestData


# This conftest.py file effectively configures pytest before any tests are run.
#
# We need to tell pytest to generate test cases for each of the subdirectories
# inside the 'column-extractor-test-cases' directory. First, find that
# directory relative to this file:
column_extractor_test_cases_directory = Path(os.path.dirname(os.path.realpath(__file__))) / 'column-extractor-test-cases'

# ... then find each subdirectory of the column_extractor_test_cases directory:
column_extractor_test_case_paths = [dir for dir in column_extractor_test_cases_directory.iterdir() if dir.is_dir()]

# ... and lastly, find the names of each of those directories. These will be
# used to name the tests. That way, when a test fails, we'll know exactly which
# one.
column_extractor_test_case_names = [path.name for path in column_extractor_test_case_paths]


# Create a fixture to give to test functions (like the test_column_extract()
# function). The fixture can be parametrized - meaning that a test case is
# generated for each element of `params`.
#
# Note that this function takes an argument of type FixtureRequest. This is
# provided by pytest when it is setting up the fixture. Notably, the
# FixtureRequest object has an attribute called `param`. This attribute points
# to an element in the `params` argument provided in the decorator.
@pytest.fixture(
    # Generate a test case for each of the elements inside of this argument:
    params=column_extractor_test_case_paths,

    # ... and the name of each test case is determined by this argument. For
    # example, the first element in the previous argument will be named with
    # the first element in this argument, and so on.
    ids=column_extractor_test_case_names
)
def test_column_extract_data(request: pytest.FixtureRequest) -> ColumnExtractTestData:
    # The param of this request is given by the `params` arguemnt in the
    # decorator. We know the type of this is Path - in fact, we know it is an
    # element of the column_extractor_test_case_paths list defined above.
    test_case_dir: Path = request.param

    # By convention, each test case holds the SQL 'CREATE TABLE' script in a
    # file called 'given.sql'.
    given_sql_file = test_case_dir / 'given.sql'

    # Likewise, by convention, each test case holds the list of columns present
    # in the 'CREATE TABLE' script in the 'expected_columns.json' file.
    expected_columns_file = test_case_dir / 'expected-columns.json'

    # Read in the two files and return their contents in a
    # ColumnExtractTestData object. This object is what is given to the
    # test_column_extract() test function.
    given_sql = given_sql_file.read_text()
    with open(expected_columns_file, 'r') as ecf:
        expected_columns = set(json.load(ecf))

    return ColumnExtractTestData(sql=given_sql, columns=expected_columns)
