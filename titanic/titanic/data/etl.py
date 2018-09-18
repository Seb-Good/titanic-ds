"""Import raw data and basic preprocessing."""

import os

import pandas as pd

from titanic.config.config import DATA_DIR


class ETL(object):
    """Import data for Titanic model."""

    def __init__(self):
        """Init ETL."""
        self._data = None

    @property
    def data(self):
        """Import data."""
        if self._data is None:
            filepath = os.path.join(DATA_DIR, 'titanic_data.csv')
            self._data = pd.read_csv(filepath)
            self._data.columns = [col.lower() for col in self._data.columns]
        return self._data
