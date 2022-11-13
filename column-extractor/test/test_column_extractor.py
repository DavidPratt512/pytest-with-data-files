from column_extractor import extract_column
from . import ColumnExtractTestData


# This is the unit test for the extract_column() function defined in the
# column_extractor module.
#
# Note that the parameter test_column_extract_data is named identically to the
# fixture in the conftest.py file. This is because pytest magically wires up
# any test parameters to fixtures. A nice feature, but not obvious to new
# users. (Try changing the parameter name on this test... you'll see that
# pytest complains that it cannot find a fixture with the new name.)
def test_column_extract(test_column_extract_data: ColumnExtractTestData):
    assert extract_column(test_column_extract_data.sql) == test_column_extract_data.columns
