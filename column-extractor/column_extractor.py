import re
from typing import Set


COLUMN_REGEX = re.compile(r'\[(\w+)\]')


def extract_column(sql: str) -> Set[str]:
    return set(COLUMN_REGEX.findall(sql))
