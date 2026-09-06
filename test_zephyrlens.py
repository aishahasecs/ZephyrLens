# test_zephyrlens.py
"""
Tests for ZephyrLens module.
"""

import unittest
from zephyrlens import ZephyrLens

class TestZephyrLens(unittest.TestCase):
    """Test cases for ZephyrLens class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZephyrLens()
        self.assertIsInstance(instance, ZephyrLens)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZephyrLens()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
