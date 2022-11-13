This is a brief guide on how to setup a pytest project to retrieve test data
from files.

I don't use pytest often, but when I do, I often find myself in a situation
where this information would come in handy.

## Why

If you use pytest, you are likely familiar with pytest's
[`pytest.mark.parametrize()`][parametrize-docs] test decorator. If not, it is a
simple way to run many tests scenarios against a single criteria. For example,
the following code block tests the `double()` function against four test cases.

```python
def double(n: int) -> int:
    return 2 * n

@pytest.mark.parametrize(
    'given,expected',
    [
        (-1, -2),
        ( 0,  0),
        ( 1,  2),
        ( 2,  4),
    ]
)
def test_double(given: int, expected: int):
    assert double(given) == expected
```

But what if you needed *many* test cases? One solution would be to execute the
test many times against random inputs. But a programmer can quickly become
stuck in a corner when using random test data. (Ask yourself how to test the
`double()` function with random test data *without* re-implementing the
`double()` function in the test... [it's possible, but not
obvious][property-based-testing].)

Another, perhaps more obvious, solution is to just pack all of those new test
cases next to the existing test cases. Now the test looks like this:

```python
@pytest.mark.parametrize(
    'given,expected',
    [
        (-1, -2),
        ( 0,  0),
        # ...
        # ... one thousand lines later
        # ...
        ( 1,  2),
        ( 2,  4),
    ]
)
def test_double(given: int, expected: int):
    assert double(given) == expected
```

Imagine having to sift through one thousand lines of test cases inside of a
python file! Yuck!

At this point, it is reasonable to ask "Why would anyone write a single
function that has one thousand test cases?". I don't have a good answer for
that. I would agree that there is likely a problem with the structure of the
code in that scenario.

While it is potentially unreasonable to have one thousand test cases for a
single function, it may not be unreasonable to have a handful of test cases
that take up one thousand lines of code. For example, suppose a function takes
a SQL `CREATE TABLE` script as an input and produces a set of column names
present in the script. SQL scripts can get pretty long, and perhaps a decent
test case would test the function against a *"real-world"* SQL script.

At this point, one may object again and ask "That function does too many
things! It shouldn't have to parse a SQL script *and* search for column
names!". That's likely correct - and the code would certainly be more
maintainable if it was broken up so each component had a single responsibility.
But try writing a SQL tokenizer in 30 minutes with a comprehensive test suite.

It would be nice if there was only one test function, much like
`test_double()`, accompanied by a comprehensive suite of SQL scripts that are
stored separately from the python code. Perhaps a test like this:

```python
def test_column_extract(test_data):
    assert column_extract(test_data.sql) == test_data.columns
```

... with a directory structure like this:

```
test/
    __init__.py
    conftest.py
    test_column_extractor.py
    column-extractor-test-cases/
        all-caps/
            given.sql
            expected-columns.json
        no-columns/
            given.sql
            expected-columns.json
        ...
```

[parametrize-docs]: https://docs.pytest.org/en/6.2.x/parametrize.html#pytest-mark-parametrize-parametrizing-test-functions
[property-based-testing]: https://youtu.be/99oO-6EIyck
