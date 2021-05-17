
import unittest
from checkout import Checkout
from pricingstrategies import PricingStrategies


class Unittesting(unittest.TestCase):
    def testBuyandReduceEqual(self):
        ps1 = PricingStrategies()
        bucket=[['atv',512],['atv',512],['atv',512],['atv',512]]
        ansbucket=[['atv',512],['atv',512],['atv',512]]
        self.assertEqual(ps1.buyandreduce(bucket, 'atv', 3, 2), ansbucket)

    def testBuyandDiscountEqual(self):
        ps1 = PricingStrategies()
        bucket = [['atv', 512], ['atv', 512], ['atv', 512], ['atv', 512]]
        ansbucket = [['atv', 200], ['atv', 200], ['atv', 200], ['atv', 200]]
        self.assertEqual(ps1.buyanddiscount(bucket, 'atv', 4, 200), ansbucket)

    def testBuyandFreeEqual(self):
        ps1 = PricingStrategies()
        bucket = [['atv', 512], ['atv', 512], ['vga', 300], ['vga', 300]]
        ansbucket = [['atv', 512], ['atv', 512], ['vga', 0], ['vga', 0]]
        self.assertEqual(ps1.buyandfree(bucket, 'atv', 'vga'), ansbucket)

    # Unit Test with a given conditions
    def testCheckOutEx1(self):
        ps1 = PricingStrategies()
        co = Checkout(ps1)
        exbucket = ["atv", "atv", "atv", "vga"]
        for item in exbucket:
            co.scan(item)
        self.assertEqual(co.total(), 249.00)

    def testCheckOutEx2(self):
        ps1 = PricingStrategies()
        co = Checkout(ps1)
        exbucket = ["atv", "ipd", "ipd", "atv", "ipd", "ipd", "ipd"]
        for item in exbucket:
            co.scan(item)
        self.assertEqual(co.total(), 2718.95)

    def testCheckOutEx3(self):
        ps1 = PricingStrategies()
        co = Checkout(ps1)
        exbucket = ["mbp", "vga", "ipd"]
        for item in exbucket:
            co.scan(item)
        self.assertEqual(co.total(), 1949.98)

    def testCheckOutEx4(self):
        ps1 = PricingStrategies()
        co = Checkout(ps1)
        exbucket = ["mbp", "mbp", "vga", "vga"]
        for item in exbucket:
            co.scan(item)
        self.assertEqual(co.total(), 2799.98)

if __name__ == '__main__':
    unittest.main()