import pkg_resources
from io import StringIO
import pandas as pd

def _load_gapminder():
    content = pkg_resources.resource_string('gapminder', 'gapminder.csv').decode()
    return pd.read_csv(StringIO(content))
