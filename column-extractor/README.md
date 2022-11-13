This example is built around a function that parses out column names from SQL
`CREATE TABLE` statements.

Test cases can be added to the `test/column-extractor-test-cases` directory
without having to modify any existing python code. Test cases are also named
identically to the directory they are found in (run `pytest -v` to see).

Execute test cases by running `pytest` from this directory.
