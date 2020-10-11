# Import the code to be tested
import offer_calculator
import unittest  # Test Framework

# Sample catalogue, basket, offers
catalogue = {
    "Baked Beans": 0.99,
    "Biscuits": 1.20,
    "Mustard": 1.30,
    "Sardines": 1.89,
    "Shampoo (Small)": 2.00,
    "Shampoo (Medium)": 2.50,
    "Shampoo (Large)": 3.50,
    "Edam": 1.20,
    "Cheddar": 1.30,
    "Gouda": 1.00,
}

offers = {
    "Baked Beans": ["buy 2 get 1 free", "10% discount"],
    "Shampoo (Large)": ["25% discount"],
    "Yogurt": ["buy 2 get 1 free"],
    "Shampoo (Medium)": ["3 for the price of two"],
}

class Test_offers(unittest.TestCase):
    def test_discounts(self):  # Check the basket total before discounts
    return None