from dataclasses import dataclass
from typing import Set


# Here, we define a type that is used by multiple files in the test module.
# I'm no pytest expert, but this seems like a reasonable place to put such a
# thing.
#
# This type is given to the test_column_extract() function as a parameter (it
# is a pytest fixture). Instances of this type are generated in the conftest.py
# file in the test_column_extract_data() function.
#
# Unlike test function parameters and fixture names, you are free to name this
# type whatever you please. The existence of this type is also completely
# optional. The test_column_extract_data() function may just as well return a
# tuple instead.
@dataclass
class ColumnExtractTestData:
    sql: str
    columns: Set[str]
