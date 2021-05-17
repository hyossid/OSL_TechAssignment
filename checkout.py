
"""
CheckOut is an interface of the pricing program.
This Object contains the pricelist and pricingRules which can be applied.

"""

class Checkout:

    # Constructor for the interface
    def __init__(self, pricingStrategy):
        self.basket = []
        self.pricelist = {'ipd':549.99,'mbp':1399.99,'atv':109.50,'vga':30.00}
        self.pricingStrategy = pricingStrategy
        self.finalprice = 0

    # Scanning Method
    def scan(self, item):
        self.basket.append([item,self.pricelist[item]])

    # Return Current PriceList of given product
    def getCurrentPriceList(self):
        return self.pricelist

    # Return Final Price of the selected product
    def total(self):
        self.applyStrategy()
        self.sumUp()
        return self.finalprice

    # Apply the product sales strategies
    def applyStrategy(self):
        self.basket = self.pricingStrategy.buyandreduce(self.basket,'atv',3,2)
        self.basket = self.pricingStrategy.buyanddiscount(self.basket, 'ipd', 4, 499.99)
        self.basket = self.pricingStrategy.buyandfree(self.basket, 'mbp', 'vga')

    # Sum up all the products in the basket
    def sumUp(self):
        for i in range(len(self.basket)):
            #print(self.basket[i])
            self.finalprice += self.basket[i][1]
