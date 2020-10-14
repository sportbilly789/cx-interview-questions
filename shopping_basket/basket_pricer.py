import offer_calculator


class Basket_Pricer:
    def __init__(self, catalogue, offers):
        self._total_amount = 0.00
        self._sub_total = 0.00
        self._discount = 1.00
        self._basket_items = []
        self._catalogue = catalogue
        self._offers = offers
        self._offer_calc = offer_calculator.Offer_Calculator(
            catalogue=catalogue, offers=offers
        )

    # getters for the output the values
    def get_discount(self):
        self._offer_calc.set_basket(basket=self._basket_items)
        self._offer_calc.calculate_offers()
        self._discount = self._offer_calc.get_overall_discount()
        return self._discount

    def get_sub_total(self):
        return round(self._sub_total, 2)

    def get_total_amount(self):
        return round(self._total_amount, 2)

    def set_basket(self, basket):
        self._basket_items = basket

    def calculate_sub_total(self):
        for item in self._basket_items:
            self._sub_total = self._sub_total + self._catalogue[item]

    def calculate_total(self):
        self._total_amount = self._sub_total - self._discount
