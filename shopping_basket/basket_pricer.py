class Basket_Pricer:
    def __init__(self):
        self._total_amount = 0.00
        self._sub_total = 0.00
        self._discount = 1.00
        self._basket_items = []
        self._catalogue = {}
        self._offers = {}

    # getters for the output the values
    def get_discount(self):
        return round(self._discount, 2)

    def get_sub_total(self):
        return round(self._sub_total, 2)

    def get_total_amount(self):
        return round(self._total_amount, 2)

    def calculate_sub_total(self, basket, catalogue):
        self._basket_items = basket
        self._catalogue = catalogue
        for item in self._basket_items:
            self._sub_total = self._sub_total + catalogue[item]

    def calculate_total(self):
        self._total_amount = self._sub_total - self._discount
