import unittest
from unittest.mock import patch
import NonWorkingCode as nwc

class TestAddStock(unittest.TestCase):

    @unittest.expectedFailure  # BUG
    def test_add_stock_correctly(self):
        with patch('builtins.input') as mock_input:
            mock_args = ["Test Product", 24.5, 25]
            mock_input.side_effect = mock_args

            nwc.add_stock()
            self.assertEqual(nwc.products, [['Desktop', 799.0, 5], ['Laptop A', 1200.0, 6], ['Test Product', 24.5, 25]])

    @unittest.expectedFailure # BUG
    def test_add_stock_cost_fail(self):
        with patch('builtins.input') as mock_input:
            mock_args = ["Test Product 2", "Not a number", 69, 420]
            mock_input.side_effect = mock_args

            nwc.add_stock()
            self.assertEqual(nwc.products, [['Desktop', 799.0, 5], ['Laptop A', 1200.0, 6], ['Test Product 2', 69.0, 420]])
            
    def test_add_stock_stock_fail(self):
        with patch('builtins.input') as mock_input:
            mock_args = ["Test Product 3", 69, "Not a number", 420]
            mock_input.side_effect = mock_args

            nwc.add_stock()
            self.assertEqual(nwc.products, [['Desktop', 799.0, 5], ['Laptop A', 1200.0, 6], ['Test Product 3', 69.0, 420]])

unittest.main()