"""Tests for both the offers and calculation of total and subtotal"""


import basket_pricer
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
    "Sardines": {"N for the price of M": [3, 2], "buy M get N free": [2, 1]},
    "Shampoo (Medium)": {"N for the price of M": [3, 2], "discount": [20]},
    "Shampoo (Small)": {
        "Buy N of X, get the cheapest one for free": [
            3,
            ["Shampoo (Large)", "Shampoo (Medium)", "Shampoo (Small)"],
        ]
    },
}

offers_dict_2 = {
    "Shampoo (Small)": {
        "Buy N of X, get the cheapest one for free": [
            3,
            ["Shampoo (Large)", "Shampoo (Medium)", "Shampoo (Small)"],
        ]
    }
}


class Test_BasketPricer(unittest.TestCase):
    def test_basket_subtotal(self):  # Check the basket total before discounts
        basket = [
            "Biscuits",
            "Biscuits",
            "Sardines",
            "Shampoo (Medium)",
            "Edam",
            "Cheddar",
        ]
        basketpricer = basket_pricer.Basket_Pricer(
            catalogue=catalogue, offers=offers_dict
        )
        basketpricer.set_basket(basket)
        basketpricer.calculate_sub_total()
        sub_total = basketpricer.get_sub_total()
        self.assertEqual(sub_total, 9.29)

    def test_basket_total(self):
        basket = ["Biscuits", "Sardines", "Shampoo (Medium)", "Edam", "Cheddar"]
        basketpricer = basket_pricer.Basket_Pricer(
            catalogue=catalogue, offers=offers_dict
        )
        basketpricer.set_basket(basket)
        basketpricer.calculate_sub_total()
        sub_total = basketpricer.get_sub_total()
        discount = basketpricer.get_discount()
        basketpricer.calculate_total()
        total = basketpricer.get_total_amount()
        self.assertEqual(total, 7.59)

    def test_basket_total_2(self):
        basket = [
            "Biscuits",
            "Sardines",  # Sardines uses the "buy M get N free": [2, 1] as it is better than the other  Discount £3.78
            "Sardines",
            "Sardines",
            "Sardines",
            "Sardines",
            "Yogurt",  # Discount one free Yogurt £3.00
            "Yogurt",
            "Yogurt",
            "Shampoo (Medium)",  # Discount 20% £0.5
            "Edam",
            "Cheddar",
        ]
        basketpricer = basket_pricer.Basket_Pricer(
            catalogue=catalogue, offers=offers_dict
        )
        basketpricer.set_basket(basket)
        basketpricer.calculate_sub_total()
        sub_total = basketpricer.get_sub_total()
        discount = basketpricer.get_discount()
        basketpricer.calculate_total()
        total = basketpricer.get_total_amount()
        self.assertEqual(sub_total, 24.65)
        self.assertEqual(discount, 7.28)
        self.assertEqual(total, 17.37)

    def test_basket_total_0(self): #Test zero
        basket = []
        basketpricer = basket_pricer.Basket_Pricer(
            catalogue=catalogue, offers=offers_dict
        )
        basketpricer.set_basket(basket)
        basketpricer.calculate_sub_total()
        sub_total = basketpricer.get_sub_total()
        discount = basketpricer.get_discount()
        basketpricer.calculate_total()
        total = basketpricer.get_total_amount()
        self.assertEqual(total, 0)

    def test_basket_m_get_one_free(self): #Test m get one free
        basket = [
            "Shampoo (Large)",
            "Shampoo (Large)",
            "Shampoo (Large)",
            "Shampoo (Medium)",
            "Shampoo (Small)",
            "Shampoo (Small)",
        ]
        basketpricer = basket_pricer.Basket_Pricer(
            catalogue=catalogue, offers=offers_dict_2
        )
        basketpricer.set_basket(basket)
        basketpricer.calculate_sub_total()
        sub_total = basketpricer.get_sub_total()
        discount = basketpricer.get_discount()
        basketpricer.calculate_total()
        total = basketpricer.get_total_amount()
        self.assertEqual(sub_total, 17.00)
        self.assertEqual(discount, 5.50)
        self.assertEqual(total, 11.50)

    def test_basket_m_get_one_free_multi_discounts(self): #Test all offers together
            "Shampoo (Large)",
            "Shampoo (Large)",
            "Shampoo (Large)",
            "Shampoo (Medium)",
            "Shampoo (Small)",
            "Shampoo (Small)",
        ]
        basketpricer = basket_pricer.Basket_Pricer(
            catalogue=catalogue, offers=offers_dict
        )
        basketpricer.set_basket(basket)
        basketpricer.calculate_sub_total()
        sub_total = basketpricer.get_sub_total()
        discount = basketpricer.get_discount()
        basketpricer.calculate_total()
        total = basketpricer.get_total_amount()
        self.assertEqual(sub_total, 17.00)
        self.assertEqual(discount, 8.10)
        self.assertEqual(total, 8.9)


if __name__ == "__main__":
    unittest.main()
