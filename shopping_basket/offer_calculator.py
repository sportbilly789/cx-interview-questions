from collections import Counter


class Offer_Calculator:
    def __init__(self):
        self._discount = 0
        self._offers = {}
        self._basket = {}
        self._catalogue = {}
        self._item_occurrences = {}
        self._item_offers = {}

    def get_overall_discount(self):
        return round(self._discount, 2)

    # Extract the info for the offers and call the relevant funtions
    def calculate_offers(self, offers, basket, catalogue):
        self._basket = basket
        self._catalogue = catalogue
        self._offers = offers
        self._basket = Counter(
            basket
        )  # Covert Basket to dictionary with counts of each item

        for key in self._basket:
            # Find if the items in the basket have any offers call the relevant function
            if key in self._offers:
                if "buy M get N free" in self._offers[key]:
                    if self._basket[key] >= self._offers[key]["buy M get N free"][0]:
                        self.calculate_get_free(
                            key,
                            self._basket[key],
                            self._offers[key]["buy M get N free"],
                        )
                        return

                if "N for the price of M" in self._offers[key]:
                    if (
                        self._basket[key]
                        >= self._offers[key]["N for the price of M"][0]
                    ):
                        self.calculate_get_for_the_price(
                            key,
                            self._basket[key],
                            self._offers[key]["N for the price of M"],
                        )
                        return

                if "discount" in self._offers[key]:
                    self.calculate_discount(
                        key, self._basket[key], self._offers[key]["discount"][0]
                    )

    def calculate_discount(self, item, num_items, discount):
        price = self._catalogue[item]
        discount_price = (price * num_items) * (discount / 100)
        self._discount += discount_price

    def calculate_get_free(self, item, num_items, get_free):
        price = self._catalogue[item]
        free_items = get_free[1] * (
            num_items // get_free[0]
        )  # Calculate the free items
        discount = price * free_items  # Discount for free times
        extra_item = num_items % get_free[0]
        if extra_item > 0:
            if "discount" in self._offers[item]:
                self.calculate_discount(
                    item, extra_item, self._offers[item]["discount"][0]
                )
        self._discount += discount

    def calculate_get_for_the_price(self, item, num_items, for_the_price):
        price = self._catalogue[item]
        items_to_pay = for_the_price[1] * (
            num_items // for_the_price[0]
        )  # Calculate the number of items to pay
        extra_item = num_items % for_the_price[0]
        if extra_item > 0:
            if "discount" in self._offers[item]:
                self.calculate_discount(
                    item, extra_item, self._offers[item]["discount"][0]
                )
        discount = price * num_items - price * (items_to_pay + (extra_item))
        self._discount += discount
