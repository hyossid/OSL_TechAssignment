
import unittest
from checkout import Checkout
from pricingstrategies import PricingStrategies


class Unittesting(unittest.TestCase):
    def utestBuyandReduceEqual(self):
        PricingStrategies = PricingStrategies()
        bucket=[['atv',512],['atv',512],['atv',512],['atv',512]]
        ansbucket=[['atv',512],['atv',512],['atv',512]]
        self.assertEqual(PricingStrategies.buyandreduce(bucket, 'atv', 3, 2), ansbucket)

    def utestBuyandDiscountEqual(self):
        PricingStrategies = PricingStrategies()
        bucket = [['atv', 512], ['atv', 512], ['atv', 512], ['atv', 512]]
        ansbucket = [['atv', 200], ['atv', 200], ['atv', 200], ['atv', 200]]
        self.assertEqual(PricingStrategies.buyanddiscount(bucket, 'atv', 4, 200), ansbucket)

    def utestBuyandFreeEqual(self):
        PricingStrategies = PricingStrategies()
        bucket = [['atv', 512], ['atv', 512], ['vba', 300], ['vba', 300]]
        ansbucket = [['atv', 200], ['atv', 200], ['vba', 0], ['vba', 0]]
        self.assertEqual(PricingStrategies.buyandfree(bucket, 'atv', 'vba'), ansbucket)

    # Unit Test with a given conditions
    def utestCheckOutEx1(self):
        pricingRules = PricingStrategies()
        co = Checkout(pricingRules)
        exbucket = ["atv", "atv", "atv", "vga"]
        for item in exbucket:
            co.scan(item)
        self.assertEqual(co.total(), 249.00)

    def utestCheckOutEx2(self):
        PricingStrategies = PricingStrategies()
        co = Checkout(PricingStrategies)
        exbucket = ["atv", "ipd", "ipd", "atv", "ipd", "ipd", "ipd"]
        for item in exbucket:
            co.scan(item)
        self.assertEqual(co.total(), 2718.95)

    def utestCheckOutEx3(self):
        PricingStrategies = PricingStrategies()
        co = Checkout(PricingStrategies)
        exbucket = ["mbp", "vga", "ipd"]
        for item in exbucket:
            co.scan(item)
        self.assertEqual(co.total(), 1949.98)

    def utestCheckOutEx4(self):
        PricingStrategies = PricingStrategies()
        co = Checkout(PricingStrategies)
        exbucket = ["mbp", "mbp", "vga", "vga"]
        for item in exbucket:
            co.scan(item)
        self.assertEqual(co.total(), 2799.98)

if __name__ == '__main__':
    unittest.main()