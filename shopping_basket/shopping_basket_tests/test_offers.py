"""Test for the offers functionalities"""

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
    "Yogurt": 3.00,
}

offers_dict = {
    "Baked Beans": {"discount": [15], "buy M get N free": [2, 1]},
    "Shampoo (Large)": {"discount": [20]},
    "Yogurt": {"buy M get N free": [2, 1], "discount": [20]},
    "Shampoo (Medium)": {"N for the price of M": [3, 2]},
}


class Test_offers(unittest.TestCase):
    def test_discounts(self):  #
        basket = ["Shampoo (Large)", "Shampoo (Large)"]
        offer = offer_calculator.Offer_Calculator(
            catalogue=catalogue, offers=offers_dict
        )
        offer.set_basket(basket=basket)
        offer.calculate_offers()
        discount = offer.get_overall_discount()
        self.assertEqual(discount, 1.40)

    def test_Multidiscounts(self):  #
        basket = ["Shampoo (Large)", "Shampoo (Large)", "Baked Beans", "Yogurt"]
        offer = offer_calculator.Offer_Calculator(
            catalogue=catalogue, offers=offers_dict
        )
        offer.set_basket(basket=basket)
        offer.calculate_offers()
        discount = offer.get_overall_discount()
        self.assertEqual(discount, 2.15)

    def test_multifree(self):
        basket = ["Yogurt", "Yogurt", "Yogurt"]
        offer = offer_calculator.Offer_Calculator(
            catalogue=catalogue, offers=offers_dict
        )
        offer.set_basket(basket=basket)
        offer.calculate_offers()
        discount = offer.get_overall_discount()
        self.assertEqual(discount, 3.00)

    def test_combinations_discount__free(self):

        basket = [
            "Shampoo (Large)",
            "Yogurt",
            "Yogurt",
            "Yogurt",
        ]

        offer = offer_calculator.Offer_Calculator(
            catalogue=catalogue, offers=offers_dict
        )
        offer.set_basket(basket=basket)
        offer.calculate_offers()
        discount = offer.get_overall_discount()
        self.assertEqual(discount, 3.7)

    def test_M_for_price_of_N(self):  # Check the basket total before discounts

        basket = [
            "Shampoo (Medium)",
            "Shampoo (Medium)",
            "Shampoo (Medium)",
            "Shampoo (Medium)",
            "Shampoo (Medium)",
            "Shampoo (Medium)",
            "Shampoo (Medium)",
            "Shampoo (Medium)",
        ]
        offer = offer_calculator.Offer_Calculator(
            catalogue=catalogue, offers=offers_dict
        )
        offer.set_basket(basket=basket)
        offer.calculate_offers()
        discount = offer.get_overall_discount()
        self.assertEqual(discount, 5.00)


if __name__ == "__main__":
    unittest.main()
