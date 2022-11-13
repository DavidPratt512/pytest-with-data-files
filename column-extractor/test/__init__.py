from dataclasses import dataclass
from typing import Set


@dataclass
class ColumnExtractTestData:
    sql: str
    columns: Set[str]
