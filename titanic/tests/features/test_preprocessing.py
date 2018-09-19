"""Test preprocessing process."""
import logging
import unittest

import numpy as np
import pandas as pd

from titanic.data.etl import ETL
from titanic.features.feature_config import CONFIG
from titanic.features.preprocessing import Preprocessing



logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


class TestPreprocessing(unittest.TestCase):
    """Simple test example."""

    def setUp(self):
        """Setup with basic ETL."""
        self.preprocessing = Preprocessing(config=CONFIG, data=ETL().data)

    def test_data_output(self):
        """Test is startproject method runs without errors."""
        data = self.preprocessing.data
        columns = [i['name'] for i in CONFIG['features']]
        columns.append(CONFIG['target']['name'])
        self.assertIsInstance(data, pd.DataFrame)
        self.assertTrue(np.isin(columns, data.columns).all())
