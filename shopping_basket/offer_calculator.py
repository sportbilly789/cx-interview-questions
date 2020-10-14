from collections import Counter
import numpy as np


class Offer_Calculator:
    def __init__(self, catalogue, offers):
        self._discount = 0
        self._offers = offers
        self._basket = {}
        self._catalogue = catalogue
        # self._item_occurrences = offers
        self._item_offers = {}
        self._discount_list = []

    def get_overall_discount(self):
        return round(self._discount, 2)

    def set_basket(self, basket):
        self._basket = Counter(
            basket
        )  # Covert Basket to dictionary with counts of each item

    # Extract the info for the offers and call the relevant funtions
    def calculate_offers(self):

        for key in self._basket:
            # Find if the items in the basket have any offers call the relevant function
            if key in self._offers:
                self._discount_list.clear()  # Clear the list in case it has any value
                self._discount_list.append(
                    0
                )  # Add zero value the item on offer returns with no discount

                if "Buy N of X, get the cheapest one for free" in self._offers[key]:
                    self.__calculate_N_items_cheapest_free(
                        key,
                        self._offers[key]["Buy N of X, get the cheapest one for free"],
                    )

                if "buy M get N free" in self._offers[key]:
                    if self._basket[key] >= self._offers[key]["buy M get N free"][0]:
                        self.__calculate_get_free(
                            key,
                            self._basket[key],
                            self._offers[key]["buy M get N free"],
                        )

                if "N for the price of M" in self._offers[key]:
                    if (
                        self._basket[key]
                        >= self._offers[key]["N for the price of M"][0]
                    ):
                        self.__calculate_get_for_the_price(
                            key,
                            self._basket[key],
                            self._offers[key]["N for the price of M"],
                        )

                if "discount" in self._offers[key]:
                    self.__calculate_discount(
                        key, self._basket[key], self._offers[key]["discount"][0]
                    )
                self._discount += max(self._discount_list)

    def __calculate_discount(self, item, num_items, discount):
        price = self._catalogue[item]
        discount_price = (price * num_items) * (discount / 100)
        self._discount_list.append(discount_price)

    def __calculate_get_free(self, item, num_items, get_free):
        price = self._catalogue[item]
        free_items = get_free[1] * (
            num_items // get_free[0]
        )  # Calculate the free items
        discount = price * free_items  # Discount for free times
        extra_item = num_items % get_free[0]
        self._discount_list.append(discount)

    def __calculate_get_for_the_price(self, item, num_items, for_the_price):
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
        self._discount_list.append(discount)

    def __calculate_N_items_cheapest_free(self, item, list_offer_items):
        number_of_items = 0
        temp_price_list = []
        discount = 0
        for item in list_offer_items[1]:
            if item in self._basket:
                number_of_items += self._basket[
                    item
                ]  # Calculate the number of items in the basket belong to the list
                for n in range(self._basket[item]):
                    temp_price_list.append(
                        self._catalogue[item]
                    )  # Add the price of the item as many times as it is on the basket

        if number_of_items >= list_offer_items[0]:
            m = number_of_items // list_offer_items[0]
            sorted_list = sorted(temp_price_list)  # Sort the list
            split_list = np.array_split(
                sorted_list, m
            )  # Split the list in m lists and take from each one the minimum value
            for items in split_list:
                discount += min(items)
            self._discount_list.append(discount)
