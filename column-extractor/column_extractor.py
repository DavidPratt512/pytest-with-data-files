import re
from typing import Set


# This isn't a very good implementation of a 'column-extractor', but that isn't
# the point of this repository, now is it? :)
def extract_column(sql: str) -> Set[str]:
    """Return a set of column names from a SQL 'CREATE TABLE' statement"""
    return set(re.findall(r'\[(\w+)\]', sql))
