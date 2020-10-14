## Documentation
The task if to create a basket pricer for a supermarket, online groceries/shop etc.
The basket-pricer project has to files the main one baske-pricer which calculates the amount before applying the offers, the total amount after the offers and also returns 
the discount amount calculated from the offer calculator.
The basket_pricer as it is not handling the addition of the items in the basket assumes that all the products in the basket are also in the catalogue so they have a price.
As it was asked also to build the interface between the basket-pricer and the rest of the modules, the basket pricer accepts the basket items as a list of items.
The catalogue has been implemented as a dictionary in the form:
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

The offer as been implemented as a nested dictionary in the form of:
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
}

The key to the dictionary is the item and in the nested dictionaries keys are the offers and the values are the parameters of the offer.
So for the discount offer the key is the "discount" and the value is the percentage of the discount.
For the buy M get N free the key is the "buy M get N free" and the values as [2,1] where the first number it the items needed for the offer and the second the free item.
The same for the N for the price of M.
Currently the module can support 4 types of offers 
Discount
buy M get N free
N for the price of M
M get of one of {N} free

If an item has Multiple offers the offer_calculator returns the offer with the maximum discount for that item.
For running the application the requirements.txt needs to be installed through the command
pip install -r requirements.txt
