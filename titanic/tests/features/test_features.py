"""Test features process."""
import logging
import unittest


from titanic.features.feature_config import CONFIG

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


class TestETL(unittest.TestCase):
    """Simple test example."""

    def setUp(self):
        """Setup with basic ETL."""
        self.config = CONFIG

    def test_config_type(self):
        """Test is startproject method runs without errors."""
        self.assertIsInstance(self.config, dict)
