gapminder
===============================================================================

This is a Python version of Jennifer Bryan's excellent 
[gapminder](https://github.com/jennybc/gapminder/) teaching package for R.

## Installation

```
pip install gapminder
```

## Usage

This package contains only one object, a Pandas DataFrame named `gapminder`.

```python
from gapminder import gapminder
gapminder.head()
```
```
       country continent  year  lifeExp       pop   gdpPercap
0  Afghanistan      Asia  1952   28.801   8425333  779.445314
1  Afghanistan      Asia  1957   30.332   9240934  820.853030
2  Afghanistan      Asia  1962   31.997  10267083  853.100710
3  Afghanistan      Asia  1967   34.020  11537966  836.197138
4  Afghanistan      Asia  1972   36.088  13079460  739.981106
```

Use it. Abuse it. It's a great dataset for teaching, which is why I'm re-hosting
it as a Python package.

