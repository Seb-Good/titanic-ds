"""Class to performing preprocessing."""

import pandas as pd


class Preprocessing(object):
    """Preprocess raw data."""

    def __init__(self, config, data):
        self.config = config
        self._raw_data = data
        self._data = None

    @property
    def data(self):
        if self._data is None:
            data = self._process_features(df=self._raw_data)
            columns = self._process_columns()
            self._data = data[columns]
        return self._data

    def _process_features(self, df):
        for i in self.config['features']:
            if 'function' in i:
                df = i['function'](df=df)
        return df

    def _process_columns(self):
        columns = [i['name'] for i in self.config['features']]
        columns.append(self.config['target']['name'])
        return columns
