# Import the code to be tested
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
}

offers = {
    "Baked Beans": ["buy 2 get 1 free", "10% discount"],
    "Shampoo (Large)": ["25% discount"],
    "Yogurt": ["buy 2 get 1 free"],
    "Shampoo (Medium)": ["3 for the price of two"],
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
        basketpricer = basket_pricer.Basket_Pricer()
        basketpricer.calculate_sub_total(basket=basket, catalogue=catalogue)
        sub_total = basketpricer.get_sub_total()
        self.assertEqual(sub_total, 9.29)

    def test_basket_total(self):
        basket = ["Biscuits", "Sardines", "Shampoo (Medium)", "Edam", "Cheddar"]
        basketpricer = basket_pricer.Basket_Pricer()
        basketpricer.calculate_sub_total(basket=basket, catalogue=catalogue)
        basketpricer.calculate_total()
        discount = basketpricer.get_discount()
        print(discount)
        total = basketpricer.get_total_amount()
        self.assertEqual(total, 7.09)


if __name__ == "__main__":
    unittest.main()
