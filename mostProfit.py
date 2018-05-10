import unittest

def mostProfit(prices):
    max_profit=0
    low_price=prices[0]
    for i in range(1,len(prices)):
        low_price=min(low_price,prices[i])
        max_profit=max(max_profit,prices[i]-low_price)
    return max_profit

class TestSMostProfit(unittest.TestCase):

    def test_mostProfit(self):
        t1=mostProfit([5,4,3])
        self.assertEqual(t1,0)

        t2=mostProfit([1,5,4,3])
        self.assertEqual(t2,4)

        t3=mostProfit([1,1,1,1])
        self.assertEqual(t3,0)

        t4=mostProfit([7,1,5,3,6,4])
        self.assertEqual(t4,5)

        t5=mostProfit([7,6,4,3,1])
        self.assertEqual(t5,0)


if __name__ == '__main__':
    unittest.main()