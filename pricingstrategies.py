

class PricingStrategies:

    def __init__(self):
        self.var=0

    def buyandreduce(self,bucket, product, N, M):

        """
        This strategy is for Buy 'N' get 'M' deal.
        :param bucket: current product and prices in the bucket
        :param product: Target product to be reduced through this strategy
        :param N: Number of Buying Criteria
        :param M: Number of Reduced Criteria
        :return: strategy applied bucket
        """

        # Number of appearance of product
        count = 0
        # New Bucket after strategy applied
        newbucket = []
        # Flag to check whether the product exists.
        flag = False

        # Iterate Current Bucket and check
        for i in range(len(bucket)):
            if bucket[i][0] == product:
                count += 1
                curprice = bucket[i][1]  # For saving product price : to reduce additional for loop.
                flag = True
            else:
                newbucket.append([bucket[i][0], bucket[i][1]])

        # Reduce as much as the given N and M.
        if flag == True:
            integer = count // N
            count = count - integer * N + integer * M
            temp = [[product, curprice]] * count
            newbucket += temp

        return newbucket

    def buyanddiscount(self,bucket, product, threshold, discountprice):

        """
        This Strategy is for buy more than "threshold", get in "discountprice".
        :param bucket: current product and prices in the bucket
        :param product: Target product to be checked through this strategy
        :param threshold: Given Threshold criteria of applying this strategy
        :param discountprice: Discounted price after buying more than threshold
        :return: strategy applied bucket
        """

        # Number of appearance of product
        count = 0

        # Iterate Current bucket and count
        for item, price in bucket:
            if item == product:
                count += 1

        # If more than threshold, change the product price to discount price
        if count >= threshold:
            for i in range(len(bucket)):
                if bucket[i][0] == product:
                    bucket[i][1] = discountprice

        return bucket

    def buyandfree(self,bucket, product, gift):

        """
        This strategy is for buy "product", "gift" offered.
        :param bucket: current product and prices in the bucket
        :param product: Target product to be checked through this strategy
        :param gift: Product to be given free
        :return: strategy applied bucket
        """

        # New Bucket after strategy applied
        newbucket = []
        # Check whether gift is included in bucket.
        giftind = -1

        # Iterate and check giftindex
        for i in range(len(bucket)):
            if bucket[i][0] == gift:
                giftind = i

        # Make gift price to 0, if not add new gift to new bucket(trivial)
        for i in range(len(bucket)):
            if bucket[i][0] == product:
                if giftind != -1:
                    bucket[giftind][1] = 0
                else:
                    newbucket.append([gift, 0])
            newbucket.append([bucket[i][0], bucket[i][1]])

        return newbucket