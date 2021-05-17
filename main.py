
"""
Requirements :

    Strategy 1 : If Buy 3 Apple TV -> 2 Apple TV
    Strategy 2 : Ipad is discounted if buy more than 4 -> each price will become 499.99
    Strategy 3 : Macbook pro -> Free VGA

    # Pricing Strategy should be changed with the least amount of coding in future
"""

from checkout import Checkout
from pricingstrategies import PricingStrategies


if __name__ == '__main__':

    # Instance for pricing strategy
    PricingStrategies = PricingStrategies()
    # checkout interface
    co = Checkout(PricingStrategies)
    # Receive Input
    bucket = input("SKUs Scanned: ").split(",")

    for item in bucket:
        co.scan(item.strip())

    # Print it in designated format
    print("Total Expected: ${:.2f}".format(co.total()))