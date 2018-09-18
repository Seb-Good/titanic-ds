"""Test ETL process."""
import logging
import unittest

import pandas as pd

from titanic.data.etl import ETL

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


class TestETL(unittest.TestCase):
    """Simple test example."""

    def setUp(self):
        """Setup with basic ETL."""
        self.etl = ETL()

    def test_data(self):
        """Test is startproject method runs without errors."""
        self.assertIsInstance(self.etl.data, pd.DataFrame)
